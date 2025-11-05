# FAW-Capstone-Project
YOLOv8-based detection of Fall Armyworm larvae in crop images with ONNX export for deployment.
# 🌽 Fall Armyworm Detection Capstone Project

## Link to Live Preview
[FAW Detection System]([https://example.com](https://faw-capstone-project-mdnekdqdcojnpndw8drl34.streamlit.app/)
## Project Overview
This project detects Fall Armyworm larvae in crop images using YOLOv8.

## Repository Structure
- `notebooks/` : Full workflow notebook (data → training → evaluation → ONNX export)
- `models/` : Trained ONNX model
- `app/` : Optional Streamlit demo
- `report/` : Project report or slides
- `requirements.txt` : Python dependencies

## Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
streamlit run app/app.py
The ONNX model faw_model.onnx is ready for inference or deployment in other frameworks.

---

## **3️⃣ requirements.txt Template**

```txt
torch
ultralytics
streamlit
Pillow
numpy
opencv-python



