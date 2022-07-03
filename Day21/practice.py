class PersonAccount:
    def __init__(self, firstname, lastname, total_income, total_expense, account_info):
        self.firstname = firstname
        self.lastname = lastname
        self.total_income = total_income
        self.total_expense = total_expense
        self.account_info = account_info
    def add_income(self, amount):
        self.incomes = amount
        self.total_income += amount
    def add_expense(self, amount):
        self.total_expense += amount
    def account_Info(self):
        return f'Firstname : {self.firstname} \nLastname : {self.lastname} \nAccount balance : {self.total_income} \nTotal expenses : {self.total_expense} \nAccount info : {self.account_info}'
    

p = PersonAccount('Manish', 'Kumar', 0, 0, 'Savings')
p.add_income(5000)
p.add_expense(2000)
p.add_income(10000)
p.add_expense(5000)
print(p.account_Info())

        