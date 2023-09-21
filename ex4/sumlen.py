#Annettuna on lista, jossa on n kokonaislukua. 
#Tehtäväsi on laskea, monessako listan osalistassa 
#on yhtä monta lukua kuin lukujen summa.

#Algoritmin aikavaativuuden tulee olla O(n).

#Toteuta tiedostoon sumlen.py funktio count, joka ilmoittaa osalistojen määrän.

def count(t):
    prefix_sum = 0
    count_dict = {0: 1}
    result = 0

    for num in t:
        prefix_sum += num
        if prefix_sum in count_dict:
            result += count_dict[prefix_sum]
            count_dict[prefix_sum] += 1
        else:
            count_dict[prefix_sum] = 1

    return result
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
