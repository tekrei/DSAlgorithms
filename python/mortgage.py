"""
Created on May 15, 2015

Plotting example from Introduction to Computation and Programming Using Python
"""
from matplotlib import pylab


def find_payment(loan: float, rate: float, m: int):
    """
    Returns the monthly payment for a mortgage of size
    loan at a monthly rate of r for m months"""
    return loan * ((rate * (1 + rate) ** m) / ((1 + rate) ** m - 1))


class MortgagePlots():
    def __init__(self, loan, paid):
        self.loan = loan
        self.paid = [paid]
        self.owed = [loan]
        self.legend = None

    def plot_payments(self, style: str):
        pylab.plot(self.paid[1:], style, label=self.legend)

    def plot_balance(self, style: str):
        pylab.plot(self.owed, style, label=self.legend)

    def plot_total_pd(self, style: str):
        total_pd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            total_pd.append(total_pd[-1] + self.paid[i])
        pylab.plot(total_pd, style, label=self.legend)

    def plot_net(self, style: str):
        total_pd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            total_pd.append(total_pd[-1] + self.paid[i])
        equity = pylab.array([self.loan] * len(self.owed))
        equity = equity - pylab.array(self.owed)
        net = pylab.array(total_pd) - equity
        pylab.plot(net, style, label=self.legend)


class Mortgage(MortgagePlots):
    """Abstract class for building different kinds of mortgages"""

    def __init__(self, loan: float, annual_rate: float, months: int):
        """Create a new mortgage"""
        MortgagePlots.__init__(self, loan, 0.0)
        self.rate = annual_rate / 12.0
        self.months = months
        self.payment = find_payment(loan, self.rate, months)
        self.legend = None  # description of mortgage

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
        self.legend = "Fixed, " + \
            str(rate * 100) + "%, " + str(payments) + " points"


class TwoRate(Mortgage):
    def __init__(self, loan: float, rate: float, months: int, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, teaser_rate, months)
        self.teaser_months = teaser_months
        self.teaser_rate = teaser_rate
        self.next_rate = rate / 12.0
        self.legend = str(teaser_rate * 100) + "% for " + \
            str(self.teaser_months) + " months,\n then " + str(rate * 100) + "%"

    def make_payment(self):
        if len(self.paid) == self.teaser_months + 1:
            self.rate = self.next_rate
            self.payment = find_payment(
                self.owed[-1], self.rate, self.months - self.teaser_months)
        Mortgage.make_payment(self)


def compare_mortgages(amount: float, years: int, fixed_rate: float, payment: float, payment_rate: float, variable_rate_1: float, variable_rate_2: float, months: int):
    total_months = years * 12
    fixed1 = Fixed(amount, fixed_rate, total_months)
    fixed2 = FixedWithPayments(amount, payment_rate, total_months, payment)
    two_rate = TwoRate(amount, variable_rate_2,
                       total_months, variable_rate_1, months)
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
    pylab.figure(payments)
    pylab.title("Monthly Payments of Different $%s Mortgages" % amount)
    pylab.xlabel("Months")
    pylab.ylabel("Monthly Payments")
    pylab.figure(cost)
    pylab.title("Cash Outlay Different $%s Mortgages" % amount)
    pylab.xlabel("Months")
    pylab.ylabel("Total Payments")
    pylab.figure(balance)
    pylab.title("Balance Remaining $%s Mortgages" % amount)
    pylab.xlabel("Months")
    pylab.ylabel("Remaining Loan Balance $")
    pylab.figure(netCost)
    pylab.title("Net Cost $%s Mortgages" % amount)
    pylab.xlabel("Months")
    pylab.ylabel("Payments - Equity $")
    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plot_payments(styles[i])
        pylab.figure(cost)
        morts[i].plot_total_pd(styles[i])
        pylab.figure(balance)
        morts[i].plot_balance(styles[i])
        pylab.figure(netCost)
        morts[i].plot_net(styles[i])
    pylab.figure(payments)
    pylab.legend(loc="upper center")
    pylab.figure(cost)
    pylab.legend(loc="best")
    pylab.figure(balance)
    pylab.legend(loc="best")


if __name__ == "__main__":
    compare_mortgages(amount=200000, years=30, fixed_rate=0.07, payment=3.25,
                      payment_rate=0.05, variable_rate_1=0.045, variable_rate_2=0.095, months=48)
    pylab.show()
