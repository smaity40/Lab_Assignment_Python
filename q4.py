'''Question 4: Employee Salary Analysis 
A company stores employee salaries in a list. Write a function to 
calculate the average salary, display salaries above the average, 
and increase every salary by 10%. '''

def salary_analysis(salary):
    print(f'average salary is: {sum(salary)/len(salary)}')
    print(f"this salary is above the average saraly:{[_ for _ in salary if _>sum(salary)/len(salary)]}")
    print(f"this salary increase 10% :{[_*1.10 for _ in salary]}")

salary_analysis([10000,20000,15000,27000,32000,28000])

