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
        self.neighbors = set()

    def __str__(self):
        return f"City: {self.name} Roads to cities: {self.neighbors}"
    

class Cities:
    def __init__(self,n):
        self.cities = [City(i) for i in range(n + 1)]

    def add_road(self,a,b):
        self.cities[a].neighbors.add(b)
        self.cities[b].neighbors.add(a)

    def has_route(self,a,b):
        visited = set()
        return self.search_for_path(a, b, visited)
    
    def search_for_path(self, current, target, visited):
        if current == target:
            return True
        
        visited.add(current)
        
        for neighbor in self.cities[current].neighbors:
            if neighbor not in visited:
                if self.search_for_path(neighbor, target, visited):
                    return True
                
        return False

def main():
    c = Cities(5)
    c.add_road(1,2)
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.has_route(1,5)) # False
    c.add_road(3,4)
    print(c.has_route(1,5)) # True
    #for city in c.cities:
    #    print(f"City: {city.name} Roads: {city.neighbors}")

if __name__ == "__main__":
    main()
