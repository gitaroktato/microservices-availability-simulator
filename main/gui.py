import networkx as nx 
import matplotlib.pyplot as plt 

from main.model import Service

class Draw:

    DEFAULT_OPTIONS = {
            'with_labels': True,
            'node_size': 500,
            'width': 0.2,
            'arrowsize': 16
        }

    def draw(self, root_service):
        graph = nx.DiGraph() 
        labels = {}
        self.add_edges(root_service, graph, labels)
        options = dict(self.DEFAULT_OPTIONS)
        options['labels'] = labels
        nx.draw_spring(graph, **options)
        plt.show()

    def add_edges(self, service, graph, labels):
        labels[service] = '%s - %.2f' % (service.get_name(), service.get_total_availability_percentage())
        for dependency in service.dependencies:
            graph.add_edge(service, dependency)
            self.add_edges(dependency, graph, labels)