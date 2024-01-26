from src.models.metro_card import MetroCardDatabase, MetroCard


class Balance:
    def __init__(self, metro_card_number: str, metro_card_balance: float, metro_card_db: MetroCardDatabase) -> None:
        self.metro_card_number = metro_card_number
        self.metro_card_balance = metro_card_balance
        self.metro_card_db = metro_card_db

    def add_metro_card(self) -> None:
        self.metro_card_db.add_metro_card(
            MetroCard(number=self.metro_card_number, balance=self.metro_card_balance))
