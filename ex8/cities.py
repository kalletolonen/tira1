#Bittimaassa on nn kaupunkia, joiden välillä ei ole vielä teitä. 
#Tehtäväsi on toteuttaa luokka, 
#jonka avulla pystyy lisäämään tien kahden kaupungin välille sekä tutkimaan, onko kahden kaupungin välillä reittiä.

#Voit olettaa, että kaupunkeja on enintään 5050 ja luokan metodeita kutsutaan enintään 100100 kertaa.

#Toteuta tiedostoon cities.py luokka Cities, jossa on seuraavat metodit:

#    konstruktori, jolle annetaan kaupunkien määrä
#    add_road lisää tien kahden kaupungin välille
#    has_route tarkastaa, onko kahden kaupungin välillä reittiä

class City:
    def __init__(self, name):
        self.name = name
        self.roads = set()

    def __str__(self):
        return f"City: {self.name} Roads: {self.roads}"
    

class Cities:
    def __init__(self,n):
        self.cities = [City({i}) for i in range(n + 1)]

    def add_road(self,a,b):
        self.cities[a].roads.add(b)

    def has_route(self,a,b):
        if a in self.cities[a].roads or b in self.cities[b].roads:
            return True
        
        return False

# Gotta account for links to nodes far away, not just the next town over
if __name__ == "__main__":
    c = Cities(5)
    print(c.cities)
    c.add_road(1,2)
    c.add_road(1,2)
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.has_route(1,5)) # False
    c.add_road(3,4)
    print(c.has_route(1,5)) # True

