'''Question 2: Online Mobile Store 
An online store maintains a list of mobile prices. Write a function 
to display all mobiles costing more than ₹20,000, calculate the 
total inventory value, and find the most expensive mobile price. '''

def mobile_info(price):
    print(f"this mobiles are costing more than 20000 : {[ _ for _ in price if _>20000]}")
    print(f"total inventory value is :{sum(price)}")
    print(f"most expensive mobile price :{max(price)}")


mobile_info([22000,25000,26000,70000,10000,20000,17000,40000])


