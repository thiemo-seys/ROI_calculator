import pytest

from investement import RealEstate

@pytest.fixture
def loan():
    return Loan(100_000, 0.05, 20)


class Test_Loan:
    def test_monthly_payment(self, loan):
        assert loan.monthly_payment == 659.9557392166588

