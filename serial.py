# importing networkx 
from main.gui import Draw
from main.model import Service


def main():
    # Configuring microservice structure
    service = Service(5, 100, 'service')
    database = Service(5, 100, 'database')
    another_app_db = Service(5, 100, 'database')
    service.add_dependency(database)
    # Simulating calls in cycles
    cycles = 100000
    for _ in range(cycles):
        service.call()
    # Drawing from root
    draw = Draw()
    draw.draw_tree(service)


if __name__ == '__main__':
    main()
