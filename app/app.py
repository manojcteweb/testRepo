```python
class LoanOffer:
    def __init__(self, offer_id, terms, customer_email, customer_phone):
        self.offer_id = offer_id
        self.terms = terms
        self.customer_email = customer_email
        self.customer_phone = customer_phone
        self.status = 'Pending'

    def view_offer_details(self):
        return f"Loan Offer ID: {self.offer_id}\nTerms: {self.terms}"

    def accept_offer(self):
        if self.confirm_acceptance():
            self.status = 'Accepted'
            self.send_confirmation()
            self.record_acceptance()

    def confirm_acceptance(self):
        # Simulate user confirmation
        return True

    def send_confirmation(self):
        # Simulate sending email/SMS
        print(f"Confirmation sent to {self.customer_email} and {self.customer_phone}")

    def record_acceptance(self):
        # Simulate recording acceptance securely
        print(f"Loan offer {self.offer_id} status updated to {self.status}")

# Example usage
loan_offer = LoanOffer(offer_id=123, terms="12 months at 5% interest", customer_email="customer@example.com", customer_phone="123-456-7890")
print(loan_offer.view_offer_details())
loan_offer.accept_offer()
```
