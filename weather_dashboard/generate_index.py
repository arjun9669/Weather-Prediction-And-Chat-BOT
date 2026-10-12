from sentence_transformers import SentenceTransformer
import faiss
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent

# Load the combined clean text
with open(ROOT / "docs/combined_text.txt", "r", encoding="utf-8") as f:
    full_text = f.read()

# Split into chunks
chunks = [full_text[i:i+512] for i in range(0, len(full_text), 512)]

# Embed
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embed_model.encode(chunks)

# FAISS Index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index and chunks
faiss.write_index(index, str(ROOT / "faiss_index.idx"))
with open(ROOT / "chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f)

print("Done: faiss_index.idx and chunks.json saved.")
