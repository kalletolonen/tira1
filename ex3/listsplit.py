#Annettuna on lista, jossa on n kokonaislukua. 
#Tehtäväsi on laskea, monellako tavalla listan voi halkaista kahteen osaan niin, 
#että molemmissa osissa pienin luku on sama.

#Algoritmin aikavaativuuden tulee olla O(n).

#Toteuta tiedostoon listsplit.py funktio count, joka palauttaa halutun tuloksen.

def count(t):
    n = len(t)
    left_minimum = [0] * n
    right_minimum = [0] * n
    count = 0

    left_minimum[0] = t[0]
    for i in range(1, n):
        left_minimum[i] = min(left_minimum[i - 1], t[i])

    right_minimum[n - 1] = t[n - 1]
    for i in range(n - 2, -1, -1):
        right_minimum[i] = min(right_minimum[i + 1], t[i])

    for i in range(1, n):
        if left_minimum[i - 1] == right_minimum[i]:
            count += 1

    return count

def main():
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0

if __name__ == "__main__":
    main()