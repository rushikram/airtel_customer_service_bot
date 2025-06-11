import streamlit as st
from typing import TypedDict
from main import chat_with_airtel  # Ensure this exists and works
import re

# Page configuration
st.set_page_config(
    page_title="Airtel Customer Service Bot",
    page_icon="📱",
    layout="centered"
)

# Custom styling with blinking cursor effect
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        background-color: white;
        color: black;
        caret-color: red; /* Cursor color */
        animation: blink 1s step-end infinite;
    }

    @keyframes blink {
        50% { caret-color: transparent; }
    }

    .user-message {
        background-color: #003366;
        color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: right;
    }

    .bot-message {
        background-color: #1e1e1e;
        color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Utility to remove HTML tags from bot output
def clean_html(text):
    return re.sub(re.compile('<.*?>'), '', text)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "bot_state" not in st.session_state:
    st.session_state.bot_state = None
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Function to handle input and get response
def process_input():
    try:
        user_msg = st.session_state.user_input.strip()
        if user_msg:
            st.session_state.chat_history.append(("user", user_msg))
            st.session_state.bot_state = chat_with_airtel(user_msg, st.session_state.bot_state)

            messages = st.session_state.bot_state.get("messages", [])
            bot_response = messages[-1].content if messages else "Sorry, no response."
            st.session_state.chat_history.append(("bot", bot_response))
    except Exception as e:
        st.session_state.chat_history.append(("bot", f"Error occurred: {e}"))
        st.error(f"[Process Input Failed]: {e}")
    finally:
        st.session_state.user_input = ""

# Header
st.title("Airtel Customer Service Bot 📱")
st.markdown("""
Welcome to Airtel's customer service! I can help you with:
- General information about Airtel services  
- SIM swap requests  
- Checking your plan details  
""")

# Show conversation history
for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(f'<div class="user-message">You: {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">Airtel Bot: {message}</div>', unsafe_allow_html=True)

# Input box for user message
st.text_input("Type your message here...", key="user_input", on_change=process_input)
