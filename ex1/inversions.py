#Annettuna on lista, joka muodostuu luvuista 1…n. Indeksipari (i,j) on inversio, jos i<j ja listan kohdassa i on suurempi luku kuin kohdassa j.
#oit olettaa, että n on enintään 100.
#Toteuta tiedostoon inversions.py funktio count, joka laskee inversioiden määrän.

def count(t):
    inversions_found = 0
    if len(t) < 2:
        return inversions_found
    
    list_lenght = len(t)

    for i in range(list_lenght):
        for j in range(i + 1, list_lenght):
            if t[i] > t[j]:
                inversions_found += 1
    
    return inversions_found
        
if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12

def main():
    count([4,3,2,1])
#Selitys: Listassa [4,3,2,1] inversiot ovat (0,1), (0,2), (0,3), (1,2), (1,3) ja (2,3). 