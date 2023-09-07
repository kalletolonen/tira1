#Annettuna on merkkijono, jonka jokainen merkki on bitti (0 tai 1). Tehtäväsi on muuttaa merkkijonoa niin, että jokainen bitti on sama. Mikä on pienin mahdollinen määrä muutoksia?
#Voit olettaa, että merkkijonossa on enintään 100 merkkiä.
#Toteuta tiedostoon samebits.py funktio count, joka antaa muutosten määrän.

def count(s):
    if len(s) < 2:
        return 0
    
    return min(s.count('1'),s.count('0'))

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4

def main():
    count("01101")
#Selitys: Kun merkkijono on 01101, paras ratkaisu on muuttaa molemmat 0-bitit 1-biteiksi. Tässä tapauksessa tarvitaan kaksi muutosta. 