import re

import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

def extract_location(query):
    # Process the query with spaCy
    doc = nlp(query)

    # Extract locations using Named Entity Recognition (NER)
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC"]:  # GPE (Geopolitical Entity) and LOC (Location)
            return ent.text

    return None  # Return None if no location is found

def extract_topic(query):
    """
    Extract topic information from a user query
    
    Args:
        query (str): The user's input query
        
    Returns:
        str or None: Extracted topic or None if not found
    """
    topic_patterns = [
        r"about ([A-Za-z\s]+)(?:\?|$|\s)",
        r"on ([A-Za-z\s]+)(?:\?|$|\s)",
        r"related to ([A-Za-z\s]+)(?:\?|$|\s)"
    ]
    
    for pattern in topic_patterns:
        match = re.search(pattern, query)
        if match:
            return match.group(1).strip()
    
    return None