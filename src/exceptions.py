class InsufficientBalanceError(Exception):
    def __init__(self, message="", balance=None, value=None):
        self.balance = balance
        self.value = value
        msg = "Insufficient balance to carry out the transaction\n"\
            f"Actual balance: {self.balance}. Amount to be withdrawn: {self.value}"
        super(InsufficientBalanceError, self).__init__(message or msg)