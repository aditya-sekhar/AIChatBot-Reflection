import streamlit as st
from OpenAILLM import OpenAILLM
from GeminiLLM import GemaniLLM

st.title('Chatbot')

# Select the chatbot implementation
chatbot_type = st.selectbox('Select the chatbot type:', ['OpenAI', 'Gemini'])

# Create the chatbot instance
if chatbot_type == 'OpenAI':
    chatbot = OpenAILLM('You are a intelligent chatbot, and will provide short answers')
else:
    chatbot = GemaniLLM('You are a intelligent chatbot, and will provide short answers')

user_message = st.text_input('Enter your message:')
if st.button('Send'):
    response = chatbot.get_response(user_message)
    st.markdown(f'**Response:** {response}')