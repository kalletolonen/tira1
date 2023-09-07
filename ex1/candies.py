#Nallekarkki maksaa a euroa ja suklaakarkki maksaa b euroa. Montako karkkia voit ostaa enintään, jos sinulla on yhteensä rahaa c euroa?
#Voit olettaa, että a, b ja c ovat kokonaislukuja välillä 1…100.
#Toteuta tiedostoon candies.py funktio count, joka antaa suurimman karkkien määrän.
import math

def count(a, b, c):
    cheapestCandy = min(a,b)
    return math.floor(c / cheapestCandy)

if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4

def main():
    count(3, 4, 3)

main()

#Selitys: Ensimmäisessä testissä nallekarkki maksaa 
# 3 euroa ja suklaakarkki maksaa 4 euroa. On mahdollista ostaa enintään 3 karkkia (esimerkiksi 2 nallekarkkia ja 1 suklaakarkki hintaan 10 euroa, rahaa jää jäljelle 1 euro). 