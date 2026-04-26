# 🤖 AI-Powered Talent Scouting & Engagement Agent

## 🚀 Project Overview

The **AI-Powered Talent Scouting & Engagement Agent** is a smart recruitment assistant that automates candidate screening, matching, and engagement.

It takes a **Job Description (JD)** as input and:

* Identifies relevant candidates
* Matches skills and roles
* Calculates **Match Score** & **Interest Score**
* Generates a **ranked shortlist**
* Simulates **AI-based candidate engagement**

---

## 🔗 Live Demo

👉 https://ai-talent-agent.onrender.com

---

## 💡 Key Features

* 📄 Job Description input
* 🎯 Automatic role detection
* 🤖 Skill-based matching
* 📊 Match + Interest scoring
* 🏆 Ranked shortlist
* 💬 AI Engagement simulation
* 🔍 Explainable results (matched skills shown)

---

## 🧠 How It Works

1. User enters Job Description
2. System detects **target role (e.g., Backend Developer)**
3. Filters candidates by role
4. Matches skills with JD
5. Calculates:

   * Match Score
   * Interest Score
6. Computes:

   * Final Score = (Match × 0.8) + (Interest × 0.2)
7. Filters candidates (≥ 0.50)
8. Displays ranked output with engagement insights

---

## 🏗️ Architecture Diagram

![Architecture](architecture.png)

---

## 🎥 Demo Video

👉 (Paste your video link here)

---

## 📊 Sample Input

```text
Looking for a Python Developer with experience in Django, REST API, SQL, and backend development. Knowledge of cloud and data handling is a plus.
```

---

## 📊 Sample Output

| Rank | Name        | Role              | Skills                   | Match | Interest | Final | AI Engagement                                   |
| ---- | ----------- | ----------------- | ------------------------ | ----- | -------- | ----- | ----------------------------------------------- |
| 1    | John Miller | Backend Developer | python, django, rest api | 1.00  | 0.85     | 0.97  | Highly interested and ready to join immediately |
| 2    | Priya Singh | Backend Developer | java, spring boot, mysql | 0.67  | 0.86     | 0.71  | Interested and open to discussion               |

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

## 🛠️ Tech Stack

* Python
* Flask
* Pandas
* HTML, CSS

---

## ▶️ Run Locally

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run app

```
python app.py
```

### 3. Open browser

```
http://127.0.0.1:10000
```

---

## 🤖 AI Engagement Logic (Simulated)

* **Final Score ≥ 0.85** → Highly interested
* **0.65 – 0.84** → Open to discussion
* **< 0.65** → Low interest

---

## 🎯 Use Case

This system helps:

* Recruiters
* HR Teams
* Hiring Managers

to quickly shortlist candidates based on job requirements.

---

## 🔮 Future Improvements

* Resume parsing (PDF/DOCX)
* Real AI chatbot integration
* LinkedIn API integration
* ML-based recommendation system

---

## 👨‍💻 Author

**Suman Samanta**
