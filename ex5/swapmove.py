#Annettuna on lista, jossa on luvut 1…n jossakin järjestyksessä. Tehtäväsi on järjestää lista kahden komennon avulla:

#SWAP: vaihtaa keskenään listan kaksi ensimmäistä lukua
#MOVE: siirtää listan ensimmäisen luvun viimeiseksi

#Suunnittele algoritmi, joka muodostaa listan komennoista, joiden suorittaminen järjestää listan. Algoritmi voi antaa minkä tahansa ratkaisun, kunhan siinä on enintään n3 komentoa.

#Toteuta tiedostoon swapmove.py funktio solve, joka antaa listan komennoista. Jokaisen komennon tulee olla merkkijono SWAP tai MOVE.

def solve(t):
    commands = []
    sorted_data = list(range(1, len(t) + 1))

    if t == sorted_data:
        return commands
    
    if len(t) == 2:
        t[0], t[1] = t[1], t[0]
        commands.append("SWAP")
        return commands
    
    while t != sorted(t):
        if t[0] > t[1]:
            t.append(t[0])
            t.pop(0)
            commands.append("MOVE")
        else:
            for i in range(1, len(t)):
                if t[i] < t[i - 1]:
                    t[i], t[i - 1] = t[i - 1], t[i]
                    commands.append("SWAP")
                    break

    return commands

def main():
    print(solve([1, 2])) # esim. []
    print(solve([2, 1])) # esim. [SWAP]
    print(solve([1, 3, 2])) # esim. [SWAP, MOVE]
    print(solve([3, 2, 1])) # esim. [MOVE, SWAP]
    print(solve([2, 3, 4, 1])) # esim. [MOVE, MOVE, MOVE]
    print(solve([2, 1, 10, 4, 8, 7, 3, 6, 9, 5]))

if __name__ == "__main__":
    main()

#Selitys: Lista [1,3,2] voidaan järjestää suorittamalla ensin komento SWAP, jolloin listasta tulee [3,1,2], ja sitten komento MOVE, jolloin listasta tulee [1,2,3]. 