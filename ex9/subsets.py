#Annettuna on lista, jossa on n kokonaislukua. Tehtäväsi on luoda uusi lista, 
#jossa on kaikki tämän listan osajoukkojen summat pienimmästä suurimpaan.
#Voit olettaa, että 1 \le n \le 10. Algoritmisi tulee toimia tehokkaasti kaikissa näissä tapauksissa.
#Toteuta tiedostoon subsets.py funktio create, joka muodostaa listan.

#Selitys: Listan [1,2,3] osajoukot ovat [], [1], [2], [3], [1,2], [1,3], [2,3] ja [1,2,3]. Näiden osajoukkojen summat ovat [0,1,2,3,3,4,5,6].
from itertools import chain, combinations

def create(t):
    subsets = []
    
    for i in range(len(t) + 1):
        for combination in combinations(t, i):
            subsets.append(list(combination))
    
    subset_sums = [sum(subset) for subset in subsets]
    return sorted(subset_sums)

def main():
    print(create([1, 2, 3])) # [0, 1, 2, 3, 3, 4, 5, 6]
    print(create([42, 1337])) # [0, 42, 1337, 1379]
    print(create([1, 1, 1])) # [0, 1, 1, 1, 2, 2, 2, 3]
    print(create([5])) # [0, 5]

if __name__ == "__main__":
    main()