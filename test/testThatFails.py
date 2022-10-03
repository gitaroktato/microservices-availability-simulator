from main.aws import EC2MultiAZ, S3, CloudFront, Route53, APIGateway, DynamoDB, EC2Instance, DynamoDBGlobalTable, SNS, \
    ELB
import unittest


class TestThatFails(unittest.TestCase):

    def test_fails(self):
        self.fail("Sorry, this test should fail")
