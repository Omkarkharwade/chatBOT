import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')


if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are an AI assistant.")]

st.set_page_config(page_title="AI  Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 AI Chatbot")
st.markdown("Ask me anything!")


user_input = st.text_input("You:", placeholder="Type something...")

if st.button("Send") or user_input:
    if user_input:
        st.session_state.chat_history.append(HumanMessage(content=user_input))

        with st.spinner("AI is thinking..."):
            result = model.invoke(st.session_state.chat_history)

        st.session_state.chat_history.append(AIMessage(content=result.content))


for msg in st.session_state.chat_history[1:]: 
    if isinstance(msg, HumanMessage):
        st.markdown(f"**You:** {msg.content}")
    elif isinstance(msg, AIMessage):
        st.markdown(f"**AI:** {msg.content}")
