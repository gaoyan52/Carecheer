import streamlit as st

from PIL import Image

import requests

import random

 

st.title("🌟 Care & Cheer App")

st.write("Upload your selfie to receive an encouraging message!")

 

uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

 

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption='Your uploaded image', use_container_width=True)

   

    # Simple encouraging message logic

    messages = [

        "You're doing amazing work! 💪",

        "Your care makes a difference! ❤️",

        "Keep up the excellent work! 🌟"

    ]

   

    st.success(random.choice(messages))