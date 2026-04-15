import google.generativeai as genai
import numpy as np
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def get_embedding(text):
    model = "models/text-embedding-004"
    result = genai.embed_content(
        model=model,
        content=text
    )
    return np.array(result['embedding'])