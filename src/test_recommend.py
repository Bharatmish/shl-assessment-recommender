from recommender import get_recommendations

query = "Looking for a cognitive test to assess problem-solving under 30 minutes"
results = get_recommendations(query, top_k=5)

for i, item in enumerate(results, 1):
    print(f"\n#{i}: {item['name']}")
    print(f"   Type: {item['type']} | Duration: {item['duration']}")
    print(f"   Remote: {item['remote']} | Adaptive: {item['adaptive']}")
    print(f"   URL: {item['url']}")
    print(f"   Description: {item['description']}")
