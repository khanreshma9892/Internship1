import nltk
import random
import string
from nltk.corpus import wordnet
from nltk.chat.util import Chat, reflections

# Download required NLTK data files (only first time)
nltk.download('punkt')
nltk.download('wordnet')

# Sample conversation pairs
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    [r"what is your name?", ["I'm a simple AI chatbot.", "You can call me Chatbot."]],
    [r"how are you?", ["I'm doing well, thank you!", "I'm just a program, but I'm functioning properly!"]],
    [r"what can you do?", ["I can chat with you and answer some simple questions."]],
    [r"bye|exit|quit", ["Goodbye!", "Have a nice day!", "Bye! See you later."]],
]

# Define a simple chatbot using NLTK's Chat classmmmm
def chatbot():
    print("Hi! I'm a chatbot. Type 'quit' to exit.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbothi

if __name__ == "__main__":
    chatbot()
