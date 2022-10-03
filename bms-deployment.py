from main.gui import Draw
from main.aws import S3, CloudFront, Route53, APIGateway, ELB, EC2MultiAZ, DynamoDB, SNS


def main():
    # Configuring microservice structure
    route53 = Route53('Route53')
    s3 = S3('S3')
    cloud_front = CloudFront('CloudFront')
    cloud_front.add_dependency(s3)
    route53.add_dependency(cloud_front)
    api_gateway = APIGateway('APIGateway')
    route53.add_dependency(api_gateway)
    # Supplier
    supplier_elb = ELB('SupplierELB')
    supplier_ec2 = EC2MultiAZ('SupplierEC2')
    supplier_dynamo = DynamoDB('SupplierDynamo')
    supplier_elb.add_dependency(supplier_ec2)
    supplier_ec2.add_dependency(supplier_dynamo)
    api_gateway.add_dependency(supplier_elb)
    # Employees
    employees_elb = ELB('EmployeesELB')
    employees_ec2 = EC2MultiAZ('EmployeesEC2')
    employees_dynamo = DynamoDB('EmployeesDynamo')
    employees_elb.add_dependency(employees_ec2)
    employees_ec2.add_dependency(employees_dynamo)
    api_gateway.add_dependency(employees_elb)
    # Administration
    administration_elb = ELB('AdminELB')
    administration_ec2 = EC2MultiAZ('AdminEC2')
    administration_dynamo = DynamoDB('AdminDynamo')
    administration_elb.add_dependency(administration_ec2)
    administration_ec2.add_dependency(administration_dynamo)
    api_gateway.add_dependency(administration_elb)
    # SNS
    sns = SNS('SNS')
    administration_ec2.add_dependency(sns)
    employees_ec2.add_dependency(sns)
    supplier_ec2.add_dependency(sns)
    # Simulating calls in cycles
    cycles = 100000
    for _ in range(cycles):
        route53.call()
    # Drawing from root
    draw = Draw()
    draw.draw_tree(route53)


if __name__ == '__main__':
    main()
