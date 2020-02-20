from main.gui import Draw
from main.model import Service, Cluster


def main():
    # Configuring microservice structure
    services = []
    maximum_number_of_services = 10
    broker = Service(5, 100, 'broker')
    broker_cluster = Cluster(broker, 2)
    for i in range(1, maximum_number_of_services + 1):
        service = Service(5, 100, 'service-%d' % (maximum_number_of_services - i + 1))
        service.add_dependency(broker_cluster)
        services.append(service)
    # Simulating calls in cycles
    cycles = 1000000
    for _ in range(cycles):
        for service in services:
            service.call()
    # Drawing from root
    draw = Draw()
    draw.draw_each(services)


if __name__ == '__main__':
    main()
