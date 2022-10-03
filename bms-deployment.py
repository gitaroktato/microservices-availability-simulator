from main.gui import Draw
from main.model import Service
from main.aws import S3, CloudFront, Route53, APIGateway, ELB


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
    supplier_ec2 = Service(10, 100000, 'SupplierEC2')
    supplier_dynamo = Service(1, 100000, 'SupplierDynamo')
    supplier_elb.add_dependency(supplier_ec2)
    supplier_ec2.add_dependency(supplier_dynamo)
    api_gateway.add_dependency(supplier_elb)
    # Employees
    employees_elb = Service(10, 100000, 'EmployeesELB')
    employees_ec2 = Service(10, 100000, 'EmployeesEC2')
    employees_dynamo = Service(1, 100000, 'EmployeesDynamo')
    employees_elb.add_dependency(employees_ec2)
    employees_ec2.add_dependency(employees_dynamo)
    api_gateway.add_dependency(employees_elb)
    # Administration
    administration_elb = Service(10, 100000, 'AdminELB')
    administration_ec2 = Service(10, 100000, 'AdminEC2')
    administration_dynamo = Service(1, 100000, 'AdminDynamo')
    administration_elb.add_dependency(administration_ec2)
    administration_ec2.add_dependency(administration_dynamo)
    api_gateway.add_dependency(administration_elb)
    # SNS
    sns = Service(100, 100000, 'SNS')
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
