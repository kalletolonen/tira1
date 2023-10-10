#Verkossa on nn tietokonetta, joiden välillä ei ole vielä yhteyksiä. 
#Tehtäväsi on toteuttaa luokka, jonka avulla pystyy 
#lisäämään yhteyden kahden koneen välille sekä etsimään suorimman reitin kahden koneen välillä.

#Voit olettaa, että tietokoneita on enintään 50 ja 
#luokan metodeita kutsutaan enintään 100 kertaa.

#Toteuta tiedostoon network.py luokka Network, jossa on seuraavat metodit:

#    konstruktori, jolle annetaan tietokoneiden määrä
#    add_link lisää yhteyden kahden koneen välille
#    best_route palauttaa pienimmän yhteyksien määrän reitillä kahden koneen välillä (tai −1−1 jos reittiä ei ole)
    

class Node():
    def __init__(self, name):
        self.name = name
        self.neighbors = set()

    def __str__(self):
        return f"City: {self.name} Roads to cities: {self.neighbors}"

class Network:
    def __init__(self, n):
        self.nodes = [Node(i) for i in range(n + 1)]

    def add_link(self, a, b):
        self.nodes[a].neighbors.add(b)
        self.nodes[b].neighbors.add(a)

    def best_route(self, a, b):
        visited = set()
        return self.search_for_path(a, b, visited)

    def search_for_path(self, current, target, visited):
        if current == target:
            return 0

        visited.add(current)

        min_path_length = float('inf')

        for neighbor in self.nodes[current].neighbors:
            if neighbor not in visited:
                path_length = self.search_for_path(neighbor, target, visited)
                if path_length != -1:
                    min_path_length = min(min_path_length, path_length + 1)

        visited.remove(current)

        if min_path_length == float('inf'):
            return -1
        else:
            return min_path_length

def main():
    w = Network(5)
    w.add_link(1,2)
    w.add_link(2,3)
    w.add_link(1,3)
    w.add_link(4,5)
    print(w.best_route(1,5)) # -1
    w.add_link(3,5)
    print(w.best_route(1,5)) # 2
    for node in w.nodes:
        print(f"Node: {node.name} Routes: {node.neighbors}")

    
if __name__ == "__main__":
    main()

#class Network:
#    def __init__(self,n):
#        self.n = n
#        self.graph = [[] for _ in range(self.n+1)]
# 
#    def add_link(self,a,b):
#        self.graph[a].append(b)
#        self.graph[b].append(a)
 
#    def best_route(self,a,b):
#        self.dist = [-1]*(n+1)
#        self.dist[a] = 0
#        queue = [a]
#        i = 0
#        while i < len(queue):
#            x = queue[i]
#            for y in self.graph[x]:
#                if self.dist[y] == -1:
#                    self.dist[y] = self.dist[x]+1
#                    queue.append(y)
#            i += 1
#        return self.dist[b]
