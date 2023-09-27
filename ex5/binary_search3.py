#https://www.codingninjas.com/studio/library/how-to-work-binary-search-algorithm-in-python
def binarySearch(arr, ele, l, h):

    while l <= h:
        mid = l + (h - l)//2
        if arr[mid] == ele:
            return mid
        elif arr[mid] < ele:
            l = mid + 1
        else:
            h = mid - 1
            
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

# Toimii ja tuottaa samat tulokset