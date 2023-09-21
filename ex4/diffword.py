#Annettuna on merkkijono, jossa on välilyönneillä erotettuja sanoja. 
#Jokainen sana muodostuu kirjaimista a–z. Tehtäväsi on laskea tehokkaasti, 
#montako eri sanaa merkkijonossa on.

#Toteuta tiedostoon diffword.py funktio count, joka laskee sanojen määrän.

def count(s):
    words = []
    target = " "
    current_word = ""

    if target in s:
        for character in s:
            if character != " ":
                current_word += character

            else:
                words.append(current_word)
                current_word = ""

        words.append(current_word)

        return len(set(words))

    else:
        return 1
        
def main():
    print(count("apina apina apina")) # 1
    print(count("apina banaani cembalo")) # 3
    print(count("a b c a b c a b c")) # 3
    print(count("saippuakauppias")) # 1

if __name__ == "__main__":
    main()

#def count(s):
#    return len(set(s.split()))
