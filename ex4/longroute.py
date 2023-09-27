# Robotti liikkuu kuten viikon aiemmassa tehtävässä, mutta 
#toistaa samaa liikesarjaa k kertaa peräkkäin. Monessako eri ruudussa robotti käy yhteensä?

#Voit olettaa, että liikesarjassa on enintään 
#100 komentoa ja k on välillä 1…109. Algoritmin tulee toimia tehokkaasti näillä rajoilla.

#Toteuta tiedostoon longroute.py funktio count, 
#joka ilmoittaa eri ruutujen määrän, kun sille annetaan robotin liikesarja ja toistojen määrä.

from collections import defaultdict

def count(s, k):
    x = 0
    y = 0
    visited = {(0, 0)}

    for move in s:
        if move == "U":
            y += 1
        elif move == "D":
            y -= 1
        elif move == "L":
            x -= 1
        elif move == "R":
            x += 1

        visited.add((x, y))

    unique_positions = len(visited)

    if unique_positions == 1:
        # Special case: Robot stays in the same place
        return 1

    # Calculate the number of distinct cells in k repetitions
    total_cells = unique_positions + (unique_positions - 1) * (k - 1)

    return total_cells
    
def main():
    print(count("UR", 100))  # 201
    print(count("UD", 100))  # 2
    print(count("UURRDDL", 500))  # 1506
    print(count("L", 10**9))  # 1000000001
    print(count("DLUR", 10**9))  # 4

if __name__ == "__main__":
    main()
