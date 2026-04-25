import pandas as pd
import random

# Load dataset
df = pd.read_csv("data/candidates.csv")

# -----------------------------
# Detect role from Job Description
# -----------------------------
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


# -----------------------------
# Main processing function
# -----------------------------
def process_candidates(jd):
    jd = jd.lower()
    jd_words = jd.split()

    target_role = detect_role(jd)

    results = []

    for _, row in df.iterrows():

        # Safe extraction (avoids errors)
        name = str(row.get("name", "N/A")).strip()
        role = str(row.get("job_title", "N/A")).lower()
        skills_raw = str(row.get("skills", ""))

        # -----------------------------
        # 1. STRICT ROLE FILTER
        # -----------------------------
        if target_role and target_role not in role:
            continue

        # -----------------------------
        # 2. CLEAN SKILLS
        # -----------------------------
        skills = [s.strip().lower() for s in skills_raw.split(",") if s.strip()]

        # -----------------------------
        # 3. SMART SKILL MATCHING
        # -----------------------------
        matched_skills = []

        for skill in skills:
            for word in jd_words:
                if word in skill or skill in jd:
                    matched_skills.append(skill)
                    break

        # -----------------------------
        # 4. MATCH SCORE
        # -----------------------------
        match_score = len(matched_skills) / len(skills) if skills else 0

        # -----------------------------
        # 5. INTEREST SCORE (simulated)
        # -----------------------------
        interest_score = random.uniform(0.5, 1.0)

        # -----------------------------
        # 6. FINAL SCORE
        # -----------------------------
        final_score = (match_score * 0.8) + (interest_score * 0.2)

        # -----------------------------
        # 7. FILTER (>= 0.60)
        # -----------------------------
        if final_score < 0.60:
            continue

        # -----------------------------
        # 8. STORE RESULT
        # -----------------------------
        results.append({
            "name": name,
            "role": role.title(),
            "skills": ", ".join(skills),
            "match_score": round(match_score, 2),
            "interest_score": round(interest_score, 2),
            "final_score": round(final_score, 2),
            "reason": f"Matched skills: {', '.join(matched_skills)}" if matched_skills else "Low match"
        })

    # -----------------------------
    # 9. SORT RESULTS
    # -----------------------------
    results = sorted(results, key=lambda x: x["final_score"], reverse=True)

    return results