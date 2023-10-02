#Tehtäväsi on tarkastaa, onko jokaisen puussa olevan lehden syvyys sama.

#Toteuta tiedostoon samedepth.py funktio check, joka tarkastaa asian.

from collections import namedtuple


def check(node):
    depths = set()
    depth_first_search(node, 0, depths)
    
    if len(depths) != 1:
        return False
    
    return True

def depth_first_search(node, depth, depths):
    if not node.children:
        depths.add(depth)
    
    for child in node.children:
        depth_first_search(child, depth + 1, depths)
 
def main():
    Node = namedtuple("Node", ["children"], defaults=[[]])

    tree1 = Node([
                Node(),
                Node([Node([Node(), Node()])]),
                Node([Node(), Node()])
            ])

    tree2 = Node([Node([Node()]), Node([Node(), Node()])])

    print(check(tree1)) # False
    print(check(tree2)) # True

if __name__ == "__main__":
    main()

#def check(node):
#    depths = set()
#    check_depths(node, 0, depths)
#    return len(depths) == 1

#def check_depths(node, depth, depths):
#    if node.children == []:
#        depths.add(depth)
#    for child in node.children:
#        check_depths(child, depth + 1, depths)