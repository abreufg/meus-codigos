#Questao 1
i = 0
lista = []
maior = 0
menor = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
while i <= 4:
    entrada = input(f"Digite o {i+1}° numero: ")
    if entrada == "sair":
        break
    else:
        entrada = int(entrada)
        if entrada > maior:
            maior = entrada
        if entrada < menor:
            menor = entrada
        lista.append(entrada)
        i = i + 1
soma = 0
for n in lista:
    n = int(n)
    soma += n
print(f"Sua lista é: {lista}")
print(f"A soma de todos os numeros da lista é {soma}")
print("A soma de todos os numeros da lista é {}".format(soma))
print(f"O Maior numero da sua lista é: {maior}")
print("O Maior numero da sua lista é: {}".format(maior))
print(f"O Menor numero da sua lista é: {menor}")
print("O Menor numero da sua lista é: {}".format(menor))

#SEGUNDA QUESTÃO

notas = ()
i = 0
while i <= 4:
    entrada = input(f"Digite a {i+1}° nota: ")
    if entrada == "sair":
        break
    else:
        entrada = float(entrada)
        notas = notas + (entrada,)
        i = i + 1
soma = 0
denominador = 0
for n in notas:
    n = float(n)
    soma += n
    denominador = denominador + 1
media = soma / denominador

print(f"A media da turma é {media: .2f}")
print("A media da turma é {}".format(media))
if media >= 9:
    print("Exelente!")
if media < 5:
    print("Ruim!")
if media >= 7 and media < 9:
    print("Bom!")
if media >= 5 and media < 7:
    print("Regular!")


#TERCEIRA QUESTÃO
alunos = {}

i = 0
while i <= 2:
    nome = input(f"Digite o nome do {i+1}° aluno: ")
    nota = int(input(f"Digite a nota do {i+1}° aluno: "))
    alunos[nome] = nota
    if nome == "sair":
        break
    else:
        i = i + 1
for a, n in alunos.items():
            if n >= 7:
                print(f"O aluno {a} tirou nota {n} e está APROVADO")
                print("O aluno {} tirou nota {} e está APROVADO".format(a,n))
            else:
                print(f"O aluno {a} tirou nota {n} e está REPROVADO!")
                print("O aluno {} tirou nota {} e está REPROVADO!".format(a,n))



#4 QUESTÃO
vogais = ("aeiouAEIOU")
i = 0
while True:
    palavra = input("Digite uma palavra ou frase para contar as vogais (sair para sair): ")
    for l in palavra:
        if l in vogais:
            i+=1
    if palavra == "sair":
        print("Encerrando programa...")
        break
    print(f"A palavra {palavra} possui {i} vogais")
    print("A palavra {} possui {} vogais".format(palavra,i))
    i=0

#QUINTA QUESTÃO
numeros = []
op = None 
i = 0
n = 0
parar = 0
while True:
    while i <= 1:
        n = input(f"Digite o {i+1}° número: ")
        if n == "sair":
            parar = "sair"
            break
        else:
            n = float(n)
            numeros.append(n)
        i = i + 1
    def soma():
        result=numeros[0]+numeros[1]
        print(f"O resultado de '{numeros[0]}' + '{numeros[1]}' é '{result}'")
        print("O resultado de '{}' + '{}' é '{}'".format(numeros[0],numeros[1],result))

    def sub():
        result=numeros[0]-numeros[1]
        print(f"O resultado de '{numeros[0]}' - '{numeros[1 ]}' é '{result}'")
        print("O resultado de '{}' - '{}' é '{}'".format(numeros[0],numeros[1],result))

    def multi():
        result=numeros[0]*numeros[1]
        print(f"O resultado de '{numeros[0]}' X '{numeros[1 ]}' é '{result}'")
        print("O resultado de '{}' X '{}' é '{}'".format(numeros[0],numeros[1],result))

    def div():
        result=numeros[0]/numeros[1]
        print(f"O resultado de '{numeros[0]}' / '{numeros[1 ]}' é '{result}'")
        print("O resultado de '{}' / '{}' é '{}'".format(numeros[0],numeros[1],result))
    def sair():
        exit

    if parar == "sair":
        break
    print("Qual operação deseja realizar?")
    print("1 para soma")
    print("2 para subtração")
    print("3 para multiplicação")
    print("4 para divisão")
    op = int(input(""))

    if op == 1:
        soma()

    if op == 2:
        sub()
    if op == 3:
        multi()
    if op == 4:
        div()
    numeros.clear()
    i = 0


