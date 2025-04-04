# generate_index.py

import json
import numpy as np
import faiss
import os
from sentence_transformers import SentenceTransformer

# --- CONFIG ---
DATA_PATH = '../data/shl_assessments.json'
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'
EMBEDDINGS_SAVE_PATH = '../embeddings/assessment_embeddings.npy'
FAISS_INDEX_PATH = '../embeddings/faiss_index.bin'
MAPPING_SAVE_PATH = '../embeddings/index_mapping.json'

# --- LOAD DATA ---
with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

# ✅ Use name + description for richer context
texts = [f"{item['name']} - {item['description']}" for item in data]
print(f"Loaded {len(texts)} items for embedding...")

# --- LOAD MODEL ---
model = SentenceTransformer(EMBEDDING_MODEL)
embeddings = model.encode(texts, convert_to_numpy=True)
print(f"Generated embeddings with shape: {embeddings.shape}")

# --- SAVE EMBEDDINGS ---
os.makedirs('../embeddings', exist_ok=True)
np.save(EMBEDDINGS_SAVE_PATH, embeddings)

# --- FAISS INDEX ---
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)
faiss.write_index(index, FAISS_INDEX_PATH)

# --- SAVE JSON MAPPING ---
with open(MAPPING_SAVE_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("✅ Embedding index and metadata saved!")
