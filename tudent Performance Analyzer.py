import numpy as np

# Student names
students = np.array([
    "Rahul",
    "Priya",
    "Amit",
    "Sneha",
    "Arjun"
])

# Marks in 3 subjects: Math, Science, English
marks = np.array([
    [85, 90, 78],
    [72, 88, 91],
    [95, 92, 89],
    [60, 75, 70],
    [45, 55, 50]
])

subjects = np.array(["Math", "Science", "English"])

# Calculate total marks for each student
total_marks = np.sum(marks, axis=1)

# Calculate average marks for each student
average_marks = np.mean(marks, axis=1)

# Find highest and lowest marks
highest_mark = np.max(marks)
lowest_mark = np.min(marks)

# Class average
class_average = np.mean(marks)

# Display student results
print("=" * 50)
print("       STUDENT PERFORMANCE ANALYZER")
print("=" * 50)

for i in range(len(students)):
    print(f"\nStudent: {students[i]}")
    print(f"Math: {marks[i][0]}")
    print(f"Science: {marks[i][1]}")
    print(f"English: {marks[i][2]}")
    print(f"Total: {total_marks[i]}")
    print(f"Average: {average_marks[i]:.2f}")

    # Grade calculation
    if average_marks[i] >= 90:
        grade = "A+"
    elif average_marks[i] >= 80:
        grade = "A"
    elif average_marks[i] >= 70:
        grade = "B"
    elif average_marks[i] >= 60:
        grade = "C"
    elif average_marks[i] >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Grade: {grade}")

# Find top student
top_student_index = np.argmax(average_marks)

print("\n" + "=" * 50)
print("CLASS STATISTICS")
print("=" * 50)

print(f"Class Average: {class_average:.2f}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")

print(
    f"Top Student: {students[top_student_index]} "
    f"({average_marks[top_student_index]:.2f})"
)

# Subject-wise average
subject_averages = np.mean(marks, axis=0)

print("\nSubject Averages:")

for i in range(len(subjects)):
    print(f"{subjects[i]}: {subject_averages[i]:.2f}")