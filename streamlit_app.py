import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define the FastAPI endpoints
RAG_ENDPOINT = os.getenv("RAG_ENDPOINT", "http://localhost:8000/rag")
CLASSIFICATION_ENDPOINT = os.getenv("CLASSIFICATION_ENDPOINT", "http://localhost:8000/classification")

st.title("FastAPI with Streamlit")

# RAG interface
st.header("RAG (Retrieval-Augmented Generation)")
rag_prompt = st.text_input("Enter a prompt for RAG:")
if st.button("Get RAG Response"):
    with st.spinner('Fetching response...'):
        try:
            response = requests.post(RAG_ENDPOINT, json={"prompt": rag_prompt})
            response.raise_for_status()
            rag_result = response.json().get("response", "No response received.")
            st.success(rag_result)
        except requests.exceptions.RequestException as e:
            st.error(f"Error in fetching RAG response: {e}")

# Classification interface
st.header("Text Classification")
classification_text = st.text_input("Enter text for classification:")
if st.button("Classify Text"):
    with st.spinner('Classifying text...'):
        try:
            response = requests.post(CLASSIFICATION_ENDPOINT, json={"text": classification_text})
            response.raise_for_status()
            classification_result = response.json().get("label", "No label received.")
            st.success(classification_result)
        except requests.exceptions.RequestException as e:
            st.error(f"Error in fetching classification response: {e}")
