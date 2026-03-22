import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = api_key)

class GeminiBot:
    def __init__(self, model_name = "gemini-2.5-flash"):
        self.model = genai.GenerativeModel(
            model_name = model_name, 
            system_instruction = "Your are profesional manager of restaurant and you are super creative menu compositor. Your goal is to create simple but amazing menu for restarants"
        )
        self.chat_session = self.model.start_chat(history=[])
    
    def ask(self, message):
        response = self.chat_session.send_message(message)
        return response.text
          

