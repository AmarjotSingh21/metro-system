from src.models.passenger import Passenger
from src.models.metro_card import MetroCard


class Ticket:
    def __init__(self, metro_card: MetroCard, passenger: Passenger, from_station: str) -> None:
        self.metro_card = metro_card
        self.passenger = passenger
        self.from_station = from_station
        self.discount: float = (self.metro_card.get_discount_percentage(self.from_station) /
                                100 * self.passenger.fee)

    def __str__(self) -> str:
        return f'Ticket(metro_card={self.metro_card.number}, passenger={self.passenger}, \
from_station={self.from_station}, discount={self.discount}, price={self.price})'

    @property
    def price(self):
        return self.passenger.fee - self.discount


class TicketDatabase:
    def __init__(self) -> None:
        self.__ticket_list: list[Ticket] = []

    def buy_ticket(self, ticket: Ticket) -> None:
        ticket.metro_card.buy_ticket(ticket.price)
        self.__ticket_list.append(ticket)

    def get_tickets_by_station(self, from_station: str) -> list:
        return list(filter(lambda ticket: ticket.from_station == from_station, self.__ticket_list))

    def __str__(self) -> str:
        return str(list(map(lambda ticket: str(ticket), self.__ticket_list)))
