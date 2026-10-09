'''Question 1: Student Marks Analysis 
A college stores students' marks in a list. Write a function that 
accepts a list of marks and displays the highest mark, lowest 
mark, average mark, and number of students who passed (marks 
of 40 or above).'''

def analyze_marks(marks):
    print(f"highest marks is {max(marks)}")
    print(f"lowest marks is {min(marks)}")
    print(f"average marks is {sum(marks)/len(marks)}")
    passed_student=[    _    for _ in marks if _>=40  ]
    print(f"no of student passed:{len(passed_student)}")
   

analyze_marks([78, 35, 92, 45, 60, 28, 88])