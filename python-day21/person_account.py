class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, description, amount):
        self.incomes.append((description, amount))

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))

    def total_income(self):
        return sum(amount for desc, amount in self.incomes)

    def total_expense(self):
        return sum(amount for desc, amount in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f"{self.firstname} {self.lastname}, Balance: {self.account_balance()}"

