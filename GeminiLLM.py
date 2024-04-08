from LLM import LLM
import google.generativeai as genai
from config import GEMINI_API_KEY


class GemaniLLM(LLM):

    def __init__(self,prompt):
        genai.configure(api_key = GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        self.prompt = prompt

    def get_response(self,message):
        message = self.prompt + message
        response = self.model.generate_content(message)
        base = "Sure !\n "
        generated_text = base+response.candidates[0].content.parts[0].text
        print("***************\n\n")
        print(generated_text)
        print("***************\n\n")
        return generated_text