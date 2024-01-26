import unittest
from src.models.metro_card import MetroCard, MetroCardDatabase


class TestMetroCard(unittest.TestCase):
    def setUp(self):
        self.metro_card = MetroCard("MC1", 50.0)

    def test_buy_ticket(self):
        self.metro_card.buy_ticket(30.0)
        self.assertEqual(self.metro_card.balance, 20.0)

    def test_recharge(self):
        self.metro_card.recharge(20.0)
        self.assertEqual(self.metro_card.balance, 70.0)

    def test_has_enough_balance(self):
        self.assertTrue(self.metro_card.has_enough_balance(20.0))
        self.assertFalse(self.metro_card.has_enough_balance(100.0))

    def test_get_discount_percentage(self):
        # Assuming last_traveled_from_station is None
        self.assertEqual(self.metro_card.get_discount_percentage("CENTRAL"), 0)
        self.metro_card.buy_ticket(30)

        # Assuming last_traveled_from_station is "CENTRAL"
        self.assertEqual(
            self.metro_card.get_discount_percentage("AIRPORT"), 50)

    def test_str(self):
        metro_card = MetroCard("MC1", 50.0)
        metro_card.last_traveled_from_station = "AIRPORT"
        expected_str = "MetroCard(number=MC1, balance=50.0, from_station=AIRPORT)"
        self.assertEqual(str(metro_card), expected_str)


class TestMetroCardDatabase(unittest.TestCase):
    def setUp(self):
        self.database = MetroCardDatabase()
        self.metro_card = MetroCard("MC1", 50.0)
        self.database.add_metro_card(self.metro_card)

    def test_add_metro_card(self):
        self.assertEqual(
            len(self.database._MetroCardDatabase__metro_card_list), 1)

    def test_get_metro_card(self):
        metro_card = self.database.get_metro_card("MC1")
        self.assertEqual(metro_card, self.metro_card)

    def test_str(self):
        metro_card_db = MetroCardDatabase()

        metro_card_1 = MetroCard("MC1", 50.0)
        metro_card_1.last_traveled_from_station = "AIRPORT"

        metro_card_2 = MetroCard("MC2", 100.0)
        metro_card_db.add_metro_card(metro_card_1)
        metro_card_db.add_metro_card(metro_card_2)

        str_representation = str(metro_card_db)

        expected_str = f"['{metro_card_1}', '{metro_card_2}']"
        self.assertEqual(str_representation, expected_str)
