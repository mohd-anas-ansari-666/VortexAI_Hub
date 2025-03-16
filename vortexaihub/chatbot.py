import random
from vortexaihub.intent_classifier import IntentClassifier
from vortexaihub.apis import get_weather, get_aqi, get_news, get_gemini_response

class ChatBot:
    def __init__(self):
        """Initialize the chatbot with an intent classifier"""
        self.intent_classifier = IntentClassifier(model_path='intent_model.h5', vectorizer_path='tfidf_vectorizer.pkl', encoder_path='label_encoder.pkl', train=False)
    
    def get_greeting(self):
        """Return a random greeting message"""
        greetings = [
            "Hello there! How can I help you today?",
            "Hi! What would you like to know?",
            "Greetings! How may I assist you?",
            "Hey! I'm here to help. What's on your mind?",
            "Good day! What can I do for you today?"
        ]
        return random.choice(greetings)
    
    def process_query(self, query):
        """
        Process a user query and return an appropriate response
        
        Args:
            query (str): The user's input query
            
        Returns:
            str: Bot response based on intent classification
        """
        # Classify the intent of the query
        intent = self.intent_classifier.predict_intent(query)
        
        # Process the query based on the intent
        if intent == "weather":
            return get_weather(query)
        elif intent == "aqi":
            return get_aqi(query)
        elif intent == "news":
            return get_news(query)
        elif intent == "greeting":
            return self.get_greeting()
        else:  # General intent, use Gemini
            return get_gemini_response(query)