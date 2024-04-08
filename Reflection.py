import streamlit as st
from OpenAILLM import OpenAILLM
from GeminiLLM import GemaniLLM

st.title('Chatbot')

# Create the chatbot instances
openai_chatbot = OpenAILLM('You create simple code and then improve based on feedback')
gemini_chatbot = GemaniLLM("Provide one actionable feedback for the code. without examples.")

itr_count = st.selectbox('Number of iterations:', [1, 2, 3, 4, 5],1)
user_message = st.text_input('Enter your message:')
if st.button('Send'):
    for i in range(itr_count):
        # OpenAI generates a response
        openai_response = openai_chatbot.get_response(user_message)
        st.markdown(f'**OpenAI Response:**')
        st.code(openai_response, language='python')

        # Gemini reviews the response
        gemini_response = gemini_chatbot.get_response(openai_response)
        st.markdown(f'**Gemini Review:**')
        st.code(gemini_response, language='python')

        # The Gemini response becomes the new user message for the next iteration
        user_message = gemini_response