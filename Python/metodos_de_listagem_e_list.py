# Podemos criar uma lista usando list():

thislist = list(("maca", "banana", "cereja"))


# Métodos de lista

# append() Acrescenta um item ao final da lista.
# clear() Elimina items da lista.
# copy() Devolve uma cópia da lista.
# count() Retorna o número de vezes que um item é encontrado na lista.
# extend() Acrescenta itens de uma lista a outra.
# index() Retorna o índice do primeiro elemento cujo valor é o especificado.
# insert() Adiciona um elemento na posição especificada.
# pop() Elimina o item na posição especificada e devolve o item eliminado.
# remove() Elimina o elemento com o valor especificado.
# reverse() Inverta a ordem da lista.
# sort() Ordene a lista.

# Os métodos mais comumente utilizados são:
# len(), append(), pop(), insert() e remove().

thislist.append("goiaba")             # insere o elemento ao final da lista
thislist.insert(2, "mexerica")        # insere o elemento na posição 2
thislist.extend(["figo", "jaca"])     # junta a nova lista a thislist
print(thislist.index("maca"))         # diz em que posição esta o elemento
print("banana" in thislist)           # imprime verdadeiro ou falso, se o elemento está na lista
thislist.remove("banana")             # remove o elemento da lista
thislist.pop()                        # elimina o último elemento de uma lista e retorna o mesmo
thislist.sort()                       # ordena a lista do menor para o maior
thislist.reverse()                    # ordena do ultimo index para o primeiro

# del elimina uma lista:

del thislist

# clear esvazia a lista, eliminando os seus elementos:

thislist.clear()

