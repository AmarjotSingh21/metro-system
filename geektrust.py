from sys import argv
from src.models.metro_card import MetroCardDatabase
from src.models.ticket import TicketDatabase
from src.models.payment import PaymentDatabase

from src.views.balance import Balance
from src.views.check_in import CheckIn
from src.views.summary import Summary


def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]

    with open(file_path, 'r') as f:
        metro_card_db = MetroCardDatabase()
        ticket_db = TicketDatabase()
        payment_db = PaymentDatabase()
        lines = f.readlines()
        for line in lines:
            input_list = line.strip().split(" ")
            command = input_list[0]

            if command == "BALANCE":
                Balance(input_list, metro_card_db).add_metro_card()
            elif command == "CHECK_IN":
                CheckIn(input_list, payment_db,
                        metro_card_db, ticket_db).buy_ticket()
            elif command == "PRINT_SUMMARY":
                Summary(ticket_db, metro_card_db, payment_db).print()


if __name__ == "__main__":
    main()
