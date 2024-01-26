from src.models.metro_card import MetroCard


class RechargePayment:
    def __init__(self, amount: float, metro_card: MetroCard, from_station: str) -> None:
        self.amount = amount
        self.metro_card = metro_card
        self.service_charge = self.amount * .02
        self.from_station = from_station

    @property
    def total_amount(self):
        return self.amount + self.service_charge

    def __str__(self) -> str:
        return f'RechargePayment(amount={self.amount}, metro_card={self.metro_card.number}, \
service_charge={self.service_charge}, from_station={self.from_station})'


class PaymentDatabase:
    def __init__(self) -> None:
        self.__payment_list: list[RechargePayment] = []

    def add_payment(self, recharge_payment: RechargePayment) -> None:
        recharge_payment.metro_card.recharge(amount=recharge_payment.amount)
        self.__payment_list.append(recharge_payment)

    def get_payments_by_station(self, from_station: str) -> list:
        return list(filter(lambda payment: payment.from_station == from_station, self.__payment_list))

    def __str__(self) -> str:
        return str(list(map(lambda payment: str(payment), self.__payment_list)))
