import json
import os

# Loading responses from Json file
file_path = os.path.join(os.path.dirname(__file__), "responses.json")
with open(file_path, "r") as file:
    responses = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return responses["default"]

# Chat loop
print("Hello! I'm MediBot. Ask me about your symptoms (type 'exit' to quit).\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("MediBot: Take care! Bye ")
        break
    response = get_response(user_input)
    print("MediBot:", response)