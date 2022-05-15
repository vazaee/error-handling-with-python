from pprint import pprint


class Client:
    def __init__(self, name, cpf, occupation):
        self.name = name
        self.cpf = cpf
        self.occupation = occupation


class TransactionAccount:
    total_accounts_created = 0
    operation_tax = None

    def __init__(self, client, agency, number):
        self.balance = 100
        self.client = client
        self.agency = agency
        self.number = number
        TransactionAccount.total_accounts_created += 1
        TransactionAccount.operation_tax = 30 / TransactionAccount.total_accounts_created

    def transfer(self, value, destination_account):
        destination_account.deposit(value)

    def withdraw(self, value):
        self.balance -= value

    def deposit(self, value):
        self.balance += value


transaction_account = TransactionAccount(None, '00', '101')