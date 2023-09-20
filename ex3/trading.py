#Annettuna on osakkeen hinta n päivän ajalta. Tehtäväsi on selvittää, mikä olisi ollut suurin mahdollinen tuotto, 
#jos olisit voinut ostaa ja myydä osakkeen enintään kahdesti. Sinulla saa olla hallussasi kerrallaan enintään yksi osake.

#Algoritmin aikavaativuuden tulee olla O(n).

#Toteuta tiedostoon trading.py funktio find, joka palauttaa halutun tuloksen.

def find(t):
    n = len(t)
    
    first_buy = -t[0]
    first_sell = 0
    second_buy = -t[0]
    second_sell = 0
    
    for i in range(n):
        #Update the maximum profit if we buy the stock at the current price
        first_buy = max(first_buy, -t[i])
        
        #Update the maximum profit if we sell the stock at the current price
        first_sell = max(first_sell, first_buy + t[i])
        
        #Update the maximum profit if we buy the stock again at the current price
        second_buy = max(second_buy, first_sell - t[i])
        
        #Update the maximum profit if we sell the stock again at the current price
        second_sell = max(second_sell, second_buy + t[i])
    
    return second_sell

def main():
    print(find([1,5,1,5])) # 8
    print(find([1,2,3,4,5])) # 4
    print(find([5,4,3,2,1])) # 0
    print(find([4,2,5,8,7,6,1,2,5,1])) # 10

if __name__ == "__main__":
    main()