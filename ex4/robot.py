#obotti on alussa ruudussa (0,0). 
#Tämän jälkeen robotti liikkuu annetun liikesarjan mukaisesti askeleen kerrallaan. 
#Liikesarja muodostuu merkeistä U (up), D (down), L (left) ja R (right). 
#Monessako eri ruudussa robotti käy yhteensä?

#Algoritmin aikavaativuuden tulee olla O(n).

#Toteuta tiedostoon robot.py funktio count, jolle annetaan robotin 
#liikesarja ja joka ilmoittaa eri ruutujen määrän.

def count(s):
    x, y = 0,0
    unique_locations = set()

    unique_locations.add((x, y))

    for move in s:
        if move == "U":
            y += 1
        if move == "D":
            y -= 1
        if move == "L":
            x -= 1
        if move == "R":
            x += 1

        unique_locations.add((x,y))

    return len(unique_locations)

def main():            
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2

if __name__ == "__main__":
    main()
