#Arquivo model
import this
this.soma = 0
this.num = 0

#1. Faça um algoritmo que calcule a soma dos números inteiros de 1 a 100.
# While = Utilizo quando eu não sei quantas vezes vou repetir
# For = Quando eu sei quantas repetições acontecerão
def somarInicioFim(inicio, fim):
    soma = 0 #Instanciei a variável
    for i in range(inicio, fim+1, 1):
        soma += i
    return soma

#2. Construa um programa que exiba a tabuada de 1 até N.
def tabuada(num, fim):
    multiplicacao = "" #Instanciando um variável do tipo texto
    for i in range(1, fim+1, 1):
        multiplicacao += "{} * {} = {}\n".format(num, i, num * i)
    return multiplicacao

#3. Faça um algoritmo que escreva na tela os números
# de um número inicial a um número final. Os números inicial
# e final devem ser informados pelo usuário;
def mostrarNum(num1, num2):
    mostrar = ""
    for i in range(num1, num2+1, 1):
        mostrar += "{}\n".format(i)
    return mostrar

#4. Escrever um algoritmo que gera e escreve  os números ímpares entre 100 e 200;
def impares(inicio, fim):
    impar = ""
    for i in range(inicio, fim+1, 1):
        if i % 2 != 0:
            impar += "{}\n".format(i)
    return impar

# 8. Escrever um algoritmo que leia 10
# números inteiros e, no final, apresente
# a soma  de todos os números lidos;
def somar10Numeros(num):
    this.soma += num #soma recebe ele mesmo + num
    return this.soma

# 9. Faça o mesmo que antes, porém, ao invés de ler 10 números, o programa deverá
# ler e somar números até que o valor digitado seja zero (0).

# Usar o mesmo método do exercício 08, faz a mesma operação

# 10. Escreva um algoritmo que calcule  a média  dos números digitados pelo usuário,
# se eles forem pares. Termine a leitura se o usuário digitar zero (0);

def calcularMedia(soma, qtde):
    return soma/ qtde

def ePar(num):
    if num % 2 == 0:
        return True
    else:
        return False

# 11. Escreva um algoritmo que leia valores inteiros e encontre o maior e menor valor deles.
# Termine a leitura se o usuário digitar zero (0).

# Não necessita de MODEL nesse exercício

# 12. Escreva um algoritmo que leia 20 valores inteiros e no final exiba:
# A) A soma dos números positivos;
# B) A quantidade de valores negativos

def contarValores():
    this.num += 1
    return this.num

# 13. Escreva um programa que lido um número, calcule e informe o seu fatorial.
# Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120.

def fatorial(num):
    aux = num #para mostrar o número que será fatorizado
    fat = 1
    while(num > 1):
        fat = fat * num
        num -= 1
    return f"O fatorial de {aux} é {fat}"


# 14. Escreva um programa que leia um valor correspondente ao número de jogadores de um time
# de vôlei. O programa deverá ler uma altura para cada um dos jogadores e, ao final,
# informar a altura média do time.

# Não precisou de Model, utilizamos métodos já existentes

# 15. Em um concurso de Miss, os jurados  precisam digitar o nome das 16 candidatas e suas
# respectivas notas (0 a 10). Crie um programa  que leia estas informações e que, ao final
# do programa, apresente apenas o nome e a nota da vencedora.