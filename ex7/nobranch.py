#Tehtäväsi on selvittää, onko annettu puu haarautumaton eli jokaisella solmulla on enintään yksi lapsi.

#Toteuta tiedostoon nobranch.py funktio check, joka ilmoittaa, onko puu haarautumaton.

from collections import namedtuple

def check(node):
    pass

def main():
    Node = namedtuple("Node", ["children"], defaults=[[]])

    tree1 = Node([
                Node(),
                Node([Node([Node(), Node()])]),
                Node([Node(), Node()])
            ])

    tree2 = Node([Node([Node([Node()])])])

    print(check(tree1)) # False
    print(check(tree2)) # True

if __name__ == "__main__":
    main()