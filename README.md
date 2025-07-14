# Crime-Report-and-Analysis-Dshboard# 🕵️ Civic Eye: Crime Report and Analysis System

A Final Year Project that integrates crime reporting, trend analysis, and predictive modeling using modern web technologies and machine learning. Built to enhance public safety awareness and aid authorities in identifying crime hotspots and forecasting future crime trends.

## 🚀 Project Overview

**Civic Eye** is a full-stack web application that allows users to:
- Report crimes online
- Visualize crime data through charts, maps, and trend graphs
- Predict future crime patterns using machine learning
- Analyze crime based on location, type, and date

This system aims to bring transparency and intelligent analysis to crime data using data science and interactive design.

---

## 🛠️ Tech Stack

### Frontend
- **React.js** – Modern component-based UI
- **Chart.js / Recharts** – Data visualization
- **Tailwind CSS / Bootstrap** – Styling and responsive design
- **Axios** – HTTP requests

### Backend
- **Flask (Python)** – RESTful API
- **MySQL** – Relational database
- **SQLAlchemy** – ORM for database interaction

### Machine Learning
- **Scikit-learn** – Linear Regression for crime trend prediction
- **Pandas / NumPy / Matplotlib** – Data preprocessing and visualization
- **Custom crime prediction module** – Trained using CSV + backend data

---

## 📂 Project Structure

crime-report-analysis/
│
├── backend/
│ └── flask_api/
│ ├── app.py
│ ├── routes/
│ ├── models/
│ └── ml/
│ ├── crime_predictor.py
│ └── trained_model.pkl
│
├── frontend/
│ └── civic-eye-app/
│ ├── src/
│ │ ├── components/
│ │ ├── pages/
│ │ └── PredictCrime.js
│ └── public/
│
├── data/
│ └── crime_dataset_india.csv
│
├── README.md
└── requirements.txt
