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

print()

study_options = ["Programming", "Math", "English", "History"] 
study_choice = input("Choose a subject to study: Programming, Math, English, and History\n")

if study_choice in study_options:

    if current_gpa <= 2.5 and study_hours <= 15:
        print("You need to study.\n")
    elif current_gpa <= 3.25 or study_hours <= 35:
        print("Nice work! Let's keep on studying.\n")
    elif current_gpa <= 3.75 and study_hours <= 50:
        print("Success is in your nearby future.\n")
    else:
        print("Excellent work!")

    if study_choice == "Programming":
        current_gpa += 0.4
        social_points -= 5
        print("Nice job! Studying programming helped boost your GPA, but you lost a few social points.")
        
    if study_choice == "Math":
        current_gpa += 0.3
        social_points += 3 
        print("Studying Math helped boost your GPA and earned you some more social points!")

    if study_choice == "English":
        current_gpa += 0.1
        social_points += 5
        print("Keep up the good work.",end=" " 
        "By studying English your social points have increased.")

    if study_choice == "History":
        current_gpa += 0.2
        social_points += 4 
        print("Nice going! Social points have increased with a small increase in GPA.")

elif study_choice not in study_options:
    print("This subject is not avaliable study.")

print()


