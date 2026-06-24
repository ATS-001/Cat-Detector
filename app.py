import streamlit as st
import cv2
import requests
import numpy as np
import base64

# 1. Page Styling
st.set_page_config(page_title="AI Cat Detector", page_icon="🐱")
st.title("🐱 Live Cat Detector")
st.write("Upload an image to check for a cat using your trained AI model.")

# 2. Injection: Hides Developer Top Bars & Adds Your Custom Footer
custom_style = """
<style>
    /* Hides the new Deploy Button class and the header background helper frames */
    .stAppDeployButton, [data-testid="stHeader"] > div:first-child > div:first-child {
        display: none !important;
    }
    
    /* Target the action toolbar explicitly to hide individual button segments except the menu */
    [data-testid="stAppToolbar"] > div {
        display: none !important;
    }
    
    /* Forces the standard multi-dot element box container block to stay interactive */
    [data-testid="stAppToolbarActions"] {
        display: inline-flex !important;
    }

    /* Hides the default "Made with Streamlit" footer text */
    footer {
        visibility: hidden !important;
    }
    
    /* Creates your custom permanent centered footer */
    .custom-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #888888;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        font-family: Arial, sans-serif;
        line-height: 1.6;
        z-index: 999;
    }
</style>

<div class="custom-footer">
    Aaron Thalakkottor Sooraj<br>
    Designed & Developed by ATS-PDZ • © Since 2023
</div>
"""
st.markdown(custom_style, unsafe_allow_html=True)

# 3. Secure API Connection
API_KEY = st.secrets["ROBOFLOW_API_KEY"]
MODEL_NAME = "cat-eugjv"
VERSION = "1"

# 4. File Uploader UI
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image files safely
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    
    # Convert BGR to RGB so the AI server sees the correct colors
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Encode to JPEG for the API payload
    _, img_encoded = cv2.imencode('.jpg', image_rgb)
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')

    st.write("Analyzing image...")

    # 5. Request predictions securely from Roboflow Hosted Cloud
    url = f"https://detect.roboflow.com/{MODEL_NAME}/{VERSION}?api_key={API_KEY}"
    try:
        response = requests.post(url, data=img_base64, headers={"Content-Type": "application/x-www-form-urlencoded"})
        result = response.json()

        if "predictions" in result and len(result["predictions"]) > 0:
            # Draw bounding boxes over the original image for display
            for pred in result["predictions"]:
                x = int(pred["x"] - pred["width"] / 2)
                y = int(pred["y"] - pred["height"] / 2)
                w = int(pred["width"])
                h = int(pred["height"])
                
                # Draw box and class label
                cv2.rectangle(image_rgb, (x, y), (x + w, y + h), (0, 255, 0), 4)
                label = f"{pred['class']} ({int(pred['confidence'] * 100)}%)"
                cv2.putText(image_rgb, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            st.image(image_rgb, caption="Detections Completed!", use_container_width=True)
            st.success("🐱 Cat Detected!")
        else:
            st.image(image_rgb, use_container_width=True)
            st.info("No cats detected in this image.")

    except Exception as e:
        st.error(f"Error talking to AI Server: {e}")
