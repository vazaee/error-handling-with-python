from pprint import pprint


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
        if value <= 0:
            raise ValueError("Attribute 'balance' must be higher than zero")
        self.__balance = value

    def transfer(self, value, destination_account):
        destination_account.deposit(value)

    def withdraw(self, value):
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
            number = input("Transaction account's number: \n")

            customer = Customer(name, None, None)

            transaction_account = TransactionAccount(customer, agency, number)
            accounts.append = transaction_account
        except ValueError as E:
            print(type(E.args[1]))
            sys.exit()
        except KeyboardInterrupt:
            print(f"\n\n {len(accounts)} created")
            sys.exit()

if __name__ == "__main__":
    main()