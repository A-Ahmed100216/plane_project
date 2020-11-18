import unittest
import pytest
from aircraft_class import Aircraft

class TestAircraft(unittest.TestCase):
    aircraft=Aircraft()

    def test_create_table(self):

        self.assertIn(self.aircraft.create_table(),self.DB.co
