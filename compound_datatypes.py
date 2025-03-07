#Excersise 1
fruits = ["apple", "banana", "cherry", "date"]

fruits.append("elderberry")
fruits.remove("banana")
fruits.sort()
print(fruits)

#Exersise 2
student = {"name": "John Doe", "age": 25, "major": "Computer Science"}

student["major"] = "Electrical Engineering"
student["year"] = "Senior"
print(student.keys())
print(student.values())

#Exersise 3
book = [
    {"title": "Verity", "author": "Colleen Hoover", "year": 2018},
    {"title": "All the Dangerous Things", "author": "Stacy Willingham", "year": 2023},
    {"title": "Throne of Glass", "author": "Sarah J. Maas", "year": 2012}
]

# print(book[1]["title"])
# print(book[2]["year"])

for b in book:
    print(b["title"], b["author"])

#Exersise 4
courses = {"math": ["Bob", "Stacy", "Joe"], "history": ["Lacy", "Nigel", "Polly"], "chemistry": ["Jack", "Jill", "Sam"]}

courses["math"].extend(["Carly", "Eavan", "Caitlin", "Ashley", "Matthew"])
courses["history"].pop(2)
courses["physics"] = ["Lacy", "Nigel", "Polly", "Jack"]
print(courses["chemistry"])
