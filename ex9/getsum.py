#Lista sisältää kokonaisluvut 1 \dots n. Monellako tavalla voit valita listalta k lukua niin, että niiden summa on x?
#Voit olettaa, että 1 \le n \le 10 ja 1 \le k \le n. Algoritmisi tulee toimia tehokkaasti kaikissa näissä tapauksissa.
#Toteuta tiedostoon getsum.py funktio count, joka palauttaa tehtävän vastauksen.

#Selitys: Kun n=8, k=3 ja x=12, vastaus on 6. Tässä lista on [1,2,3,4,5,6,7,8] ja mahdolliset tavat ovat [1,3,8], [1,4,7], [1,5,6], [2,3,7], [2,4,6] ja [3,4,5].
from itertools import combinations

def count(n, k, x):
    number_list = list(range(1, n + 1))

    combinations_that_sum_to_x = [comb for comb in combinations(number_list, k) if sum(comb) == x]
    return len(combinations_that_sum_to_x)

def main():
    print(count(1, 1, 1)) # 1
    print(count(5, 2, 6)) # 2
    print(count(8, 3, 12)) # 6
    print(count(10, 4, 20)) # 16

if __name__ == "__main__":
    main()