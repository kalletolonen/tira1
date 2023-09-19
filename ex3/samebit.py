#Annettuna on bittijono, joka muodostuu merkeistä 0 ja 1. 
#Monellako tavalla voit valita bittijonosta kaksi kohtaa niin, 
#että molemmissa kohdissa on sama bitti?

#Algoritmin aikavaativuuden tulee olla O(n).

#Toteuta tiedostoon samebit.py funktio count, joka palauttaa halutun tuloksen.

def count(s):
    result = 0
    counts = {'0': 0, '1': 0}

    for bit in s:
        result += counts[bit]
        # the number of bits encountered that are the same
        counts[bit] += 1

    return result

def main():
    print(count("0101")) # 2
    print(count("000000")) # 15
    print(count("000111")) # 6
    print(count("00100001101100")) # 46

if __name__ == "__main__":
    main()