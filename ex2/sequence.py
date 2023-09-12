#Lukujonon jokainen alkio on pienin positiivinen kokonaisluku, 
#jota ei ole vielä esiintynyt lukujonossa ja jossa on yksi tai useampi toistuva numero.

#Lukujono alkaa näin:
#11,22,33,44,55,66,77,88,99,100,101,110,111,112,113,114,…

#Tehtäväsi on etsiä lukujonon kohdassa n oleva luku. Voit olettaa, että n on enintään 1000.
#Toteuta tiedostoon sequence.py funktio generate, joka palauttaa halutun lukujonon alkion.
number_array = []
max_length = 1000

def contains_repeating_digits(number):
    str_number = str(number)
    
    for digit in str_number:
        if str_number.count(digit) >= 2:
            return True
    return False

while len(number_array) < max_length:
    for number in range(10, 10000):
        str_number = str(number)
        if contains_repeating_digits(number) and number not in number_array:
            number_array.append(str_number)

def generate(n):
    count = 0
    value = 0
    while count < n:
        value += 1
        if len(str(value)) != len(set(str(value))):
            count += 1
    return value

def main():
    print(generate(1)) # 11
    print(generate(2)) # 22
    print(generate(3)) # 33
    print(generate(10)) # 100
    print(generate(123)) # 505

if __name__ == "__main__":
    main()

#def generate(n):
#    count = 0
#    value = 0
#    while count < n:
#        value += 1
#        if len(str(value)) != len(set(str(value))):
#            count += 1
#    return value