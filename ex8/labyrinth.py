#Annettuna on n×mn×m -ruudukko, joka esittää labyrinttiä. 
#Tehtäväsi on laskea lyhimmän reitin pituus ruudusta A ruutuun B. Jokainen ruutu on joko lattiaa (.) tai seinää (#), ja jokainen reunalla oleva ruutu on seinää.

#Voit olettaa, että 1≤n,m≤201≤n,m≤20. Jos mitään reittiä ei ole olemassa, palauta −1−1.

#Toteuta tiedostoon labyrinth.py funktio count, joka kertoo lyhimmän reitin pituuden.

from collections import deque

def count(r):
    def is_valid(x, y):
        return 0 <= x < len(r) and 0 <= y < len(r[0]) and r[x][y] != '#'

    # Find the positions of 'A' and 'B' in the labyrinth
    start = end = None
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j] == 'A':
                start = (i, j)
            elif r[i][j] == 'B':
                end = (i, j)

    # The possible moves
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Initialize a queue for BFS
    queue = deque([(start, 0)])

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps

        # Explore possible moves
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                queue.append(((new_x, new_y), steps + 1))
                # Mark the visited cell to avoid revisiting it
                r[new_x] = r[new_x][:new_y] + '#' + r[new_x][new_y + 1:]

    return -1

def main():
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7

if __name__ == "__main__":
    main()