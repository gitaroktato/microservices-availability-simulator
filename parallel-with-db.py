from main.gui import Draw
from main.model import Service
from main.model import Cluster


def main():
    # Configuring microservice structure
    service = Service(5, 100, 'service')
    database = Service(5, 100, 'database')
    service.add_dependency(database)
    cluster = Cluster(service, 5)
    # Simulating calls in cycles
    cycles = 100000
    for _ in range(cycles):
        cluster.call()
    # Drawing from root
    draw = Draw()
    draw.draw_tree(cluster)


if __name__ == '__main__':
    main()
