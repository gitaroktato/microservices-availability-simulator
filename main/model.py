from enum import Enum

class ValidationException(Exception):
    def __init__(self):
        pass

class Call(Enum):
    PASS = 1
    FAIL = 2

class Service:

    def __init__(self, failure_rate, total_rate):
        self.failure_rate = failure_rate
        self.total_rate = total_rate
        self.dependencies = []

    def selfCall(self, passFailRange):
        if passFailRange <= self.failure_rate:
            return Call.FAIL
        elif passFailRange <= self.total_rate and self.failure_rate < passFailRange:
            return Call.PASS
        else:
            raise ValidationException
    
    def call(self, passFailRange):
        for dependency in self.dependencies:
            if dependency.call(passFailRange) == Call.FAIL:
                return Call.FAIL
        return self.selfCall(passFailRange)
            

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)