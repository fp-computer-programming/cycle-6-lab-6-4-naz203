"""
Create a Python file named lab_6-4

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a list of 3 subjects that you have studied at Prep and store it as a variable.
Use a method to add a fourth subject you have studied to the end of the list.
Use a method to return the index of one of the subjects in your list.
Order the subjects alphabetically using a method.
Use a method to make a copy of this list and store it in a different variable.
Use a method to order this second list in reverse alphabetical order.
"""
#author = "nazeer thompson"
# stores subjects studies as variables 
subjects= ['math','science', 'English']

# method to add a fourth subject you have studied to the end of the list.
subjects.append('History')

# method to return the index of one of the
index = subjects.index ('Science')

# Method used to Order the subjects alphabetically 
subjects.sort()

# method to make a copy of this list and store it in a different variable.
subjects_copy = subjects.copy()

#method to order this second list in reverse alphabetical order.
subjects_copy.sort (reverse=True)
print (subjects)