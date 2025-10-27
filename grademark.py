# Determine the grade based on the mark
mark = int(input("Enter the mark:"))
if 90 <= mark <= 100:
    grade = "A"
    print(grade, "He/She is an excellent student")
elif 80 <= mark < 90:
    grade = "B"
    print(grade, "He/She is a good student")
elif 70 <= mark < 80:
    grade = "C"
    print(grade, "He/She is an average student")
elif 60 <= mark < 70:
    grade = "D"
    print(grade, "He/She needs improvement")
elif 0 <= mark < 60:
    grade = "F"
    print(grade, "He/She has failed")
else:
    print("Invalid mark. Please enter a value between 0 and 100.")

