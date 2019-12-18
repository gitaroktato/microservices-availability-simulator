import unittest
from main.model import Service
from main.model import Call
from main.model import ValidationException


class TestService(unittest.TestCase):

    def create_service_which_always_succeeds(self):
        return Service(0, 100)
    
    def create_service_which_always_fails(self):
        return Service(100, 100)

    def test_init(self):
        sut = Service(2, 1000)
        self.assertEquals(sut.failure_threshold, 2)
        self.assertEquals(sut.granularity, 1000)
        self.assertEquals(sut.get_self_availability_percentage(), (1 - 2 / 1000) * 100)

    def test_counters(self):
        sut = self.create_service_which_always_fails()
        sut.call()
        self.assertEquals(sut.get_failed_count(), 1)
        self.assertEquals(sut.get_total_availability_percentage(), 0)

    def test_counters_with_dependency(self):
        sut = self.create_service_which_always_succeeds()
        failing_dependency = self.create_service_which_always_fails()
        sut.add_dependency(failing_dependency)
        sut.call()
        self.assertEquals(sut.get_failed_count(), 1)
        self.assertEquals(sut.get_total_availability_percentage(), 0)

    def test_call_and_succeed(self):
        sut = self.create_service_which_always_succeeds()
        result = sut.call()
        self.assertEquals(result, Call.PASS)
    
    def test_call_and_fail(self):
        sut = self.create_service_which_always_fails()
        result = sut.call()
        self.assertEquals(result, Call.FAIL)

    def test_with_dependencies(self):
        sut = self.create_service_which_always_succeeds()
        dependency = self.create_service_which_always_fails()
        sut.add_dependency(dependency)
        result = sut.call()
        self.assertEquals(result, Call.FAIL)
    
    def test_with_dependencies_when_self_fails(self):
        sut = self.create_service_which_always_fails()
        dependency = self.create_service_which_always_succeeds()
        sut.add_dependency(dependency)
        result = sut.call()
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