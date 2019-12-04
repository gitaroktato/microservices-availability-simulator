# importing networkx 
from main.gui import Draw
# importing matplotlib.pyplot 
import matplotlib.pyplot as plt 

from main.model import Service
from main.model import Call
from main.model import ValidationException

def main():
    # Configuring microservice structure
    aggregate = Service(5, 100, 'aggregate')
    app = Service(5, 100, 'app')
    another_app = Service(5, 100, 'another_app')
    database = Service(5, 100, 'database')
    another_app_db = Service(5, 100, 'database')
    cache = Service(5, 100, 'cache')
    aggregate.add_dependency(app)
    aggregate.add_dependency(another_app)
    app.add_dependency(database)
    app.add_dependency(cache)
    another_app.add_dependency(another_app_db)
    # Simulating calls in cycles
    cycles = 100000
    for _ in range(cycles):
        aggregate.call()
    # Drawing from root
    draw = Draw()
    draw.draw(aggregate)

if __name__ == '__main__':
    main()