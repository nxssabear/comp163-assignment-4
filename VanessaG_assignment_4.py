#required variables
student_name = input()
current_gpa = float(input())
study_hours = int(input())
social_points = int(input())
stress_level = int(input())

print("Welcome to College Life\nHere are your current stats:")
print(student_name)
print(current_gpa)
print(study_hours)
print(social_points)
print(stress_level)

print("Choose the level of coursework you would like to take on this semester: ")
print("(A) Light (12 credits)")
print("(B) Normal (15 credits)")
print("(C) Heavy (18 credits)")

choice = input("Your choice: ") 