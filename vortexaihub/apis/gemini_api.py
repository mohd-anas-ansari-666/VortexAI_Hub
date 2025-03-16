import google.generativeai as genai
from vortexaihub.config import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(query):
    """
    Get response from Gemini 1.5 Pro model
    
    Args:
        query (str): The user's input query
        
    Returns:
        str: Gemini model response
    """
    try:
        # Safety settings to ensure appropriate responses
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
        ]
        
        # Configure the Gemini model
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        # Generate response
        response = model.generate_content(
            query,
            safety_settings=safety_settings,
            generation_config={
                "temperature": 0.7,
                "top_p": 0.9,
                "top_k": 40,
                "max_output_tokens": 1024,
            }
        )
        
        return response.text
    except Exception as e:
        return f"I'm sorry, I had trouble processing that request. Error: {str(e)}"