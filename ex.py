import random

def embaralhar(lista):
    for i in range (len(lista)-1, 0, -1):
        indice_alestorio = random.randint(0, i)

        valor_temporario = lista [i]
        lista[i] = lista[indice_alestorio]
        lista[indice_alestorio] = valor_temporario
    return lista

valores = [1, 2, 3, 4, 5, 6, 7]

embaralhado = embaralhar(valores)
print [embaralhado]

# 4 /////////////////////

meninos = ["Luiz", "João", "Alex", "Guilherme"]
meninas = ["Lais", "Lolo", "Ana"]

i = 1

for menino in meninos:
    for menina in meninas:
        print(f"Casalzinho {i}:{menino} e {menina}")
        i += 1

# 5 ////////////////////////////

meninos = ["Luiz", "João", "Alex", "Guilherme"]
meninas = ["Lais", "Lolo", "Ana"]

todos = meninos + meninas

i=1
j=0

for pessoa1 in todos:
    for k in range(j, len (todos))
        if pessoa1 != todos[k]:
        print(f"Parzinho {i}:{pessoa1} e {pessoa2}")
        i+=1

j+=1

# 6 ///////////////////////////////

iguais = ['a', 'a', 'a', 'a', 'a']
diferentes = ['a', 'a', 'a', 'b', 'a']

def todos_iguais(lista):
    for i in range(1, len(lista)):
        if lista[i] != lista [i-1]:
            return False

    return True

print (todos_iguais(iguais))
print(todos_iguais(diferentes))
