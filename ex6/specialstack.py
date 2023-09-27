#Toteuta luokka SpecialStack, jossa on seuraavat metodit:

    #push(x): lisää luku x pinon päälle
    #pop(): palauta ja poista pinon ylin luku
    #increase(k): kasvata pinon k ylimmän luvun arvoa yhdellä

#Kaikkien metodien tulee toimia ajassa O(1).

#Toteuta tiedostoon specialstack.py luokka SpecialStack seuraavan mallin mukaisesti.

class SpecialStack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, x):
        self.stack.append(x)

    def push_many(self, x, k):
        for i in range(k):
            self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def increase(self, k):
        #stack_length = len(self.stack)
        #for i in range(max(stack_length - k, 0), stack_length):
            #self.stack[i] += 1
        if len(self.stack) == k:
            [x+k for x in self.stack]
        else:
            self.stack[-k:] = [x + 1 for x in self.stack[-k:]]

def main():
    s = SpecialStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.increase(2)
    print(s.pop()) # 4
    s.push(1)
    s.increase(2)
    print(s.pop()) # 2
    print(s.pop()) # 4
    print(s.pop()) # 1

    s = SpecialStack()
    for i in range(5*10**4):
        s.push(i+1)
    
    for i in range(5*10**4):
        s.increase(5*10**4)

    print(s.pop())

if __name__ == "__main__":
    main()

#Selitys: Pinon sisältö käyttäytyy koodipohjassa näin:
#[]

#push(1) →
#[1]

#push(2) →
#[1,2]

#push(3) →
#[1,2,3]

#increase(2) →
#[1,3,4]

#pop() →
#[1,3]

#push(1) →
#[1,3,1]

#increase(2) →
#[1,4,2]

#pop() →
#[1,4]

#pop() →
#[1]

#pop() →
#[]