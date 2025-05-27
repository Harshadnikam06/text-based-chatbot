import nltk
from nltk.chat.util import Chat, reflections

# You may need to download these once
# nltk.download('punkt')

# Define some basic patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great, how about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry about it", "It's okay"]
    ],
    [
        r"what is your name ?",
        ["You can call me Chatty!", "I'm a chatbot, nice to meet you!"]
    ],
    [
        r"how can you help me ?",
        ["I can chat with you, answer your questions, or just keep you company!"]
    ],
    [
        r"(.*) your name ?",
        ["I'm called Chatty, your friendly assistant."]
    ],
    [
        r"quit",
        ["Bye-bye!", "See you soon!", "Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase?", "Interesting... tell me more!", "Let's talk about something else."]
    ]
]

# Create and run the chatbot
def start_chat():
    print("Hi! I'm Chatty, your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run chatbot
if __name__ == "__main__":
    start_chat()
