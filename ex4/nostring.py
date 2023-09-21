#Annettuna on merkkijono, jossa on n merkkiä väliltä a–z.

#Tehtäväsi on selvittää, kuinka pitkä on lyhin merkkijono, 
#joka muodostuu merkeistä a–z eikä ole annetun merkkijonon osajono.

#Voit olettaa, että n on enintään 105. Algoritmin tulee toimia tehokkaasti kaikissa tapauksissa.

#Toteuta tiedostoon nostring.py funktio find, joka antaa merkkijonon pituuden.

def find(s):
    # TODO

if __name__ == "__main__":
    print(find("zzz")) # 1
    print(find("aybabtu")) # 1
    print(find("abcdefghijklmnopqrstuvwxyz")) # 2

#Selitys: Kahdessa ensimmäisessä esimerkissä vastaus on 1, 
#koska kummassakaan merkkijonossa ei ole esimerkiksi osajonoa x. 
#Kolmannessa esimerkissä vastaus on 2, koska merkkijonossa on kaikki 1 
#merkin pituiset osajonot mutta ei esimerkiksi 2 merkin pituista osajonoa aa. 
