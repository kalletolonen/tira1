#Toteuta luokka MaxList, jossa on seuraavat metodit:

    #add(x): lisää luku x listalle
    #max(): ilmoita listan suurin luku (tai None jos lista on tyhjä)

#Kummankin metodin tulee toimia ajassa O(1).

#Toteuta tiedostoon maxlist.py luokka MaxList seuraavan mallin mukaisesti.

class MaxList:
    def __init__(self):
        self.number_list = []

    def add(self, x):
        if len(self.number_list) > 0:
            if x > self.number_list[-1]:
                self.number_list.append(x)
            else:
                self.number_list.insert(-2, x)
        else:
            self.number_list.append(x)

    def max(self):
        if self.number_list == []:
            return None
        
        return self.number_list[-1]

def main():
    m = MaxList()
    print(m.max()) # None
    m.add(1)
    m.add(2)
    m.add(3)
    print(m.max()) # 3
    m.add(8)
    m.add(5)
    print(m.max()) # 8

if __name__ == "__main__":
    main()