# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount

service_year=int(input("Enter the service years of employee:"))
salary=int(input("Enter the salary of employee:"))

if service_year>5:
  bonus=salary*5/100
  total_salary=salary+bonus
  print("Your payable amaount is:",total_salary)

else:
  print("Your payable amount is:",toatal_salary)