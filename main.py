# ==============================
# Student Course Tracker
# Starter Template
# ==============================

# Starter data (DO NOT MODIFY)
students = [
    ("Alice", 20),
    ("Bob", 22),
    ("Charlie", 21)
]

courses = ["Python", "JavaScript", "Python", "Databases"]

student_data = {
    "Alice": {"courses": ["Python", "Databases"], "grades": [85, 90]},
    "Bob": {"courses": ["Python", "JavaScript"], "grades": [78, 82]},
    "Charlie": {"courses": ["JavaScript"], "grades": [88]}
}

# ------------------------------
# Task 1: Remove Duplicate Courses
# ------------------------------
# TODO:
# - Convert the courses list into a set
# - Print the unique courses
unique_courses = set(courses)
print(unique_courses)
# ------------------------------
# Task 2: Display Student Info
# ------------------------------
# TODO:
# - Loop through the students list
# - For each student, print:
#   Name, age, and enrolled courses
for student in students:
    name, age = student 
    enrolled_courses = student_data[name]["courses"]
    print(f"Name: {name}, Age: {age}, Courses: {enrolled_courses}")

# ------------------------------
# Task 3: Add Course for Bob
# ------------------------------
# TODO:
# - Add "Databases" to Bob's course list
#   ONLY if he is not already enrolled
# - Print Bob's updated course list
for student in student_data:
    if "Databases" not in student_data["Bob"]["courses"]:
        student_data["Bob"]["courses"].append("Databases")
print(student_data["Bob"]["courses"])
# ------------------------------
# Task 4: Calculate Average Grades
# ------------------------------
# TODO:
# - Loop through student_data
# - Calculate and print each student's average grade
for student, info in student_data.items():
    grades = info["grades"]
    average_grade = sum(grades) / len(grades)
    print(f"{student}'s average grade: {average_grade}")
# ------------------------------
# Task 5: Find Students in a Course
# ------------------------------
# TODO:
# - Ask the user to enter a course name
# - Print all students enrolled in that course
course_name = input("Enter a course name: ")
enrolled_students = []
for student, info in student_data.items():
    if course_name in info["courses"]:
        enrolled_students.append(student)
print(f"Students enrolled in {course_name}: {enrolled_students}")
# ------------------------------
# Bonus (Optional)
# ------------------------------
# TODO:
# - Store each student's average grade in the dictionary
# - Print the student with the highest average grade
for student, info in student_data.items():
    grades = info["grades"]
    average_grade = sum(grades) / len(grades)
    info["average_grade"] = average_grade
highest_avg_student = max(student_data.items(), key=lambda x: x[1]["average_grade"])
print(f"Student with highest average grade: {highest_avg_student[0]} with average {highest_avg_student[1]['average_grade']}")

