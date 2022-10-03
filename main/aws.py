from main.model import Service


class S3(Service):
    """
    Creates S3 component with 99.9% availability.
    See: https://aws.amazon.com/s3/sla/
    """
    def __init__(self, name: str = ''):
        super().__init__(100, 100000, name)


class CloudFront(Service):
    """
    Creates CloudFront component with 99.9% availability.
    See: https://aws.amazon.com/cloudfront/sla/
    """
    def __init__(self, name: str = ''):
        super().__init__(100, 100000, name)


class Route53(Service):
    """
    Creates Route53 component with 100% availability.
    See: https://aws.amazon.com/route53/sla/
    """
    def __init__(self, name: str = ''):
        super().__init__(0, 100000, name)


class APIGateway(Service):
    """
    Creates API Gateway component with 99.95% availability.
    See: https://aws.amazon.com/api-gateway/sla/
    """
    def __init__(self, name: str = ''):
        super().__init__(50, 100000, name)


class ELB(Service):
    """
    Creates AWS ELB component with 99.99% availability.
    See: https://aws.amazon.com/elasticloadbalancing/sla/
    """
    def __init__(self, name: str = ''):
        super().__init__(10, 100000, name)


class EC2MultiAZ(Service):
    """
    Creates AWS EC2 Multi AZ component with 99.99% availability.
    See: https://aws.amazon.com/ec2/sla/
    """
    def __init__(self, name: str = ''):
        super().__init__(10, 100000, name)


class EC2Instance(Service):
    """
    Creates a single instance of AWS EC2 component with 99.5% availability.
    See: https://aws.amazon.com/ec2/sla/
    """
    def __init__(self, name: str = ''):
        super().__init__(500, 100000, name)


class DynamoDB(Service):
    """
    Creates DynamoDB component with 99.99% availability.
    See: https://aws.amazon.com/dynamodb/sla/
    """
    def __init__(self, name: str = ''):
        super().__init__(10, 100000, name)


class DynamoDBGlobalTable(Service):
    """
    Creates DynamoDB global table component with 99.999% availability.
    See: https://aws.amazon.com/dynamodb/sla/
    """
    def __init__(self, name: str = ''):
        super().__init__(1, 100000, name)


class SNS(Service):
    """
    Creates SNS component with 99.9% availability.
    See: https://aws.amazon.com/dynamodb/sla/
    """
    def __init__(self, name: str = ''):
        super().__init__(100, 100000, name)


class SQS(Service):
    """
    Creates SNS component with 99.9% availability.
    See: https://aws.amazon.com/dynamodb/sla/
    """
    def __init__(self, name: str = ''):
        super().__init__(100, 100000, name)

