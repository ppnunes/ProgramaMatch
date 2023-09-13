# Diferente das listas, não se usa índice para acessar os elementos de um dicionario: usa-se o nome da chave entre colchetes:

x = thisdict["modelo"]     # obtem o valor da chave 'modelo' 

Pode-se usar tambem o metodo get() para obter o mesmo resultado:

dic2 = {
    0: "zero",
    1: "um",
    2: "dois",
    3: "tres"
}

dic2[0]
# 'zero'

dic2[3]
# 'tres'

Podemos utilizar qualquer objeto imutavel como chave de um dicionario: tuplas, strings, numeros, etc.


dic3 = {
   (0, "zero"): "cero",
    (1, "um"): "uno",
   (2, "dois"): "dos",
}

dic3[1, "um"]
# 'uno"


## Podemos navegar por um dicionario utilizando o for:

for x in dic1:      # imprime todas as chaves
    printt(x)

for x in dic1:      # imprime os valores 
    print(dic1[x])    


## Usando a função values() pra retornar valores de um dicionario:

for x in dic1.values():
    print(x)



##Usando a função items() para percorrer chaves e valores:

for x, y in dic1.items():
    print(x,y)


Para adicionar um novo elemento a um dicionario:

dic1["cor"] = "azul"        # adiciona a chave cor e o valor azul

##Eliminar elementos do dicionario:

# utilizando pop():

dic1.pop("cor")     # elimina o elemento cor

# utilizando del:

del dic1["cor"]

## Para esvaziar o dicionario utilizamos clear():

dic1.clear()



## Para copiar um dicionario:

# usando copy():

dic4 = dic1.copy()      #dic4 é uma cópia doe dic1

# usando dict()

dic4 = dict(dic1)



## Dicionarios aninhados: podemos criar dicionarios com outros dicionarios dentro:

dic5 = {
    "Dic1" : dic1,
    "Dic2": dic2,
    "Dic3": dic3
}

