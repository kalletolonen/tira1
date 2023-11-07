#Tehtäväsi on laskea, montako sulkulauseketta voidaan muodostaa n sulusta niin, että joka kohdassa on sisäkkäin enintään k sulkua.
#Voit olettaa, että 2 <= n <= 16 ja 1 <= k <= n/2. Algoritmisi tulee toimia tehokkaasti kaikissa tapauksissa.
#Toteuta tiedostoon brackets.py funktio count, joka antaa tehtävän vastauksen.

import itertools

def count(n, k):
    return count_sequences(n)

def count_sequences(n):
    count = 0
    for sequence in itertools.product("()", repeat=n):
        if valid_sequence(sequence):
            count += 1
    return count
    
def valid_sequence(sequence):
    depth = 0
    for bracket in sequence:
        if bracket == "(":
            depth += 1
        if bracket == ")":
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

def main():
    print(count(6, 1)) # 1
    print(count(6, 2)) # 4
    print(count(6, 3)) # 5
    print(count(9, 1)) # 0
    print(count(16, 4)) # 1094

if __name__ == "__main__":
    main()


