# Write a Python program that prints all the keywords available in Python. 


from ast import keyword


print("The keywords in Python are:")
for k in keyword.kwlist:
    print(k)    
