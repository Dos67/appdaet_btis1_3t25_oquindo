#Tuple
course_catalog = [
    ("CS101", "Intro to Python", 4),
    ("MATH201", "Calculus I", 3),
    ("CS102", "Data Structures", 4)
]

#Dictionary
student_roster = {
    "S101": {
        "name": "Dos",
        "major": "Information Systems",
        "enrolled_courses": ["CS101", "MATH201"]
    },

    "S102": {
        "name": "Kick",
        "major": "Cyber Security",
        "enrolled_courses": ["CS101", "CS102"]
    }
}

#Sets
unique_courses = set()

for student in student_roster.values():
    unique_courses.update(student["enrolled_courses"])

common_courses = (
    set(student_roster["S101"]["enrolled_courses"])
    &
    set(student_roster["S102"]["enrolled_courses"])
)

#List | Tuple
grade_submissions = [
    ("S101", "CS101", "A"),
    ("S101", "MATH201", "B"),
    ("S102", "CS101", "A"),
    ("S102", "CS102", "C")
]

def get_student_gpa(student_id):
    grade_scale = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0
    }

    grades = []

    for sid, course, grade in grade_submissions:
        if sid == student_id:
            grades.append(grade_scale[grade])

    return sum(grades) / len(grades)

# Output

print("--- Course Catalog ---")

for code, title, credits in course_catalog:
    print(f"{code}: {title} ({credits} credits)")

print()

print("--- Enrollment Analytics ---")
print(f"All unique courses being taken: {unique_courses}")
print(f"Common courses taken by all students: {common_courses}")

print()

print("--- Grade Report ---")
print(f"Student S101 Final GPA: {get_student_gpa('S101')}")