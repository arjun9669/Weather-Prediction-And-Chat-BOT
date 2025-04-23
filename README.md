
# 🌦️ Real-Time Weather Prediction & PDF Chatbot App

This is a full-stack data science project that integrates **real-time weather data simulation**, **temperature prediction using machine learning**, and a **PDF-based intelligent chatbot** built with modern NLP tools.

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

## 📂 Project Structure

```
weather_dashboard/
├── app.py                  # Streamlit dashboard
├── chatbot.py              # PDF chatbot script
├── generate_index.py       # Chunking & FAISS index creator
├── model.joblib            # Trained ML model
├── combined_text.txt       # Combined text from PDFs
├── faiss_index.idx         # Vector index file
├── chunks.pkl              # Pickled text chunks
├── README.md               # Project documentation
├── docs/                   # PDF resources
│   ├── ml_guide.pdf
│   ├── python_cheatsheet.pdf
│   └── sql_cheatsheet.pdf
├── screenshots/            # App screenshots
│   ├── dashboard.png
│   ├── chatbot.png
│   └── ml_output.png
```

---

## 🚀 How to Run

### 1. Clone this repo
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd weather_dashboard
```

### 2. Install required libraries
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install streamlit scikit-learn pandas numpy matplotlib joblib sentence-transformers faiss-cpu PyMuPDF transformers
```

### 3. Run the dashboard
```bash
streamlit run app.py
```

### 4. Run the chatbot
```bash
streamlit run chatbot.py
```

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
Aspiring Data Analyst | Python • SQL • ML • NLP  
[LinkedIn Profile](https://www.linkedin.com/in/arjun-analytics)

---

## 📌 Keywords
#streamlit #machinelearning #chatbot #nlp #faiss #weatherdashboard #datascience #huggingface #pdfchatbot #imarticus
