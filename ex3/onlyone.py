#Annettuna on lista, jossa on n kokonaislukua. Luvuista 
#n−1 on samaa lukua ja lisäksi listalla on jokin toinen luku, joka esiintyy vain kerran. Tehtäväsi on etsiä tämä luku.

#Algoritmin aikavaativuuden tulee olla O(n). Voit olettaa, että n>2.

#Toteuta tiedostoon onlyone.py funktio find, joka palauttaa halutun tuloksen.

def find(t):
    previous_number = t[0]
    first_different_numbers = []
    second_different_numbers = []
    for i in range(0, len(t)):
        if t[i] != previous_number:
            first_different_numbers.append(t[i])
        else:
            second_different_numbers.append(t[i])

    if len(first_different_numbers) < len(second_different_numbers):
        return first_different_numbers[0]
    
    return second_different_numbers[0]

def main():
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5pass

if __name__ == "__main__":
    main()

#def find(t):
    #other = None
    #for x in t:
     #   if x == other:
      #      continue
       # if t.count(x) == 1:
        #    return x
        #other = x

#def find(t):
#    number1 = min(t)
#    number2 = max(t)
#    if t.count(number1) == 1:
#        return number1
#    else:
#        return number2