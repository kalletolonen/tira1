#Etsi tietoa, millainen algoritmi on lomitusjärjestäminen (merge sort) ja miten sen voi toteuttaa. 
#Mittaa algoritmin suoritusaika, kun n=105 ja syöte sisältää satunnaisessa järjestyksessä luvut 1,2,…,n.

#Varmista, että algoritmin suorituksen jälkeen syöte on tosiaan järjestyksessä, mutta älä ota tätä mukaan suoritusajan mittaukseen.

#Tässä tehtävässä saat pisteen automaattisesti, kun ilmoitat tulokset ja käyttämäsi koodin ja painat lähetysnappia.
#https://www.geeksforgeeks.org/merge-sort/

import time
import random

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    result.extend(left)
    result.extend(right)
    return result

def main():
    n = 10**5
    input_data = list(range(1, n + 1))
    random.shuffle(input_data)

    start_time = time.time()
    sorted_data = mergeSort(input_data)
    end_time = time.time()

    assert sorted_data == list(range(1, n + 1))

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} sekuntia")

if __name__ == "__main__":
    main()

