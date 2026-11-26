from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def pay(self, amt):
        pass


class RazorpayCard(PaymentMethod):
    def __init__(self, card_number, **kw):
        self.card = card_number

    def get_details(self):
        return "Razorpay Card: " + self.card

    def pay(self, amt):
        print("Paid", amt, "via", self.get_details())
        return True


class RazorpayUPI(PaymentMethod):
    def __init__(self, upi_id, **kw):
        self.upi = upi_id

    def get_details(self):
        return "Razorpay UPI: " + self.upi

    def pay(self, amt):
        print("Paid", amt, "via", self.get_details())
        return True


class StripeCard(PaymentMethod):
    def __init__(self, card_number, **kw):
        self.card = card_number

    def get_details(self):
        return "Stripe Card: " + self.card

    def pay(self, amt):
        print("Paid", amt, "via", self.get_details())
        return True


class StripeUPI(PaymentMethod):
    def __init__(self, upi_id, **kw):
        self.upi = upi_id

    def get_details(self):
        return "Stripe UPI: " + self.upi

    def pay(self, amt):
        print("Paid", amt, "via", self.get_details())
        return True


class FactoryPaymentMethod(ABC):
    factory = {}

    @classmethod
    def get_payment_object(cls, typ, **kw):
        if typ in cls.factory:
            return cls.factory[typ](**kw)
        raise ValueError("Method not found")


class RazorpayFactory(FactoryPaymentMethod):
    factory = {
        "card": RazorpayCard,
        "upi": RazorpayUPI
    }


class StripeFactory(FactoryPaymentMethod):
    factory = {
        "card": StripeCard,
        "upi": StripeUPI
    }
