#Monellako tavalla luvuista 1 ... n voidaan muodostaa lista, jossa kaikkien vierekkäisten lukuparien summat ovat erisuuria ja ensimmäinen luku on x?
#Voit olettaa, että 1 <= n <= 8 ja 1 <= x <= n. Algoritmisi tulee olla tehokas kaikissa näissä tapauksissa.
#Toteuta tiedostoon oddlist.py funktio count, joka antaa tehtävän vastauksen.

#Selitys: Kun n=4 ja x=2, vastaus on 4, koska listat ovat [2,1,3,4], [2,1,4,3], [2,4,1,3] ja [2,4,3,1].

def count(n, x):
    pass

def main():
    print(count(1, 1)) # 1
    print(count(4, 2)) # 4
    print(count(8, 5)) # 830

if __name__ == "__main__":
    main()