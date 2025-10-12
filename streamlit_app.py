import streamlit as st
import random

# List of famous quotes
QUOTES = [
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
    ("Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill"),
    ("You miss 100% of the shots you don’t take.", "Wayne Gretzky"),
    ("The best way to predict the future is to invent it.", "Alan Kay"),
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
    ("Whether you think you can or you think you can’t, you’re right.", "Henry Ford"),
    ("If you want to lift yourself up, lift up someone else.", "Booker T. Washington"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("The purpose of our lives is to be happy.", "Dalai Lama"),
]

# Streamlit app layout
st.set_page_config(page_title="Random Quote Generator", page_icon="💬", layout="centered")

st.title("💬 Random Famous Quote")

# Random quote selection
if st.button("✨ Get a New Quote"):
    quote, author = random.choice(QUOTES)
    st.markdown(f"> **“{quote}”**  \n— *{author}*")
else:
    quote, author = random.choice(QUOTES)
    st.markdown(f"> **“{quote}”**  \n— *{author}*")

# Optional styling
st.markdown("---")
st.markdown("Made with ❤️ using [Streamlit](https://streamlit.io)")
