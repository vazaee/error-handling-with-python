from pprint import pprint
from exceptions import InsufficientBalanceError, FinancialOperationError
from reader import FileReader

class Customer:
    def __init__(self, name, cpf, occupation):
        self.name = name
        self.cpf = cpf
        self.occupation = occupation


class TransactionAccount:
    total_accounts_created = 0
    operation_tax = None

    def __init__(self, customer, agency, number):
        self.__balance = 100
        self.customer = customer
        self.__agency = agency
        self.__number = number
        self.withdrawals_not_allowed = 0
        self.transfers_not_allowed = 0
        self.__set_agency(agency)
        self.__set_number(number)
        TransactionAccount.total_accounts_created += 1
        TransactionAccount.operation_tax = 30 / TransactionAccount.total_accounts_created

    @property
    def agency(self):
        return self.__agency

    def __set_agency(self, value):
        if not isinstance(value, int):
            raise ValueError("Attribute 'agency' must be an integer", value)
        if value <= 0:
            raise ValueError("Attribute 'agency' must be higher than zero")

        self.__agency = value

    @property
    def number(self):
        return self.__number

    def __set_number(self, value):
        if not isinstance(value, int):
            raise ValueError("Attribute 'number' must be an integer")
        if value <= 0:
            raise ValueError("Attribute 'number' must be higher than zero")
        self.__number = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, int):
            raise ValueError("Attribute 'balance' must be an integer")

        self.__balance = value

    def transfer(self, value, destination_account):
        if value < 0:
            raise ValueError("The amount to be deposited cannot be less than zero")

        try:
            self.withdraw(value)
        except InsufficientBalanceError as E:
            self.transfers_not_allowed += 1
            E.args = ()
            raise FinancialOperationError("Operation not finished") from E
        destination_account.deposit(value)

    def withdraw(self, value):
        if value < 0:
            raise ValueError("The amount to be withdrawn cannot be less than zero.")
        if self.balance < value:
            self.withdrawals_not_allowed += 1
            raise InsufficientBalanceError("", balance=self.balance, value=value)

        self.balance -= value

    def deposit(self, value):
        self.balance += value


def main():
    import sys

    accounts =[]
    while True:
        try:
            name = input("Customer's name: \n")
            agency = input("Agency number: \n")
            breakpoint()
            number = input("Transaction account's number: \n")

            customer = Customer(name, None, None)

            transaction_account = TransactionAccount(customer, agency, number)
            accounts.append = transaction_account

        except KeyboardInterrupt:
            print(f"\n\n {len(accounts)} created")
            sys.exit()

# if __name__ == "__main__":
#     main()

# transaction_account1 = TransactionAccount(None, 400, 1234567)
# transaction_account2 = TransactionAccount(None, 401, 1234568)
#
# try:
#     transaction_account1.withdraw(1000)
#     print("Transaction Account1 Balance: ",transaction_account1.balance)
#     print("Transaction Account2 Balance: ",transaction_account2 .balance)
# except FinancialOperationError as E:
#     breakpoint()
#     pass

with FileReader("file.txt") as reader:
    reader.read_next_line()