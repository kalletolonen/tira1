#Piirissä on n leikkijää, jotka on numeroitu 1,2,…,n. 
#Vuoro kiertää piirissä ja joka toinen leikkijä lähtee pois, 
#kunnes piiri on tyhjä. Tehtäväsi on selvittää järjestys, jossa leikkijät poistuvat.

#Voit olettaa, että n on välillä 1…100.

#Toteuta tiedostoon circlegame.py funktio create, joka muodostaa järjestyksen.

def create(n):

    players = list(range(1, n + 1))
    players_that_have_left = []

    index = 1
    while len(players) > 0:
        index %= len(players)
        players_that_have_left.append(players.pop(index))
        index += 1
    
    return players_that_have_left
    
def main():
    print(create(1))  # [1]
    print(create(3))  # [2, 1, 3]
    print(create(4))  # [2, 4, 3, 1]
    print(create(7))  # [2, 4, 6, 1, 5, 3, 7]

if __name__ == "__main__":
    main()
    
## Model solution

#def create(n):
#    players = list(range(1, n+1))
#    order = []

#    i = 0
#    while i < len(players):
#        if i%2 == 0:
#            players.append(players[i])
#        else:
#            order.append(players[i])
#        i += 1
#    return order
