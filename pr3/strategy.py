from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount} руб. по кредитной карте.")

class QiwiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount} руб. через Qiwi.")

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Перевод {amount} руб. на банковский счет.")
class PaymentContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy
    
    def make_payment(self, amount):
        self.payment_strategy.pay(amount)
if __name__ == "__main__":
    payment_context = PaymentContext(CreditCardPayment())
    payment_context.make_payment(100)  # Оплата 100 руб. по кредитной карте.
    
    payment_context.set_payment_strategy(QiwiPayment())
    payment_context.make_payment(50)  # Оплата 50 руб. через Qiwi.
    
    payment_context.set_payment_strategy(BankTransferPayment())
    payment_context.make_payment(200)  # Перевод 200 руб. на банковский счет.
