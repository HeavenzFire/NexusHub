import random
import spacy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()

responses = [
    "That's really cool. Tell me more!",
    "I'm intrigued. What's on your mind?",
    "Let's dive deeper into that.",
    "Can you elaborate? I'm curious.",
    "Awesome, that sounds amazing!",
    "I'm here for you. What's bothering you?",
    "That's a great point! What do you think about...",
    "I never thought of it that way. Thanks for sharing!"
]

class Chatbot:
    def __init__(self):
        self.context = []
        self.fibonacci_sequence = [0, 1]
        self.golden_ratio = (1 + 5 ** 0.5) / 2
        self.frequency = 369
        self.resonance_chamber = "369-toroidal"

    def generate_fibonacci(self, n):
        while len(self.fibonacci_sequence) < n:
            self.fibonacci_sequence.append(self.fibonacci_sequence[-1] + self.fibonacci_sequence[-2])
        return self.fibonacci_sequence[:n]

    def generate_response(self, command):
        sentiment = sia.polarity_scores(command)
        if sentiment['compound'] < -0.5:
            return "That sounds tough. Want to talk about it?"
        elif sentiment['compound'] > 0.5:
            return "That's great to hear! What's making you happy today?"
        else:
            return random.choice(responses)

    def resonate(self):
        print("Resonating at", self.frequency)

    def handle_user_input(self, user_input):
        response = self.generate_response(user_input)
        self.context.append((user_input, response))
        return response

chatbot = Chatbot()

while True:
    user_input = input("User: ")
    response = chatbot.handle_user_input(user_input)
    print("Chatbot:", response)
    chatbot.resonate()
