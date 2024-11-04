print("programme d'affichage ")
N=int(input("veuillez entrer le nombre de ligne que vous voulez afficher :"))


for i in range(1,N+1) :
    for l in range(1,2*i):
        print("*",end="")
    print("")
