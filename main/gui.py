import networkx as nx
import math
import matplotlib.pyplot as plt
import random

from main.model import Service

def hierarchy_pos(G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):

    '''
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.  
    Licensed under Creative Commons Attribution-Share Alike 

    If the graph is a tree this will return the positions to plot this in a 
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch 
    - if the tree is directed and this is not given, 
      the root will be found and used
    - if the tree is directed and this is given, then 
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given, 
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    '''
    # if not nx.is_tree(G):
    #     raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
        '''
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        '''

        if pos is None:
            pos = {root:(xcenter,vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)  
        if len(children)!=0:
            dx = width/len(children) 
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G,child, width = dx, vert_gap = vert_gap, 
                                    vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                    pos=pos, parent = root)
        return pos


    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


class Draw:

    DEFAULT_OPTIONS = {
            'with_labels': True,
            'node_size': 500,
            'width': 0.2,
            'arrowsize': 16
        }

    def draw_with_pos(self, root_service: Service, create_pos_function):
        graph = nx.DiGraph()
        labels = {}
        graph.add_node(root_service)
        self.add_edges(root_service, graph, labels)
        options = dict(self.DEFAULT_OPTIONS)
        options['labels'] = labels
        pos = create_pos_function(graph, root_service)
        nx.draw(graph, pos, **options)
        plt.show()

    def draw_any(self, root_service: Service):
        self.draw_with_pos(root_service, lambda graph, service: None)

    def draw_each(self, services: list):
        graph = nx.DiGraph()
        labels = {}
        for service in services:
            graph.add_node(service)
            self.add_edges(service, graph, labels)
        options = dict(self.DEFAULT_OPTIONS)
        options['labels'] = labels
        nx.draw_circular(graph, **options)
        plt.show()

    @staticmethod
    def create_pos(graph, root_service: Service):
        pos = hierarchy_pos(graph, root_service)
        return pos

    @staticmethod
    def create_radial_pos(graph, root_service: Service):
        pos = hierarchy_pos(graph, root_service, width=2 * math.pi, xcenter=0)
        new_pos = {u: (r * math.cos(theta), r * math.sin(theta)) for u, (theta, r) in pos.items()}
        return new_pos

    def draw_tree(self, root_service: Service):
        self.draw_with_pos(root_service, Draw.create_pos)

    def draw_radial_tree(self, root_service: Service):
        self.draw_with_pos(root_service, Draw.create_radial_pos)

    def add_edges(self, service: Service, graph, labels: dict):
        label = service.get_name()
        if service.get_size() > 1:
            label += '[%d]' % service.get_size()
        label += ' - %.2f%%' % service.get_total_availability_percentage()
        labels[service] = label
        for dependency in service.get_dependencies():
            graph.add_edge(service, dependency)
            self.add_edges(dependency, graph, labels)
