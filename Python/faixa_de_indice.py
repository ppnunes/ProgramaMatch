#Ao especificar o intervalod e uma lista, o valor de retorno será uma nova lista com os índices especificados. Ex:

thislist = ["maca", "banana", "cereja", "laranja", "kiwi", "melao", "manga"]
print(thislist[2:5])

# Os valores imprimidos serão ['cereja', 'laranja', kiwi], lembrando que 'maca' tem índice 0, o índice 2está incluído e o índice 5 esta excluído.

#Pode-se especificar índices negativos quando a busca começar peli final da lista. Ex:

thislist = ["maca", "banana", "cereja", "laranja", "kiwi", "melao", "manga"]
print(thislist[-4:-1])

# Os valores imprimidos serão ['laranja', 'kiwi', melao], lembrando que 'manga' aqui tem o índice -1, o índice -4 está incluído e o índice -1 esta excluído.

# Pode-se mudar o valor de um elemento consultando o número do índice. Ex:

thislist = ["maca", "banana", "cereja"]
thislist[1] = "pera"
print(thislist)

# Os valores imprimidos serão ['maca', 'pera', cereja].

# Para verificar se um elemento está presente na lista, utilizar a palavra chave in:

thislist = ["maca", "banana", "cereja"]
if "maca" in thislist:
    print("Sim, 'maca' se encontra la lista.")

#Para determinar quantos elementos estão na lista, utilize len() :

thislist = ["maca", "banana", "cereja"]
print(len(thislist))

#Não é possivel fazer a cópia de uma lista apenas digitando lista2 =l ista1, pois dessa forma a lista2 será uma referência à lista1 e todas as mudanças feitas na lista1 também serão feitas na lista2.

#Uma das maneiras de se fazer uma cópia é utilizando o método de lista incorporando a copy():

thislist = ["maca", "banana", "cereja"]
mylist = thislist.copy()
print(mylist)

# Valores impressos:'maca', 'banana', 'cereja'.

# Outra forma é utilizar o método list():

thislist = ["maca", "banana", "cereja"]
mylist = list(thislist)
print(mylist)

# Valores impressos:'maca', 'banana', 'cereja'.