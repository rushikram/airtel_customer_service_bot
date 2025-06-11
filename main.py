import os
from typing import Sequence, TypedDict, Optional
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]


if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please add it to your .env file.")

# Initialize model and embeddings
model = ChatGroq(api_key=GROQ_API_KEY, model_name="llama3-70b-8192")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Vector store setup
def create_vector_db(knowledge_file: str):
    with open(knowledge_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(raw_text)
    vector_store = FAISS.from_texts(chunks, embeddings)
    return vector_store

vector_store = create_vector_db('./airtel_knowledge.txt')

# Agent state definition
class AgentState(TypedDict):
    messages: Sequence[BaseMessage]
    current_agent: str
    user_details: dict
    intent: str

# General query agent
def general_query_agent(state: AgentState) -> AgentState:
    latest_message = state["messages"][-1].content
    context_chunks = vector_store.similarity_search(latest_message, k=3)
    context = "\n".join([chunk.page_content for chunk in context_chunks])

    prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are an Airtel bot. Use the following context:\n{context}"),
        ("human", "{question}")
    ])

    response = model.invoke(prompt.format_messages(question=latest_message))
    state["messages"].append(AIMessage(content=response.content))
    return state

# Streamlit-friendly function
def chat_with_airtel(user_query: str, prev_state: Optional[AgentState] = None) -> AgentState:
    if prev_state is None:
        prev_state = AgentState(
            messages=[],
            current_agent="general_query",
            user_details={},
            intent="general_query"
        )
    prev_state["messages"].append(HumanMessage(content=user_query))
    return general_query_agent(prev_state)

# Optional CLI test
if __name__ == "__main__":
    result = chat_with_airtel("What is the Airtel Black plan?")
    print(result["messages"][-1].content)
