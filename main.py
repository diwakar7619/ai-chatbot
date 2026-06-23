import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def get_ai_response(messages):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", messages=messages
    )

    return response.choices[0].message.content


st.title("AI Chatbot")

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

user_message = st.chat_input("Type a message")

if user_message:
    st.session_state.messages.append({"role": "user", "content": user_message})

    ai_reply = get_ai_response(st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
