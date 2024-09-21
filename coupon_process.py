
from dataclasses import dataclass


@dataclass
class Subscriber:
    email: str
    rec_count: int


@dataclass
class Coupon:
    code: str
    rank: str


@dataclass
class Message:
    who: str
    to: str
    subject: str 
    body: str


rank1 = "best"
rank2 = "good"


def sub_coupon_rank(subscriber):
    return "best" if subscriber.rec_count >= 10 else "good"


def select_coupons_by_rank(coupons, rank):
    return [c for c in coupons if c.rank == rank]


def email_for_subscriber(subscriber: Subscriber, goods, bests):
    rank = sub_coupon_rank(subscriber)
    if rank == "best":
        return Message(who="newsletter@coupondog.com", to=subscriber.email,
                       subject="Your best weekly coupon inside",
                       body="Here are the best coupons.")
    else:
        return Message(who="newsletter@coupondog.com", to=subscriber.email,
                       subject="Your good weekly coupons inside",
                       body=f"Here are the good coupons: {', '.join(goods)}")


def emails_for_subscribers(subscribers, goods, bests):
    return [email_for_subscriber(subscriber, goods, bests)
            for subscriber in subscribers]


def send_issue():
    coupons = fetch_coupons_from_db()
    good_coupons = select_coupons_by_rank(coupons, "good")
    best_coupons = select_coupons_by_rank(coupons, "best")
    subscribers = fetch_subscribers_from_db()
    emails = emails_for_subscribers(subscribers, good_coupons, best_coupons)
    for email in emails:
        email_system.send(email)
