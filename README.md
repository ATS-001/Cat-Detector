# 🐱 Live Cat Detector

A secure, cloud-powered web application that detects cats in real-time from uploaded images using a custom-trained object detection model. Built with Streamlit, OpenCV, and the Roboflow Inference API.

🚀 **Live Demo:** [Launch App on Streamlit Community Cloud](https://share.streamlit.io/) *(Replace this with your actual live Streamlit URL link)*

---

## 📅 Workshop Context

* **Event:** Day 1 of Projectathon conducted by μLearn LBSITW, AI x DS (23rd June 2026)
* **Presented by:** Darshana D Devi, AI & ML IG LEAD, µLearn LBSITW
* **Focus:** Training custom computer vision datasets on Roboflow and building production-ready deployment structures.

---

## ✨ Features
* **Custom AI Model:** Powered by a fine-tuned computer vision model trained on specific feline datasets.
* **On-Demand Cloud Inference:** Image data is securely transmitted via Base64 to Roboflow's hosted cloud engine for instantaneous bounding box calculations.
* **Production-Grade Security:** Utilizes Streamlit's encrypted backend storage system (`st.secrets`) to completely hide production API keys from client-side inspectors and repository viewers.
* **Responsive Frontend UI:** Minimalist interactive interface featuring automated color-channel corrections ($BGR \rightarrow RGB$) for precision tracking.

---

## 🛠️ Architecture & Tech Stack

* **Frontend Framework:** Streamlit (Python-driven reactive web UI)
* **Image Processing Engine:** OpenCV (Open Source Computer Vision Library)
* **Machine Learning Platform:** Roboflow Hosted Inference API (RF-DETR Architecture)
* **Repository Architecture:** GitHub Cloud Ecosystem

---

## 🚀 Local Setup & Installation

If you want to run this application locally on your machine, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/ats-001/Cat-Detector.git](https://github.com/ats-001/Cat-Detector.git)
cd Cat-Detector
```

### 2. Install System Dependencies
Ensure you have Python installed, then run the pip installation wrapper:
```pip install -r requirements.txt```

### 3. Configure Local Environment Secrets
Create the hidden Streamlit directory and configuration file in your root folder:
```
mkdir .streamlit
touch .streamlit/secrets.toml
```
# Open 
```.streamlit/secrets.toml``` 
in your local text editor and insert your private credential mapping exactly like this:

```ROBOFLOW_API_KEY = "your_actual_roboflow_api_key_here"```

### 4. Execute the Application
```streamlit run app.py```

---

## 🔮 Acknowledgments
Special thanks to Darshana D Devi ([LinkedIn Profile](https://www.linkedin.com/in/darshana-d-devi-1b1094326/)) for providing the foundational dataset structural guidelines and the hands-on workshop instruction regarding Roboflow integration that enabled this end-to-end model training and application deployment.

---

## 👤 Author
**Aaron Thalakkottor Sooraj** - B.Tech Computer Science & Engineering Student

---
