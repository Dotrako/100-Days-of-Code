student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# creating a student_grades empty dictionary
student_grades = {}

# iterating in each item of our student_scores to update our stu_grades
for key, value in student_scores.items():
    if value >= 91 and value <= 100:
        student_grades.update({key:"Outstanding"})
    elif value >= 81 and value <= 90:
        student_grades.update({key:"Exceeds Expectations"})
    elif value >= 71 and value <= 80:
        student_grades.update({key:"Acceptable"})
    else:
        student_grades.update({key:"Fail"})
print(student_grades)