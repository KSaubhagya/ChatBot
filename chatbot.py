import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only once)
nltk.download('punkt')

# Define patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name ?",
        ["I am a simple chatbot. You can call me Chatty.",]
    ],
    [
        r"how are you ?",
        ["I'm good, thank you! How are you?",]
    ],
    [
        r"quit",
        ["Bye! Have a great day.", "See you later!"]
    ],
]
