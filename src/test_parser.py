from query_parser import parse_query_with_llm

query = "Looking for a 30-minute Python and SQL test with behavioral traits and soft skills"
result = parse_query_with_llm(query)

print("\n🎯 Extracted Structured Data:")
print(result)
