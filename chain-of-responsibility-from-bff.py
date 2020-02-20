from main.gui import Draw
from main.model import Service


def main():
    # Configuring microservice structure
    proxy = Service(5, 100, 'proxy')
    bff = Service(5, 100, 'BFF')
    bff_database = Service(5, 100, 'BFF_database')
    cart = Service(5, 100, 'cart')
    cart_cache = Service(5, 100, 'cart_cache')
    user = Service(5, 100, 'user')
    user_database = Service(5, 100, 'user_database')
    proxy.add_dependency(bff)
    bff.add_dependency(bff_database)
    bff.add_dependency(cart)
    cart.add_dependency(cart_cache)
    bff.add_dependency(user)
    user.add_dependency(user_database)
    # Simulating calls in cycles
    cycles = 100000
    for _ in range(cycles):
        proxy.call()
    # Drawing from root
    draw = Draw()
    draw.draw_tree(proxy)


if __name__ == '__main__':
    main()
