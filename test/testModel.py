import unittest
from main.model import Service
from main.model import Call
from main.model import ValidationException

class TestService(unittest.TestCase):


    def create_service_which_always_succeeds(self):
        return Service(0, 100)

    def test_init(self):
        sut = Service(2, 1000)
        self.assertEquals(sut.failure_threshold, 2)
        self.assertEquals(sut.granularity, 1000)

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
        sut = self.create_service_which_always_succeeds()
        dependency = Service(100, 100)
        sut.add_dependency(dependency)
        result = sut.call(1)
        self.assertEquals(result, Call.FAIL)
    
    def test_with_dependencies_when_self_fails(self):
        sut = Service(100, 100)
        dependency = self.create_service_which_always_succeeds()
        sut.add_dependency(dependency)
        result = sut.call(1)
        self.assertEquals(result, Call.FAIL)

    def test_with_dependency_of_different_granularity(self):
        sut = Service(2, 5)
        dependency = Service(2,30)
        try:
            sut.add_dependency(dependency)
            self.fail("Expected exception")
        except ValidationException:
            pass

    # Dependency calculation