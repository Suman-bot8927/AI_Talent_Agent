# 🤖 AI-Powered Talent Scouting & Engagement Agent

## 🚀 Project Overview

The **AI-Powered Talent Scouting & Engagement Agent** is a smart recruitment assistant designed to automate candidate screening and ranking.

Recruiters often spend hours manually filtering candidates. This system simplifies the process by:

* Taking a **Job Description (JD)** as input
* Matching candidates based on **skills and role**
* Calculating **Match Score** and **Interest Score**
* Generating a **ranked shortlist** with explanations
* Simulating an **AI engagement response**

---

## 🔗 Live Demo

👉 [https://ai-talent-agent-1.onrender.com]

---

## 💡 Key Features

* 📄 Job Description input
* 🎯 Automatic role detection (Data Analyst, Backend, etc.)
* 🤖 Skill-based candidate matching
* 📊 Match Score & Interest Score calculation
* 🏆 Ranked candidate shortlist
* 💬 AI-like engagement simulation
* 🔍 Explainable results (matched skills shown)
* 🌐 Clean and responsive web interface

---

## 🧠 How It Works

1. User enters a Job Description
2. System detects the **target role**
3. Filters candidates based on role
4. Matches candidate skills with JD keywords
5. Calculates:

   * **Match Score** = matched skills / total skills
   * **Interest Score** = simulated (0.5 – 1.0)
6. Computes:

   * **Final Score = (Match × 0.8) + (Interest × 0.2)**
7. Filters candidates with **Final Score ≥ 0.50**
8. Displays ranked results with AI engagement messages

---

## 🤖 AI Engagement (Simulated)

The system includes a **simulated AI engagement agent** that predicts candidate interest.

Example:

* High score → *Highly interested and ready to join*
* Medium score → *Open to discussion*
* Low score → *Not very interested*

---

## 🏗️ Architecture Diagram

![Architecture](architecture.png)

## 🏗️ Architecture

```
User Input (Job Description)
        ↓
Flask Web App (app.py)
        ↓
Processing Engine (utils.py)
        ↓
Candidate Dataset (CSV)
        ↓
Scoring System
   → Match Score
   → Interest Score
        ↓
AI Engagement Simulation
        ↓
Ranked Output (UI)
```

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **Pandas**
* **HTML, CSS**

---

## 📂 Project Structure

```
AI_Talent_Agent/
│
├── app.py
├── utils.py
├── requirements.txt
│
├── data/
│   └── candidates.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## 📊 Sample Input

```
Data Analyst with SQL, Excel, Power BI
```

---

## 📊 Sample Output

| Rank | Name        | Role         | Final Score | AI Engagement      |
| ---- | ----------- | ------------ | ----------- | ------------------ |
| 1    | Rahul Verma | Data Analyst | 0.72        | Highly interested  |
| 2    | Sneha Roy   | Data Analyst | 0.66        | Open to discussion |

---

## ▶️ How to Run Locally

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run the application

```
python app.py
```

### 3. Open in browser

```
http://127.0.0.1:10000
```

---

## 🎯 Use Case

This system helps:

* 👨‍💼 Recruiters
* 🏢 HR Teams
* 📊 Hiring Managers

to quickly shortlist candidates based on job requirements.

---

## 🔮 Future Improvements

* Resume parsing (PDF/DOCX)
* Real AI chatbot integration
* LinkedIn / GitHub integration
* Machine Learning-based scoring

---

## 🎥 Demo Video

(Add your demo video link here)

---

## 👨‍💻 Author

**Suman Samanta**
