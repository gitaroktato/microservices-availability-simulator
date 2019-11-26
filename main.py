# importing networkx 
import networkx as nx 
# importing matplotlib.pyplot 
import matplotlib.pyplot as plt 

from main.model import Service
from main.model import Call
from main.model import ValidationException

def main():
    app = Service(5, 10000)
    database = Service(5, 10000)
    app.add_dependency(database)
    failed = 0
    cycles = 100000
    for i in range(cycles):
        if app.call() == Call.FAIL:
            failed += 1
    print (1 - failed/cycles)
    # Drawing graph
    # https://www.geeksforgeeks.org/python-visualize-graphs-generated-in-networkx-using-matplotlib/
    g = nx.Graph() 
    g.add_edge(app, database)
    options = {
        'with_labels': True,
        'node_size': 4500,
        'width': 0.2,
        'labels': {
            app: 'app - %.2f' % ((1 - 5/10000) * 100),
            database: 'database - %.2f' % ((1 - 5/10000) * 100)
        }
    }
    total_availability = 'Total system availability %f' % ((1 - failed/cycles) * 100)
    nx.draw_shell(g, **options, label = total_availability)
    plt.show()

if __name__ == '__main__':
    main()