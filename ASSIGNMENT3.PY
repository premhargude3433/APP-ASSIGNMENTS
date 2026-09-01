from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print("Paying", amount, "using Credit Card")

class PayPal(PaymentStrategy):
    def pay(self, amount):
        print("Paying", amount, "using PayPal")

class Bitcoin(PaymentStrategy):
    def pay(self, amount):
        print("Paying", amount, "using Bitcoin")

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount) 
    
# Create payment methods

card = CreditCard()
paypal = PayPal()
bitcoin = Bitcoin()

# Credit Card

processor = PaymentProcessor(card)
processor.process_payment(100)

# PayPal

processor = PaymentProcessor(paypal)
processor.process_payment(200)

# Bitcoin

processor = PaymentProcessor(bitcoin)
processor.process_payment(300)

