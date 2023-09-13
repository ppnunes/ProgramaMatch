# Os sets permitem armazenar varios elementos em uma unica variavel. Um set é um conjunto de tipos de dados:

{val1, val2, ..., valn}

frutas = {"pera", "banana", "laranja", "tomate"}
legumes = {"cenoura", "chuchu", "abobrinha"}, "tomate"}

# Os valores não são retornado em uma ordem.

# Para adicionar um novo elemento:

frutas.add("maca")

# Para adicionar varios elementos:

frutas.add({"jaca", "mamao", "uva"})

# update() também adiciona:

frutas.update("coco", "abacaxi")


# União de conjuntos:

union = frutas | legumes

feira = frutas.union(legumes)   # feira é um novo conjunto com a uniao dos conjuntos fruta e legumes e exclui os elementops duplicados, se houver

# Se um item estiver repetido nos conjuntos ele não vai ser repetido quando retornado

# Para fazer a intersecção de dois conjuntos:

interseccao = frutas & legumes

# Utilizar sets ajuda a eliminar duplicatas. Podemos criar um novo conjunto com os elementos não duplicados:

diferenca = frutas - legumes


## Para eliminar elementos podemos usar remove() ou discard():

frutas.remove("banana")
frutas.discard("laranja")

pop() elimina o último elemento:

x = frutas.pop()
print(x)               # x retorna o elemento eliminado



### FROZENSET é um set umutável