#SEXTA QUESTÃO
nomes = []
i = 0
while True:
    nome = input(f"Digite o {i+1}° para a lista: ")
    if nome == "sair":
        break
    nomes.append(nome)
    i = i + 1
print(f"Os nomes digitados foram {nomes}")


#SETIMA QUESTAO
maiusculas = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
palavra = str(input("Digite uma palavra: "))
i = 0
for l in palavra:
    if l in maiusculas:
        i = i + 1
print(f"A palavra {palavra} possue {i} letras maiusculas!")
print("A palavra {} possue {} letras maiusculas!".format(palavra,i))

#OITAVA QUESTÃO
produtos = {"arroz": 20,"feijap": 10,"macarrao": 7,"notebbok": 25000}

produto = input("Digite o nome de um produto: ")

def busca_preco(produtos, produto):
    if produto in produtos:
        return produtos[produto]
    else:
        return "Produto não encontrado"

print(f"O preço é R${busca_preco(produtos, produto)}")

#NONA QUESTÃO
numeros = []
i = 0
while i <= 4:
    n = int(input("Digite um numero: "))
    numeros.append(n)
    i = i +1

def analise_lista(numeros):
    maior = numeros[0]
    menor = numeros[0]
    soma = 0
    for n in numeros:
        soma += n
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    print(f"O maior é {maior}")
    print(f"O menor é {menor}")
    print(f"A soma é {soma}")
analise_lista(numeros)


#10 questao
notas = (7.5, 8.0, 5.0, 9.0, 6.5)
def media_turma(notas):
    soma = 0
    denominador = 0

    for n in notas:
        n = float(n)
        soma += n
        denominador = denominador + 1
    media = soma / denominador

    print(f"A media da turma é {media: .2f}")
    print("A media da turma é {}".format(media))
    if media >= 9:
        print("Exelente!")
    if media < 5:
        print("Ruim!")
    if media >= 7 and media < 9:
        print("Bom!")
    if media >= 5 and media < 7:
        print("Regular!")

media_turma(notas)

#11questão

alunos = {"Gabriel": 10, "João": 5, "Pedro": 7}
situacao = {}
def resultados_aluno(alunos):
    for a, n in alunos.items() :
        if n >= 7:
            situacao.update({a:"Aprovado"})
        if n < 7:
            situacao.update({a:"Reprovado"})
    print(situacao)
resultados_aluno(alunos)

#12questão

palavra = "O rato roeu a roupa do rei de roma"
vogais = "aieouAEIOU"
def conta_vogais(palavra):
    i = 0
    for l in palavra:
        if l in vogais:
            i = i + 1
    print(f"A palavra {palavra} possui {i} vogais!")
    print("A palavra {} possui {} vogais!".format(palavra, vogais))
conta_vogais(palavra)

#13questão
a = 2.5
b = 2.5
def operacoes(a,b):
    resultados = (f"A soma entre '{a}' e '{b}' é '{a+b}'. \nA subtração entre '{a}' e '{b}' é '{a-b}'. \nA Multiplicação entre '{a}' e '{b}' é '{a*b}'. \nA divisão entre '{a}' e '{b}' é '{a/b}'.")
    print(resultados)
operacoes(a,b)

#14 questão


def coletar_nomes():
    nomes = []
    i = 0
    while True:
        n = str(input(f"Digite o {i+1}° nome: "))
        if n == "sair" or n == "Sair" or n == "SAIR":
            break
        nomes.append(n)
        i = i + 1
    print(nomes)
coletar_nomes()

#questao 15
palavra = "Gabriel Farias de Abreu"
maiusculas = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def conta_maiusculas(palavra):
    i = 0
    for l in palavra:
        if l in maiusculas:
            i = i + 1
    print(f"A palavra '{palavra}' tem '{i}' letras maiusculas")

conta_maiusculas(palavra)