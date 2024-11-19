# Apollos Eastman
# Nov 19 2024
# Return Statements

print()

# Destination Europe
def describe_vacation(destination, activity, season = 'summer'):
    desc = (f'I am going to {destination} for {season} vacation. I will {activity} there.')
    return desc

description1 = describe_vacation('Florida', 'play volleyball')
description2 = describe_vacation('Canada', 'go fishing', 'spring')

for description in (description1, description2):
    print(description)

print()

# Student Major
def show_major(first_name, university, major = 'Sports Medicine'):
    student = (f'{first_name} attends {university} and is majoring {major}.')
    return student

student_major1 = show_major('Ben', 'University of Virginia', 'Audio Technology')
student_major2 = show_major('Mark', 'University of Oklahoma')

for stud in (student_major1, student_major2):
    print(stud)
