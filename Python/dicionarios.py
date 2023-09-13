# Exemplos de dicionarios:

dic1 = {
    "key1": "valor1"
    "key2": "valor2"
}

dic2 = {
    "key3": "valor3"
    "key4": "valor4"
}

dic1 is dic2
# False

dic1 == dic2
# False

dic1 == dic1
# True

dic1 is dic1
# True

# Removendo valores de um dicionario:

dicionario.pop("idade")     # remove o par idade:43

# Colocando um dicionario dentro de outro dicionario:

meuDicionario4 = {"nome" : "Jordan", "equipe" : "Bulls", "anos": {"temporadas" : [19991, 1992, 1993, 1996, 1997, 1998]}}
print(meuDicionario4)

print(meuDicionario.keys())         # imprime as chaves
print(meuDicionario.values())       # imprime o valor das chaves
print(len(meuDicionario))           # imprime o tamanho do dicionario
print(meuDicionario[Brasil])        # busca a chave e o valor
print(meuDicionario)                # imprime o dicionario inteiro

## Criando um dicionario a partir de duas listas:

lista_chaves = ["nome", "idade"]
lista_valores = ["Ana", 43]
dicionario = dict(zip(lista_chaves, lista_valores))     # devolve um objeto do tipo zip e deve ser convertido em lista assim:

lista = list(zip(chaves, valores))


## Verificando se ua chave está em um dicionario:

"nome" in dicionario        #devolve True ou False


## Os dicionarios podem ser criados de maneiras diferentes, eis algumas:

# Partindo de um dicionario vazio e adicionando os campos um a um:

dicionario1 = {}

dicionario1["nome"] = "Ana"
dicionario1["idade"] = 9
dicionario1["turma"] = "1 serie"
dicionario1

# {'nome': 'Ana', 'idade': 9, 'turma': '1 serie'}

# Utilizando a função dict:

dicionario2 = dict(nome = "Ana",
                    idade = 9,
                    turma="1 serie")
dicionario2

# {'nome': 'Ana', 'idade': 9, 'turma': '1 serie'}


## Unindo lista de chaves e valores com a função zip:

chaves = ["nome", "idade", "turma"]
valores = ["Ana", 9, "1 serie"]
zip(chaves, valores)

list(zip(chaves, valores))      # convertemos para uma lista


## Assim como as listas, os dicionarios tambem permitem aninhamento. os dicionarios podem ser usados para criar estruturas e fazer buscas dentro delas.

# Usando a indexação por chaves podemos fazer pesquisa d euma maneira facil.

d['notas']['ingles'] = 'notavel'        # cria uma nova entrada em um dict aninhado

o dicionario d contem:
{'nome': 'Ana',
'sobrenomes': ['Garcia', 'Fernandes'],
'idade': 9
'serie': '1 serie,
'notas': {'matematica' : 'SS',
          'portugues': 'SS',
          'música': 'SS'}
}

d["nome"]
# 'Ana'

d["notas"]["musica"]        # acessa o dicionario aninhado
# 'SS'

d["sobrenomes"][0]          # acessa o primeiro elemento da lista aninhada
# 'Garcia'