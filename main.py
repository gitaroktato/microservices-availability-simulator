# importing networkx 
import networkx as nx 
# importing matplotlib.pyplot 
import matplotlib.pyplot as plt 

from main.model import Service
from main.model import Call
from main.model import ValidationException

def main():
    aggregate = Service(5, 10000)
    app = Service(5, 10000)
    another_app = Service(5, 10000)
    database = Service(5, 10000)
    cache = Service(5, 10000)
    aggregate.add_dependency(app)
    aggregate.add_dependency(another_app)
    app.add_dependency(database)
    app.add_dependency(cache)
    cycles = 100000
    for _ in range(cycles):
        aggregate.call()
    print (aggregate.get_total_availability_percentage())
    g = nx.DiGraph() 
    g.add_edge(app, database)
    g.add_edge(app, cache)
    g.add_edge(aggregate, app)
    g.add_edge(aggregate, another_app)
    options = {
        'with_labels': True,
        'node_size': 500,
        'width': 0.2,
        'labels': {
            aggregate: 'aggregate - %.2f' % aggregate.get_total_availability_percentage(),
            another_app: 'another_app - %.2f' % another_app.get_total_availability_percentage(),
            app: 'app - %.2f' % app.get_total_availability_percentage(),
            database: 'database - %.2f' % database.get_total_availability_percentage(),
            cache: 'cache - %.2f' % cache.get_total_availability_percentage()
        }
    }
    nx.draw_spring(g, **options)
    plt.show()

if __name__ == '__main__':
    main()