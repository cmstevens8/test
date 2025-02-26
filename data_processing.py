# 1. Prompt the user to enter a sentence and print it in uppercase
sentence = input("Enter a sentence: ")
print("Uppercase:", sentence.upper())

print("\n")

# 2. Prompt the user to enter a paragraph and count the number of words
paragraph = input("Enter a paragraph: ")
word_count = len(paragraph.split())  # Splitting the paragraph into words
print("Word count:", word_count)

print("\n")

# 3. Prompt the user for a string and check if all characters are digits
user_string = input("Enter a string: ")
print("All characters are digits:", user_string.isdigit())

print("\n")

# 4. Prompt the user for a string and replace all occurrences of "a" with "o"
replace_string = input("Enter a string: ")
modified_string = replace_string.replace("a", "o")
print("Modified string:", modified_string)

print("\n")

# 5. Prompt the user to enter their full name and print their initials
full_name = input("Enter your full name: ")
name_parts = full_name.split()  # Split name into parts
initials = "".join([name[0].upper() for name in name_parts])  # Get the first letter of each part
print("Your initials:", initials)

print("\n")

# 6. Prompt the user for a string and print its length
string_input = input("Enter a string: ")
print("Length of string:", len(string_input))
