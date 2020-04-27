from oops_020_variables import Employee


class Developer(Employee):

    def __init__(self, name, last_name, salary, prog_lang):

        """
        We may also use
        Employee.__init__(self, name, last_name, salary)
        """
        super().__init__(name, last_name, salary)

        self.prog_lang = prog_lang


dev_i: Developer = Developer('Parvesh', 'Tandon', 100, 'Python')
print(help(Developer))