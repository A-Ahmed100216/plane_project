import unittest
import pytest
from aircraft_class import Aircraft,Query


class TestAircraft(unittest.TestCase):
    aircraft=Aircraft()

    def test_create_table(self):
        # The table has already been created so the following test checks whether an error is raised.
        self.assertRaises(Exception,self.aircraft.create_table())




