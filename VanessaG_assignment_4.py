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

#test case 2:
print("Choose the level of coursework you would like to take on this semester: ")
print("(A) Easy (12 credits)")
print("(B) Normal (15 credits)")
print("(C) Hard (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    if current_gpa <= 2.5:
        study_hours -= 10
        stress_level += 5

elif choice == "B":
    if current_gpa >= 3.25:
        study_hours += 5
        stress_level += 10
        
elif choice == "C":
    if current_gpa >= 3.75:
        study_hours += 15
        stress_level +=20
else:
    print("Invalid") 

