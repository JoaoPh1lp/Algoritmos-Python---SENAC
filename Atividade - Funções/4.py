## Escreva uma função que verifique se um número é par.

def num_par():

    num = int(input("\nDigite um número qualquer para verificar se o mesmo é par: "))
    if num %2 == 0:
        print("\nO número é par!\n")
    else:
        print("\nO número não é par!\n")

num_par()