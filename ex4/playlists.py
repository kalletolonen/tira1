#Annettuna on soittolista, jossa jokaista laulua vastaa tietty kokonaisluku. 
#Tehtäväsi on selvittää, monessako soittolistan osassa kaikki laulut ovat eri lauluja.

#A#lgoritmin aikavaativuuden tulee olla O(n).

#Toteuta tiedostoon playlists.py funktio count, joka laskee osien määrän.

def count(t):
    song_index = {}
    count = 0
    start_index = 0

    for i, song in enumerate(t):
        if song in song_index and song_index[song] >= start_index:
            start_index = song_index[song] + 1

        song_index[song] = i
        count += i - start_index + 1

    return count

def main():
    print(count([1,2,3,4])) # 10
    print(count([1,1,1,1])) # 4
    print(count([5])) # 1
    print(count([1,3,2,3,4,2,4,1,2,1])) # 24

if __name__ == "__main__":
    main()