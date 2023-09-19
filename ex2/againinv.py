#Tehtäväsi on muodostaa luvuista 1…n lista, jossa on tasan k inversiota.

#Voit olettaa, että n≤100 ja k on valittu niin, että ratkaisu on olemassa. Voit muodostaa minkä tahansa kelvollisen listan.

#Toteuta tiedostoon againinv.py funktio create, joka muodostaa listan.
#https://stackoverflow.com/questions/54506366/algorithm-to-generate-an-array-with-n-length-and-k-number-of-inversions-in-on-l

def create(n, k):
    
    number_list = list(range(1, n + 1))
    if k >= n:
        k = n

    for i in range(n - 1):
        if k >= n - i:
            k_swap = n - i
        else:
            k_swap = k
        
        temp = number_list[i]
        number_list[i] = number_list[i + k_swap]
        number_list[i + k_swap] = temp

        k -= k_swap

    return number_list
        
def main():
    print(create(3, 0)) # [1,2,3]
    print(create(3, 1)) # esim. [1,3,2]
    print(create(3, 2)) # esim. [3,1,2]

if __name__ == "__main__":
    main()