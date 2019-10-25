from enum import Enum

class Call(Enum):
    PASS = 1
    FAIL = 2

class Service:

    def __init__(self, failure_rate, total_rate):
        self.failure_rate = failure_rate
        self.total_rate = total_rate

    def call(self, passFailRange):
        if passFailRange <= self.failure_rate:
            return Call.FAIL
        elif passFailRange <= self.total_rate and self.failure_rate < passFailRange:
            return Call.PASS