#Tehtäväsi on laskea, montako lukua on annetulla listalla. 
#Listan alkioina voi olla listoja, joiden alkioina voi jälleen olla listoja jne. 
#Kaikissa listoissa jokainen alkio on joko lista tai luku.

#Voit olettaa, että lukujen määrä on enintään 100 ja listoja voi olla sisäkkäin enintään 100 kerrosta.

#Toteuta tiedostoon nestedlist.py funktio count, joka palauttaa lukujen määrän.
# https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists

def count(t):
    return len(flatten_list(t))

def flatten_list(list_to_flatten):
    
    result = []
    for item in list_to_flatten:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            # Add single integers separately
            result.append(item)
    return result
    
def main():
    print(count([1,2,3])) # 3
    print(count([1,[2,3],4,5,[6]])) # 6
    print(count([1,[1,[1,[1]]]])) # 4
    print(count([[1,2,[3,4]],5,[[6,[7],8]]])) # 8

if __name__ == "__main__":
    main()