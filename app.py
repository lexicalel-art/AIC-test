import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("Lagos guide (test)")
question = st.text_input("Ask anything about Lagos")

if question:
    with st.spinner("Thinking..."):
        try:
            reply = client.models.generate_content(model="gemma-4-26b-a4b-it", contents=question)
            st.markdown(reply.text)
        except Exception as e:
            st.error(str(e))
