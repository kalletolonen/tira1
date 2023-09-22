#Etsi tietoa, millainen algoritmi on lisäysjärjestäminen (insertion sort) ja miten sen voi toteuttaa. 
#Mittaa toteutetun algoritmin suoritusaika, kun n=105 ja syöte sisältää satunnaisessa järjestyksessä 
#luvut 1,2,…,n.

#Varmista, että algoritmin suorituksen jälkeen syöte on tosiaan järjestyksessä, 
#mutta älä ota tätä mukaan suoritusajan mittaukseen.

#Tässä tehtävässä saat pisteen automaattisesti, kun ilmoitat tulokset ja 
#käyttämäsi koodin ja painat lähetysnappia.

#Algoritmin suoritusaika:
#https://www.javatpoint.com/insertion-sort

import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    n = 105
    random_numbers = [random.randint(1, n) for _ in range(n)]

    start_time = time.time()
    insertion_sort(random_numbers)
    end_time = time.time()

    execution_time = end_time - start_time

    print("Sorted list:", random_numbers)

    is_sorted = all(random_numbers[i] <= random_numbers[i + 1] for i in range(len(random_numbers) - 1))
    if is_sorted:
        print("The list is ok")
    else:
        print("The list is not ok")

    print(f"Execution time: {execution_time} seconds")

if __name__ == "__main__":
    main()
