import unittest
from main.model import Service
from main.model import Call

class TestService(unittest.TestCase):

    def test_init(self):
        sut = Service(2, 1000)
        self.assertEquals(sut.failure_rate, 2)
        self.assertEquals(sut.total_rate, 1000)

    def test_call_with_valid_values(self):
        sut = Service(2, 1000)
        result = sut.call(1)
        self.assertEquals(result, Call.FAIL)
        result = sut.call(3)
        self.assertEquals(result, Call.PASS)
    
    def test_call_with_invalid_value(self):
        sut = Service(2, 5)
        try {
            result = sut.call(8)
        }