# https://www.geeksforgeeks.org/binary-search/
# Python3 Program for recursive binary search.
 
# Returns index of x in arr if present, else -1
def binarySearch(arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
 
    # Element is not present in the array
    else:
        return -1
 
def main():
    array_lenght = 10**7
    numbers_to_repeat = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    random_array = numbers_to_repeat * (array_lenght // len(numbers_to_repeat))
    
    x = 44
    print("-1 == false / place in arr:")
    print(binarySearch(random_array, 0, len(random_array)-1, x))

    random_array.append(x)
    print("-1 == false / place in arr:")
    print(binarySearch(random_array, 0, len(random_array)-1, x))

if __name__ == '__main__':
    main()

# Tuottaa samat tulokset, toimii nopeasti isolla syötteellä.