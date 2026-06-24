import streamlit as st
import cv2
import requests
import numpy as np

# 1. Page Styling
st.set_page_config(page_title="AI Cat Detector", page_icon="🐱")
st.title("🐱 Live Cat Detector")
st.write("Upload an image to check for a cat using your trained AI model.")

# 2. Securely grab the API key from Streamlit's backend environment
# (Nobody visiting the website can ever see this)
API_KEY = st.secrets["ROBOFLOW_API_KEY"]
MODEL_NAME = "cat-eugjv"
VERSION = "1"

# 3. File Uploader UI
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert uploaded file to OpenCV format
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    
    # Encode image back to JPEG to send to Roboflow
    _, img_encoded = cv2.imencode('.jpg', image)
    img_bytes = img_encoded.tobytes()

    st.write("Analyzing image...")

    # 4. Request predictions securely from Roboflow Cloud API
    url = f"https://detect.roboflow.com/{MODEL_NAME}/{VERSION}?api_key={API_KEY}"
    try:
        response = requests.post(url, data=img_bytes, headers={"Content-Type": "application/x-www-form-urlencoded"})
        result = response.json()

        if "predictions" in result and len(result["predictions"]) > 0:
            # Draw bounding boxes over the image
            for pred in result["predictions"]:
                # Roboflow gives center coordinates; convert to top-left corners
                x = int(pred["x"] - pred["width"] / 2)
                y = int(pred["y"] - pred["height"] / 2)
                w = int(pred["width"])
                h = int(pred["height"])
                
                # Draw green box
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)
                
                # Draw text banner
                label = f"{pred['class']} ({int(pred['confidence'] * 100)}%)"
                cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Display the result
            st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Detections Completed!", use_container_width=True)
            st.success("🐱 Cat Detected!")
        else:
            st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), use_container_width=True)
            st.info("No cats detected in this image.")

    except Exception as e:
        st.error(f"Error talking to AI Server: {e}")
