from decorators import require_keywords
from investement import Loan, Stock, RealEstate
from portfolio import Portfolio


class PortfolioFactory:
    def get_portfolio(self, portfolio_type: str, **kwargs):
        if portfolio_type == "house":
            return self.house_portfolio(**kwargs)

    @require_keywords("houses")
    def house_portfolio(self, **kwargs):
        for i in range(kwargs["houses"]):
            house = RealEstate()
        return Portfolio()