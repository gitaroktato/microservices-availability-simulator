import random

def main():
    availability_range = (2,100)
    failed = 0
    total = 100000
    for i in range(total):
        random_result = random.randint(1, availability_range[1])
        if (random_result <= availability_range[0]):
            failed += 1
    print (failed/total)
    
if __name__ == '__main__':
    main()