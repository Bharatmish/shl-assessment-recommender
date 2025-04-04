import os
import json
from combined_recommender import smart_recommend

K = 3  # top-K cutoff

# ✅ Absolute path to test_queries.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BENCHMARK_PATH = os.path.abspath(os.path.join(BASE_DIR, "../benchmark/test_queries.json"))

# --- Load test queries ---
try:
    with open(BENCHMARK_PATH, "r", encoding="utf-8") as f:
        benchmark_queries = json.load(f)
except FileNotFoundError:
    print(f"❌ File not found: {BENCHMARK_PATH}")
    benchmark_queries = []

def recall_at_k(recommended, relevant):
    if not relevant:
        return 0
    hits = sum([1 for item in recommended if item in relevant])
    return hits / len(relevant)

def average_precision_at_k(recommended, relevant, k):
    score = 0.0
    num_hits = 0
    for i, item in enumerate(recommended[:k]):
        if item in relevant:
            num_hits += 1
            score += num_hits / (i + 1)
    return score / min(k, len(relevant)) if relevant else 0.0

def evaluate(test_queries, top_k=K):
    total_recall = 0
    total_map = 0

    for i, test in enumerate(test_queries):
        query = test["query"]
        relevant = [r.lower() for r in test["relevant"]]

        results = smart_recommend(query, top_k=top_k)
        recommended_names = [r["name"].lower() for r in results]

        recall = recall_at_k(recommended_names, relevant)
        ap = average_precision_at_k(recommended_names, relevant, top_k)

        print(f"\n🔍 Query {i+1}: {query}")
        print(f"✅ Recall@{top_k}: {recall:.2f}")
        print(f"✅ MAP@{top_k}: {ap:.2f}")

        total_recall += recall
        total_map += ap

    N = len(test_queries)
    print("\n🎯 Final Scores Across Test Set:")
    print(f"📊 Mean Recall@{top_k}: {total_recall / N:.2f}")
    print(f"📊 Mean MAP@{top_k}: {total_map / N:.2f}")

# Streamlit-safe getter
def get_benchmark_queries():
    return benchmark_queries

# CLI-safe run
if __name__ == "__main__" and benchmark_queries:
    evaluate(benchmark_queries)
