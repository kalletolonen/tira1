#Muodosta lista, jossa on luvut 1…n ja kaikkien vierekkäisten 
#lukuparien summat ovat erisuuria. Voit antaa minkä tahansa kelvollisen ratkaisun.

#Voit olettaa, että n on välillä 1…100.

#Toteuta tiedostoon sumdiff.py funktio create, joka palauttaa halutunlaisen listan.
def create(n):
    no_same_sums = []

    for digit in range(1, n + 1):
        no_same_sums.append(digit)

    return no_same_sums

def main():
    print(create(6)) # [3, 1, 6, 2, 4, 5]
    print(create(10)) # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2]
    print(create(15)) # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10]

if __name__ == "__main__":
    main()
    
#Selitys: Koodipohjan esimerkissä [3,1,6,2,4,5], 
#vierekkäisten lukujen summat ovat 4, 7, 8, 6 ja 9. 
#Koska kaikki nämä luvut ovat erisuuria, on ratkaisu kelvollinen. 
#Kuitenkaan esimerkiksi [1,5,2,6,4,3] ei olisi kelvollinen ratkaisu, sillä 5+2=7 ja 4+3=7. 

# Ei siis listaan yhtään samaa summaa
