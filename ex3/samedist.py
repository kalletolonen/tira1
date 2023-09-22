#Annettuna on lista, jossa on n kokonaislukua. 
#Tehtäväsi on selvittää suurin etäisyys listassa kahden saman luvun välillä. 
#Etäisyys tarkoittaa lukujen indeksien erotusta.

#Algoritmin aikavaativuuden tulee olla O(n).

#Toteuta tiedostoon samedist.py funktio find, joka etsii suurimman etäisyyden.

def find(t):
    hash_array = {}

    for index, value in enumerate(t):
        hash_array[index] = value

    value_last_index = {}
    max_distance = 0

    for index, value in hash_array.items():
        if value in value_last_index:
            distance = index - value_last_index[value]
            max_distance = max(max_distance, distance)
        else:
            value_last_index[value] = index

    return max_distance

def main():
    print(find([1,2,1,1,2])) # 3
    print(find([1,2,3,4])) # 0
    print(find([1,1,1,1,1])) # 4
    print(find([1,1,2,3,4])) # 1
    print(find([1,5,1,5,1])) # 4

if __name__ == "__main__":
    main()

#def find(t):
#    first_pos = {}
#    max_dist = 0
 
#    for i, x in enumerate(t):
#        if x not in first_pos:
#            first_pos[x] = i
#        max_dist = max(max_dist, i - first_pos[x])
 
#    return max_dist