import google.generativeai as genai
from config import GEMINI_API_KEY, MODEL_NAME
from utils.prompts import COVER_LETTER_PROMPT

genai.configure(api_key=GEMINI_API_KEY)

def generate_cover_letter(resume, job):
    model = genai.GenerativeModel(MODEL_NAME)

    prompt = COVER_LETTER_PROMPT.format(
        resume=resume[:3000],
        job=job[:3000]
    )

    response = model.generate_content(prompt)
    return response.text