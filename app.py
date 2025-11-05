import streamlit as st
from ultralytics import YOLO
from PIL import Image

# Load your trained model
model = YOLO("faw_model_trained.pt")

st.title("🌽 Fall Armyworm Early Detection System")
st.write("Upload a maize leaf image to detect Fall Armyworm or related conditions.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)

    if st.button("Detect"):
        results = model.predict(image, conf=0.25)
        st.image(results[0].plot(), caption="Detection Result", use_container_width=True)
