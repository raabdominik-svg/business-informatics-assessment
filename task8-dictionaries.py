# A dictionary mapping Student IDs (keys) to their Final Grades (values)
student_grades = {
    "ID123": 85,
    "ID456": 92,
    "ID789": 78,
    "ID999": 100
}

# The student ID we want to look up today
search_id = "ID456"

found_grade = student_grades.get(search_id)
print(f"Student {search_id} got a grade of {found_grade}.")
