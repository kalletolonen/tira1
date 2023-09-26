#Toteuta luokka TrackRepeat, jossa on seuraavat metodit:

 #   add(x, k): lisää luku x listalle k kertaa
 #  check(): ilmoita True jos kaikki listan luvut toistuvtt eri määrän kertoja ja muuten False

#Kummankin metodin tulee toimia ajassa O(1).

#Esimerkiksi listalla [1,3,1,1,2,3,1] on kolme lukua 1, 2 ja 3. Luku 1 toistuu 4 kertaa, luku 2 toistuu 1 kerran ja luku 3 toistuu 2 kertaa. 
#Niinpä kaikki listan luvut toistuvat eri määrän kertoja (4, 1 ja 2 kertaa).

#Toteuta tiedostoon trackrepeat.py luokka TrackRepeat seuraavan mallin mukaisesti.
#https://www.geeksforgeeks.org/python-test-if-all-values-are-same-in-dictionary/

class TrackRepeat:
    def __init__(self):
        self.tracks = []
 
    def add(self, x, k):
        for item in range(0,k+1):
            self.tracks.append(x)
 
    def check(self):
        if len(self.tracks) == 0:
            return True
        print(self.tracks)        
        #print("list of values: ", test_val)
        #return test_val.count(test_val[0]) == len(test_val)

def main():
    t = TrackRepeat()
    print(t.check()) # True
    t.add(1, 3)
    print(t.check()) # True
    t.add(2, 3)
    print(t.check()) # False
    t.add(2, 2)
    print(t.check()) # True
    t.add(3, 1)
    print(t.check()) # True
    t.add(3, 4)
    print(t.check()) # False

if __name__ == "__main__":
    main()