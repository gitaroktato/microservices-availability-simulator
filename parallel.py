from main.gui import Draw
from main.model import Service
from main.model import Cluster


def main():
    # Configuring microservice structure
    service = Service(50, 100, 'service')
    cluster = Cluster(service, 2)
    # Simulating calls in cycles
    cycles = 100000
    for _ in range(cycles):
        cluster.call()
    # Drawing from root
    draw = Draw()
    draw.draw_any(cluster)


if __name__ == '__main__':
    main()
