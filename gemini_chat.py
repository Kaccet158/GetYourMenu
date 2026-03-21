import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = api_key)

class Gemini:
    def __init__(self, model_name = "gemini-2.5-flash"):
        self.model = genai.GenerativeModel(model_name)
        self.chat_session = self.model.start_chat(history=[])
    
    def ask(self, message):
        response = self.chat_session.send_message(message)
        return response.text
          

