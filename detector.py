import re

def check_username(name):
    score = 0
    reasons = []
    if re.search(r'\d{3,}', name):
        score += 30
        reasons.append("Username has many numbers like bot accounts")
    if len(name) == 0:
        score += 20
        reasons.append("Name is empty")
    return score, reasons

def check_bio(bio):
    score = 0
    reasons = []
    if len(bio) < 20:
        score += 40
        reasons.append("Bio is too short / empty - fake profiles do this")
    spam = ["crypto expert", "forex trader", "seeking opportunity", "dm me"]
    for word in spam:
        if word in bio.lower():
            score += 25
            reasons.append(f"Spam keyword found: '{word}'")
    return score, reasons

def check_photo():
    return 20, ["AI photo check: Over-smooth skin / No background noise (demo check)"]

def final_verdict(total):
    if total >= 70:
        return "HIGH RISK - Likely Fake Profile"
    elif total >= 40:
        return "SUSPICIOUS - Check manually"
    else:
        return "LOW RISK - Likely Real"