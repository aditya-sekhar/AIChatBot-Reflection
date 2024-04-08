# llm.py
from openai import OpenAI
from LLM import LLM
from config import OPENAI_API_KEY

class OpenAILLM(LLM):
    def __init__(self,prompt):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = "gpt-3.5-turbo"
        self.temperature = 0.5
        self.prompt = prompt

    def get_response(self, user_message):
        messages = [
            {"role": "system", "content": self.prompt},
            {"role": "user", "content": user_message},
        ]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature
        )
        generated_text = response.choices[0].message.content
        print("***************\n\n")
        print(generated_text)
        print("***************\n\n")
        return generated_text