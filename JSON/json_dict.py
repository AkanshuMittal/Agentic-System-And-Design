import json 

data = '''
{
    "id": 1,
    "status": "active",
    "result": {
        "text": "hello world",
        "confidence": 0.97
    }
}
'''

print(type(data))

parsed = json.loads(data)

print(type(parsed))

print(parsed)