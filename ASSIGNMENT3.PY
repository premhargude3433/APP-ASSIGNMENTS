from abc import ABC, abstractmethod

class payment_strategy(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass
    

class creditcardpayment(payment_strategy):
    def pay(self, amount):
        print("paying with credit card")
        
class paypalpayment(payment_strategy):
    def pay(self,amount):
        print("paying with paypal")
class bitcoinpayment(payment_strategy):
    def pay(self,amount):
        print("payning using bitcoin")
        
class paymentprocessor:
    def __init__(self,strategy):
        self.set_strategy(strategy)
        
    def set_strategy(self,strategy):
        
        self._strategy=strategy

    def process_payment(self,amount):
        self._strategy.pay(amount)     
        
card=creditcardpayment()
paypal=paypalpayment()
bitcoin=bitcoinpayment()

processor=paymentprocessor(card)
processor.process_payment(100)

processor.set_strategy(paypal)
processor.process_payment(200)

processor.set_strategy(bitcoin)
processor.process_payment(300)