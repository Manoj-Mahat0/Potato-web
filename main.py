import streamlit as st
import requests
from PIL import Image

# Render API URL
api_url = "https://potato-leaf.onrender.com/predict"

st.title("Potato Leaf Disease Classifier")

uploaded_file = st.file_uploader("Choose a potato leaf image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

    if st.button("Predict"):
        try:
            # Convert the image to bytes
            img_bytes = uploaded_file.read()

            # Send POST request to the API
            response = requests.post(api_url, files={"file": img_bytes})

            if response.status_code == 200:
                result = response.json()
                st.success(f"Prediction: {result['class']}")
                st.warning(f"Confidence: {result['confidence']:.2%}")

            else:
                st.error(f"Error: {response.status_code} - {response.text}")

        except Exception as e:
            st.error(f"An error occurred: {e}")
