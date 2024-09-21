from dataclasses import dataclass


@dataclass
class Affiliate(object):
    sales: float
    commision: float
    bank_code: str


def figure_payout(affiliate):
    owed = affiliate.sales * affiliate.commision
    if owed > 100:
        send_payout(affiliate.bank_code, owed)


def affiliate_payout(affiliates):
    for affiliate in affiliates:
        figure_payout(affiliate)


def send_payout(bank, amount):
    print(f"Paying {amount} to {bank}")


if __name__ == "__main__":
    affiliates = [
        Affiliate(sales=100.5, commision=0.23, bank_code="1234"),
        Affiliate(sales=9876.5, commision=0.23, bank_code="4321"),
        Affiliate(sales=0.01, commision=0.23, bank_code="1234"),
        Affiliate(sales=98765.5, commision=0.23, bank_code="4321"),
    ]

    affiliate_payout(affiliates)
