#Laske, monessako puussa on nn solmua ja kk lehteä.

#Esimerkiksi kun n=4n=4 ja k=2k=2, puut ovat seuraavat:
#1
#1.1    1.2
#1.1.1

#1
#1.1    1.2
#       1.2.1

#1
#1.1
#1.1.1  1.1.2



#Voit olettaa, että 1≤n≤101≤n≤10.

#Toteuta tiedostoon alltree.py funktio count, joka laskee tuloksen.

def count(n, k):
    # TODO

if __name__ == "__main__":
    print(count(4, 1)) # 1
    print(count(4, 2)) # 3
    print(count(4, 3)) # 1
    print(count(4, 4)) # 0
    print(count(10, 4)) # 1176