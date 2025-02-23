# Jacob Achenbach Module 8.2
# 2/23/2025
# Loads students from JSON file, then prints the original list, adds a new student, prints the updated list, and saves the changes back to the JSON file.

import json
import os
import time

# JSON file name
json_file = "students.json"

# Function to load student list from JSON file
def load_students():
    try:
        with open(json_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to print student list
def print_students(student_list, message):
    print("\n" + message)
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Function to save student list back to JSON file
def save_students(student_list):
    with open(json_file, "w") as file:
        json.dump(student_list, file, indent=4)
    print("\nJSON file has been updated.")

# Load original student list
students = load_students()

# Print original student list
print_students(students, "Original Student List:")

# Append new student details
new_student = {
    "F_Name": "John",
    "L_Name": "Doe",
    "Student_ID": 99999,
    "Email": "johndoe@example.com"
}
students.append(new_student)

# Print updated student list
print_students(students, "Updated Student List:")

# Save updated student list back to JSON file
save_students(students)

# Waits 2 seconds
time.sleep(2)

# Reopen the file in Notepad
if os.name == "nt":  # Windows
    os.system(f'notepad.exe {json_file}')
elif os.name == "posix":  # macOS/Linux
    os.system(f'open -e {json_file}')  # macOS uses TextEdit
