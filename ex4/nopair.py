#Annettuna on lista, jossa on n kokonaislukua. 
#Kaikkia muita lukuja on listassa tasan kaksi, 
#mutta yhtä lukua on vain yksi. Tehtäväsi on etsiä tämä luku.

#Algoritmin aikavaativuuden tulee olla O(n).

#Toteuta tiedostoon nopair.py funktio find, joka etsii halutun luvun.
from collections import Counter

def find(t):
    counts = Counter(t)
    unique_number = [number for number, count in counts.items() if count == 1]

    return unique_number[0]

def main():
    print(find([2,1,3,2,3])) # 1
    print(find([5,5,9])) # 9
    print(find([1,2,3,4,1,3,4])) # 2
    print(find([8])) # 8
    print(find([7,1,7,4,4,5,1])) # 5

if __name__ == "__main__":
    main()

#def find(t):
#    count = {}
 
#    for x in t:
#        if x not in count:
#            count[x] = 0
#        count[x] += 1
 
#    for x in t:
#        if count[x] == 1:
#            return x

#def find(t):
#    result = 0
#    for x in t:
#        result ^= x
#    return result
