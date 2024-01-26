import unittest
from src.models.ticket import Ticket, TicketDatabase, MetroCard, Passenger


class TestTicket(unittest.TestCase):
    def setUp(self):
        self.metro_card = MetroCard("MC1", 100.0)
        self.passenger_adult = Passenger("ADULT", 200)
        self.passenger_child = Passenger("KID", 50)

    def test_price(self):
        ticket_adult = Ticket(self.metro_card, self.passenger_adult, "AIRPORT")
        self.assertEqual(ticket_adult.price, 200)
        ticket_child = Ticket(self.metro_card, self.passenger_child, "AIRPORT")
        self.assertEqual(ticket_child.price, 50)

    def test_str(self):
        metro_card = MetroCard("MC1", 100.0)
        passenger = Passenger("ADULT", 200)
        ticket = Ticket(metro_card, passenger, "AIRPORT")
        str_representation = str(ticket)
        expected_str = "Ticket(metro_card=MC1, passenger=ADULT, from_station=AIRPORT, discount=0.0, price=200.0)"
        self.assertEqual(str_representation, expected_str)


class TestTicketDatabase(unittest.TestCase):
    def setUp(self):
        self.database = TicketDatabase()
        self.metro_card = MetroCard("MC1", 100.0)
        self.passenger_adult = Passenger("ADULT", 200)

    def test_buy_ticket(self):
        ticket = Ticket(self.metro_card, self.passenger_adult, "AIRPORT")
        self.database.buy_ticket(ticket)
        self.assertEqual(len(self.database._TicketDatabase__ticket_list), 1)

    def test_get_tickets_by_station(self):
        ticket_1 = Ticket(self.metro_card, self.passenger_adult, "AIRPORT")
        ticket_2 = Ticket(self.metro_card, self.passenger_adult, "CENTRAL")
        self.database.buy_ticket(ticket_1)
        self.database.buy_ticket(ticket_2)

        tickets = self.database.get_tickets_by_station("AIRPORT")
        self.assertEqual(len(tickets), 1)
        self.assertEqual(tickets[0].from_station, "AIRPORT")

    def test_str(self):
        ticket_1 = Ticket(self.metro_card, self.passenger_adult, "AIRPORT")
        ticket_2 = Ticket(self.metro_card, self.passenger_adult, "CENTRAL")

        ticket_db = TicketDatabase()
        ticket_db.buy_ticket(ticket_1)
        ticket_db.buy_ticket(ticket_2)

        str_representation = str(ticket_db)
        expected_str = f"['{ticket_1}', '{ticket_2}']"

        self.assertEqual(str_representation, expected_str)
