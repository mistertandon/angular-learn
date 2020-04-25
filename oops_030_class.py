class Employee:

    """
    Class variables are variables that are shared among all instances of class.
    """

    full_name = None

    email = None

    raise_amount = 1.05

    def __init__(self, name, last_name, salary):

        self.name = name
        self.last_name = last_name
        self.salary = salary

        self.create_email_id()
        self.get_full_name()

    """
    1. Regular methods in a class automatically take instance <self> as the first argument,
       by convetion we call it as <self>
    """
    def get_full_name(self):

        self.full_name = "{} {}".format(self.name, self.last_name)

        return

    def create_email_id(self):

        self.email = "{}{}@company.com".format(self.name, self.last_name)

        return

    def apply_raise(self):
        """
        What happens, when we try to access an attribute on instance, it'll first check if the instance
        contains that attribute and if it doesn't then it'll see if class (or) any class it inherited
        from contain that attribute.
        We may use either Employee.raise_amount (or) self.raise_amount
        """
        self.salary = self.salary * self.raise_amount

    def display_salary(self):

        print("{} Salary is {}".format(self.full_name, self.salary))

        return True

    """
    2. Class methods take class reference as the first argument.
    """
    @classmethod
    def set_raise_amount(cls, amount):

        cls.raise_amount = amount

        return True