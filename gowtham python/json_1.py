import json

quiz = {
    "question": "What does len() return?",
    "answer": "The number of items"
}

text = json.dumps(quiz)
print(text)

parsed = json.loads(text)
print(parsed["answer"])
