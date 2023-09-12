#Sinulle annetaan kaksi listaa A ja B, jotka molemmat sisältävät luvut 1…n jossain järjestyksessä.

#Tehtäväsi on laskea, moniko luvuista 1…n esiintyy aiemmin listalla A kuin listalla B. 
#Tässä tehtävässä n voi olla suuri ja sinun täytyy keksiä tehokas algoritmi. Algoritmin aikavaativuuden tulee olla O(n).

#Toteuta tiedostoon twolists.py funktio count, joka palauttaa halutun tuloksen.

def count(a, b):
    if a == b:
        return 0
    
    a_dictionary = {item: index for index, item in enumerate(a)}
    b_dictionary = {item: index for index, item in enumerate(b)}

    items_found_with_smaller_index = 0

    for item in b:
        index_of_a = a_dictionary[item]
        index_of_b = b_dictionary[item]

        if index_of_b > index_of_a:
            items_found_with_smaller_index += 1

    return items_found_with_smaller_index

def main():
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([1,2,3,4], [1,2,3,4])) # 0
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5

if __name__ == "__main__":
    main()
    
#Selitys: Ensimmäisessä testissä luvut 2, 3 ja 4 esiintyvät listalla A aiemmin kuin listalla B. 