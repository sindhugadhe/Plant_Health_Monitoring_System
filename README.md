# 🌿 Plant Health Monitoring System using Machine Learning

An AI-powered web application that detects plant leaf diseases from uploaded images and provides disease predictions along with recommended treatments. The application uses an ensemble of deep learning models to improve prediction accuracy and is built with Flask for a simple and interactive user interface.

---

## 📌 Project Overview

Plant diseases can significantly reduce crop yield and quality. Early disease detection helps farmers take preventive measures and improve productivity.

This project uses **Deep Learning (CNN-based models)** to classify plant leaf diseases from images. Users can upload an image of a plant leaf through a web interface, and the system predicts the disease and suggests possible remedies.

---

## 🚀 Features

- Upload plant leaf images through a web interface
- Automatic image preprocessing
- Disease prediction using Deep Learning
- Ensemble prediction using multiple models
- Displays predicted disease
- Provides disease treatment recommendations
- Simple and responsive Flask web application

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Framework
- Flask

### Deep Learning
- TensorFlow
- Keras

### Image Processing
- OpenCV
- NumPy
- Pillow

### Frontend
- HTML
- CSS
- Bootstrap

### Database
- SQLite

---

## 📂 Project Structure

```
Plant-Leaf-Disease-Detection/
│
├── app.py
├── model1.h5
├── model_xception.h5
├── requirements.txt
├── database.db
│
├── static/
│   ├── uploads/
│   ├── css/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── prediction.html
│   ├── login.html
│   └── register.html
│
├── dataset/
│
└── README.md
```

---

## ⚙️ How It Works

1. User uploads a plant leaf image.
2. The image is resized to **224 × 224 pixels**.
3. Image preprocessing is performed.
4. The image is passed to two trained deep learning models.
5. Predictions from both models are combined using ensemble learning.
6. The disease with the highest confidence score is selected.
7. The predicted disease and recommended treatment are displayed to the user.

---

## 🧠 Model Details

- Input Size: **224 × 224 × 3**
- Deep Learning Framework: TensorFlow/Keras
- Batch Size: 128
- Epochs: 40
- Ensemble Model:
  - CNN Model
  - Xception Model

The ensemble approach improves prediction stability and overall accuracy compared to using a single model.

---

## 🌱 Supported Plant Diseases

The model can classify multiple plant diseases, including:

- Tomato Leaf Diseases
- Potato Leaf Diseases
- Corn Leaf Diseases
- Apple Leaf Diseases
- Grape Leaf Diseases
- Pepper Leaf Diseases
- Healthy Leaves

> The supported classes depend on the dataset used during training.

---

## 💻 Installation

### Clone the repository

```bash
git clone https://github.com/sindhugadhe/Plant_Health_Monitoring_System.git
```

```bash
cd Plant-Leaf-Disease-Detection
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📊 Dataset

The model is trained on a publicly available plant disease dataset containing healthy and diseased leaf images.

Dataset characteristics:

- Thousands of labeled images
- Multiple crop species
- Multiple disease categories
- Healthy leaf classes

---

## 📈 Future Improvements

- Mobile application
- Real-time disease detection using camera
- Cloud deployment
- Multi-language support
- Severity estimation
- Fertilizer recommendation
- Weather-based disease prediction
- Farmer chatbot integration

---



## 👨‍💻 Author

**Sindhu Gadhe**

B.Tech – Data Science

Interested in Artificial Intelligence, Machine Learning, Computer Vision, Data Analytics, and Generative AI.

GitHub: https://github.com/sindhugadhe

LinkedIn: https://linkedin.com/in/sindhugadhe

---

## 📜 License

This project is developed for educational and research purposes.

---

## ⭐ If you found this project useful

Please consider giving this repository a ⭐ to support the project.
