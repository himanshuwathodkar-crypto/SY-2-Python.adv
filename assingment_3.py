class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class DebitCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card")


class UPI(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


processor = PaymentProcessor(CreditCard())
processor.process_payment(1000)

processor.set_strategy(DebitCard())
processor.process_payment(2000)

processor.set_strategy(UPI())
processor.process_payment(500)