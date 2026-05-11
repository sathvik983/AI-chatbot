import tkinter as tk
from tkinter import scrolledtext
import random
import datetime

# Chatbot responses
responses = {
    "hello": ["Hello! 👋", "Hi there!", "Hey!"],
    "how are you": ["I'm doing great!", "Awesome!", "Doing well!"],
    "your name": ["I'm AlgoBot 🤖", "AI Chatbot here!"],
    "time": [f"Current time is {datetime.datetime.now().strftime('%H:%M:%S')}"],
    "date": [f"Today's date is {datetime.date.today()}"],
    "bye": ["Goodbye!", "See you soon!", "Take care!"],
    "help": ["Ask me about date, time, greetings and more!"]
}

# Function to process messages
def send_message():

    user_message = user_input.get()

    if user_message.strip() == "":
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_message + "\n", "user")

    user_input.delete(0, tk.END)

    response = "Sorry, I don't understand."

    for key in responses:
        if key in user_message.lower():
            response = random.choice(responses[key])
            break

    chat_area.insert(tk.END, "Bot: " + response + "\n\n", "bot")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

# Main window
window = tk.Tk()
window.title("AI Chatbot")
window.geometry("500x600")
window.configure(bg="#1e1e1e")

# Heading
heading = tk.Label(
    window,
    text="AI CHATBOT",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)

heading.pack(pady=10)

# Chat area
chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    font=("Arial", 12),
    bg="#2b2b2b",
    fg="white"
)

chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_area.tag_config("user", foreground="cyan")
chat_area.tag_config("bot", foreground="lightgreen")

chat_area.config(state=tk.DISABLED)

# Input frame
input_frame = tk.Frame(window, bg="#1e1e1e")
input_frame.pack(pady=10)

# User input
user_input = tk.Entry(
    input_frame,
    width=30,
    font=("Arial", 14)
)

user_input.grid(row=0, column=0, padx=10)

# Send button
send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=send_message
)

send_button.grid(row=0, column=1)

# Run app
window.mainloop()
