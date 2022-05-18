class FinancialOperationError(Exception):
    pass

class InsufficientBalanceError(FinancialOperationError):
    def __init__(self, message="", balance=None, value=None):
        self.balance = balance
        self.value = value
        msg = "Insufficient balance to carry out the transaction\n"\
            f"Actual balance: {self.balance}. Amount to be withdrawn: {self.value}"
        self.msg = message or msg
        super(InsufficientBalanceError, self).__init__(self.msg)