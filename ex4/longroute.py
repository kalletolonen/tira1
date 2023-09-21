# Robotti liikkuu kuten viikon aiemmassa tehtävässä, mutta 
#toistaa samaa liikesarjaa k kertaa peräkkäin. Monessako eri ruudussa robotti käy yhteensä?

#Voit olettaa, että liikesarjassa on enintään 
#100 komentoa ja k on välillä 1…109. Algoritmin tulee toimia tehokkaasti näillä rajoilla.

#Toteuta tiedostoon longroute.py funktio count, 
#joka ilmoittaa eri ruutujen määrän, kun sille annetaan robotin liikesarja ja toistojen määrä.

from collections import defaultdict

def count(s, k):
    dp = defaultdict(int)

    # Lähtöasetelma
    dp[(0, 0)] = 1

    # Siirrot
    for i in range(1, k + 1):
        for move in s:
            if move == "U":
                dp[(0, i)] += dp[(0, i - 1)]
            if move == "D":
                dp[(0, i)] += dp[(0, i + 1)]
            if move == "L":
                dp[(i, 0)] += dp[(i - 1, 0)]
            if move == "R":
                dp[(i, 0)] += dp[(i + 1, 0)]

    # Saapumispiste
    return dp[(k, 0)]
    
def main():
    print(count("UR", 100))  # 201
    print(count("UD", 100))  # 2
    print(count("UURRDDL", 500))  # 1506
    print(count("L", 10**9))  # 1000000001
    print(count("DLUR", 10**9))  # 4

if __name__ == "__main__":
    main()
