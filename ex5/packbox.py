#Varastossa on n laatikkoa, joilla jokaisella on tietty paino. 
#Montako laatikkoa voit pakata enintään autoon, kun auton lastin maksimipaino on x?

#Algoritmin aikavaativuuden tulee olla O(nlogn).

#Toteuta tiedostoon packbox.py funktio solve, joka ilmoittaa, 
#montako laatikkoa voit pakata enintään.

def solve(t, x):
    total_mass = 0
    packed_items = 0
    sorted_list = sorted(t)
    
    if x < min(t):
        return packed_items

    for item in sorted_list:
        if item + total_mass <= x:
            total_mass = total_mass + item
            packed_items += 1

    return packed_items
    
def main():
    print(solve([1, 1, 1, 1], 2)) # 2
    print(solve([2, 5, 3, 2, 8, 7], 10)) # 3
    print(solve([2, 3, 4, 5], 1)) # 0
    print(solve([2, 3, 4, 5], 10**9)) # 4
    print(solve([10**9, 1, 10**9], 10**6)) # 1

if __name__ == "__main__":
    main()

#Selitys: Ensimmäisessä esimerkissä voit pakata mitkä tahansa kaksi laatikkoa. 
#Toisessa esimerkissä voit pakata kolme laatikkoa, 
#esimerkiksi listan kolme ensimmäistä laatikkoa, 
#jotka painavat yhteensä 10. Kolmannessa esimerkissä et voi pakata 
#mitään laatikkoa, koska jokainen painaa enemmän kuin 1. 
