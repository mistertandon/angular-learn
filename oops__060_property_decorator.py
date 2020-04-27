class Employee:

    full_name: str = None

    email: str = None

    def __init__(self, name, last_name):

        self.name = name
        self.last_name = last_name

    @property
    def email(self) -> str:

        return "{}.{}@company.com".format(self.name, self.last_name)

    @property
    def full_name(self) -> str:

        return "{} {}".format(self.name, self.last_name)

    @full_name.setter
    def full_name(self, name):

        self.name, self.last_name = name.split(' ')

    @full_name.deleter
    def full_name(self):
        self.name, self.last_name = None, None