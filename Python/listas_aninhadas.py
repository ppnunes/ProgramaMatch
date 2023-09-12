# Uma lista pode incluir qqr tipo de objeto, inclusive outra lista. Uma lista pode conter uma sub-lista, que por sua vez pode conter outra sub-lista. Ex:

thislist = [["a1", "a2", "a3"],
            ["b1", "b2", "b3"],
            ["c1", "c2", "c3"]]


# Assim se pode criar matrizes

print(thislist[1])

# imprime ["b1", "b2", "b3"]

print(thislist[1:])

# imprime a segunda e a terceira lista : ["b1", "b2", "b3"], ["c1", "c2", "c3"]

print(thislist[O][-1])

# imprime o último elemento [-1] da primeira fila [0] : "a3"


# Aninhamento não homogeneo:

lista = [1, [2,[3, 4], 5], 6]

print(lista[0])

# imprime: 1

print(lista[1])

# imprime: [2,[3, 4], 5]

# Para acesar os elementos de ima sublista usamos a sintaxe [][]:

print(lista[1][0])

# imprime o elemento de indice 0 da lista de indice 1: 2

print(lista[1][1])

# imprime: [3, 4]

print(lista[1][1][0])

# imprime: 3

# IMPORTANTE:

print([3, 4] in lista)

# false pois ele não esta inscrito na primeira lista

print([3, 4] in lista[1])

# true

# para percorrer os itens de uma lista

novalista = ["texto1", "texto2", "texto3", "texto4", "texto5"]

# Indexing:
lista[0]        # 'texto1'
lista[-1]       # 'texto5'

# Slicing:
lista[2, 4]     # 'texto3', texto4'
lista[:3]       # 'texto1', 'texto2', 'texto3'
lista[2:]       # 'texto3', 'texto4', 'texto5'

# Stride
lista[0:4:2]    # 'texto1', 'texto3'

# Podemos usar o stride para inverter uma lista:

lista[::-1]     # é o mesmo que [0:0:-1] - o último índice vira o primeiro na sequencia de tras pra frente: ['text5', 'texto4', 'texto3', 'texto2', 'texto1']

