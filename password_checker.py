import re

def validate_password(password):
    if len(password) < 7:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def check_password_strength(password):
    length_criteria = len(password) >= 7
    upper_criteria = bool(re.search(r'[A-Z]', password))
    lower_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if length_criteria and upper_criteria and lower_criteria and digit_criteria and special_criteria:
        return "Strong password"
    elif length_criteria and (upper_criteria or lower_criteria) and (digit_criteria or special_criteria):
        return "Moderate password"
    else:
        return "Weak password"

password = input("Input your password: ")

is_valid = validate_password(password)
if is_valid:
    print("Valid Password.")
    strength = check_password_strength(password)
    print(strength)
else:
    print("Password does not meet requirements.")
