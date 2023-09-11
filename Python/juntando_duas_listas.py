# Usando o operador +:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Valores impressos: ['a', 'b', 'c', 1, 2, 3]


# Adicionando todos os elementos da list2 à list1, um por um, usando append():

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Valores impressos: ['a', 'b', 'c', 1, 2, 3]

# Utilizando extend(), cujo objetivo é acrescentar elementos de uma lista a outra:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# Valores impressos: ['a', 'b', 'c', 1, 2, 3]

