import random
import datetime
import json
import os
import sys
import ast
import operator

# ---------------------- UTF-8 SUPPORT ----------------------
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ---------------------- FILES ----------------------
HISTORY_FILE = "chat_history.txt"
USER_FILE = "user_data.json"
NOTES_FILE = "notes.txt"

# ---------------------- LOAD USER ----------------------
def load_user():
    if os.path.exists(USER_FILE):
        try:
            with open(USER_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {"name": "User"}

def save_user(user):
    with open(USER_FILE, "w") as f:
        json.dump(user, f)

user_data = load_user()

# ---------------------- RESPONSES ----------------------
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": [
        "I'm doing great!",
        "I'm fine, thank you!",
        "All good!"
    ],
    "thanks": [
        "You're welcome!",
        "Glad to help!",
        "Anytime!"
    ]
}

# ---------------------- DATE & TIME ----------------------
def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_date():
    return datetime.datetime.now().strftime("%d-%m-%Y")

# ---------------------- CHAT HISTORY ----------------------
def save_chat(line):
    with open(HISTORY_FILE, "a") as f:
        f.write(line + "\n")

def show_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return f.read()
    return "No chat history found."

# ---------------------- NOTES ----------------------
def add_note(note):
    if note == "":
        return "Please enter a note."

    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")

    return "Note saved!"

def show_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            data = f.read().strip()
            if data:
                return data

    return "No notes found."

# ---------------------- MOOD DETECTION ----------------------
def detect_mood(text):
    sad_words = ["sad", "upset", "tired", "depressed"]
    happy_words = ["happy", "great", "good", "awesome"]

    for word in sad_words:
        if word in text:
            return "Don't worry. Things will get better."

    for word in happy_words:
        if word in text:
            return "That's awesome! Keep smiling."

    return None

# ---------------------- SAFE MATH ----------------------
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg
}

def calculate(node):
    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.BinOp):
        return operators[type(node.op)](
            calculate(node.left),
            calculate(node.right)
        )

    if isinstance(node, ast.UnaryOp):
        return operators[type(node.op)](
            calculate(node.operand)
        )

    raise TypeError

def solve_math(expression):
    try:
        tree = ast.parse(expression, mode="eval")
        answer = calculate(tree.body)
        return f"Answer: {answer}"
    except:
        return "Invalid math expression."

# ---------------------- CHATBOT ----------------------
def chatbot_response(user_input):

    # Save user's name
    if "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip().title()

        if name:
            user_data["name"] = name
            save_user(user_data)
            return f"Nice to meet you, {name}!"

    # Recall user's name
    if "what is my name" in user_input:
        return f"Your name is {user_data['name']}."

    # Time
    if "time" in user_input:
        return "Current Time: " + get_time()

    # Date
    if "date" in user_input:
        return "Today's Date: " + get_date()

    # Show Notes
    if "show notes" in user_input:
        return show_notes()

    # Add Note
    if user_input.startswith("note"):
        note = user_input.replace("note", "", 1).strip()
        return add_note(note)

    # History
    if "history" in user_input:
        return show_history()

    # Math
    if any(ch.isdigit() for ch in user_input):
        return solve_math(user_input)

    # Mood
    mood = detect_mood(user_input)
    if mood:
        return mood

    # Normal Responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # Exit
    if user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day."

    return "Sorry, I don't understand."

# ---------------------- MAIN ----------------------
def start_chat():
    print(f"\nSmartBot Started! Welcome {user_data['name']}!")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").strip().lower()

        save_chat("You: " + user)

        response = chatbot_response(user)

        print("Bot:", response)

        save_chat("Bot: " + response)

        if user in ["bye", "exit", "quit"]:
            break

# ---------------------- RUN ----------------------
if __name__ == "__main__":
    start_chat()