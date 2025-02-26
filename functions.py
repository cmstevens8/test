def dollarizer(word):
    return word.replace("s", "$")

def eurizer(word):
    return word.replace("e", "€")

def replacer(word, char1, char2):
    return word.replace(char1, char2)

def wonky_text(word):
    return word.replace("s", "$").replace("e", "€").replace("l", "£")

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def age_in_days(age):
    return age * 365

def simple_interest(principal, rate, time):
    return principal * rate * time

def plan_finances(principle, rate, time, final_amount):
    return (final_amount - principle) / (rate * time)