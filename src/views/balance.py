from src.models.metro_card import MetroCardDatabase, MetroCard


class Balance:
    def __init__(self, input_list: list, metro_card_db: MetroCardDatabase) -> None:
        self.metro_card_number = input_list[1]
        self.metro_card_balance = float(input_list[2])
        self.metro_card_db = metro_card_db

    def add_metro_card(self) -> None:
        self.metro_card_db.add_metro_card(
            MetroCard(number=self.metro_card_number, balance=self.metro_card_balance))
