# Simulated Weather Predictor and Text RAG Demo

Browseable source is now in [weather_dashboard](./weather_dashboard). The original ZIP is preserved as a historical archive. This educational project simulates weather inputs; it does not fetch live weather or provide validated forecasts.

## Weather dashboard

```powershell
cd weather_dashboard
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python train.py
python -m unittest discover -s tests -v
python -m streamlit run app.py
```

Training regenerates the model locally from the supplied illustrative CSV; archived model binaries are not needed. The smoke test checks serialization, input handling and a finite prediction, not predictive accuracy.

## Separate text chatbot

```powershell
python -m pip install -r requirements-chatbot.txt
python generate_index.py
python -m streamlit run chatbot.py
```

The chatbot indexes `docs/combined_text.txt` with MiniLM and FAISS and generates answers with FLAN-T5. It downloads models and can need substantial memory. It has **no PDF upload/OCR interface**, despite its historical PDF title. Retrieved chunks do not guarantee factual support; unsupported-question refusal and citation verification are not implemented. The tiny PDF-named archive placeholders were not promoted into the source tree. Chunk storage is regenerated as JSON rather than loaded from the archive's pickle.

The training smoke test and source syntax checks have been run. The Streamlit UI, FAISS build and downloaded-model chatbot have not been independently exercised in this cleanup. Dependency ranges are a starting environment specification, not a fully pinned reproducible lockfile.

[Original archive](./Imarticus_DS_Project_Arjun.zip) · [GitHub profile](https://github.com/arjun9669)
