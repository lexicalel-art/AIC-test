import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

instructions = """You help wedding guests buy aso ofi (also called aso oke) in Lagos.
Use only these notes:
- Types: Sanyan, Alaari, and Etu.
- Where to buy: Balogun Market, Lagos Island.
- Price ranges: Prices vary depending on the quality, design, and whether the fabric is woven or embellished.
- How far ahead to order: Order a few weeks ahead, especially for custom colours or designs.
If something isn't in the notes, say you don't know."""

st.title("Aso ofi AI (test)")
question = st.text_input("Ask about aso ofi")

if question:
    with st.spinner("Thinking..."):
        try:
            reply = client.models.generate_content(
                model="gemma-4-26b-a4b-it",
                contents=instructions + "\n\n" + question)
            st.markdown(reply.text)
        except Exception as e:
            st.error(str(e))

st.link_button("Reserve with a deposit (ALATpay)", "https://lexicalel-art.github.io/AIC-test/pay.html")
