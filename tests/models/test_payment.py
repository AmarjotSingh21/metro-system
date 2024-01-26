import unittest
from src.models.payment import RechargePayment, PaymentDatabase, MetroCard
from src.models.metro_card import MetroCard


class TestRechargePayment(unittest.TestCase):
    def setUp(self):
        self.metro_card = MetroCard("MC1", 50.0)

    def test_total_amount(self):
        recharge_payment = RechargePayment(100.0, self.metro_card, "AIRPORT")
        self.assertEqual(recharge_payment.total_amount, 102.0)

    def test_str(self):
        metro_card = MetroCard("MC1", 100.0)

        recharge_payment = RechargePayment(50.0, metro_card, "AIRPORT")

        str_representation = str(recharge_payment)

        expected_str = "RechargePayment(amount=50.0, metro_card=MC1, service_charge=1.0, from_station=AIRPORT)"

        self.assertEqual(str_representation, expected_str)


class TestPaymentDatabase(unittest.TestCase):
    def setUp(self):
        self.database = PaymentDatabase()
        self.metro_card = MetroCard("MC1", 50.0)

    def test_add_payment(self):
        recharge_payment = RechargePayment(100.0, self.metro_card, "AIRPORT")
        self.database.add_payment(recharge_payment)
        self.assertEqual(len(self.database._PaymentDatabase__payment_list), 1)

    def test_get_payments_by_station(self):
        recharge_payment_1 = RechargePayment(100.0, self.metro_card, "AIRPORT")
        recharge_payment_2 = RechargePayment(200.0, self.metro_card, "CENTRAL")
        self.database.add_payment(recharge_payment_1)
        self.database.add_payment(recharge_payment_2)

        payments = self.database.get_payments_by_station("AIRPORT")
        self.assertEqual(len(payments), 1)
        self.assertEqual(payments[0].from_station, "AIRPORT")

    def test_str(self):
        payment_db = PaymentDatabase()

        payment_1 = RechargePayment(100.0, self.metro_card, "AIRPORT")
        payment_2 = RechargePayment(200.0, self.metro_card, "CENTRAL")
        payment_db.add_payment(payment_1)
        payment_db.add_payment(payment_2)

        str_representation = str(payment_db)

        expected_str = f"['{payment_1}', '{payment_2}']"
        self.assertEqual(str_representation, expected_str)
