from enum import Enum
import random

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Call(Enum):
    PASS = 1
    FAIL = 2

class Service:

    def __init__(self, failure_threshold, granularity, name = ''):
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
        for dependency in self.dependencies:
            if dependency.call() == Call.FAIL:
                return Call.FAIL
        return self._self_call()

    def add_dependency(self, dependency):
        if dependency.granularity != self.granularity:
            raise ValidationException("Granularity for dependency {} should be equal to the service's {}"
                .format(dependency.granularity, self.granularity))
        self.dependencies.append(dependency)