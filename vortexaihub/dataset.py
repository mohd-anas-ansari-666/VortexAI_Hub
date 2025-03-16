def get_training_data():
    return [
        # Weather intents
        {"text": "what's the weather like today", "intent": "weather"},
        {"text": "weather forecast for tomorrow", "intent": "weather"},
        {"text": "will it rain today", "intent": "weather"},
        {"text": "temperature in New York", "intent": "weather"},
        {"text": "how hot is it outside", "intent": "weather"},
        {"text": "weather conditions in London", "intent": "weather"},
        {"text": "is it going to snow this weekend", "intent": "weather"},
        {"text": "current weather in Tokyo", "intent": "weather"},
        {"text": "weather in Paris today", "intent": "weather"},
        {"text": "forecast for next week", "intent": "weather"},
        {"text": "will it be sunny in the afternoon", "intent": "weather"},
        {"text": "how cold is it in Toronto", "intent": "weather"},
        {"text": "when is the next storm coming", "intent": "weather"},
        {"text": "weather updates in Dubai", "intent": "weather"},
        {"text": "current temperature in San Francisco", "intent": "weather"},

        # AQI intents
        {"text": "what's the air quality today", "intent": "aqi"},
        {"text": "air quality index in Delhi", "intent": "aqi"},
        {"text": "is the air pollution bad today", "intent": "aqi"},
        {"text": "AQI levels in Beijing", "intent": "aqi"},
        {"text": "pollution levels near me", "intent": "aqi"},
        {"text": "air quality forecast", "intent": "aqi"},
        {"text": "PM2.5 levels in my area", "intent": "aqi"},
        {"text": "is it safe to go outside with current air quality", "intent": "aqi"},
        {"text": "air quality in Los Angeles", "intent": "aqi"},
        {"text": "how is the air quality in London today", "intent": "aqi"},
        {"text": "current pollution in Mumbai", "intent": "aqi"},
        {"text": "will the air quality improve tomorrow", "intent": "aqi"},
        {"text": "PM10 levels in Beijing", "intent": "aqi"},
        {"text": "what are the pollutants in the air right now", "intent": "aqi"},
        {"text": "is the air quality dangerous in my city", "intent": "aqi"},

        # News intents
        {"text": "latest news", "intent": "news"},
        {"text": "what's happening in the world", "intent": "news"},
        {"text": "breaking news today", "intent": "news"},
        {"text": "news about technology", "intent": "news"},
        {"text": "current events", "intent": "news"},
        {"text": "sports news", "intent": "news"},
        {"text": "business headlines", "intent": "news"},
        {"text": "what's in the news about climate change", "intent": "news"},
        {"text": "political news today", "intent": "news"},
        {"text": "latest news in the world of finance", "intent": "news"},
        {"text": "news about the stock market", "intent": "news"},
        {"text": "what's happening in Hollywood", "intent": "news"},
        {"text": "updates from the world of science", "intent": "news"},
        {"text": "global news on health and wellness", "intent": "news"},
        {"text": "is there any news about space exploration", "intent": "news"},

        # Greeting intents
        {"text": "hello", "intent": "greeting"},
        {"text": "hi there", "intent": "greeting"},
        {"text": "hey", "intent": "greeting"},
        {"text": "good morning", "intent": "greeting"},
        {"text": "good afternoon", "intent": "greeting"},
        {"text": "howdy", "intent": "greeting"},
        {"text": "greetings", "intent": "greeting"},
        {"text": "nice to meet you", "intent": "greeting"},
        {"text": "hi", "intent": "greeting"},
        {"text": "yo", "intent": "greeting"},
        {"text": "what's up", "intent": "greeting"},
        {"text": "good evening", "intent": "greeting"},
        {"text": "sup", "intent": "greeting"},
        {"text": "how's it going", "intent": "greeting"},

        # General intents (fallback to Gemini)
        {"text": "tell me a joke", "intent": "general"},
        {"text": "what can you do", "intent": "general"},
        {"text": "who are you", "intent": "general"},
        {"text": "give me information about machine learning", "intent": "general"},
        {"text": "explain quantum computing", "intent": "general"},
        {"text": "how to make pasta", "intent": "general"},
        {"text": "tell me about the history of Rome", "intent": "general"},
        {"text": "what's the meaning of life", "intent": "general"},
        {"text": "who invented the internet", "intent": "general"},
        {"text": "tell me about ancient Egypt", "intent": "general"},
        {"text": "how does the brain work", "intent": "general"},
        {"text": "what is artificial intelligence", "intent": "general"},
        {"text": "what's the tallest mountain in the world", "intent": "general"},
        {"text": "can you explain the theory of relativity", "intent": "general"},
        {"text": "what is a black hole", "intent": "general"},
        {"text": "how can I improve my productivity", "intent": "general"},
        {"text": "tell me the history of the Roman Empire", "intent": "general"},
        {"text": "what is the capital of Japan", "intent": "general"},
        {"text": "tell me about Leonardo da Vinci", "intent": "general"},
        {"text": "what's the largest ocean", "intent": "general"},
        {"text": "who is the president of the United States", "intent": "general"},
        {"text": "what happened during World War II", "intent": "general"},
        {"text": "how do vaccines work", "intent": "general"},
        {"text": "what is blockchain technology", "intent": "general"}
    ]

import pandas as pd

def save_dataset_to_csv(filename="training_data.csv"):
    # Convert dataset to pandas DataFrame
    data = get_training_data()
    df = pd.DataFrame(data)
    
    # Save DataFrame to CSV
    df.to_csv(filename, index=False)
    print(f"Dataset saved to {filename}")

# Example usage
if __name__ == "__main__":
    save_dataset_to_csv("training_data.csv")