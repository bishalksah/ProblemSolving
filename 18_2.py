#percentage  marks of obtained by students are input through keyboard (0-100). Write a program to find out grade of the student according to the following criteria:
# % >= 60 is ---1st class
# % >= 50 and < 60 is ---2nd class
# % >= 40 and < 50 is ---3rd class
# % < 40 is ---Fail

percentage = float(input("Enter the percentage marks obtained by the student: "))
if percentage >= 60:
    grade = "1st class"
elif percentage >= 50:
    grade = "2nd class"
elif percentage >= 40:
    grade = "3rd class"
else:
    grade = "Fail"

print("The grade of the student is:", grade)