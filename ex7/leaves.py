#Tehtäväsi on laskea, montako lehteä annetussa puussa on. Puun solmu on lehti, jos sillä ei ole yhtään lasta.

#Toteuta tiedostoon leaves.py funktio count, joka palauttaa lehtien määrän.

from collections import namedtuple

def count(node):
    
    if not node.children:
        return 1

    leafs = 0

    for child in node.children:
        leafs += count(child)

    return leafs

def main():
    Node = namedtuple("Node", ["children"], defaults=[[]])

    tree = Node([
               Node(),
               Node([Node([Node(), Node()])]),
               Node([Node(), Node()])
           ])

    print(count(tree)) # 5

if __name__ == "__main__":
    main()

#Huomaa, että tämän viikon tehtävissä Node määritellään lyhyellä tavalla:
#Node = namedtuple("Node", ["children"], defaults=[[]])
#Tämä vastaa suunnilleen seuraavaa luokkaa:

#class Node:
#    def __init__(self, children=[]):
#        self.children = children

#    def __repr__(self):
#        return "Node(children="+str(self.children)+")"