# Dictionary comprehension
import random
from pprint import pprint

# Create a list which will be used to create our dictionary
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# Create a dictionary from a list with no condition
student_scores = {name: random.randint(1, 100) for name in names}

# Create a dictionary from another dictionary if a condition is met
passed_students = {name: score for name, score in student_scores.items() if score >= 50}

# Use pprint because why not
pprint(passed_students)
