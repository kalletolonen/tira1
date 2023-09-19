#Tehtäväsi on laskea, monessako merkkijonon osajonossa ei ole a-merkkiä.
#Algoritmin aikavaativuuden tulee olla O(n).
#Toteuta tiedostoon forbidden.py funktio count, joka palauttaa halutun tuloksen.

def count(s):
    count_without_a = 0
    sequence_start = 0

    for sequence_end in range(len(s)):
        if s[sequence_end] == 'a':
            sequence_start = sequence_end + 1
        else:
            count_without_a += sequence_end - sequence_start + 1

    return count_without_a

def main():
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9

if __name__ == "__main__":
    main()

#def count(s):
    #result = 0
    #counter = 0
    #for x in s:
    #    if x == "a":
    #        counter = 0
    #    else:
    #        counter += 1
    #    result += counter
    #return result