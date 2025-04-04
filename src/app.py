# app.py
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import streamlit as st
from combined_recommender import smart_recommend

# Accuracy evaluation support
def evaluate_inline():
    from evaluate import benchmark_queries
    recall_total, map_total = 0, 0
    N = len(benchmark_queries)

    for q in benchmark_queries:
        results = smart_recommend(q['query'], top_k=3)
        recommended_names = [r['name'].lower() for r in results]
        relevant = [name.lower() for name in q['relevant']]

        # Recall@3
        matched = sum(1 for name in relevant if name in recommended_names)
        recall = matched / len(relevant)

        # MAP@3
        avg_precision = 0
        hits = 0
        for idx, name in enumerate(recommended_names):
            if name in relevant:
                hits += 1
                avg_precision += hits / (idx + 1)
        avg_precision = avg_precision / min(3, len(relevant))

        recall_total += recall
        map_total += avg_precision

    return round(recall_total / N, 2), round(map_total / N, 2)


st.set_page_config(page_title="SHL Assessment Recommender", page_icon="✅", layout="centered")

# --- Header ---
st.markdown("""
<h1 style='text-align: center;'>🔍 SHL Assessment Recommender</h1>
<p style='text-align: center; font-size: 18px; color: gray;'>
Intelligently recommend SHL tests from a job description or natural query
</p>
<hr>
""", unsafe_allow_html=True)

# --- Input Area ---
query = st.text_area("📝 Enter a job description or query", height=150, placeholder="E.g. Looking for a 30-minute Python and SQL test with behavioral and technical coverage")

if st.button("🎯 Recommend Assessments"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Running Gemini + Search..."):
            results = smart_recommend(query)

        if results:
            st.success(f"✅ Found {len(results)} recommendations")
            for r in results:
                with st.container():
                    st.markdown(f"""
                    <div style='padding: 15px; border: 1px solid #eee; border-radius: 10px; margin-bottom: 15px; background-color: #f9f9f9;'>
                        <h4 style='margin-bottom: 5px;'>{r['name']}</h4>
                        <p style='margin: 0;'><strong>Type:</strong> {r['type']} | <strong>Duration:</strong> {r['duration']}</p>
                        <p style='margin: 0;'><strong>Remote:</strong> {r['remote']} | <strong>Adaptive:</strong> {r['adaptive']}</p>
                        <p style='margin-top: 10px; color: #333;'>{r['description']}</p>
                        <a href='{r['url']}' target='_blank'>🔗 View on SHL Catalog</a>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.warning("❌ No assessments matched your filters.")

# --- Accuracy Metrics Section ---
st.markdown("<hr><h3>📊 Accuracy Metrics</h3>", unsafe_allow_html=True)
if st.button("🧪 Evaluate Accuracy on Benchmark Queries"):
    with st.spinner("Evaluating Recall@3 and MAP@3..."):
        recall, map_score = evaluate_inline()
        st.success(f"🎯 Mean Recall@3: **{recall}**")
        st.success(f"📈 Mean MAP@3: **{map_score}**")
