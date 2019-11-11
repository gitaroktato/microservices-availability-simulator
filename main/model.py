from enum import Enum

class ValidationException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Call(Enum):
    PASS = 1
    FAIL = 2

class Service:

    def __init__(self, failure_threshold, granularity):
        self.failure_threshold = failure_threshold
        self.granularity = granularity
        self.dependencies = []

    def self_call(self, pass_fail):
        if pass_fail > self.granularity:
            raise ValidationException("Pass-fail {} is bigger than service's granularity {}"
                .format(pass_fail, self.granularity))
        elif pass_fail <= self.failure_threshold:
            return Call.FAIL
        elif pass_fail <= self.granularity and self.failure_threshold < pass_fail:
            return Call.PASS
    
    def call(self, pass_fail):
        for dependency in self.dependencies:
            if dependency.call(pass_fail) == Call.FAIL:
                return Call.FAIL
        return self.self_call(pass_fail)

    def add_dependency(self, dependency):
        if (dependency.granularity != self.granularity):
            raise ValidationException("Granularity for dependency {} should be equal to the service's {}"
                .format(dependency.granularity, self.granularity))
        self.dependencies.append(dependency)