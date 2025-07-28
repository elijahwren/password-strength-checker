import re

def check_strength(password):
    score = 0
    length_error = len(password) < 10
    
    #regex checks
    has_lower = re.search(r"[a-z]", password)
    has_upper = re.search(r"[A-Z]", password)
    has_number = re.search(r"\d", password)
    has_symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    
    #add to score based off features
    if not length_error:
        score += 1
    if has_lower and has_upper:
        score += 1
    if has_number:
        score += 1
    if has_symbol:
        score += 1
        
    #score feedback
    strength = {
        4: "Very Strong",
        3: "Strong",
        2: "Neutral",
        1: "Weak",
        0: "Very Weak"
    }
    
    return strength[score]

password = input("Enter a password to check strength: ")
strength = check_strength(password)
print(f"Password Strength: {strength}")
