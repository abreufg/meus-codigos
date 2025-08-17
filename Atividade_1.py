#Exercicio 1
a = "123"
b = int(a)
c = float(b)
print(b)
print(c)
#Exercico 2
texto = "Python é incrível!"
print(len(texto)) # a função len() serve para contar caracteres
print(texto.upper()) #.upper serve para converter minusculas para maiusculas
print(texto.replace("incrível", "poderoso")) #.replace serve para substituir caracteres por outros
#exercicio 3
numero = [10, 20, 30, 40, 50]
print(numero[2]) #imprime o 3 elemento da lista
numero.append(60)#.append adiciona o numero 60 ao final da lista
numero.remove(20)#remove serve para remover um numero da lista
print(numero)#imprime a lista alterada
#exercicio 4
aluno = {"nome": "Maria", "idade": 22, "curso": "Engenharia"}
aluno.update({"notas": [8.5, 7.0, 9.2]})#.updade() serve para adicionar uma nova chave ao dicionario
print(aluno["curso"])
#exercicio 5
cores = ("vermelho", "verde", "azul", "verde")
conjunto = set(cores) #set() converte tupla em conjunto
conjunto.add("amarelo")
print(conjunto)
#exercicio 6
a = int(15)
b = int(4)
c = int(a/b)
print(c)
d = a%b  # % operador para resto da divisao
print(d)
#exercicio 7
dados= [42, 3.14, "Python",True, [1, 2]]
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))
print(type(dados[4]))
#exercicio 8
text = "programação"
invert = text[::-1] #[::-1] serve para ionverter a string
print(invert)
if text == invert:
    print(True)
else:
    print(False)
#exercicio 9
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][1])
matriz[2][1] = 10
print(matriz)
#exercicio final
estoque = {"maça": 10, "banana": 5, "laranja": 8}
estoque["pera"] = 12 # adiciona a variavel estoque a chave pera e atribue o valor 12
del estoque["banana"]#del deleta a chave escolhida
print(estoque.keys()) #keys() retorna as chaves ex.: maça