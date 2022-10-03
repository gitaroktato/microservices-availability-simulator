from main.aws import EC2MultiAZ, S3, CloudFront, Route53, APIGateway, DynamoDB, EC2Instance, DynamoDBGlobalTable, SNS, \
    ELB
import unittest


class TestAws(unittest.TestCase):

    def test_ec2(self):
        sut = EC2MultiAZ('')
        self.assertEqual(sut.get_self_availability_percentage(), 99.99)

    def test_s3(self):
        sut = S3('')
        self.assertEqual(sut.get_self_availability_percentage(), 99.9)

    def test_cloud_front(self):
        sut = CloudFront('')
        self.assertEqual(sut.get_self_availability_percentage(), 99.9)

    def test_route_53(self):
        sut = Route53('')
        self.assertEqual(sut.get_self_availability_percentage(), 100.0)

    def test_api_gateway(self):
        sut = APIGateway('')
        self.assertEqual(sut.get_self_availability_percentage(), 99.95)

    def test_elb(self):
        sut = ELB('')
        self.assertEqual(sut.get_self_availability_percentage(), 99.99)

    def test_ec2_instance(self):
        sut = EC2Instance('')
        self.assertEqual(sut.get_self_availability_percentage(), 99.5)

    def test_dynamo_db(self):
        sut = DynamoDB('')
        self.assertEqual(sut.get_self_availability_percentage(), 99.99)

    def test_dynamo_db_global_table(self):
        sut = DynamoDBGlobalTable('')
        self.assertAlmostEqual(sut.get_self_availability_percentage(), 99.999, delta=0.0001)

    def test_sns(self):
        sut = SNS('')
        self.assertEqual(sut.get_self_availability_percentage(), 99.9)

    def test_sqs(self):
        sut = SNS('')
        self.assertEqual(sut.get_self_availability_percentage(), 99.9)
