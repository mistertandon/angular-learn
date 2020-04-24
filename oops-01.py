class Employee:
    pass


emp_i = Employee()
emp_ii = Employee()

emp_i.name = 'parvesh'
emp_i.last_name = 'tandon'
emp_i.email = "{}{} @company.com".format(emp_i.name, emp_i.last_name)
emp_i.salary = 2000000

emp_ii.name = 'jiyanshi'
emp_ii.last_name = 'tandon'
emp_ii.email = "{}{} @company.com".format(emp_ii.name, emp_ii.last_name)
emp_ii.salary = 2500000

print(emp_i)
print(emp_ii)