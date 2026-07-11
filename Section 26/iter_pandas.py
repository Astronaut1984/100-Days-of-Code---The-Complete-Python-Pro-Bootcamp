import pandas

students_dict = {"student": ["Angela", "James", "George"], "score": [70, 80, 90]}
student_df = pandas.DataFrame(students_dict)

# We use DataFrame.iterrows() to iterate over each row and access each item in said row
for idx, row in student_df.iterrows():
    print(f"{idx}: {row.student}, {row.score}")
