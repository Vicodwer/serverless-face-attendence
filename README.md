# serverless-face-attendence
# 🎯 AI-Based Face Recognition Attendance System

A real-time automated attendance system using computer vision and deep learning.  
The system captures facial images via webcam, recognizes registered users, and logs attendance automatically.

---

## 📌 Project Overview

This project eliminates manual attendance marking by using facial recognition technology. It detects and recognizes faces in real time and stores attendance records digitally.

The system supports:

- Student registration
- Real-time face recognition
- Automatic attendance marking
- Web-based dashboard for viewing logs
- CSV export functionality

---

## 🏗️ System Architecture

User → Webcam → Face Detection → Face Encoding → Recognition Engine → Attendance Log → Dashboard

---

## 🧠 Technologies Used

- Python 3.10+
- OpenCV
- face_recognition (dlib-based)
- NumPy
- Pandas
- Flask
- SQLite / CSV storage

---

## 📁 Project Structure
face-recognition-attendance-system/
│
├── dataset/
├── models/
│ └── face_encodings.pkl
│
├── attendance.csv
├── register.py
├── recognize.py
├── app.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone the repository


git clone https://github.com/your-username/face-recognition-attendance-system.git

cd face-recognition-attendance-system


### 2️⃣ Create virtual environment (recommended)


python -m venv venv


Activate:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


### 3️⃣ Install dependencies


pip install -r requirements.txt


---

## 📄 requirements.txt


dlib
face_recognition
flask
numpy
opencv-python
pandas


---

## 👤 How to Register a Student

Run:


python register.py


- Enter student name
- Press `s` to capture face
- Face encoding is saved to:

models/face_encodings.pkl


---

## 🎥 Start Face Recognition


python recognize.py


- System opens webcam
- Detects and recognizes faces
- Marks attendance automatically
- Prevents duplicate entry for same day

Attendance stored in:


attendance.csv


---

## 🌐 View Attendance Dashboard


python app.py


Open browser:


http://127.0.0.1:5000


---

## 📊 Sample Attendance Log


Name,Date,Time
Vishal,2026-02-27,09:01:12
Rahul,2026-02-27,09:05:43


---

## 🔒 Features

- Contactless biometric attendance
- Real-time recognition
- One attendance per day validation
- Lightweight and efficient
- Easy to deploy locally

---

## ☁️ Optional Cloud Integration

The system can be extended using:

- AWS Rekognition
- Azure Face API

For scalable, serverless deployment.

---

## 📈 Future Enhancements

- Liveness detection (anti-spoofing)
- Database integration (MySQL/PostgreSQL)
- Multi-camera support
- Mobile application
- Cloud-native deployment
- Role-based authentication

---

## ⚠️ Limitations

- Performance depends on lighting conditions
- Masked faces may reduce accuracy
- Requires clear frontal face image

---

## 🎓 Academic Use

This project is suitable for:

- Final year engineering projects
- AI/ML coursework
- Computer vision demonstrations
- Cloud computing integration projects

---

## 📜 License

This project is for educational purposes only.

---

## 👨‍💻 Author

Team Vishal  
AI & Cloud Enthusiasts  
