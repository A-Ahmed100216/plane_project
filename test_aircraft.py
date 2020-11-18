import unittest
import pytest
from aircraft_class import Aircraft,Query


class TestAircraft(unittest.TestCase):
    aircraft=Aircraft()

    # def test_create_table(self):
    #     # The table has already been created so the following test checks whether an error is raised.
    #     self.assertRaises(Exception,self.aircraft.create_table())

    # def test_add_data(self):
    #     # Checks if an error is raised with invalid data
    #     self.assertRaises(Exception,self.aircraft.add_data())


