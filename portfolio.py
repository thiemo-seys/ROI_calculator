from investement import Investment

class Portfolio:
    def __init__(self, investements: list[Investment]):
        self.investements = investements

    def value(self):
        pass

    # These functions deserve better names
    def equity(self):
        pass

    def liability(self):
        pass

    def income(self):
        pass

    def expenses(self):
        pass

    def liquid_equity(self):
        pass

    # TODO: these methods feel dirty
    def real_estate(self):
            return [investement for investement in self.investements if investement.__class__.__name__ == "RealEstate"]

    def stocks(self):
        return [investement for investement in self.investements if investement.__class__.__name__ == "Stock"]

    def loans(self):
        return [investement for investement in self.investements if investement.__class__.__name__ == "Loan"]

