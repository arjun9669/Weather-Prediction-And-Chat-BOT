import streamlit as st
import faiss
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
from sentence_transformers import SentenceTransformer
from transformers import pipeline

@st.cache_resource
def load_all():
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
    index = faiss.read_index(str(ROOT / "faiss_index.idx"))
    with open(ROOT / "chunks.json", encoding="utf-8") as f:
        chunks = json.load(f)
    rag_model = pipeline("text2text-generation", model="google/flan-t5-base")
    return embed_model, index, chunks, rag_model

st.title("📚 PDF-Based RAG Chatbot")
st.markdown("Ask questions about the bundled indexed text. PDF upload is not implemented.")

embed_model, index, chunks, rag_model = load_all()

question = st.text_input("Ask a question:")

if question:
    try:
        question_embedding = embed_model.encode([question])
        D, I = index.search(question_embedding, k=3)
        selected_chunks = [chunks[i] for i in I[0] if 0 <= i < len(chunks)]
        context = "\n".join(selected_chunks)
        prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        answer = rag_model(prompt, max_length=200, do_sample=False)[0]["generated_text"]

        st.subheader("💬 Answer")
        st.write(answer)

        with st.expander("📄 Source Chunks"):
            for idx, chunk in enumerate(selected_chunks):
                st.markdown(f"**Chunk {idx+1}**:\n{chunk}")

    except Exception as e:
        st.error(f"❌ Error during search or answer generation:\n{e}")
