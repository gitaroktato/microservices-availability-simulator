# importing networkx 
from main.gui import Draw
from main.model import Service


def main():
    # Configuring microservice structure
    poor_developer = Service(0, 100, 'hapless_developer')
    for i in range(100):
        service = Service(1, 100, 'service-%d' % i)
        poor_developer.add_dependency(service)
    # Simulating calls in cycles
    cycles = 100000
    for _ in range(cycles):
        poor_developer.call()
    # Drawing from root
    draw = Draw()
    draw.draw_radial_tree(poor_developer)


if __name__ == '__main__':
    main()
