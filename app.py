from dotenv import load_dotenv
import os
import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import streamlit as st

# load environment variables from .env file
load_dotenv()

# set API key
openai.api_key = os.getenv("OPENAI_API_KEY")

chat = ChatOpenAI(temperature=0)

# Streamlit code
st.title('OpenAI Chat Model')

uploaded_file = st.file_uploader("Choose a document...", type=['txt', 'pdf'])

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio.read())
    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

user_input = st.text_input("Please enter your message:", "")

if st.button('Generate Response'):
    if user_input:
        response = chat.predict_messages([HumanMessage(content=user_input)])
        st.text(response.content)
    else:
        st.write("Please enter a message.")
