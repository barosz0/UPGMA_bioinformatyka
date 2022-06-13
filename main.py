from distutils.spawn import spawn
import UPGMA




def load(path):
    with open(path,"r") as f:
        dane = f.readlines();
    
    size = int(dane[0])
    dane.pop(0)

    tab = []

    for i in range(size):
        tab.append([])
        for j in range(size):
            tab[i].append(0)
    


    for l in dane:
        pom = l.split(" ")
        a = int(pom[0])
        b = int(pom[1])
        d = int(pom[2])

        # print(f"{a} {b} {d}")
        tab[a][b] = d
        tab[b][a] = d

    for i in range(size):
        for j in range(size):
            if j != i:
                if(tab[i][j] == 0):
                    print(f"brak danych dla {i} {j}")
        
    return tab

def loadMatrix(path, separator = ","):
    with open(path,"r") as f:
        lines = f.readlines();

    dane = []

    for l in lines:
        l = l.replace("\n","")
        pom = []
        for i in l.split(separator):
            pom.append(int(i))
        
        

        dane.append(pom)
    
    return dane


def main():
    file = "daneM8.txt"
    #mat = load("dane2.txt")
    mat = loadMatrix("dane\\"+file)

    print(mat)
    print("Wczytano:")
    UPGMA.print_matrix(mat)

    UPGMA.make_tree(mat)

if __name__ == "__main__":
    main()