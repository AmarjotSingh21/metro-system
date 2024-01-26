class Passenger:
    passenger_fees_map: dict = {
        "ADULT": 200,
        "SENIOR_CITIZEN": 100,
        "KID": 50
    }

    def __init__(self, category: str, fee: float) -> None:
        self.category = category
        self.fee = fee

    @classmethod
    def create_passenger(cls, category: str):
        fee = cls.__get_passenger_fee(category)
        return cls(category, fee)

    @classmethod
    def __get_passenger_fee(cls, category: str) -> int:
        return cls.passenger_fees_map[category]

    def __str__(self) -> str:
        return self.category
