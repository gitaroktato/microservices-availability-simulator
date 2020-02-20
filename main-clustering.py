from main.gui import Draw
from main.model import Service, Cluster


def main():
    # Configuring microservice structure
    proxy = Cluster(Service(5, 100, 'proxy'), 10)
    aggregate = Cluster(Service(5, 100, 'aggregate'), 5)
    app = Cluster(Service(5, 100, 'app'), 2)
    another_app = Cluster(Service(5, 100, 'another_app'), 3)
    database = Service(5, 100, 'database')
    another_app_db = Service(5, 100, 'database')
    cache = Service(5, 100, 'cache')
    proxy.add_dependency(aggregate)
    aggregate.add_dependency(app)
    aggregate.add_dependency(another_app)
    app.add_dependency(database)
    app.add_dependency(cache)
    another_app.add_dependency(cache)
    another_app.add_dependency(another_app_db)
    # Simulating calls in cycles
    cycles = 100000
    for _ in range(cycles):
        proxy.call()
    # Drawing from root
    draw = Draw()
    draw.draw_tree(proxy)


if __name__ == '__main__':
    main()
