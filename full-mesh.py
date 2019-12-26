from main.gui import Draw
from main.model import Service


def main():
    # Configuring microservice structure
    services = []
    maximum_number_of_services = 10
    for i in range(1, maximum_number_of_services + 1):
        service = Service(1, 100, 'service-%d' % (maximum_number_of_services - i + 1))
        for other_service in services:
            other_service.add_dependency(service)
        services.append(service)
    # Simulating calls in cycles
    cycles = 100000
    for _ in range(cycles):
        for service in services:
            service.call()
    # Drawing from root
    draw = Draw()
    draw.draw_radial_tree(services[0])


if __name__ == '__main__':
    main()
