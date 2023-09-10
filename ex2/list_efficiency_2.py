import time

def add_to_list(numbers, n):
    for number in range(0, n + 1):
        numbers.append(n)
    
def remove_from_list(numbers, n):
    for number in range(0, n):
        numbers.pop(0)

def main():
    n = 10**5
    start_time_add = time.time()
    numbers = []
    add_to_list(numbers, n)
    end_time_add = time.time()

    start_time_remove = time.time()
    remove_from_list(numbers, n)
    end_time_remove = time.time()
    
    print(f"Adding took: {end_time_add - start_time_add} s")
    print(f"Removing took: {end_time_remove - start_time_remove} s")


if __name__ == "__main__":
    main()

