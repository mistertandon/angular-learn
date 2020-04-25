from oops_020_variables import Employee

"""
Instance variables [like name, last_name, salary] can be unique for each instances.
"""
emp_i = Employee('Prabhash', 'Tandon', 100)
emp_i.raise_amount = 1.10
emp_i.apply_raise()
emp_i.display_salary()

emp_ii = Employee('Jiyanshi', 'Tandon', 100)
emp_ii.apply_raise()
emp_ii.display_salary()

"""
Now lets update Class <raise_amount> attribute and see how does it impact different
instances of class
"""
Employee.raise_amount = 1.10

emp_iii = Employee('Parvesh', 'Tandon', 100)
emp_iii.apply_raise()
emp_iii.display_salary()

emp_iv = Employee('Parveen', 'Tandon', 100)
emp_iv.apply_raise()
emp_iv.display_salary()

