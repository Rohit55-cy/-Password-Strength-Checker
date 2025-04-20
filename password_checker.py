# pip install requests
import re

def check_password_strength(password):
    length = len(password) >= 8
    digit = re.search(r"\d", password) is not None
    uppercase = re.search(r"[A-Z]", password) is not None
    lowercase = re.search(r"[a-z]", password) is not None
    special = re.search(r"[ !@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password) is not None
    
    score = sum([length, digit, uppercase, lowercase, special])
    
    if score == 5:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    elif score >= 2:
        return "Weak"
    else:
        return "Very Weak"

password = input("Enter password to check: ")
print(f"Password strength: {check_password_strength(password)}")
