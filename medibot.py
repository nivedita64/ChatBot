import json
import os
import tkinter as tk

# Loading responses from JSON file
file_path = os.path.join(os.path.dirname(__file__), "responses.json")
with open(file_path, "r") as file:
    responses = json.load(file)

# Response function
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return responses.get("default", "Sorry, I couldn't understand. Can you please rephrase your symptoms?")

# GUI setup
def send_message():
    user_input = entry.get()
    chat_log.insert(tk.END, f"You: {user_input}\n")
    response = get_response(user_input)
    chat_log.insert(tk.END, f"MediBot: {response}\n\n")
    entry.delete(0, tk.END)

# Creating window
root = tk.Tk()
root.title("MediBot - Chat with me!")
root.geometry("400x500")

chat_log = tk.Text(root, bg="light green", fg="black")
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=(0,10), side=tk.LEFT, expand=True, fill=tk.X)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=(0,10), side=tk.RIGHT)

root.mainloop() 


