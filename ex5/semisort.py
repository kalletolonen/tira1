#Lista sisältää luvut 1…n jossakin järjestyksessä. Saat jokaisella siirrolla vaihtaa kaksi vierekkäistä lukua keskenään. 
#Tehtäväsi on järjestää lista siten, että kaikki alkupuoliskon luvut ovat pienempiä kuin kaikki loppupuoliskon luvut. 
#Mikä on pienin mahdollinen määrä siirtoja?

#Algoritmin aikavaativuuden tulee olla O(n). Voit olettaa, että n on parillinen kaikissa testeissä.

#Toteuta tiedostoon semisort.py funktio solve, joka antaa pienimmän siirtojen määrän.

def solve(t):
    n = len(t)
    swaps = 0

    for i in range(n // 2):
        for j in range(n // 2, n):
            if t[j] < t[i]:
                t[i], t[j] = t[j], t[i]
                swaps += 1

    return swaps

def main():
    print(solve([2, 1, 4, 3])) # 0
    print(solve([5, 3, 4, 1, 6, 2])) # 6
    print(solve([6, 5, 4, 3, 2, 1])) # 9
    print(solve([10, 1, 9, 2, 8, 3, 7, 4, 6, 5])) # 15

if __name__ == "__main__":
    main()

#Selitys: Listalla [2,1,4,3] alkupuoliskon luvut eli 2 ja 1 ovat jo valmiiksi kaikki pienempiä kuin 
# loppupuolen luvut 4 ja 3. Listalla [5,3,4,1,6,2] tarvitaan ainakin 6 siirtoa. Tässä on yksi optimaalinen ratkaisu: 
# [5,3,4,1,6,2] → [5,3,4,1,2,6] → [3,5,4,1,2,6] → [3,5,1,4,2,6] → [3,1,5,4,2,6] → [3,1,5,2,4,6] → [3,1,2,5,4,6]