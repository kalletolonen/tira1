#Tehtäväsi on laskea, monessako puun solmussa kaikkien lasten alipuissa on yhtä monta solmua.

#Toteuta tiedostoon subtrees.py funktio count, joka laskee tuloksen.

from collections import namedtuple

def count(node):
    # TODO

if __name__ == "__main__":
    Node = namedtuple("Node", ["children"], defaults=[[]])

    tree = Node([
               Node(),
               Node([Node([Node(), Node()])]),
               Node([Node(), Node()])
           ])

    print(count(tree)) # 8