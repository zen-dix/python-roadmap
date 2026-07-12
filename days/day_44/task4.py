class StripeProcessor:
    def pay(self, amount):
        print(f"Processing ${amount} via Stripe")


class PayPalProcessor:
    def pay(self, amount):
        print(f"Processing ${amount} via PayPal")


class Order:
    def __init__(self, amount, payment_processor):
        self.amount = amount
        self.payment_processor = payment_processor

    def checkout(self):
        self.payment_processor.pay(self.amount)

    def change_processor(self, new_processor):
        self.payment_processor = new_processor


order = Order(150, StripeProcessor())
order.checkout()
order.change_processor(PayPalProcessor())
order.checkout()
