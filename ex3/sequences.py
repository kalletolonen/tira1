#Tehtäväsi on laskea, moniko annetun merkkijonon osajono sisältää merkkijonon tira alijonona.

#Merkkijono sisältää jonon tira alijonona silloin, 
# kun merkkijonosta voidaan muodostaa merkkijono tira poistamalla siitä 
# mahdollisesti osa merkeistä muuttamatta merkkien järjestystä. 
# Esimerkiksi taikurinhattu sisältää sanan tira alijonona, mutta ritari ei sisällä.

#Algoritmin aikavaativuuden tulee olla O(n).

#Toteuta tiedostoon sequences.py funktio count, joka palauttaa sellaisten osajonojen määrän, joilla on tira alijonona.

def count(s):
    pass

def main():
    print(count("ritari")) # 0
    print(count("taikurinhattu")) # 4
    print(count("ttiirraa")) # # 4
    print(count("tixratiyra")) # 11 
    print(count("aotiatraorirratap")) # 42
    
if __name__ == "__main__":
    main()

#Selitys: Esimerkiksi merkkijonossa tixratiyra on 11 osajonoa, jotka sisältävät jonon tira alijonona:
#    tixratiyra
#    tixratiyra
#    tixratiyra
#    tixratiyra
#    tixratiyra
#    tixratiyra
#    tixratiyra
#    tixratiyra
#    tixratiyra
#    tixratiyra
#    tixratiyra

#Huomaa, että kelvollinen osajono saa sisältää sanan tira alijonona myös useampia kertoja. Esimerkiksi sanasta tixratiyra voidaan lukea tira mm. tixratiyra tai tixratiyra
