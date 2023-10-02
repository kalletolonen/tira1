#Tarkastellaan suuntaamatonta verkkoa, jossa on solmut 2,3,…,N. 

#Kahden solmun a ja b välillä on kaari, jos a on jaollinen b:llä tai b on jaollinen a:lla.

#Esimerkiksi solmujen 44 ja 1212 välillä on kaari, koska 1212 on jaollinen 44:llä. 
#Vastaavasti solmujen 33 ja 1313 välillä ei ole kaarta.

#Tee ohjelma, joka laskee verkon komponenttien määrän, kun N=1000.

def count_components(n):
    nodes = 0
    links = 0

    for a in range(2, n + 1):
        connected = False

        for b in range(2, n + 1):
            if a != b and (a % b == 0 or b % a == 0):
                connected = True
                links += 1

        if not connected:
            nodes += 1

    return nodes + links

def main():
    print(count_components(1000))

if __name__ == "__main__":
    main()

