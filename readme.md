# 🔍 SHL Assessment Recommendation System

This project is an end-to-end AI-based system that recommends the most relevant SHL assessments for recruiters based on **natural language job descriptions** or **free-form queries**.

It combines the power of **Google Gemini LLMs** for query parsing and **FAISS semantic search** for matching assessments, making it a fast, intelligent, and accurate alternative to manual keyword filtering.

---

## 🚀 Features

- ✅ Accepts **natural language job queries** or JD text
- 🤖 Parses out **skills, duration, test types** using **Gemini 1.5 Pro**
- 🔎 Uses **Sentence Transformers + FAISS** to match with SHL assessments
- 📋 Returns **top 10 relevant tests** with rich metadata (duration, type, adaptive, remote)
- 📊 Evaluates system with **Mean Recall@3** and **MAP@3**
- 🌐 Streamlit-based frontend with clean design
- 🔌 FastAPI backend to expose recommendation API

---

## 🧪 Example Queries

```text
1. Looking for a 30-minute Python and SQL test with behavioral and technical coverage
2. Hiring for an analyst. Need cognitive and personality test under 45 minutes
3. Hiring Java developers, must test technical and logical reasoning skills under 30 mins

🛠 Tech Stack
Component	Tool / Library
LLM Parsing	Google Gemini 1.5 Pro API
Embeddings	Sentence Transformers (MiniLM)
Vector Search	FAISS
Backend	FastAPI
Frontend	Streamlit
Evaluation	Custom Recall@K + MAP@K

📁 Folder Structure
SHL-ASSESSMENT-RECOMMENDER/
├── benchmark/               # Benchmark queries
│   └── test_queries.json
├── data/                    # SHL catalog JSON
│   └── shl_assessments.json
├── embeddings/              # FAISS index & vectors
│   ├── faiss_index.bin
│   ├── assessment_embeddings.npy
│   └── index_mapping.json
├── src/                     # Source code
│   ├── app.py               # Streamlit UI
│   ├── api.py               # FastAPI backend
│   ├── combined_recommender.py
│   ├── query_parser.py
│   ├── generate_index.py
│   ├── evaluate.py
│   └── test_*.py            # Unit testing & dev
├── .env                     # Gemini API key (not committed)
├── .env.example             # Sample environment file
├── requirements.txt         # Python dependencies
└── README.md                # This file

⚙️ Setup Instructions
🔧 1. Clone the Repository :
  git clone https://github.com/Bharatmish/shl-assessment-recommender.git
  cd shl-assessment-recommender

📦 2. Install Requirements
  pip install -r requirements.txt

🔐 3. Add Gemini API Key
  Create a .env file: GEMINI_API_KEY=your-gemini-api-key-here

📌 4. Build the Embedding Index
cd src
  python generate_index.py

🖥 5. Run Frontend (Streamlit)
  streamlit run app.py

🔗 6. Run API (Optional)
  uvicorn api:app --reload

Now open your browser at:
📍 http://localhost:8000/recommend?query=hiring%20python%20developer

📊 Accuracy Evaluation
  python src/evaluate.py

✍️ Author
Bharat Kumar Mishra 
