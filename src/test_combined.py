from combined_recommender import smart_recommend

query = "Looking for a 30-minute Python and SQL test with behavioral and technical coverage"

results = smart_recommend(query, top_k=5)

print("\n🎯 Final Filtered Recommendations:\n")
for i, item in enumerate(results, 1):
    print(f"#{i}: {item['name']}")
    print(f"   Type: {item['type']} | Duration: {item['duration']}")
    print(f"   Remote: {item['remote']} | Adaptive: {item['adaptive']}")
    print(f"   URL: {item['url']}")
    print(f"   Description: {item['description']}\n")
