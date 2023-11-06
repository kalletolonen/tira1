#Tehtäväsi on laskea, monessako puun solmussa 
#kaikkien lasten alipuissa on yhtä monta solmua.

#Toteuta tiedostoon subtrees.py funktio count, joka laskee tuloksen.

from collections import namedtuple

def count(node):
    if not node.children:
        return 1, 1  # A leaf node has 1 node and 1 subtree.

    total_subtrees = 1

    child_counts = []

    for child in node.children:
        _, child_subtrees = count(child)
        total_subtrees += child_subtrees
        child_counts.append(child_subtrees)

    # Check if all child subtrees have the same number of nodes
    if all(child_subtrees == child_counts[0] for child_subtrees in child_counts):
        return 1, total_subtrees
    else:
        return 0, total_subtrees  # Return 0 if subtrees are not equal



def main():
    Node = namedtuple("Node", ["children"], defaults=[[]])
    tree = Node([
               Node(),
               Node([Node([Node(), Node()])]),
               Node([Node(), Node()])
           ])
    print(count(tree)) # 8

if __name__ == "__main__":
    main()