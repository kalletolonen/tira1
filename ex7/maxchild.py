#Tehtäväsi on laskea, mikä on suurin määrä lapsia puussa olevassa solmussa.

#Toteuta tiedostoon maxchild.py funktio count, joka ilmoittaa suurimman lasten määrän.

from collections import namedtuple

def count(node):
    if not node.children:
        return 0
    
    max_count = len(node.children)

    for child in node.children:
        child_count = count(child)
        if child_count > max_count:
            max_count = child_count

    return max_count

def main():
    Node = namedtuple("Node", ["children"], defaults=[[]])

    tree1 = Node([
                Node(),
                Node([Node([Node(), Node()])]),
                Node([Node(), Node()])
            ])

    tree2 = Node([Node([Node(), Node()])])

    print(count(tree1)) # 3
    print(count(tree2)) # 2

if __name__ == "__main__":
    main()

#def count(node):
#    result = len(node.children)
#    for child in node.children:
#        result = max(result, count(child))
#    return result