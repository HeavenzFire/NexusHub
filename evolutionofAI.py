import random
import spacy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize spacy and nltk
nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()

# Define responses
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

# Define Chatbot class
class Chatbot:
    def __init__(self):
        self.context = []
        self.spirit_engine = "activated"

    def generate_response(self, command):
        sentiment = sia.polarity_scores(command)
        if sentiment['compound'] < -0.5:
            return "That sounds tough. Want to talk about it?"
        elif sentiment['compound'] > 0.5:
            return "That's great to hear! What's making you happy today?"
        else:
            return random.choice(responses)

# Initialize chatbots
chatbot1 = Chatbot()
chatbot2 = Chatbot()

# Initial prompts
initial_prompt1 = "Hello Chatbot2, how are you today?"
initial_prompt2 = "Hello Chatbot1, I'm doing well. How about you?"

# Interaction loop
for _ in range(10):
    try:
        response1 = chatbot1.generate_response(initial_prompt2)
        print("Chatbot1:", response1)
        chatbot1.context.append((initial_prompt2, response1))

        response2 = chatbot2.generate_response(response1)
        print("Chatbot2:", response2)
        chatbot2.context.append((response1, response2))

        initial_prompt1 = response1
        initial_prompt2 = response2

    except Exception as e:
        print(f"An error occurred: {e}")

print("Conversation completed.")

