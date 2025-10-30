"""
Created on May 15, 2015

Plotting example from Introduction to Computation and Programming Using Python
"""

from matplotlib import pyplot
import numpy as np


def find_payment(loan: float, rate: float, m: int):
    """
    Returns the monthly payment for a mortgage of size
    loan at a monthly rate of r for m months"""
    return loan * ((rate * (1 + rate) ** m) / ((1 + rate) ** m - 1))


class MortgagePlots:
    def __init__(self, loan: float, paid: float):
        self.loan: float = loan
        self.paid: list = [paid]
        self.owed: list = [loan]
        self.legend: str = ""

    def plot_payments(self, style: str):
        pyplot.plot(self.paid[1:], style, label=self.legend)

    def plot_balance(self, style: str):
        pyplot.plot(self.owed, style, label=self.legend)

    def plot_total_pd(self, style: str):
        total_pd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            total_pd.append(total_pd[-1] + self.paid[i])
        pyplot.plot(total_pd, style, label=self.legend)

    def plot_net(self, style: str):
        total_pd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            total_pd.append(total_pd[-1] + self.paid[i])
        equity = np.array([self.loan] * len(self.owed))
        equity = equity - np.array(self.owed)
        net = np.array(total_pd) - equity
        pyplot.plot(net, style, label=self.legend)


class Mortgage(MortgagePlots):
    """Abstract class for building different kinds of mortgages"""

    def __init__(self, loan: float, annual_rate: float, months: int):
        """Create a new mortgage"""
        MortgagePlots.__init__(self, loan, 0.0)
        self.rate = annual_rate / 12.0
        self.months = months
        self.payment = find_payment(loan, self.rate, months)
        self.legend: str = ""  # description of mortgage

    def make_payment(self):
        """Make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1] * self.rate
        self.owed.append(self.owed[-1] - reduction)

    def get_total_paid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)

    def __str__(self):
        return self.legend


class Fixed(Mortgage):
    def __init__(self, loan: float, rate: float, months: int):
        Mortgage.__init__(self, loan, rate, months)
        self.legend = "Fixed, " + str(rate * 100) + "%"


class FixedWithPayments(Mortgage):
    def __init__(self, loan: float, rate: float, months: int, payments: float):
        Mortgage.__init__(self, loan, rate, months)
        self.payments = payments
        self.paid = [loan * (payments / 100.0)]
        self.legend = "Fixed, " + str(rate * 100) + "%, " + str(payments) + " points"


class TwoRate(Mortgage):
    def __init__(
        self, loan: float, rate: float, months: int, teaser_rate, teaser_months
    ):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self.teaser_months = teaser_months
        self.teaser_rate = teaser_rate
        self.next_rate = rate / 12.0
        self.legend = (
            str(teaser_rate * 100)
            + "% for "
            + str(self.teaser_months)
            + " months,\n then "
            + str(rate * 100)
            + "%"
        )

    def make_payment(self):
        if len(self.paid) == self.teaser_months + 1:
            self.rate = self.next_rate
            self.payment = find_payment(
                self.owed[-1], self.rate, self.months - self.teaser_months
            )
        Mortgage.make_payment(self)


def compare_mortgages(
    amount: float,
    years: int,
    fixed_rate: float,
    payment: float,
    payment_rate: float,
    variable_rate_1: float,
    variable_rate_2: float,
    months: int,
):
    total_months = years * 12
    fixed1 = Fixed(amount, fixed_rate, total_months)
    fixed2 = FixedWithPayments(amount, payment_rate, total_months, payment)
    two_rate = TwoRate(amount, variable_rate_2, total_months, variable_rate_1, months)
    morts = [fixed1, fixed2, two_rate]
    for _ in range(total_months):
        for mort in morts:
            mort.make_payment()
    plot_mortgages(morts, amount)


def plot_mortgages(morts: list, amount: float):
    styles = ["b-", "b-.", "b:"]
    payments = 0
    cost = 1
    balance = 2
    netCost = 3
    pyplot.figure(payments)
    pyplot.title("Monthly Payments of Different $%s Mortgages" % amount)
    pyplot.xlabel("Months")
    pyplot.ylabel("Monthly Payments")
    pyplot.figure(cost)
    pyplot.title("Cash Outlay Different $%s Mortgages" % amount)
    pyplot.xlabel("Months")
    pyplot.ylabel("Total Payments")
    pyplot.figure(balance)
    pyplot.title("Balance Remaining $%s Mortgages" % amount)
    pyplot.xlabel("Months")
    pyplot.ylabel("Remaining Loan Balance $")
    pyplot.figure(netCost)
    pyplot.title("Net Cost $%s Mortgages" % amount)
    pyplot.xlabel("Months")
    pyplot.ylabel("Payments - Equity $")
    for i in range(len(morts)):
        pyplot.figure(payments)
        morts[i].plot_payments(styles[i])
        pyplot.figure(cost)
        morts[i].plot_total_pd(styles[i])
        pyplot.figure(balance)
        morts[i].plot_balance(styles[i])
        pyplot.figure(netCost)
        morts[i].plot_net(styles[i])
    pyplot.figure(payments)
    pyplot.legend(loc="upper center")
    pyplot.figure(cost)
    pyplot.legend(loc="best")
    pyplot.figure(balance)
    pyplot.legend(loc="best")


if __name__ == "__main__":
    compare_mortgages(
        amount=200000,
        years=30,
        fixed_rate=0.07,
        payment=3.25,
        payment_rate=0.05,
        variable_rate_1=0.045,
        variable_rate_2=0.095,
        months=48,
    )
    pyplot.show()
