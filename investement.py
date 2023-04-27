class Investment:
    def __init__(self, value: float, yearly_apr: float):
        self.value = value
        self.yearly_apr = yearly_apr

    def appreciate(self):
        self.value *= 1 + self.yearly_apr


class Stock(Investment):
    def __init__(self, value: float, yearly_apr: float, yearly_cr: float):
        super().__init__(value, yearly_apr)
        self.yearly_cr = yearly_cr

    def appreciate(self):
        super().appreciate()
        self.value *= 1 - self.yearly_cr


class RealEstate(Investment):
    def __init__(self, value: float, yearly_apr: float, yearly_cr: float, yearly_gry: float):
        super().__init__(value, yearly_apr)
        self.yearly_cr = yearly_cr
        self.yearly_gry = yearly_gry

    @property
    def income(self):
        return self.value * self.yearly_gry

    @property
    def expenses(self):
        self.value *= 1 - self.yearly_cr

    def appreciate(self):
        super().appreciate()
        self.value += self.income
        self.value -= self.expenses()


class Loan:
    def __init__(self,balance: float, apr: float, loan_term: int):
        self.balance = balance
        self.apr = apr
        self.loan_term = loan_term

    @property
    def total_amount_of_payments(self):
        return self.loan_term * 12

    @property
    def monthly_rate(self):
        return self.apr / 12

    @property
    def monthly_payment(self):
        payment = self.balance * (self.monthly_rate * (1 + self.monthly_rate) ** self.total_amount_of_payments) \
                  / ((1 + self.monthly_rate) ** self.total_amount_of_payments - 1)
        return payment
