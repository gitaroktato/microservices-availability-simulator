from main.model import Service
from main.model import Call
from main.model import ValidationException

def main():
    entrypoint = Service(1, 100)
    entrypoint.add_dependency(Service(1, 100))
    entrypoint.add_dependency(Service(1, 100))
    entrypoint.add_dependency(Service(1, 100))
    entrypoint.add_dependency(Service(1, 100))
    failed = 0
    cycles = 100000
    for i in range(cycles):
        if entrypoint.call() == Call.FAIL:
            failed += 1
    print (1 - failed/cycles)
    
if __name__ == '__main__':
    main()