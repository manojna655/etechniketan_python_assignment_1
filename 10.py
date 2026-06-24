# Accept the following inputs from the user: Student Name, Age, City, Course Name, Marks in Subject 1, Marks in Subject 2, Marks in Subject 3. Store all values in appropriate variables and calculate the percent and print it. 
name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")
course_name = input("Enter Course Name: ")
marks1 = float(input("Enter Marks in Subject 1: "))
marks2 = float(input("Enter Marks in Subject 2: "))
marks3 = float(input("Enter Marks in Subject 3: "))
total_marks = marks1 + marks2 + marks3
percent = (total_marks / 300) * 100
print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Course Name: {course_name}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percent}%")

    
