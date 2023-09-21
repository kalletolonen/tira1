#Annettuna on lista, jossa on n kokonaislukua. Tehtäväsi on poimia listalta 
#mahdollisimman monta kokonaislukua. Ensimmäinen luku saa olla mikä 
#tahansa listan luku. Tämän jälkeen jokaisen seuraavan poimitun 
#luvun tulee olla yhden suurempi kuin edellinen. Montako lukua voit poimia enintään?


#Algoritmin aikavaativuuden tulee olla O(nlogn).

#Toteuta tiedostoon interval.py funktio count, joka ilmoittaa, 
#montako lukua listalta voidaan enintään poimia halutulla tavalla.

def count(t):

    number_set = set(t)

    max_length = 0

    for number in number_set:
        if number - 1 not in number_set:
            current_number = number
            current_length = 1

            while current_number + 1 in number_set:
                current_number += 1
                current_length += 1

            max_length = max(max_length, current_length)

    return max_length    
    
def main():
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3
    
if __name__ == "__main__":
    main()
    
#Selitys: Listalta [10,4,8] voidaan poimia vain yksi luku, 
#sillä minkään kahden luvun erotus ei ole tasan 1. Listalta [7,6,1,8] 
#on mahdollista poimia 3 lukua järjestyksessä 6, 7 ja 8. 
