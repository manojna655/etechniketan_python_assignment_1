# Create a list named subjects containing: Python, SQL, Excel, Tableau Perform the following: a. Display the complete list  b. Display the first subject and the last subject  c. Add one new subject between Python and SQL. Display the updated list  d. Delete Excel from the list and display the updated list e. Copy the list into another list. f. Sort the new list in ascending order. g. Check if Excel is present in the list (use appropriate operator) 
subjects = ["Python", "SQL", "Excel", "Tableau"]
print("Complete list:", subjects)
print("First subject:", subjects[0])
print("Last subject:", subjects[-1])
subjects.insert(1, "Data Science")
print("Updated list:", subjects)
subjects.remove("Excel")
print("Updated list after deleting Excel:", subjects)
new_list = subjects.copy()
new_list.sort()
print("New list in ascending order:", new_list)
if "Excel" in subjects:
    print("Excel is present in the list.")
else:
    print("Excel is not present in the list.")
