class MetroCard:
    def __init__(self, number: str, balance: float) -> None:
        self.number = number
        self.balance = balance
        self.last_traveled_from_station: str | None = None
        self.__traveled_count: int = 0

    def buy_ticket(self, fee: float) -> None:
        self.__traveled_count += 1
        self.balance -= fee

    def recharge(self, amount: float):
        self.balance += amount

    def has_enough_balance(self, amount: float) -> bool:
        return amount <= self.balance

    def get_discount_percentage(self, from_station: str) -> float:
        discount: float = 0
        if (self.last_traveled_from_station is not None and
                self.last_traveled_from_station != from_station and
                self.__traveled_count % 2 != 0
            ):
            discount = 50
        self.last_traveled_from_station = from_station
        return discount

    def __str__(self) -> str:
        return f'MetroCard(number={self.number}, balance={self.balance}, from_station={self.last_traveled_from_station})'


class MetroCardDatabase:
    def __init__(self) -> None:
        self.__metro_card_list: list[MetroCard] = []

    def add_metro_card(self, metro_card: MetroCard) -> None:
        self.__metro_card_list.append(metro_card)

    def get_metro_card(self, metro_card_number: str) -> MetroCard:
        return next(filter(lambda metro_card: metro_card.number == metro_card_number, self.__metro_card_list))

    def __str__(self) -> str:
        return str(list(map(lambda metro_card: str(metro_card), self.__metro_card_list)))
