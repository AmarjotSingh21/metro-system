from collections import Counter

from src.models.payment import PaymentDatabase, RechargePayment
from src.models.metro_card import MetroCardDatabase
from src.models.ticket import TicketDatabase


class Summary:
    def __init__(self, ticket_db: TicketDatabase, metro_card_db: MetroCardDatabase,
                 payment_db: PaymentDatabase):
        self.ticket_db = ticket_db
        self.metro_card_db = metro_card_db
        self.payment_db = payment_db

    def print(self):
        self.__print_station_summary("CENTRAL")
        self.__print_station_summary("AIRPORT")

    def __print_station_summary(self, station: str):
        tickets = self.ticket_db.get_tickets_by_station(station)
        payments = self.payment_db.get_payments_by_station(station)

        ticket_amount = self.__get_total(tickets, 'price')
        ticket_discount = self.__get_total(tickets, "discount")
        service_charge_amount = self.__get_total(
            payments, "service_charge")
        total_amount = ticket_amount + service_charge_amount

        print("TOTAL_COLLECTION", station,
              total_amount, ticket_discount)

        passenger_counter = Counter(
            [ticket.passenger.category for ticket in tickets])
        passenger_list: list = sorted(
            passenger_counter.items(), key=lambda x: (-x[1], x[0]))

        print("PASSENGER_TYPE_SUMMARY")
        for passenger in passenger_list:
            self.__print_if_exists(passenger)

    def __print_if_exists(self, passenger: tuple):
        if passenger[1] > 0:
            print(passenger[0], passenger[1])

    def __get_total(self, data: list, attr: str): return sum(
        map(lambda value: getattr(value, attr), data))
