#contador de vogais
dizeres = str(input("digite algo: "))
contador = 0

for victor in dizeres:
    if victor == "a" or victor == "e" or victor == "i" or victor == "o" or victor == "u":
        contador += 1
print("tem ",contador," vogais nessa querida frase")
