# MarkMate - AI Powered Smart Attendance System

## Overview

MarkMate is an AI-powered attendance management system that automates student attendance using facial recognition technology.

The system allows students to register their facial profiles and automatically mark attendance through face detection and recognition, eliminating manual attendance procedures and reducing proxy attendance.

---

## Features

### Student Features

* Face-based login and authentication
* New student registration using facial enrollment
* Subject enrollment using subject codes
* View enrolled subjects
* View attendance statistics
* Unenroll from subjects

### Teacher Features

* Teacher account registration and login
* Create and manage subjects
* View enrolled students
* Conduct attendance sessions
* View attendance records
* Generate attendance reports

### AI Features

* Face detection using Dlib
* Face embedding generation (128-dimensional facial descriptors)
* Face recognition using Support Vector Machine (SVM)
* Automatic attendance marking
* Duplicate attendance prevention

---

## System Architecture

### Frontend

* Streamlit

### Backend

* Python

### Database

* Supabase (PostgreSQL)

### Machine Learning

* Dlib
* Face Recognition Models
* Scikit-learn (SVM Classifier)
* NumPy

---

## Project Structure

```text
markmate/
│
├── app.py
│
├── src/
│   ├── screens/
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│   │
│   ├── pipelines/
│   │   └── face_pipeline.py
│   │
│   ├── database/
│   │   ├── config.py
│   │   └── db.py
│   │
│   ├── components/
│   │   ├── dialog_enroll.py
│   │   ├── dialog_create_subject.py
│   │   ├── subject_card.py
│   │   └── ...
│   │
│   └── ui/
│
├── requirements.txt
└── README.md
```

---

## Working of the System

### Step 1: Student Registration

1. Student opens the Student Portal.
2. Camera captures the student's face.
3. Dlib detects facial landmarks.
4. A 128-dimensional face embedding is generated.
5. The embedding is stored in the database.

Stored Information:

* Student Name
* Student ID
* Face Embedding

---

### Step 2: Subject Enrollment

1. Teacher creates a subject.
2. A unique subject code is generated.
3. Student enters the subject code.
4. Enrollment record is stored in the database.

---

### Step 3: Face Recognition

1. Student opens the application.
2. Camera captures a facial image.
3. Face embedding is generated.
4. Stored embeddings are retrieved from the database.
5. The trained SVM classifier identifies the student.
6. The captured embedding is compared with registered embeddings.
7. The student's identity is verified and attendance can be marked.

---

### Step 4: Attendance Logging

Attendance records include:

* Student ID
* Subject ID
* Timestamp
* Attendance Status

These records are stored in the attendance_logs table.

---

## Face Recognition Pipeline

### Face Detection

The system uses Dlib's frontal face detector to identify faces in the image.

### Facial Landmark Detection

68 facial landmarks are extracted using Dlib's pretrained predictor.

### Face Embedding Generation

A 128-dimensional facial feature vector is generated for each detected face.

### Classification

An SVM classifier is trained using all registered student embeddings.

### Face Recognition

The generated embedding is compared against stored embeddings and the student is identified based on the closest match.

---

## Database Schema

### teachers

| Field      | Description        |
| ---------- | ------------------ |
| teacher_id | Unique Teacher ID  |
| username   | Login Username     |
| password   | Encrypted Password |
| name       | Teacher Name       |

### students

| Field          | Description         |
| -------------- | ------------------- |
| student_id     | Unique Student ID   |
| name           | Student Name        |
| face_embedding | Face Feature Vector |

### subjects

| Field        | Description     |
| ------------ | --------------- |
| subject_id   | Subject ID      |
| subject_code | Enrollment Code |
| name         | Subject Name    |
| section      | Class Section   |
| teacher_id   | Owner Teacher   |

### subject_students

| Field      | Description |
| ---------- | ----------- |
| student_id | Student     |
| subject_id | Subject     |

### attendance_logs

| Field      | Description       |
| ---------- | ----------------- |
| student_id | Student           |
| subject_id | Subject           |
| timestamp  | Attendance Time   |
| is_present | Attendance Status |

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd markmate
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m streamlit run app.py
```

---

## Future Improvements

* Real-time classroom attendance
* Multi-face attendance detection
* Attendance analytics dashboard
* Attendance export to Excel/PDF
* Email notifications
* QR-based backup attendance
* Face anti-spoofing
* Cloud deployment

---

## Tech Stack

* Python
* Streamlit
* Dlib
* Scikit-Learn
* NumPy
* Supabase
* PostgreSQL

---

## Authors

Developed as an AI-powered Smart Attendance Management System using Computer Vision and Machine Learning techniques.

### Tagline

**MarkMate – Smart Attendance Through Face Recognition**
