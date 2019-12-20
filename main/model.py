from enum import Enum
import random


class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Call(Enum):
    PASS = 1
    FAIL = 2


class Service:

    def __init__(self, failure_threshold: int, granularity: int, name: str = ''):
        self.failure_threshold = failure_threshold
        self.granularity = granularity
        self.dependencies = []
        self.failed_count = 0
        self.total_count = 0
        self.name = name

    def get_self_availability_percentage(self):
        return (1 - self.failure_threshold / self.granularity) * 100

    def get_total_availability_percentage(self):
        return (1 - self.failed_count / self.total_count) * 100

    def get_failed_count(self):
        return self.failed_count

    def get_name(self):
        return self.name

    def get_dependencies(self):
        return self.dependencies

    def _self_call(self):
        pass_fail = random.randint(1, self.granularity)
        if pass_fail <= self.failure_threshold:
            return Call.FAIL
        elif pass_fail <= self.granularity and self.failure_threshold < pass_fail:
            return Call.PASS

    def call(self):
        result = self._inner_call()
        if result == Call.FAIL:
            self.failed_count += 1
        self.total_count += 1
        return result

    def _inner_call(self):
        for dependency in self.get_dependencies():
            if dependency.call() == Call.FAIL:
                return Call.FAIL
        return self._self_call()

    def add_dependency(self, dependency: 'Service'):
        if dependency.granularity != self.granularity:
            raise ValidationException("Granularity for dependency {} should be equal to the service's {}"
                                      .format(dependency.granularity, self.granularity))
        self.dependencies.append(dependency)

    def get_size(self):
        return 1


class Cluster(Service):

    def __init__(self, service: Service, size: int):
        super().__init__(0, 1, service.name)
        self.service = service
        self.size = size

    def _self_call(self):
        for _ in range(0, self.size):
            if self.service._self_call() == Call.PASS:
                return Call.PASS
        return Call.FAIL

    def add_dependency(self, dependency: 'Service'):
        raise ValidationException("Cluster is not allowed to have dependencies")

    def get_self_availability_percentage(self):
        return 100

    def get_size(self):
        return self.size

    def get_dependencies(self):
        return self.service.get_dependencies()
