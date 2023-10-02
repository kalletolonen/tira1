#Tehtäväsi on laskea yhteen kaikkien puussa olevien solmujen syvyydet.

#Toteuta tiedostoon depths.py funktio count, joka laskee syvyyksien summan.

from collections import namedtuple

def count(node, depth=0):

    if not node.children:
        return depth
    
    total_depths = depth

    for child in node.children:
        child_depth = count(child, depth + 1)
        total_depths += child_depth

    return total_depths

def main():
    Node = namedtuple("Node", ["children"], defaults=[[]])

    tree = Node([
               Node(),
               Node([Node([Node(), Node()])]),
               Node([Node(), Node()])
           ])

    print(count(tree)) # 15

if __name__ == "__main__":
    main()

#def count(node):
    #return count_depths(node, 0)

#def count_depths(node, depth):
 #   result = 0
  #  for child in node.children:
   #     result += count_depths(child, depth + 1)
   # return result + depth