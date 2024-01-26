from src.models.metro_card import MetroCardDatabase
from src.models.ticket import TicketDatabase
from src.models.payment import PaymentDatabase

from src.views.balance import Balance
from src.views.check_in import CheckIn
from src.views.summary import Summary


def run(lines):
    metro_card_db = MetroCardDatabase()
    ticket_db = TicketDatabase()
    payment_db = PaymentDatabase()
    for line in lines:
        input_list = line.strip().split(" ")
        command = input_list[0]

        if command == "BALANCE":
            metro_card_number = input_list[1]
            metro_card_balance = float(input_list[2])
            Balance(metro_card_number, metro_card_balance,
                    metro_card_db).add_metro_card()
        elif command == "CHECK_IN":
            metro_card_number = input_list[1]
            passenger_category = input_list[2]
            from_station = input_list[3]
            CheckIn(metro_card_number, passenger_category, from_station, payment_db,
                    metro_card_db, ticket_db).buy_ticket()
        elif command == "PRINT_SUMMARY":
            Summary(ticket_db, metro_card_db, payment_db).print()
