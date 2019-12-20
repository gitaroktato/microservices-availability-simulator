import unittest
from main.model import Service
from main.model import Cluster
from main.model import Call
from main.model import ValidationException


class TestService(unittest.TestCase):

    @staticmethod
    def create_service_which_always_succeeds():
        return Service(0, 100)
    
    @staticmethod
    def create_service_which_always_fails():
        return Service(100, 100)

    def test_init(self):
        sut = Service(2, 1000)
        self.assertEqual(sut.failure_threshold, 2)
        self.assertEqual(sut.granularity, 1000)
        self.assertEqual(sut.get_self_availability_percentage(), (1 - 2 / 1000) * 100)

    def test_counters(self):
        sut = TestService.create_service_which_always_fails()
        sut.call()
        self.assertEqual(sut.get_failed_count(), 1)
        self.assertEqual(sut.get_total_availability_percentage(), 0)

    def test_counters_with_dependency(self):
        sut = TestService.create_service_which_always_succeeds()
        failing_dependency = TestService.create_service_which_always_fails()
        sut.add_dependency(failing_dependency)
        sut.call()
        self.assertEqual(sut.get_failed_count(), 1)
        self.assertEqual(sut.get_total_availability_percentage(), 0)

    def test_call_and_succeed(self):
        sut = TestService.create_service_which_always_succeeds()
        result = sut.call()
        self.assertEqual(result, Call.PASS)
    
    def test_call_and_fail(self):
        sut = TestService.create_service_which_always_fails()
        result = sut.call()
        self.assertEqual(result, Call.FAIL)

    def test_with_dependencies(self):
        sut = TestService.create_service_which_always_succeeds()
        dependency = TestService.create_service_which_always_fails()
        sut.add_dependency(dependency)
        result = sut.call()
        self.assertEqual(result, Call.FAIL)
    
    def test_with_dependencies_when_self_fails(self):
        sut = TestService.create_service_which_always_fails()
        dependency = TestService.create_service_which_always_succeeds()
        sut.add_dependency(dependency)
        result = sut.call()
        self.assertEqual(result, Call.FAIL)

    def test_with_dependency_of_different_granularity(self):
        sut = Service(2, 5)
        dependency = Service(2,30)
        try:
            sut.add_dependency(dependency)
            self.fail("Expected exception")
        except ValidationException:
            pass


class TestCluster(unittest.TestCase):

    def test_cluster_call_and_succeed(self):
        service = TestService.create_service_which_always_succeeds()
        cluster = Cluster(service, 1)
        result = cluster.call()
        self.assertEqual(result, Call.PASS)

    def test_cluster_call_and_fail(self):
        service = TestService.create_service_which_always_fails()
        cluster = Cluster(service, 1)
        result = cluster.call()
        self.assertEqual(result, Call.FAIL)

    def test_cluster_self_availability_percentage(self):
        service = TestService.create_service_which_always_fails()
        cluster = Cluster(service, 1)
        self.assertEqual(100, cluster.get_self_availability_percentage())

    def test_cluster_call_and_get_better_availability(self):
        service = Service(50, 100)
        cluster = Cluster(service, 2)
        for _ in range(0, 100000):
            cluster.call()
            service.call()
        self.assertLess(cluster.get_failed_count(), service.get_failed_count())

    def test_cluster_with_dependencies(self):
        dependency = TestService.create_service_which_always_fails()
        service = TestService.create_service_which_always_succeeds()
        cluster = Cluster(service, 100)
        service.add_dependency(dependency)
        result = cluster.call()
        self.assertEqual(result, Call.FAIL)

# call() can be made only on roots