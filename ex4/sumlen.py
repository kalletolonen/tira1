#Annettuna on lista, jossa on n kokonaislukua. 
#Tehtäväsi on laskea, monessako listan osalistassa 
#on yhtä monta lukua kuin lukujen summa.

#Algoritmin aikavaativuuden tulee olla O(n).

#Toteuta tiedostoon sumlen.py funktio count, joka ilmoittaa osalistojen määrän.

def count(t):
    total = 0
    sublist_sums = set()
    count = 0

    for num in t:
        total += num

        if total == 0:
            count += 1

        if total in sublist_sums:
            sublist_sums.clear()
            total = num

        sublist_sums.add(total)

    return count

def main():
    print(count([1,1,1,1,1])) # 15
    print(count([3])) # 0
    print(count([6,-4])) # 1
    print(count([5,4,-2,1,-3,2])) # 4

if __name__ == "__main__":
    main()
#Selitys: Viimeisessä esimerkissä halutut osalistat ovat 
#[1], [4,−2], [4,−2,1] ja [5,4,−2,1,−3]. 
#Näissä osalistoissa lukujen summat ovat vastaavasti 1, 2, 3 ja 5. 
