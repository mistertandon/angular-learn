from oops_030_classmethod import Employee

emp_i: Employee = Employee('Parvesh', 'Tandon', 100)

"""
Here we are setting instance variable <raise_amount> to 1.20, thus it's
scope would be limited to emp_i instance only.
"""
emp_i.raise_amount = 1.20
emp_i.apply_raise()
emp_i.display_salary()


"""
Here we are setting class variable <raise_amount> to 1.50 therefore,
future instances would have value <1.5> instead of <1.10>
"""
emp_ii: Employee = Employee('Prabhash', 'Tandon', 100)
emp_ii.set_raise_amount(1.50)
emp_ii.apply_raise()
emp_ii.display_salary()

emp_iii: Employee = Employee('Jiyanshi', 'Tandon', 100)
emp_iii.apply_raise()
emp_iii.display_salary()

"""
How do we may use classmethod as alternative constructor
"""
emp_info: str = "praveen-tandon-100"
emp_iv: Employee = Employee.from_string(emp_info)