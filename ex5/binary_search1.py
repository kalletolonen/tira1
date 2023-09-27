# Binary Search in python
# https://www.programiz.com/dsa/binary-search
def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array_lenght = 10**7
numbers_to_repeat = [1, 2, 3, 4, 5, 6, 7, 8, 9]

random_array = numbers_to_repeat * (array_lenght // len(numbers_to_repeat))
    
x = 44
print("-1 == false / place in arr:")
print(binarySearch(random_array, x, 0, len(random_array)-1))

random_array.append(x)
print("-1 == false / place in arr:")
print(binarySearch(random_array, x, 0, len(random_array)-1))


# Tuottaa oikean tuloksen ja toimii isolla syötteellä