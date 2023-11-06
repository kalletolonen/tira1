#Annettuna on n×mn×m -ruudukko, joka esittää labyrinttiä. 
#Tehtäväsi on laskea lyhimmän reitin pituus ruudusta A ruutuun B. Jokainen ruutu on joko lattiaa (.) tai seinää (#), ja jokainen reunalla oleva ruutu on seinää.

#Voit olettaa, että 1≤n,m≤201≤n,m≤20. Jos mitään reittiä ei ole olemassa, palauta −1−1.

#Toteuta tiedostoon labyrinth.py funktio count, joka kertoo lyhimmän reitin pituuden.

from collections import deque

def count(r):
    def is_valid(x, y):
        return 0 <= x < len(r) and 0 <= y < len(r[0]) and r[x][y] != '#'

    # Find the positions of 'A' and 'B' in labyrinth
    start = end = None
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j] == 'B':
                start = (i, j)
            elif r[i][j] == 'Y':
                end = (i, j)

    # Moves to use
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Initialize a queue for BFS
    queue = deque([(start, 0)])

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                queue.append(((new_x, new_y), steps + 1))
                # Mark the visited cell to avoid revisiting it
                r[new_x] = r[new_x][:new_y] + '#' + r[new_x][new_y + 1:]

    return -1

def main():
    r = ["########",
         "#......#",
         "#.#.Y#.#",
         "#.#B.#.#",
         "#..X.#.#",
         "#.#..#.#",
         "########"]
    print(count(r)) # 18

if __name__ == "__main__":
    main()

#def count(r):
#    n = len(r)
#    m = len(r[0])
#    for i in range(n):
#        if "A" in r[i]:
#            start_pos = (i,r[i].index("A"))
#    dist = {}
#    queue = [start_pos]
#    dist[start_pos] = 0
#    i = 0
#    while i < len(queue):
#        my_pos = queue[i]
#        if r[my_pos[0]][my_pos[1]] == "B":
#            return dist[my_pos]
#        for move in [(0,1),(0,-1),(1,0),(-1,0)]:
#            new_pos = (my_pos[0]+move[0],my_pos[1]+move[1])
#            if r[new_pos[0]][new_pos[1]] == "#":
#                continue
#            if new_pos not in dist:
#                dist[new_pos] = dist[my_pos]+1
#                queue.append(new_pos)
#        i += 1
#    return -1