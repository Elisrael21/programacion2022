def convierteletra(letra):
    ascii= ord(letra)
    binario= bin(ascii)
    return binario     

print ("Israel Marin Espinoza")
nombrecompleto=['Israel','Marin','Espinoza']


for palabra in nombrecompleto:
    for letra in palabra:
        print(convierteletra(letra))
    print(bin(32))

def convierteletra(letra):
    ascii= ord(letra)
    binario= bin(ascii)
    return binario
    
print ("Brenda Paola Lopez Herrera")
nombrepao=['Brenda','Paola','Lopez','Herrera']

for palabra in nombrepao:
    for letra in palabra:
        print(convierteletra(letra))
    print(bin(32))
