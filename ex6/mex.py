#oteuta luokka Mex, jossa on seuraava metodi:

 #   add(x): lisää kokonaisluku x listalle ja palauta listan mex-luku

#Listan mex-luku on pienin epänegatiivinen kokonaisluku, jota ei esiinny listalla. Esimerkiksi listan [2,0,3,4,2] mex-luku on 1.

#Metodin add tulee toimia keskimäärin ajassa O(1). Voit olettaa, että jokainen lisätty luku on epänegatiivinen.

#Toteuta tiedostoon mex.py luokka Mex seuraavan esimerkin mukaisesti.

class Mex:
    def __init__(self):
        self.number_set = set()
        self.mex = 0

    def add(self, x):
        self.number_set.add(x)
        
        while self.mex in self.number_set:
            self.mex += 1
        
        return self.mex
        
def main():
    m = Mex()
    print(m.add(1)) # 0
    print(m.add(3)) # 0
    print(m.add(4)) # 0
    print(m.add(0)) # 2
    print(m.add(5)) # 2
    print(m.add(2)) # 6

if __name__ == "__main__":
    main()