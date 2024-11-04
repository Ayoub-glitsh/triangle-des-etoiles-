print("calculatrice")
N1=int(input("vruillez entrer la valeur du premeir nombre :"))
N2=int(input("veuillez entrer la valeue du deuxieme nombre :"))
OP=input("veuillez entrer l'operatuer de votre operation :")
while (OP != "*") and (OP != "+") and (OP != "-") and (OP != "/") :
    print("l'operateur saisie est non definie veuillez le changer ")
    OP = input("veuillez entrer l'operatuer de votre operation :")
if OP == "+" :
    print("le resultat de votre operation est :",N1+N2)
elif OP == "-" :
    print("le resultat de votre operation est :",N1-N2)
elif OP == "*" :
    print("le resultat de votre operation est :",N1*N2)
else  :
    while N2 == 0 :
        N2=int(input("veuillez entrer une autre valeur de N2 differant de 0 :"))
    print("le resultat de votre operation est :",N1/N2)
