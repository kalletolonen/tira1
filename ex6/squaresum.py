#Kun aineistossa on havainnot (x1,y1),(x2,y2),…,(xn,yn) ja suoraa ax+b sovitetaan aineistoon, virhe voidaan laskea neliösummana kaavalla
#∑i=1n(yi−(axi+b))2.

#Esimerkiksi kun aineisto on (1,1),(3,2),(5,3), ja suora on x−1 (eli a=1 ja b=−1), virhe on
#(1−(1−1))2+(2−(3−1))2+(3−(5−1))2=2.

#Toteuta luokka SquareSum, jossa on seuraavat metodit:

#    add(x, y): lisää havainto aineistoon
#    calc(a, b): ilmoita virheen neliösumma annetuilla parametreilla

#Kummankin metodin tulee toimia ajassa O(1).

#Toteuta tiedostoon squaresum.py luokka SquareSum seuraavan mallin mukaisesti.

class SquareSum:
    def __init__(self):
        self.n = 0
        self.x_sum = 0
        self.y_sum = 0
        self.xy_sum = 0
        self.x_squared_sum = 0

    def add(self, x, y):
        self.n += 1
        self.x_sum += x
        self.y_sum += y
        self.xy_sum += x * y
        self.x_squared_sum += x * x

    def calc(self, a, b):
        if self.n == 0:
            return 0

        y_hat = a * self.x_sum / self.n + b
        error = self.y_sum - y_hat
        return error * error / self.n

def main():
    s = SquareSum()
    s.add(1, 1)
    s.add(3, 2)
    s.add(5, 3)
    print(s.calc(1, 0)) # 5
    print(s.calc(1, -1)) # 2
    print(s.calc(0.5, 0.5)) # 0
    s.add(4, 2)
    print(s.calc(0.5, 0.5)) # 0.25

if __name__ == "__main__":
    main()