#Merkkijonon osajono on yhtenäinen merkkijonon sisällä oleva merkkijono. 
#Esimerkiksi merkkijonon abc osajonot ovat a, b, c, ab, bc ja abc. 
#Tehtäväsi on laskea, monessako merkkijonon osajonossa jokainen merkki on sama.

#A#lgoritmin aikavaativuuden tulee olla O(n).

#Toteuta tiedostoon samechar.py funktio count, joka palauttaa halutun tuloksen.

def count(s):
    count = 0
    consecutive_count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            consecutive_count += 1
        else:
            count += (consecutive_count * (consecutive_count + 1)) / 2
            consecutive_count = 1

    count += (consecutive_count * (consecutive_count + 1)) / 2

    return int(count)

def main():
    print(count("aaa"))     # 6
    print(count("abbbcaa")) # 11
    print(count("abcde"))   # 5

if __name__ == "__main__":
    main()

#a
#b
#bb
#bbb
#c
#a
#aa

#def count(s):
#    result = 0
#    counter = 0
#    for i in range(len(s)):
#        if i > 0 and s[i-1] != s[i]:
#            counter = 0
#        counter += 1
#        result += counter
#    return result
