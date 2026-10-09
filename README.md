
# 🌦️ Weather Simulation, Temperature Prediction & PDF Chatbot

An educational data-science project combining **simulated weather observations**, a machine-learning temperature predictor and a PDF-question-answering demo. Simulated weather readings are not live measured weather forecasts.

---

## 🧩 Problem Statement

To develop an end-to-end real-time weather prediction dashboard with machine learning integration and a chatbot that can answer questions based on PDF documents using NLP and vector search (FAISS + embeddings).

---

## ✨ Project Highlights

- 🌦️ **Real-time weather data simulation** using Streamlit with randomized city-wise data
- 📈 **ML model** (Linear Regression) trained to predict temperature based on humidity, wind speed, and location
- 🤖 **Chatbot** powered by Retrieval-Augmented Generation (RAG)
- 📚 **Semantic search** over PDFs using SentenceTransformers + FAISS
- 🧠 **Answer generation** using Hugging Face’s flan-t5-base model
- 🖥️ Streamlit-based clean UI for live monitoring and chatbot interaction

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas, NumPy
- SentenceTransformers
- FAISS
- PyMuPDF
- HuggingFace Transformers
- Matplotlib

---

## 📦 Repository contents and current limitation

At the repository root, the application is stored as [`Imarticus_DS_Project_Arjun.zip`](./Imarticus_DS_Project_Arjun.zip), alongside this README. **The application source is not presently checked in as browseable individual files.** The original README previously showed a `weather_dashboard/` tree and commands as though that directory existed at repository root; it does not.

### Inspect and run locally

1. Download and extract the ZIP into a new folder.
2. Inspect the extracted file tree for `app.py`, `chatbot.py`, `requirements.txt` and the model/vector-index assets described in the archive.
3. Create and activate a Python virtual environment in the application directory.
4. If the extracted archive includes `requirements.txt`, install it with `python -m pip install -r requirements.txt`. Otherwise inspect the actual imports and install the required packages.
5. If the extracted archive has the indicated scripts, launch them from the directory containing those files:

```bash
python -m streamlit run app.py
# Or, in a separate terminal:
python -m streamlit run chatbot.py
```

These commands are conditional on the archive structure and have **not** been independently executed in this cleanup. Future improvement: unpack the archive into normal tracked project files, provide a tested environment specification and add an end-to-end smoke test.

---

## 📸 Screenshots

### Dashboard
![Dashboard](https://github.com/user-attachments/assets/1b503daf-f267-45c2-b850-939cc8c6c0f0)

### Chatbot
![Chatbot](https://github.com/user-attachments/assets/d557f001-158b-4179-984c-e710716d2400)

### ML Output
![ML Output](https://github.com/user-attachments/assets/1da748a1-2358-44c1-ad5d-165023279938)
---

## 🙋‍♂️ Author

**Arjun Kumar**  
Python • SQL • Machine Learning • NLP  
[LinkedIn Profile](https://www.linkedin.com/in/arjun-analytics)

---

## 📌 Keywords
#streamlit #machinelearning #chatbot #nlp #faiss #weatherdashboard #datascience #huggingface #pdfchatbot #imarticus
