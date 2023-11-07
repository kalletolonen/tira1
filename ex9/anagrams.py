#Merkkijonon anagrammi sisältää kaikki merkkijonon merkit jossakin järjestyksessä. Tehtäväsi on muodostaa kaikki annetun merkkijonon anagrammit.
#Voit olettaa, että merkkijono muodostuu merkeistä a–z ja siinä on enintään 8 merkkiä. Algoritmisi tulee toimia tehokkaasti kaikissa näissä tapauksissa.
#Toteuta tiedostoon anagrams.py funktio create, joka palauttaa merkkijonon anagrammit listana aakkosjärjestyksessä.
from itertools import permutations

def create(s):
    anagram_list = [''.join(p) for p in permutations(s)]
    unique_anagrams = sorted(set(anagram_list))
    
    return unique_anagrams

def main():
    print(create("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create("aaaaa")) # ['aaaaa']
    print(create("abab")) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    print(len(create("aybabtu"))) # 1260

if __name__ == "__main__":
    main()