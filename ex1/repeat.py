#ehtäväsi on selvittää, kuinka pitkä on lyhin merkkijono,
# jota toistamalla voidaan muodostaa annettu merkkijono. 
#Esimerkiksi kun merkkijono on abcabcabcabc, lyhin toistettava merkkijono on abc.
#Merkkijono muodostuu merkeistä a–z ja siinä on enintään 100 merkkiä.
#Toteuta tiedostoon repeat.py funktio find, joka antaa toistettavan merkkijonon pituuden.
import re

def find(s):
    if len(s) < 2:
        return 1
    
    input_lenght = len(s)
    for i in range(1, input_lenght // 2 + 1):
        pattern = s[:i]
        repeats = input_lenght // i

        if pattern * repeats == s:
            return len(pattern)
        
    
if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7

def main():
    find("abc")