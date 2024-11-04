print("programme de convertion d'une chaine de caractaire du minuscule en majuscule ")
A=input("veuillez entrer un mot :")
for i in A :
    print(chr(ord(i)-32),end="")
