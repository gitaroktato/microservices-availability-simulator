import unittest
from main.model import Service
from main.model import Call
from main.model import ValidationException

def create_service_which_always_succeeds():
    return Service(0, 100)

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
        try:
            sut.call(8)
            self.fail("Expected exception")
        except ValidationException:
            pass
    
    def test_with_dependencies(self):
        sut = create_service_which_always_succeeds()
        dependency = Service(100, 100)
        sut.add_dependency(dependency)
        result = sut.call(1)
        self.assertEquals(result, Call.FAIL)
    
    def test_with_dependencies_when_self_fails(self):
        sut = Service(100, 100)
        dependency = create_service_which_always_succeeds()
        sut.add_dependency(dependency)
        result = sut.call(1)
        self.assertEquals(result, Call.FAIL)

    def test_with_dependency_of_different_total_rate(self):
        sut = Service(2, 5)
        dependency = Service(2,30)
        try:
            sut.add_dependency(dependency)
            self.fail("Expected exception")
        except ValidationException:
            pass

    # Dependency calculation