# Sinulle annetaan lista, jonka jokainen alkio on kokonaisluku. 
#Tehtäväsi on muodostaa uusi lista, jossa jokaiseen alkioon lisätty luku x.

#Voit olettaa, että listalla on enintään 100 lukua ja 
#jokainen luku on kokonaisluku välillä 1…109.

#Toteuta tiedostoon listadd.py funktio create, joka palauttaa uuden listan.

def create(t, x):
    new_list = t.copy()

    for item in range(len(new_list)):
        new_list[item] += x
        
    return new_list

def main():
    print(create([1,2,3],1)) # [2,3,4]
    print(create([1,1,1,1,1],4)) # [5,5,5,5,5]
    print(create([0],10**9)) # [1000000000]
    
if __name__ == "__main__":
    main()
    
#Huom! Toteuta funktio niin, että se ei aiheuta parametrina 
#annettuun listaan sivuvaikutusta 
#(eli funktio rakentaa uuden listan eikä muokkaa annettua listaa). 
