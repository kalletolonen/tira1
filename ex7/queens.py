#Tehtäväsi on laskea, monellako tavalla n×nn×n shakkilaudalle
# voidaan sijoittaa nn kuningatarta niin, että mitkään kaksi kuningatarta eivät uhkaa toisiaan ja yksi kuningatar on laudan vasemmassa ylänurkassa.

#Voit olettaa, että 0≤n≤100≤n≤10. Sinun tulee palauttaa koodi, joka laskee tuloksen (eikä sisällä valmiiksi laskettuja tuloksia).

#Toteuta tiedostoon queens.py funktio count, joka laskee tuloksen.

def count(n):
    # TODO

if __name__ == "__main__":
    print(count(1)) # 1
    print(count(4)) # 0
    print(count(5)) # 2
    print(count(8)) # 4