import requests
from vortexaihub.config import NEWS_API_KEY, NEWS_PAGE_SIZE
from vortexaihub.utils.text_processors import extract_topic

def get_news(query):
    """
    Get news information based on a topic
    
    Args:
        query (str): The user's input query
        
    Returns:
        str: News information response
    """
    # Extract topic from query
    topic = extract_topic(query)
    
    try:
        # Call News API
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "apiKey": NEWS_API_KEY,
            "language": "en",
            "pageSize": NEWS_PAGE_SIZE
        }
        
        if topic:
            params["q"] = topic
        else:
            params["category"] = "general"
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200 and data.get("articles"):
            news_info = f"Latest news{' about ' + topic if topic else ''}:\n\n"
            
            for i, article in enumerate(data["articles"][:NEWS_PAGE_SIZE], 1):
                title = article.get("title", "No title")
                source = article.get("source", {}).get("name", "Unknown source")
                url = article.get("url", "#")
                
                news_info += f"{i}. {title} ({source})\n"
            
            return news_info
        else:
            return f"Sorry, I couldn't retrieve news information{' about ' + topic if topic else ''}."
    
    except Exception as e:
        return f"Error retrieving news data: {str(e)}"