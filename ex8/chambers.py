#Annettuna on n×mn×m -ruudukko, joka esittää talon pohjapiirrosta. Jokainen ruutu on joko lattiaa (.) tai seinää (#), ja jokainen reunalla oleva ruutu on seinää.

#Kaksi lattiaruutua kuuluvat samaan huoneeseen, jos ne ovat vierekkäin pysty- tai vaakasuunnassa. Montako huonetta talossa on?

#Voit olettaa, että 1≤n,m≤201≤n,m≤20.

#Toteuta tiedostoon chambers.py funktio count, joka antaa huoneiden määrän.

def count(r):
    def is_valid(x, y):
        return 0 <= x < len(r) and 0 <= y < len(r[0])

    def depth_first_search(x, y):
        if not is_valid(x, y) or r[x][y] != '.':
            return

        # Don't revisit the current position
        r[x] = r[x][:y] + 'X' + r[x][y+1:]

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            depth_first_search(x + dx, y + dy)

    count = 0
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j] == '.':
                depth_first_search(i, j)
                count += 1

    return count

def main():
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3

if __name__ == "__main__":
    main()

#def fill(house,y,x):
#    if house[y][x] == "#":
#        return
#    house[y][x] = "#"
#    fill(house,y-1,x)
#    fill(house,y+1,x)
#    fill(house,y,x-1)
#    fill(house,y,x+1)
 
#def count(r):
#    n = len(r)
#    m = len(r[0])
#    house = [list(r[x]) for x in range(n)]
#    result = 0
#    for i in range(n):
#        for j in range(m):
#            if house[i][j] == ".":
#                fill(house,i,j)
#                result += 1
#    return result