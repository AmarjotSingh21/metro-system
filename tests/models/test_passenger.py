import unittest
from src.models.passenger import Passenger


class TestPassenger(unittest.TestCase):
    def test_create_passenger(self):
        adult_passenger = Passenger.create_passenger("ADULT")
        self.assertEqual(adult_passenger.category, "ADULT")
        self.assertEqual(adult_passenger.fee, 200)

        senior_passenger = Passenger.create_passenger("SENIOR_CITIZEN")
        self.assertEqual(senior_passenger.category, "SENIOR_CITIZEN")
        self.assertEqual(senior_passenger.fee, 100)

        kid_passenger = Passenger.create_passenger("KID")
        self.assertEqual(kid_passenger.category, "KID")
        self.assertEqual(kid_passenger.fee, 50)

    def test_str(self):
        passenger = Passenger("ADULT", 200)
        passenger.category = "CHILD"

        str_representation = str(passenger)
        self.assertEqual(str_representation, "CHILD")
