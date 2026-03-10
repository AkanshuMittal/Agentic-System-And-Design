import json

data = """{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
"""

parsed = json.loads(data)

print(f"Request ID: {parsed['id']}")
print(f"Status: {parsed['status']}")
print(f"Text result: {parsed['result']['text']}")
print(f"Confidence score: {parsed['result']['confidence']}")

if parsed['result']['confidence'] < 0.9:
    print("Warning: Low confidence in result.")
    
# Create new dictionary
follow_up = {
    "request_id": parsed['id'],
    "status": parsed['status'],
    "processed": True,
    "confidence": parsed['result']['confidence']
}

json_output = json.dumps(follow_up)
print(json_output)

with open("python-json-assignment/response.json", "w") as f:
    json.dump(follow_up, f)
