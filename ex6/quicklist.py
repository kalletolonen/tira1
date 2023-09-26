#Toteuta luokka QuickList, jossa on seuraavat metodit:

#    move(k): siirrä listan k ensimmäistä alkiota listan loppuun
#    get(i): ilmoita indeksissä i oleva alkio

#Listan sisältö annetaan konstruktorissa, ja kummankin metodin tulee toimia ajassa O(1).

#Toteuta tiedostoon quicklist.py luokka QuickList seuraavan mallin mukaisesti.

class QuickList:
    def __init__(self, t):
        self.number_list = t
        self.offset = 0

    def move(self, k):
        self.offset = (self.offset + k) % len(self.number_list)

    def get(self, i):
        return self.number_list[(i + self.offset) % len(self.number_list)]

def main():
    q = QuickList([1,2,3,4,5,6,7,8,9,10])
    print(q.get(4)) # 5
    q.move(3)
    print(q.get(4)) # 8
    q.move(3)
    print(q.get(4)) # 1
    q.move(10)
    print(q.get(4)) # 1
    q.move(7)
    q.move(5)
    print(q.get(0)) # 9

if __name__ == "__main__":
    main()

#Selitys Listan sisältö käyttäytyy koodipohjassa näin:

#    [1,2,3,4,5,6,7,8,9,10]
#move(3) →
#[4,5,6,7,8,9,10,1,2,3]

#move(3) →
#[7,8,9,10,1,2,3,4,5,6]

#move(10) →
#[7,8,9,10,1,2,3,4,5,6]

#move(7) →
#[4,5,6,7,8,9,10,1,2,3]

#move(5) →
#[9,10,1,2,3,4,5,6,7,8]

#class QuickList:
#    def __init__(self, t):
#        self.t = t
#        self.shift = 0
 
#    def move(self, k):
#        self.shift += k
 
#    def get(self, i):
#        return self.t[(i+self.shift) % len(self.t)]