Listagem por compreensão - maneira de criar listas a partir de valores que já estão armazenados.


minhaLista = [1,2,3,4,5,6,7]

# minhaLista2 cria uma lista com o dobro dos valores presentes em minhaLista:

minhaLista2 = [2*elemento for elemento in minhaLista]
print(minhaLista2)


# Cria uma lista com os elementos pares de minhaLista:

listaPares = [elemento for elemento in minhaLista if elemento%2==0]
print(listaPares)


# Aninha listas:

a = ["a", 'b', "c"]
b = [1, 2, 3]
c = [elemento1*elemento2 for elemento1 in a for elemento2 in b]

# Também pode inserir uma condição:

c = [elemento1*elemento2 for elemento1 in a for elemento2 in b if elemento2 != 2]


# Gera uma lista com os elementos de uma matriz:

m = [["a1", "a2", "a3"], ["b1", "b2", "b3"], ["c1", "c2", "c3"]]
col2 = [row[1] for row in m]
print(col2)

# imprime : ['a2', 'b2', 'c2']

# Nota-se que não modifica a matriz m, somente gera outra lista chamada col2.


# Também é possível adicionar outras expressões e filtros com if dentro das listas de compreensão:

# extrai a diagonal da matriz:

[m[i][i] for i in [0, 1, 2]]
# ['a1', 'b2', 'c3']


## COPIA DE OBJETOS

import copy                     # importa o modulo copy
la = [1, 2 [31, 32, 33]]        # lista aninhada
lb = copy.copy(la)              # cópia plana de la (o mesmo que lb = la[:])
lc = copy.deepcopy(la)          # cópia profunda de la, copia os elementos aninhados
la[1] = 'z'
la[2][2] = 'zz'

print(la)
imprime [1, 'z', [31, 32, 'zz']]

print(lb)
imprime [1, 2, [31, 32, 'zz']]      # copia elementos de primeiro nivel de aninhamento

print(lc)
imprime [1, 2, [31, 32, 33]]        # copia elementos de todos os niveis de aninhamento