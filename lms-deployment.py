from main.gui import Draw
from main.model import Service, Cluster


def main():
    # Configuring microservice structure
    route53 = Service(10, 100000, 'Route53')
    s3 = Service(100, 100000, 'S3')
    cloud_front = Service(100, 100000, 'CloudFront')
    cloud_front.add_dependency(s3)
    cluster_cloud_front = Cluster(cloud_front, 2)
    route53.add_dependency(cluster_cloud_front)
    api_gateway = Service(50, 100000, 'APIGateway')
    cluster_api_gateway = Cluster(api_gateway, 2)
    route53.add_dependency(cluster_api_gateway)
    # BFF
    bff_elb = Service(10, 100000, 'BFF ELB')
    bff_ec2 = Service(10, 100000, 'BFF EC2')
    bff_elb.add_dependency(bff_ec2)
    api_gateway.add_dependency(bff_elb)
    # Backend
    backend_elb = Service(10, 100000, 'Backend ELB')
    backend_ec2 = Service(10, 100000, 'Backend EC2')
    backend_aurora = Service(10, 100000, 'Backend Aurora')
    backend_ec2.add_dependency(backend_aurora)
    backend_elb.add_dependency(backend_ec2)
    bff_ec2.add_dependency(backend_elb)
    # Simulating calls in cycles
    cycles = 100000
    for _ in range(cycles):
        route53.call()
    # Drawing from root
    draw = Draw()
    draw.draw_tree(route53)


if __name__ == '__main__':
    main()
