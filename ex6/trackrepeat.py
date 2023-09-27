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
        self.track_dictionary = {}
 
    def add(self, x, k):
        if x in self.track_dictionary:
            self.track_dictionary[x] += k
        else:
            self.track_dictionary[x] = k
 
    def check(self):
        if len(self.track_dictionary) == 0:
            return True
        
        frequencies = list(self.track_dictionary.values())
        unique_frequencies = set(frequencies)
 
        return len(frequencies) == len(unique_frequencies)
    
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