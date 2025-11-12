#Collect student details via dictionary and function
def student_details():
       student = {}
       student['name'] = input("Enter student's name: ")
       student['age'] = input("Enter student's age: ")
       student['grade'] = input("Enter student's grade: ")
       student['student_id'] = input("Enter student's ID: ")
       return student
print (student_details())




