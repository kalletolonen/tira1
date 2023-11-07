#Käytössäsi on kolikot, joiden arvot ovat 1, 2 ja 5. Montako kolikkoa tarvitaan vähintään, jotta voidaan muodostaa tasan summa x?
#Tässä tehtävässä 1 <= x <= 10^{100} eli x voi olla hyvin suuri. Algoritmisi tulee antaa vastaus tehokkaasti kaikissa tapauksissa.
#Toteuta tiedostoon fastcoin.py funktio count, joka antaa pienimmän kolikoiden määrän.

def count(x):
    number_of_fives = x // 5
    if (x - 5 * number_of_fives == 0):
        return number_of_fives
    left_for_twos = x - 5 * number_of_fives
    number_of_twos = left_for_twos // 2
    if (left_for_twos - 2 * number_of_twos == 0):
        return number_of_twos + number_of_fives
    left_for_ones = x - 5 * number_of_fives - 2 * number_of_twos
    return number_of_twos + number_of_fives + left_for_ones

def main():
    print(count(13)) # 4
    print(count(12345)) # 2469
    print(count(1337**9)) # 2730314408854633746890878156

if __name__ == "__main__":
    main()

#def count(x):
#    return x//5 + [0, 1, 1, 2, 2][x%5]