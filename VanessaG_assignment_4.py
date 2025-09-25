#required variables
student_name = ("Vanessa Gray")
current_gpa = 4.0 #between 1.0-4.0
study_hours = 30 # (ex. 25)
social_points = 55 #(ex. 50)
stress_level = 75 #0-100

#test case 1:
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

#main if statement for coursework choice
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

#main if statement for study choice
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

#test case 4:
print("============= FINAL SCORES RELEASED =============")

grades = ["A", "B", "C", "D"]

print("Scored have been released for the subject you studied.\n")

final_grade = input("Enter your final grade for subject studied (A, B, C or D):\n")

print()

#pass or fail check
if final_grade not in grades:
    print("Failed. You need to repeat this class to graduate.")

elif final_grade in grades:
    print("Congratulations! You passed and will be able to graduate.")

print()

#graduation messages
if current_gpa <= 2.5:
    if social_points <= 35:
        print("You graduated with a plain social life.")
    else:
        print("You graduated and made sure you never missed a night out.")
    
if current_gpa <= 3.25:
    if social_points <= 35:
        print("You stayed on top of your work but missed out on your social life.")
    else:
        print("You balanced the best of both worlds: social and work!")

if current_gpa <= 3.75:
    if social_points <= 35:
        print("You excelled outstandingly in your major but lacked in the social world.")
    else:
        print("Congrats! You lived the full college expereince all while staying on track!")

else:
    print("You soaked in your College Daze to the fullest. Well done!")

print()

#final stats
print("Here are your final stats:")
print(f"Final GPA: {current_gpa}")
print(f"Final Hours Studied: {study_hours}")
print(f"Final Social Points: {social_points}")
print(f"Final Subject Studied: {study_choice}")
