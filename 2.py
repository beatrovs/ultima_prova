
n = int(input("Qual o número escolhido? "))


if n < 10:
    print("Você escolheu o número {},logo menor que 10 ".format(n))
else:
    print("Esse número que escolheu não é menor que 10")

resto = n % 2

if resto == 0:
    print("O número é par")
else:
    print("O número é impar")

    
if n == 51 or n == 80:
    print("O número é 51 ou 80")


if n >= 8 and n <=16:
    print("O número está entre 8 e 16")
else:
    print("Número desconhecido")

