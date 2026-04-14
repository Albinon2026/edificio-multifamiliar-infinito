class IncomeRegistration:
    def __init__(self):
        self.bank_balance = 28613.29
        self.payments = []

    def register_payment(self, department, amount, date):
        payment_info = {
            'department': department,
            'amount': amount,
            'date': date,
            'status': self.classify_payment(date)
        }
        self.payments.append(payment_info)
        self.bank_balance += amount

    def classify_payment(self, date):
        from datetime import datetime
        current_month = datetime.utcnow().strftime('%Y-%m')
        payment_month = date.strftime('%Y-%m')
        if payment_month == current_month:
            return 'current'
        elif payment_month < current_month:
            return 'arrears'
        else:
            return 'advance'

    def handle_unrecognized_quota(self, quota):
        # Logic for managing unrecognized quota
        return f'Department {quota} has an unrecognized payment.'

# Example usage
# income_reg = IncomeRegistration()
# income_reg.register_payment(department='Department A', amount=500, date=datetime(2026, 4, 14))
