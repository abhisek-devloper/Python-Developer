# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.


# Initialize list to store marks
marks = []
total_subjects = 3

# Take input using a loop
for i in range(total_subjects):
    mark = float(input(f"Enter marks for Subject {i+1} (out of 100): "))
    marks.append(mark)

# Calculate total and percentage
total_marks = sum(marks)
percentage = (total_marks / (total_subjects * 100)) * 100

# Check pass/fail condition
if percentage >= 40 and all(mark >= 33 for mark in marks):
    print("🎉 The student has PASSED.")
else:
    print("❌ The student has FAILED.")
