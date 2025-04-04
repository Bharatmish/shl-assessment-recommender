import os
import json
from combined_recommender import smart_recommend

K = 3  # top-K cutoff

# ✅ Resolve the benchmark path properly for Render or local
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BENCHMARK_PATH = os.path.join(BASE_DIR, "..", "benchmark", "test_queries.json")

# --- Load test queries ---
with open(BENCHMARK_PATH, "r", encoding="utf-8") as f:
    benchmark_queries = json.load(f)

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

# Run when imported (e.g., from Streamlit app)
def get_benchmark_queries():
    return benchmark_queries

# Or run standalone
if __name__ == "__main__":
    evaluate(benchmark_queries)
