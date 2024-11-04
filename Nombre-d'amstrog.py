N=int(input("entrer un nombre :"))
N1=N
Q=1
S= 0
while Q != 0 :
    Q = N // 10
    R = N % 10
    S =( R*R*R )+ S
    N = Q
if N1 == S :
    print("le nombre est d'emstrong ")
else :
    print("le nombre saisie n'est pas un nombre d'amstrong ")
