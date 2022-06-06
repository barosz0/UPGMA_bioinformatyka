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


def main():
    mat = load("dane2.txt")

    print("Wczytano:")
    UPGMA.print_matrix(mat)

    UPGMA.make_tree(mat,"abcde")

if __name__ == "__main__":
    main()