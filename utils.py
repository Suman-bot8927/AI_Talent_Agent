import pandas as pd
import random

# Load dataset
df = pd.read_csv("data/candidates.csv")

# Detect role
def detect_role(jd):
    jd = jd.lower()

    if "data analyst" in jd:
        return "data analyst"
    elif "data scientist" in jd:
        return "data scientist"
    elif "backend" in jd:
        return "backend developer"
    elif "frontend" in jd:
        return "frontend developer"
    elif "devops" in jd:
        return "devops engineer"

    return None


# 🤖 AI Engagement (Simulated)
def generate_ai_response(name, role, score):
    if score > 0.85:
        return f"{name} is highly interested in the {role} role and ready to join immediately."
    elif score > 0.70:
        return f"{name} is interested and open to discussion."
    elif score > 0.50:
        return f"{name} is moderately interested."
    else:
        return f"{name} is not very interested."


def process_candidates(jd):
    jd = jd.lower()
    jd_words = jd.split()

    target_role = detect_role(jd)

    results = []

    for _, row in df.iterrows():

        role = str(row["job_title"]).lower()

        # Role filter
        if target_role and target_role not in role:
            continue

        # Skills
        skills = [s.strip().lower() for s in str(row["skills"]).split(",")]

        # Matching
        matched = [
            skill for skill in skills
            if any(word in skill for word in jd_words)
        ]

        match_score = len(matched) / len(skills) if skills else 0
        interest_score = random.uniform(0.5, 1.0)

        final_score = (match_score * 0.8) + (interest_score * 0.2)

        # ⚠️ Important: Not too strict
        if final_score < 0.30:
            continue

        name = row["name"]
        job_role = row["job_title"]

        results.append({
            "name": name,
            "role": job_role,
            "skills": ", ".join(skills),
            "match_score": round(match_score, 2),
            "interest_score": round(interest_score, 2),
            "final_score": round(final_score, 2),
            "reason": f"Matched skills: {', '.join(matched)}" if matched else "Low match",
            "ai_response": generate_ai_response(name, job_role, final_score)
        })

    results = sorted(results, key=lambda x: x["final_score"], reverse=True)

    print(results)  # Debug

    return results