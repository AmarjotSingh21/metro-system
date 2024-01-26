from src.models.payment import PaymentDatabase, RechargePayment
from src.models.metro_card import MetroCardDatabase
from src.models.passenger import Passenger
from src.models.ticket import Ticket, TicketDatabase


class CheckIn:
    def __init__(self, metro_card_number: str, passenger_category: str,
                 from_station: str, payment_db: PaymentDatabase,
                 metro_card_db: MetroCardDatabase, ticket_db: TicketDatabase) -> None:
        self.metro_card_number = metro_card_number
        self.passenger_category = passenger_category
        self.from_station = from_station
        self.metro_card_db = metro_card_db
        self.payment_db = payment_db
        self.ticket_db = ticket_db

    def buy_ticket(self) -> None:
        self.ticket = self.__create_ticket()
        if self.__insufficient_balance():
            self.__recharge_metro_card()

        self.ticket_db.buy_ticket(self.ticket)

    def __create_passenger(self) -> Passenger:
        return Passenger.create_passenger(self.passenger_category)

    def __create_ticket(self) -> Ticket:
        passenger = self.__create_passenger()
        return Ticket(metro_card=self.metro_card_db.get_metro_card(
            self.metro_card_number), passenger=passenger, from_station=self.from_station)

    def __recharge_metro_card(self):
        self.payment_db.add_payment(RechargePayment(
            amount=self.ticket.price - self.ticket.metro_card.balance,
            metro_card=self.ticket.metro_card, from_station=self.from_station))

    def __insufficient_balance(self):
        return not self.ticket.metro_card.has_enough_balance(self.ticket.price)
