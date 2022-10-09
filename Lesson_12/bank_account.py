from decimal import Decimal
from datetime import datetime
from uuid import uuid4, UUID
from pprint import pprint





class BankAccount:

    def __init__(self, account_name: str, account_id: UUID):

        self.account_name = account_name
        self.account_id = account_id
        self.__balance = Decimal('0.0')
        self.transactions = []



    def deposit(self, amount: float):
        deposit_transaction = []
        now = datetime.now().date()
        self.__balance += Decimal(str(amount))
        deposit_transaction.append(now.strftime('%Y-%m-%d'))
        deposit_transaction.append('deposit')
        deposit_transaction.append(amount)
        self.transactions.append(deposit_transaction)



    def withdrawal(self, amount: float, commission: float = 1):
        withdrawal_transaction = []
        bank_commission = commission / 100
        now = datetime.now().date()
        self.__balance -= Decimal(str(amount + (amount * bank_commission)))
        withdrawal_transaction.append(now.strftime('%Y-%m-%d'))
        withdrawal_transaction.append('withdrawal')
        withdrawal_transaction.append(amount)
        self.transactions.append(withdrawal_transaction)




    def get_balance(self) -> str:
        return f"{self.account_name}, account balance:{self.__balance.quantize(Decimal('1.000'))}"






if __name__ == '__main__':

    bank_account = BankAccount('Bohdan Savchuk', uuid4())
    print(bank_account.account_name, bank_account.account_id)
    #print(bank_account.get_balance())
    bank_account.deposit(100)
    bank_account.deposit(100)
    bank_account.deposit(100)
    bank_account.withdrawal(100)
    bank_account.withdrawal(100)
    bank_account.withdrawal(100)
    pprint(bank_account.transactions)
    print(bank_account.get_balance())