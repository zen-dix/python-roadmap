class PaymentGateway:
    def process_payment(self, amount: float):
        raise NotImplementedError()


class StripeGateway(PaymentGateway):
    def process_payment(self, amount: float):
        print(f"[Stripe] Processing credit card payment: ${amount}")


class CryptoGateway(PaymentGateway):
    def process_payment(self, amount: float):
        print(f"[Crypto] Verifying blockchain transaction for: ${amount}")


s = StripeGateway()
c = CryptoGateway()

gateways = [s, c]

for gateway in gateways:
    payment = gateway
    payment.process_payment(150.50)

