# TODO - 
# 1. load json data
# 2. calculate productivity score for each student 
# productive score = (hours_worked * 2) + hours_studied
# 3. find most productivity score 
# 4. group by department and find - total_hours_worked, total_hours_studied, avg_score and display for each department
# 5. Most productive student name 

import json
from collections import defaultdict

def load_data():
    with open('students.json') as file:
        student_data = json.load(file)
    return student_data

def main():
    print("Hello from student-data!")
    student_data = load_data()
    print("Json data = ")
    print("\n")
    print(student_data)

    filtered_data = [student for student in student_data]
    # print(filtered_data)
    productivity_score = [((student["hours_worked"]*2) + student["hours_studied"]) for student in filtered_data]
    print("\n")
    print("productivity score = ")
    print("\n")
    print(productivity_score)
    print("\n")

    for student in student_data:
        student["prod_score"] = (student["hours_worked"]*2) + student["hours_studied"]

    print("Added productivity score in original data \n", student_data)

    sort_by_score = sorted(filtered_data, key = lambda  s: (s["hours_worked"] * 2) + s["hours_studied"] , reverse=True)
    print("\n")
    print("Most productive student = ")
    print(sort_by_score[0]['name'])
    print("\n")

    dept_dict = defaultdict(lambda : [0,0,0,0])
    total_hours_worked = 0
    total_hours_studied = 0
    total_score = 0
    avg_score = 0.0

    for student in student_data:
        dept = student['department']

        worked = student['hours_worked']
        studied = student['hours_studied']
        score = worked * 2 + studied

        dept_dict[dept][0] += worked
        dept_dict[dept][1] += studied
        dept_dict[dept][2] += score
        dept_dict[dept][3] += 1

    
    for key, val in dept_dict.items():
        total_worked, total_studied, total_score, count = val
        print("\n")
        print("Department ", key)

        print("Total worked = ", total_worked)
        print("Total studied = ", total_studied)
        print("Total score = ", total_score)
        print("Avg score = ", total_score / count)


if __name__ == "__main__":
    main()
