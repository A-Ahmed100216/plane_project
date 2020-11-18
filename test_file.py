import unittest
import pytest
from aircraft_class import Aircraft,Query
from Booking_class import Booking
from User_functions import User_functions


class TestAircraft(unittest.TestCase):
    aircraft=Aircraft()

    def test_create_table(self):
        # The table has already been created so the following test checks whether an error is raised.
        self.assertRaises(Exception,self.aircraft.create_table())

class TestBooking(unittest.TestCase):
    booking=Booking()

    def test_seat_counter(self):
        self.assertEqual(self.booking.seat_counter(2,1),"There are 397 seats remaining on the flight")


class TestLogin(unittest.TestCase):
    interface=User_functions()

    def test_login(self):
        # Is the output of login function, the user interface
        self.assertEqual(self.interface.login(),self.interface.user_interface())