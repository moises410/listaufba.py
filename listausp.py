#1 questão:
# Inicialize uma lista para armazenar os números que atendem ao critério
numeros_que_atendem = []

# Verifique os números no intervalo de 1000 a 2000
for numero in range(1000, 2001):
    if numero % 11 == 5:
        numeros_que_atendem.append(numero)

# Exiba os números que atendem ao critério
print("Números entre 1000 e 2000 que divididos por 11 têm resto igual a 5:")
for numero in numeros_que_atendem:
    print(numero)

#2 questão:

n = int(input("Digite um valor inteiro e positivo (n): "))

if n <= 0:
    print("O valor de 'n' deve ser um número inteiro positivo.")
else:
    soma = 0
    for i in range(1, n + 1):
        soma += 1/i

    print(f"A soma da série 1 + 1/2 + 1/3 + ... + 1/{n} é igual a: {soma:.2f}")

#questão 3:
# Loop externo de 1 a 10 (para os números de 1 a 10)
for i in range(1, 11):
    print(f"Tabuada do {i}:")

    # Loop interno de 1 a 10 (para os múltiplos)
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")

    # Pula uma linha entre as tabuadas
    print()
#4 questão:
# Inicializa uma lista para armazenar os grupos
grupos = []

# Ler cinco grupos de quatro valores
for _ in range(5):
    grupo = []
    for _ in range(4):
        valor = int(input("Digite um valor: "))
        grupo.append(valor)
    grupos.append(grupo)

# Mostrar os grupos na ordem lida
print("Grupos na ordem lida:")
for grupo in grupos:
    print(grupo)

# Mostrar os grupos na ordem crescente
print("Grupos na ordem crescente:")
for grupo in grupos:
    grupo.sort()
    print(grupo)

# Mostrar os grupos na ordem decrescente
print("Grupos na ordem decrescente:")
for grupo in grupos:
    grupo.sort(reverse=True)
    print(grupo)
#5 questão:
# Inicializa uma lista para armazenar os grupos
grupos = []

# Ler cinco grupos de quatro valores
for _ in range(5):
    grupo = []
    for _ in range(4):
        valor = int(input("Digite um valor: "))
        grupo.append(valor)
    grupos.append(grupo)

# Mostrar os grupos na ordem lida
print("Grupos na ordem lida:")
for grupo in grupos:
    print(grupo)

# Mostrar os grupos na ordem crescente
print("Grupos na ordem crescente:")
for grupo in grupos:
    grupo.sort()
    print(grupo)

# Mostrar os grupos na ordem decrescente
print("Grupos na ordem decrescente:")
for grupo in grupos:
    grupo.sort(reverse=True)
    print(grupo)

# Inicializa uma lista para armazenar os nomes dos clientes e os valores de compras
clientes = []

# Lê o nome e o valor das compras de cada cliente
for _ in range(15):
    nome = input("Digite o nome do cliente: ")
    compras = float(input("Digite o valor das compras do cliente no ano passado: "))
    clientes.append((nome, compras))

# Calcula e mostra o bônus para cada cliente
print("Bônus para os clientes:")
for nome, compras in clientes:
    if compras < 1000:
        bonus = compras * 0.10
    else:
        bonus = compras * 0.15

    print(f"{nome}: R${bonus:.2f}")
#6 questão:
# Inicializa as variáveis
preco_base = 5.00
despesas = 200.00
ingressos_base = 120
aumento_ingressos = 26
lucro_maximo = 0
preco_maximo = 0
vendidos_maximo = 0

# Loop para variar o preço do ingresso de R$5,00 a R$1,00 com incrementos de R$0,50
for preco_ingresso in range(500, 0, -50):
    preco_real = preco_ingresso / 100  # Convertendo centavos para reais
    ingressos_vendidos = ingressos_base + aumento_ingressos * (5 - preco_real)
    lucro = (preco_real * ingressos_vendidos) - despesas

    # Verifica se o lucro atual é o máximo
    if lucro > lucro_maximo:
        lucro_maximo = lucro
        preco_maximo = preco_real
        vendidos_maximo = ingressos_vendidos

    print(f"Preço do Ingresso: R${preco_real:.2f}, Ingressos Vendidos: {ingressos_vendidos}, Lucro: R${lucro:.2f}")

# Exibe o lucro máximo esperado, preço do ingresso e quantidade de ingressos vendidos
print(f"\nLucro Máximo Esperado: R${lucro_maximo:.2f}")
print(f"Preço do Ingresso para Lucro Máximo: R${preco_maximo:.2f}")
print(f"Quantidade de Ingressos Vendidos para Lucro Máximo: {vendidos_maximo}")

#7 questão:
# Inicializa a variável para contar as pessoas maiores de 18 anos
quantidade_maior_dezoito = 0

# Loop para receber a idade de 10 pessoas
for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    
    if idade >= 18:
#questão 8
# Inicialize as variáveis para contar as pessoas em cada faixa etária
faixa1 = faixa2 = faixa3 = faixa4 = faixa5 = 0

# Solicita ao usuário que insira a idade de 15 pessoas
for i in range(15):
    idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))

    if idade <= 15:
        faixa1 += 1
    elif 16 <= idade <= 30:
        faixa2 += 1
    elif 31 <= idade <= 45:
        faixa3 += 1
    elif 46 <= idade <= 60:
        faixa4 += 1
    else:
        faixa5 += 1

# Calcula a porcentagem de pessoas na primeira e última faixa etária em relação ao total
total_pessoas = faixa1 + faixa2 + faixa3 + faixa4 + faixa5
porcentagem_primeira_faixa = (faixa1 / total_pessoas) * 100
porcentagem_ultima_faixa = (faixa5 / total_pessoas) * 100

# Exibe os resultados
print(f"Quantidade de pessoas na primeira faixa etária (até 15 anos): {faixa1}")
print(f"Quantidade de pessoas na segunda faixa etária (16 a 30 anos): {faixa2}")
print(f"Quantidade de pessoas na terceira faixa etária (31 a 45 anos): {faixa3}")
print(f"Quantidade de pessoas na quarta faixa etária (46 a 60 anos): {faixa4}")
print(f"Quantidade de pessoas na quinta faixa etária (acima de 61 anos): {faixa5}")
print(f"Porcentagem de pessoas na primeira faixa etária em relação ao total: {porcentagem_primeira_faixa:.2f}%")
print(f"Porcentagem de pessoas na última faixa etária em relação ao total: {porcentagem_ultima_faixa:.2f}%")
#questão 09
# Solicita ao usuário que insira um número para calcular a tabuada
numero = int(input("Digite um número para calcular a tabuada: "))

# Loop de 1 a 10 para calcular a tabuada
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


#questão 10
# Loop externo para os números de 1 a 10
for numero in range(1, 11):
    print(f"Tabuada do {numero}:")
    
    # Loop interno para os múltiplos de 1 a 10
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
    
    # Espaço em branco entre as tabuadas
    print()
#questão 11
import os
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def check_value(n):
    try:
        n = Decimal(n)
        if n <= 0:
            raise Exception()
    except:
        clear_screen()
        print("Valor invalido, por favor insira um numero maior que 0")
        return False
    else:
        return True
    
def check_char(ch):
    try:
        if len(ch) == 0 or (ch[0].upper() != "P" and ch[0].upper() != "V"):
            raise Exception()
    except:
        clear_screen()
        print("ERRO: por favor insira \'P\' ou \'V\'\n")
        return False
    else:
        return True
    

def get_input():
    getcontext().prec = 2
    parcela = []
    total_P = 0
    total_V = 0
    for i in range(15):
        done = False
        while done != True:
            ch = input("Insira \'P\' para compra parcelada ou insira 'V' para compra a vista:\nNOTA: Apenas o primeiro valor inserido sera válido\n").strip()
            done = check_char(ch)
        done = False
        clear_screen()
        while done != True:
            n = input()
            done = check_value(n)
        n = n
        clear_screen()
        if ch[0].upper() == "P":
            parcela.append(float(n))
            total_P += Decimal(n)
        elif ch[0].upper() == "V":
            total_V += Decimal(n)
    return total_P,total_V,parcela

if __name__ == "__main__":
    clear_screen()
    total_p,total_v,parcela = get_input()
    print("Total das compras a vista: R$%.2f\nTotal das compras parceladas: R$%.2f\nTotal das compras: R$%.2f\n" % (total_v,total_p,(total_p+total_v)))
    for i in range(len(parcela)):
        print("Valor da primeira parcela da compra parcela #%d = R$%.2f" % ((i+1),Decimal(parcela[i]/3)))
#questão 12
import os,math
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def age_check(age):
    try:
        n = int(input("Please insert your age:\n").strip())
        if n <= 0 or n >= 120:
            raise Exception()
    except:
        clear_screen()
        print("Please insert a number between 1 and 120\n")
        return age,False
    else:
        age.append(n)
        return age,True
    
def weight_check(weight):
    try:
        n = float(input("Please insert your weight:\n").strip())
        if math.floor(n) <= 0 or n >= 350:
            raise Exception()
    except:
        clear_screen()
        print("please insert a valid weight\nmust be between 1 and 350KG\n")
        return weight, False
    else:
        weight.append(n)
        return weight,True
    
def height_check(height):
    try:
        n = float(input("Please insert your height:\n").strip())
        if math.floor(n) <= 25 or n >= 250:
            raise Exception()
    except:
        clear_screen()
        print("please insert a valid height\nmust be between 25 and 250cm\n")
        return height, False
    else:
        height.append(n)
        return height,True

def get_input(age,height,weight):
    done = False
    while done != True:
        age,done = age_check(age)
    clear_screen()
    done = False
    while done != True:
        height,done = height_check(height)
    clear_screen()
    done = False
    while done != True:
        weight,done = weight_check(weight)
    clear_screen()
    return age,height,weight

def age_group(age):
    elder = 0
    for i in range(len(age)):
        if age[i] > 50:
            elder += 1
    return elder

def avg_height(age,height):
    getcontext().prec = 2
    sum,count = 0,0 
    for i in range(len(age)):
        if age[i] >= 10 and age[i] <= 20:
            sum += height[i]
            count += 1
    if count != 0:
        avg = Decimal(sum/count)
    else:
        avg = 0
    return avg

def under_40(weight):
    getcontext().prec = 2
    count = 0
    for i in range(len(weight)):
        if weight[i] < 40:
            count += 1
    if count != 0:
        percent = Decimal((count/len(weight))*100)
    else:
        percent = 0
    return percent

if __name__ == "__main__":
    clear_screen()
    age,height,weight = [],[],[]
    for i in range(25):
        age,height,weight = get_input(age,height,weight)
    elder = age_group(age)
    avg = avg_height(age,height)
    percent = under_40(weight)
    print("Older than 50yo: %d person(s)\nAverage height of people who are between 10 and 20yo: %.2fcm\nPercentage of people under 40KG: %.2f%%\n" % (elder,avg,percent))
#questão 13
import math,os
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def age_check(age):
    try:
        n = int(input("Please insert your age:\n").strip())
        if n <= 0 or n >= 120:
            raise Exception()
    except:
        clear_screen()
        print("Please insert a number between 1 and 120\n")
        return age,False
    else:
        age.append(n)
        return age,True

def weight_check(weight):
    try:
        n = float(input("Please insert your weight:\n").strip())
        if math.floor(n) <= 0 or n >= 350:
            raise Exception()
    except:
        clear_screen()
        print("please insert a valid weight\nmust be between 1 and 350KG\n")
        return weight, False
    else:
        weight.append(n)
        return weight,True
    
def get_input(age,weight):
    done = False
    while done != True:
        age,done = age_check(age)
    clear_screen()
    done = False
    while done != True:
        weight,done = weight_check(weight)
    clear_screen()
    return age,weight

def over_90(weight):
    count = 0
    getcontext().prec = 2
    for i in range(len(weight)):
        weight[i] = Decimal(weight[i])
        if weight[i] > 90:
            count += 1
    return count

def avg_age(age):
    getcontext().prec = 2
    sum = 0
    for i in range(len(age)):
        sum += age[i]
    avg = Decimal(sum/len(age))
    return avg

if __name__ == "__main__":
    clear_screen()
    age,weight = [],[]
    for i in range(7):
        age,weight = get_input(age,weight)
    print(weight)
    print(age)
    input()
    ov_90 = over_90(weight)
    avg = avg_age(age)
    print("Heavier than 90KG: %d person(s)\nAverage age: %.2f years\n" % (ov_90,avg))
    #questão 14
    import os
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def get_weigth(weigth):
    getcontext().prec = 2
    continue_op = True
    while continue_op != False:
        try:
            weigth_i = Decimal(input("Por favor insira seu peso em KG:\n"))
            if weigth_i < 20 or weigth_i > 300:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira um peso entre 20KG e 300KG")
        else:
            clear_screen()
            weigth.append(weigth_i)
            break
    return weigth

def get_height(weigth):
    continue_op = True
    while continue_op != False:
        try:
            heigth_i = int(input("Por favor insira sua altura em cm:\n"))
            if heigth_i < 50 or heigth_i > 250:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira uma altura entre 50 e 250cm")
        else:
            clear_screen()
            heigth.append(heigth_i)
            break
    return heigth

def get_age(age):
    continue_op = True
    while continue_op != False:
        try:
            age_i = int(input("Por favor insira sua idade:\n"))
            if age_i < 1 or age_i > 120:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira um numero entre 1 e 120")
        else:
            clear_screen()
            age.append(age_i)
            break
    return age

def eye_color(eye):
    continue_op = True
    while continue_op != False:
        try:
            eye_c = input("Por favor escolha a cor do seu olho:\nA - Azul\nP - Preto\nV - Verde\nC -Castanho\n")[0].strip().upper()
            match eye_c:
                case 'A':
                    eye_c = "Azul"
                case 'P':
                    eye_c = "Preto"
                case 'V':
                    eye_c = "Verde"
                case 'C':
                    eye_c = "Castanho"
                case _:
                    raise Exception()
        except:
            clear_screen()
            print("Error, por favor escolha uma das opções disponiveis")
        else:
            clear_screen()
            eye.append(eye_c)
            break
    return eye

def hair_color(hair):
    continue_op = True
    while continue_op != False:
        try:
            hair_c = input("Por favor insira a cor do seu cabelo:\nP - Preto\nC- Castanho\nR - Ruivo\nL - Louro\n")[0].strip().upper()
            match hair_c:
                case 'L':
                    hair_c = "Louro"
                case 'P':
                    hair_c = "Preto"
                case 'R':
                    hair_c = "Ruivo"
                case 'C':
                    hair_c = "Castanho"
                case _:
                    raise Exception()
        except:
            clear_screen()
            print("Error, por favor escolha uma das opções disponiveis")
        else:
            clear_screen()
            hair.append(hair_c)
            break
    return hair

def condition_1(age,weigth):
    count = 0
    for i in range(len(age)):
        if age[i] > 50 and weigth[i] < 60:
            count += 1
    return count

def condition_2(age,heigth):
    getcontext().prec = 2
    sum,count = 0,0
    for i in range(len(age)):
        if heigth[i] < 150:
            sum += age[i]
            count += 1
    media = Decimal(sum/count)
    return media

def conditions_3_and_4(eye,hair,n):
    getcontext().prec = 2
    x,D = 0,0
    for i in range(len(eye)):
        if eye[i] == "Azul":
            x += 1
        elif eye[i] != "Azul" and hair[i] == "Ruivo":
            D += 1
    C = Decimal((x/n)*100)
    return C,D

def print_results(A,B,C,D):
    print("Maiores de 50 anos e com peso inferior a 50KG: %d pessoa(s)" % A)
    print("Media de idade das pessoas com altura inferior a 1.5m: %.2f ano(s)" % B)
    print("Porcentagem de pessoas que tem olho azul: %.2f%%" % C)
    print("Tem cabelo ruivo e não tem olho azul: %d pessoa(s)" % D)

if __name__ == "__main__":
    clear_screen()
    n = 20
    weigth,age,eye,hair,heigth = [],[],[],[],[]
    for i in range(n):
        age = get_age(age)
        heigth = get_height(heigth)
        weigth = get_weigth(weigth)
        eye = eye_color(eye)
        hair = hair_color(hair)
    A = condition_1(age,weigth)
    B = condition_2(age,heigth)
    C,D = conditions_3_and_4(eye,hair,n)
    print_results(A,B,C,D)
    #questão 15
    import os
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def get_input(nums):
    done = False
    while done != True:
        nums,done = check_input(nums)
    return nums

def check_input(nums):
    try:
        l1 = input("Insert a number:\n").split()
        n = Decimal(l1[0])
    except:
        clear_screen()
        print("Error, please insert a number")
        return nums, False
    else:
        nums.append(n)
        return nums,True

def between(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] >= 30 and nums[i] <= 90:
            count += 1
    return count

if __name__ == "__main__":
    clear_screen()
    nums = []
    for i in range(10):
        nums = get_input(nums)
        clear_screen()
    count = between(nums)
    print("Amount of numbers between 30 and 90 (Including 30 and 90): %d\n" % count)
    #questão 16
    import os
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def get_weigth(weigth):
    getcontext().prec = 2
    continue_op = True
    while continue_op != False:
        try:
            weigth_i = Decimal(input("Por favor insira seu peso em KG:\n"))
            if weigth_i < 20 or weigth_i > 300:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira um peso entre 20KG e 300KG")
        else:
            clear_screen()
            weigth.append(weigth_i)
            break
    return weigth

def get_height(weigth):
    continue_op = True
    while continue_op != False:
        try:
            heigth_i = int(input("Por favor insira sua altura em cm:\n"))
            if heigth_i < 50 or heigth_i > 250:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira uma altura entre 50 e 250cm")
        else:
            clear_screen()
            heigth.append(heigth_i)
            break
    return heigth

def get_age(age):
    continue_op = True
    while continue_op != False:
        try:
            age_i = int(input("Por favor insira sua idade:\n"))
            if age_i < 1 or age_i > 120:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira um numero entre 1 e 120")
        else:
            clear_screen()
            age.append(age_i)
            break
    return age

def condition_1(age,n):
    getcontext().prec = 2
    sum = 0
    for i in range(len(age)):
        sum += age[i]
    media = Decimal(sum/n)
    return media

def condition_2(weigth,heigth):
    count = 0
    for i in range(len(weigth)):
        if weigth[i] > 90 and heigth[i] < 150:
            count += 1
    return count

def condition_3(age,heigth,n):
    getcontext().prec = 2
    count = 0
    for i in range(len(age)):
        if (age[i] >= 10 and age[i] <= 30) and heigth[i] > 190:
            count += 1
    percent = Decimal((count/n)*100)
    return percent

def print_results(A,B,C):
    print("Média de idade: %.2f ano(s)" % A)
    print("Peso superior a 90KG e altura inferior a 1.5m: %d pessoa" % B)
    print("Porcentagem de pessoas que tem mais de 1.9m de altura e tem entre 10 e 30 anos de idade: %.2f%%" %C)

if __name__ == "__main__":
    clear_screen()
    n = 10
    weigth,age,heigth = [],[],[]
    for i in range(n):
        age = get_age(age)
        heigth = get_height(heigth)
        weigth = get_weigth(weigth)
    A,B,C = condition_1(age,n),condition_2(weigth,heigth),condition_3(age,heigth,n)
    print_results(A,B,C)
    #questão 17
    import os,math
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def age_check(age):
    try:
        n = int(input("Please insert your age:\n").strip())
        if n <= 0 or n >= 120:
            raise Exception()
    except:
        clear_screen()
        print("Please insert a number between 1 and 120")
        return age,False
    else:
        age.append(n)
        return age,True
    
def sex_check(sex):
    try:
        ch = input("Type \'M\' for male or \'F\' for female:\n").strip()
        ch = ch[0].upper()
        if ch != 'M' and ch != 'F':
            raise Exception()
    except:
        clear_screen()
        print("Error, invalid input")
        return sex,False
    else:
        sex.append(ch)
        return sex,True

def averages(age,sex):
    getcontext().prec = 2
    sum,sum_m,sum_f,male,female = 0,0,0,0,0
    for i in range(len(age)):
        if sex[i] == "M":
            sum_m += age[i]
            sum += age[i]
            male += 1
        elif sex[i] == "F":
            sum_f += age[i]
            sum += age[i]
            female += 1
    avg = Decimal(sum/len(age))
    if male != 0:
        avg_m = Decimal(sum_m/male)
    else:
        avg_m = 0
    if female != 0:
        avg_f = Decimal(sum_f/female)
    else:
        avg_f = 0
    return avg,avg_m,avg_f

def get_inputs(age,sex):
    done = False
    while done != True:
        age,done = age_check(age)
    clear_screen()
    done = False
    while done != True:
        sex,done = sex_check(sex)
    clear_screen()
    return sex,age

if __name__ == "__main__":
    clear_screen()
    age,sex = [],[]
    for i in range(7):
        sex,age = get_inputs(age,sex)
    avg,m,f = averages(age,sex)
    print("Average age = %.2f Years\nAverage age (Men) = %.2f Years\nAverage age (Women) = %.2f Years\n" % (avg,m,f))
    #questão 18
    import os,math
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def get_num():
    getcontext().prec = 5
    done = False
    while done != True:
        try:
            l1 = input("Por favor insira o valor do carro:\n").split()
            num = Decimal(l1[0])
            if num <= 300:
                raise Exception()
        except:
            clear_screen()
            print("Valor invalido, por favor insira um numero maior que 300")
            done = False
        else:
            clear_screen()
            num = Decimal(l1[0])
            done = True
    return num

if __name__ == "__main__":
    clear_screen()
    getcontext().prec = 5
    num = get_num()
    print("Preço a vista: R$%.2f\nOpções de parcelamento:" % Decimal((num/10)*8))
    for i in range(1,11):
        juros = Decimal(1 + ((3/100) * i))
        parcela = Decimal((num*juros)/(i*6))
        print ("%dx R$%.2f" % ((i*6),parcela))

# floating point precision de 5 casas decimais utilizada para reduzir margem de erro.
#questão 19
import math,os
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

if __name__ == "__main__":
    clear_screen()
    getcontext().prec = 2
    done = False
    age = []
    while done != True:
        try:
            l1 = input("Por favor insira a idade ou digite 0 para terminar:\n").split()
            n = int(l1[0])
            if n < 0:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira um numero positivo ou nulo")
        else:
            if n == 0:
                done = True
            else:
                age.append(n)
            clear_screen()
    if len(age) == 0:
        print("Nenhum numero inserido portanto a media de idade é 0")
    else:
        sum = 0
        for i in range(len(age)):
            sum += age[i]
        avg = Decimal(sum/len(age))
        print("Média de idade: %.2f anos" % avg)
        #questão 20
        import math,os
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

if __name__ == "__main__":
    clear_screen()
    getcontext().prec = 2
    age = []
    done = False
    while done != True:
        try:
            l1 = input("Por favor insira um numero inteiro e positivo ou digite 0 para terminar:\n").split()
            n = int(l1[0])
            if n < 0:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira um numero inteiro e positivo")
        else:
            if n == 0:
                done = True
            else:
                age.append(n)
            clear_screen()
    age.sort()
    if len(age) != 0:
        low,high = age[0],age[-1]
    print("Valor mais baixo: %d\nValor mais alto: %d" % (low,high))
    #questão 21
    import math,os

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def get_num():
    done = False
    while done != True:
        try:
            l1 = input("Por favor insira um numero inteiro e positivo ou nulo:\n").split()
            num = int(l1[0])
            if num < 0:
                raise Exception()
        except:
            clear_screen()
            print("Erro, valor invalido:\n")
        else:
            done = True
    clear_screen()
    return num

def fatorial(num):
    result = 1
    if num != 0:
        for i in range(1,num+1):
            result *= i
    else:
        pass
    return result

def exit_prompt():
    done = False
    while done != True:
        try:
            l1 = input("Digite \"SIM\" para continuar ou digite \"NAO\" para terminar o programa\n").split()
            s = (l1[0].upper())[0:3]
            print(len(s))
            if (s != "SIM" and s != "NAO" and s != "NÃO"):
                raise Exception()
        except:
            clear_screen()
            print("Não consegui entender")
        else:
            if s == "SIM":
                return not(True)
            else:
                return not(False)

if __name__ == "__main__":
    clear_screen()
    done = False
    while done != True:
        clear_screen()
        num = get_num()
        result =  fatorial(num)
        print("%d! = %d" % (num,result))
        done = exit_prompt()
    clear_screen()
    #questão 22
    import math,os

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def age_check(age):
    try:
        n = int(input("Please insert your age:\n").strip())
        if n <= 0 or n >= 120:
            raise Exception()
    except:
        clear_screen()
        print("Please insert a number between 1 and 120\n")
        return age,False
    else:
        age.append(n)
        return age,True
    
def weight_check(weight):
    try:
        n = float(input("Please insert your weight:\n").strip())
        if math.floor(n) <= 0 or n >= 350:
            raise Exception()
    except:
        clear_screen()
        print("please insert a valid weight\nmust be between 1 and 350KG\n")
        return weight, False
    else:
        weight.append(n)
        return weight,True

def get_input(age,weight):
    clear_screen()
    done = False
    while done != True:
        age,done = age_check(age)
    clear_screen()
    done = False
    while done != True:
        weight,done = weight_check(weight)
    clear_screen()
    return age,weight

def groups(age,weight):
    results = [[0 for i in range(0)]for j in range(4)]
    for i in range(len(age)):
        if age[i] <= 10:
            results[0].append(weight[i])
        elif age[i] > 10 and age[i] <= 20:
            results[1].append(weight[i])
        elif age[i] > 20 and age[i] <= 30:
            results[2].append(weight[i])
        elif age[i] > 30:
            results[3].append(weight[i])
    return results

if __name__ == "__main__":
    clear_screen()
    age, weight = [],[]
    for i in range(5):
        age, weight = get_input(age,weight)
    results = groups(age,weight)
    strings = ["1 to 10 year(s) old","11 to 20 years old", "21 to 30 years old", "31 and older"]
    for i in range(len(results)):
        sum = 0
        for j in range(len(results[i])):
            sum += results[i][j]
        else:
            if len(results[i]) != 0:
                avg = (sum/len(results[i]))
            else:
                avg = 0
            print("Average weight in age group - %s: %.2f" % (strings[i],avg))
    #questão 23
    import os

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def age_check(age):
    try:
        n = int(input("Please insert your age:\n").strip())
        if n <= 0 or n >= 120:
            raise Exception()
    except:
        clear_screen()
        print("Please insert a number between 1 and 120\n")
        return age,False
    else:
        clear_screen()
        age.append(n)
        return age,True

def review_check(review):
    try:
        n = int(input("Please insert the score for the movie:\n1 - Regular\n2 - Good\n3 - Great\n").strip())
        match n:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case _:
                raise Exception
    except:
        clear_screen()
        print("Error, please input one of the values below\n")
        return review,False
    else:
        clear_screen()
        review.append(n)
        return review,True

def get_input(age,review):
    clear_screen()
    done = False
    while done != True:
        age,done = age_check(age)
    done = False
    while done != True:
        review,done = review_check(review)
    clear_screen()
    return age,review

def op_A(age,review):
    sum,count = 0,0
    for i in range(len(age)):
        if review[i] == 3:
            sum += age[i]
            count += 1
    avg = (sum/count)
    return avg

def op_B(review):
    count = 0
    for i in range(len(review)):
        if review[i] == 1:
            count += 1
    return count

def op_C(review):
    count = 0
    for i in range(len(review)):
        if review[i] == 2:
            count += 1
    percentage = ((count/len(review))*100)
    return percentage

def print_result(A,B,C):
    print("Average age of people who tought the movie was great: %.2f year(s) old" % A)
    print("People who tought the movie was regular: %d" % B)
    print("Percentage of people who tought the movie was good: %.2f%%" % C)

if __name__ == "__main__":
    clear_screen()
    age,review,n = [],[],15
    for i in range(n):
        age,review = get_input(age,review)
    A,B,C = op_A(age,review),op_B(review),op_C(review)
    print_result(A,B,C)
    #questão 24
    import os

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def sex_check(sex):
    try:
        ch = input("Type \'M\' for male or \'F\' for female:\n").strip()
        ch = ch[0].upper()
        if ch != 'M' and ch != 'F':
            raise Exception()
    except:
        clear_screen()
        print("Error, invalid input")
        return sex,False
    else:
        sex.append(ch)
        return sex,True

def answer_check(answer):
    try:
        ch = input("Did you like our new product?\nType \"Y\" for Yes or \"N\" for No\n").strip().upper()[0]
        if ch != "Y" and ch != "N":
            raise Exception()
    except:
        clear_screen()
        print("Error, please input one of the available options")
        return answer,False
    else:
        clear_screen()
        answer.append(ch)
        return answer,True
    
def get_inputs(sex,answer):
    done = False
    while done != True:
        sex,done = sex_check(sex)
    clear_screen()
    done = False
    while done != True:
        answer,done = answer_check(answer)
    clear_screen()
    return sex,answer

def op_A(answer):
    count = 0
    for i in range(len(answer)):
        if answer[i] == 'Y':
            count += 1
    return count

def op_B(answer):
    count = 0
    for i in range(len(answer)):
        if answer[i] == 'N':
            count += 1
    return count

def op_C(sex,answer):
    count = 0
    for i in range(len(answer)):
        if answer[i] == 'Y' and sex[i] == 'F':
            count += 1
    return count

def op_D(sex,answer):
    count = [0,0]
    for i in range(len(answer)):
        if sex[i] == 'M':
            if answer[i] == 'N':
                count[0] += 1
            count[1] += 1
    percentage = ((count[0]/count[1])*100)
    return percentage

def print_result(A,B,C,D):
    print("Answered \"Yes\": %d person(s)" % A)
    print("Answered \"No\": %d person(s)" % B)
    print("Amount of women who answered \"Yes\": %d" % C)
    print("Percentage of men who answered \"No\": %.2f%%" % D)

if __name__ == "__main__":
    sex,answer,n = [],[],5
    clear_screen()
    for i in range(n):
        sex,answer = get_inputs(sex,answer)
    A,B,C,D = op_A(answer),op_B(answer),op_C(sex,answer),op_D(sex,answer)
    print_result(A,B,C,D)
    #questão 25
    import os

class duplicate_registration(Exception):
    #exception triggered if registration value is a duplicate
    pass

#Global variable for names
sim_names = ["James","Kirk","Lars","Robert","Jason","Cliff","Dave","Gary","Tom","Scott","Becker","Steve","Yngwie","Zakk","Joe"]

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def get_score(score,i):
    n = 1
    while len(score[i]) != 3:
        try:
            x = int(input("please insert score #%d:\n" % n).strip())
            if x < 0 or x > 10:
                raise Exception()
        except:
            clear_screen()
            print("Error, please insert a number between 0 and 10")
        else:
            clear_screen()
            n += 1
            score[i].append(x)
            if score[i][0] == -1:
                del score[i][0]
    return score,True

def get_attendance(attendance):
    try:
        x = int(input("please insert the amount of lessons attended:\nNOTES: Max value is 120\n").strip())
        if x < 0 or x > 120:
            raise Exception()
    except:
        clear_screen()
        print("Error, please insert a number between 0 and 120")
        return attendance,False
    else:
        clear_screen()
        attendance.append(x)
        return attendance,True
    
def get_registration(registration):
    try:
        s = input("Please insert your registration number:\nNote:must contain 8 numbers\n").strip()
        if len(s) != 8:
            raise Exception()
        n = int(s)
        if len(registration) != 0:
            for i in range(len(registration)):
                if n == registration[i]:
                    raise duplicate_registration()
    except duplicate_registration:
        clear_screen()
        print("Error, this registration has already been inserted, please type a different registration")
        return registration,False
    except:
        clear_screen()
        print("Error, please insert a valid registration number")
        return registration,False
    else:
        clear_screen()
        registration.append(n)
        return registration,True

def get_input(n):
    attendance,registration = [],[]
    score = [[-1 for i in range(1)] for j in range(n)]
    for i in range(n):
        clear_screen()
        done = False
        while done != True:
            registration,done = get_registration(registration)
        clear_screen()
        done = False
        while done != True:
            score,done = get_score(score,i)
        clear_screen()
        done = False
        while done != True:
            attendance,done = get_attendance(attendance)
        clear_screen()
    return registration,score,attendance

def student_result(result,score,i):
    sum = 0
    for j in range(3):
        sum += score[i][j]
    avg = sum/3
    result.append(avg)
    return result

def extremes(result,registration):
    low = min(result)
    high = max(result)
    lowest = [i for i in range(len(result)) if result[i] == low]
    highest = [i for i in range(len(result)) if result[i] == high]
    return lowest,highest,low,high

def automated_inputs():
    #function used only during testing
    clear_screen()
    n = 15
    print("Automated inputs\nValues:")
    registration = [i for i in range(12345671,(12345671+n+1))]
    score = [[(j+5) for i in range(3)] for j in range(n) if j + 5 <= 10]
    while len(score) != n:
        for i in range(len(score),n):
            score.append([4,4,4])
    attendance = [i for i in range(40,(40+(n*10)),10) if i < 120]
    while len(attendance) != n:
        k = 50
        for i in range(len(attendance),n):
            attendance.append(k)
            k -= 3
    print(registration)
    print(attendance)
    print(score)
    print("Press enter")
    input()
    clear_screen()
    return registration,score,attendance,n
    #function used only during testing

def print_min_max(lowest,highest,low,high,registration):
    print("Lowest score: %d" % low)
    print("Student(s) with the lowest score:")
    for i in range(len(lowest)):
       print("Name: %s - Registration: %d" % (sim_names[lowest[i]],registration[lowest[i]]))
       if i == (len(lowest)-1):
        print()
    print("Highest score: %d" % high)
    print("Student(s) with the highest score:")
    for i in range(len(highest)):
        print("Name: %s - Registration: %d" % (sim_names[highest[i]],registration[highest[i]]))
        if i == (len(highest)-1):
            print()

def failed(result,attendance):
    count = [0,0,0,0]
    for i in range(len(result)):
        if attendance[i] < 40 and result[i] < 6:
            count[3] += 1
            count[2] += 1
        elif attendance[i] < 40:
            count[3] += 1
            count[1] += 1
        elif result[i] < 6:
            count[3] += 1
            count[0] += 1
    return count

def print_fails(count):
    print("Students who weren't approved: %d" % (count[3]))
    print("Students who weren't approved due to having both low scores and low attendance: %d" % (count[2]))
    print("Students who weren't approved due to low scores (and only low scores): %d" % (count[0]))
    print("Students who weren't approved due to low attendance (and only low attendance): %d" % (count[1]))

def print_student(registration,result,attendance):
    print("Students: \n")
    for i in range(len(result)):
        print("Registration: %d" % registration[i])
        print("Name: %s" % sim_names[i])
        if result[i] < 6 or attendance[i] < 40:
            print("Not approved")
        else:
            print("approved")
        if i != len(result)-1:
            print()

def print_everything(registration,result,attendance,lowest,highest,low,high,count):
    print_student(registration,result,attendance)
    print_min_max(lowest,highest,low,high,registration)
    print_fails(count)

if __name__ == "__main__":
    n = 3
    result = []
    op = 0
    #op = 1 #used only during testing
    if op == 0:
        registration,score,attendance = get_input(n)
    else:
        #sets automated values for the inputs, used to streamline testing
        registration,score,attendance,n = automated_inputs()
    for i in range(n):
        result = student_result(result,score,i)
    lowest,highest,low,high = extremes(result,registration)
    count = failed(result,attendance)
    print_everything(registration,result,attendance,lowest,highest,low,high,count)
#questão 26
import os
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def age_check(age):
    done = False
    i = 1
    while done == False:
        try:
            n = int(input("#%d Please insert your age:\nalternatively insert 0 to end\n" % i).strip())
            if n < 0 or n >= 120:
                raise Exception()
        except:
            clear_screen()
            print("Please insert a number between 1 and 120 or type 0 to end\n")
        else:
            clear_screen()
            i += 1
            if n == 0:
                return age
            else:
                age.append(n)

def average_calc(age):
    if len(age) == 0:
        return "No value"
    else:
        getcontext().prec = 2
        sum = 0
        for i in range(len(age)):
            sum += age[i]
        avg = "Media: " + str(Decimal(sum/len(age)))
        return avg

if __name__ == "__main__":
    clear_screen()
    age = []
    age = age_check(age)
    avg = average_calc(age)
    print(avg)
    #questão 27
    import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_channel():
    done,end = False, False
    while done != True:
        try:
            n = int(input("Insira o numero do canal:\nopcoes: 4,5,7,12\n"))
            match n:
                    case 0:
                        end = True
                    case 4:
                        n = 0
                    case 5:
                        n = 1
                    case 7:
                        n = 2
                    case 12:
                        n = 3
                    case _:
                        raise Exception()
        except:
            clear_screen()
            print("Erro, valor invalido")
        else:
            clear_screen()
            return n,end

def get_views(l1,pos):
    done,end = False,False
    while done != True:
        try:
            n = int(input("Insira o numero de espectadores:\n"))
            if n < 0:
                raise Exception()
            if n == 0:
                end = True
        except:
            clear_screen()
            print("Valor Invalido")
        else:
            clear_screen()
            l1[pos] += n
            return l1,end
        
def get_total(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

def get_percentages(arr,sum):
    percent = [0,0,0,0]
    for i in range(len(arr)):
        percent[i] = ((arr[i]/sum)*100)
    return percent

def print_results(percent):
    channels = [4,5,7,12]
    for i in range(len(percent)):
        print("Porcentagem de espectadores do canal %d: %.2f%%" % (channels[i],percent[i]))

if __name__ == "__main__":
    clear_screen()
    end = False
    arr = [0,0,0,0]
    while end != True:
        pos,end = get_channel()
        if end == True:
            break
        arr,end = get_views(arr,pos)
    sum = get_total(arr)
    if sum != 0:
        percent = get_percentages(arr,sum)
        print_results(percent)
    else:
        print("Nenhum espectador")
    #questão 28
    import os
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_salario(salario):
    global done
    while done != True:
        try:
            n = Decimal(input("Insira o valor do salário:\n"))
        except:
            clear_screen()
            print("valor invalido")
        else:
            break
    clear_screen()
    if n < 0:
        return salario,True
    else:
        salario.append(n)
        return salario,False


def get_filhos(filhos):
    global done
    while done != True:
        try:
            n = int(input("Insira o numero de filhos:\n"))
        except:
            clear_screen()
            print("valor invalido")
        else:
            break
    clear_screen()
    if n < 0:
        filhos.append(0)
        return filhos,True
    else:
        filhos.append(n)
        return filhos,False

def get_values(salario,filhos):
    global done
    done = False
    while done == False:
        salario,done = get_salario(salario)
        if done == True:
            break
        filhos,done = get_filhos(filhos)
    return salario,filhos

def highest_wage(salario):
    salario.sort(reverse=True)
    return("Maior salário: R$%.2f" % (salario[0]))

def avg_wage(salario):
    getcontext().prec = 2
    sum = Decimal(0)
    for i in range(len(salario)):
        sum += salario[i]
    avg = Decimal(sum/len(salario))
    return ("Média dos salários: R$%.2f" % avg)
    
def avg_filhos(filhos):
    getcontext().prec = 2
    sum = Decimal(0)
    for i in range(len(filhos)):
        sum += filhos[i]
    avg = Decimal(sum/len(filhos))
    return ("Média do numero de filhos: %.2f" % avg)

def percentage(salario):
    getcontext().prec = 2
    count = 0
    for i in salario:
        if i <= 150:
            count += 1
    percent = Decimal((count/len(salario))*100)
    return ("Porcentagem de pessoas com salário até R$150: %.2f%%" % percent)
    
if __name__ == "__main__":
    clear_screen()
    salario,filhos = [],[]
    salario,filhos = get_values(salario,filhos)
    if len(salario) == 0:
        print("Nenhum valor inserido")
        exit()
    print(avg_wage(salario))
    print(avg_filhos(filhos))
    print(highest_wage(salario))
    print(percentage(salario))
#questão 29
import os
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_salario(salario):
    global done
    while done != True:
        try:
            n = Decimal(input("Insira o valor do salário:\n"))
        except:
            clear_screen()
            print("valor invalido")
        else:
            break
    clear_screen()
    salario.append(n)
    return salario
    
def age_check(age):
    global done
    while done != True:
        try:
            n = int(input("Por favor insira sua idade:\n").strip())
            if n >= 120:
                raise Exception()
        except:
            clear_screen()
            print("Por favor insira uma idade até 120\n")
        else:
            break
    if n < 0:
        return age,True
    else:
        age.append(n)
        return age,False

def sex_check(sex):
    global done
    while done != True:  
        try:
            ch = input("Digite \'M\' para masculino ou \'F\' para feminino:\n").strip()
            ch = ch[0].upper()
            if ch != 'M' and ch != 'F':
                raise Exception()
        except:
            clear_screen()
            print("Erro, valor invalido")
        else:
            break
    sex.append(ch)
    return sex
    
def get_values():
    global done
    done = False
    age,sex,salario = [],[],[]
    while done != True:
        age,done = age_check(age)
        if done == True:
            break
        clear_screen()
        sex = sex_check(sex)
        clear_screen()
        salario = get_salario(salario)
    clear_screen()
    return age,sex,salario

def avg_wage(salario):
    getcontext().prec = 2
    sum = Decimal(0)
    for i in range(len(salario)):
        sum += salario[i]
    avg = Decimal(sum/len(salario))
    return ("Média dos salários: R$%.2f" % avg)

def extremes_age(age):
    min_val = min(age)
    max_val = max(age)
    return("Menor idade: %s\nMaior idade: %s" % (min_val,max_val))

def condition_C(salario,sex):
    count = 0
    for i in range(len(salario)):
        if salario[i] <= 200 and sex[i] == 'F':
            count += 1
    return("Numero de mulheres com o salário até R$200: %d" % count)

def condition_D(age,sex,salario):
    indexes = []
    print("\nDados referentes ao menor salário:")
    for i in range(len(salario)):
        if salario[i] == min(salario):
            indexes.append(i)
    for i in range(len(indexes)):
        if i > 0:
            print()
        print("Idade: %s" % age[indexes[i]])
        print("Sexo: %s" % sex[indexes[i]])
        print("Salario: %s" % sex[indexes[i]])
    print()

if __name__ == "__main__":
    clear_screen()
    age,sex,salario = get_values()
    print(avg_wage(salario))
    print(extremes_age(age))
    print(condition_C(salario,sex))
    condition_D(age,sex,salario)
    #questão 30
    import random,os,sys
from decimal import *

#NOTA PARA O PROFESSOR: SE O SENHOR QUISER FAZER OS TESTES MAIS RÁPIDO, BASTA APERTAR ENTER QUE ELE VAI ATRIBUIR UM VALOR ALEATORIO AO INPUT


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_price(og_price):
    try:
        n = float(input("Insira o preço do produto:\n"))
        if n < 0:
            raise Exception()
    except:
        clear_screen()
        n = float(random.randint(10,500)+(random.randint(0,99)/100))
        print("Erro, valor invalido, inserido valor aleatorio\nvalor inserido: R$%d\n" % n)
        og_price.append(n)
    else:
        clear_screen()
        og_price.append(n)
    return og_price

def get_code(code):
    try:
        n = int(input("Insira o codigo do produto:\n"))
    except:
        clear_screen()
        n = int(random.randint(1,9999))
        print("Erro, valor invalido, inserindo valor aleatorio\nvalor inserido: %d\n" % n)
        code.append(n)
        return code, False
    else:
        clear_screen()
        if n < 0:
            return code,True
        else:
            code.append(n)
            return code,False

def get_values():
    code,og_price = [],[]
    done = False
    while done != True:
        code,done = get_code(code)
        if done == True:
            break
        og_price = get_price(og_price)
    return code,og_price

def alter_prices(adjusted_price):
    for i in range(len(adjusted_price)):
        adjusted_price[i] *= 1.2
    return adjusted_price

def price_avgs(og_price,adjusted_price):
    getcontext().prec = 2
    sum = [0,0]
    for i in range(len(og_price)):
        sum[0] += og_price[i]
        sum[1] += adjusted_price[i]
    avg_og,avg_adj = Decimal(sum[0]/len(og_price)), Decimal(sum[1]/len(adjusted_price))
    print("Media dos preços originais: R$%.2f\nMedia dos preços ajustados (aumento de 20%%): R$%.2f" % (avg_og,avg_adj))

def print_values(code,og_price,adjusted_price):
    lengths = [0 for i in range(len(code))]
    for i in range(len(code)):
        print("Codigo do produto: %d\nPreço original: R$%.2f\nPreço ajustado: R$%.2f\n" % (code[i],og_price[i],adjusted_price[i]))

if __name__ == "__main__":
    clear_screen()
    code,og_price = get_values()
    if len(code) == 0:
        print("Nenhum valor inserido")
        sys.exit()
    else:
        adjusted_price = [x for x in og_price]
        adjusted_price = alter_prices(adjusted_price)
        print_values(code,og_price,adjusted_price)
        price_avgs(og_price,adjusted_price)
        #questão 31
        import random,os,string,sys
from decimal import *

#NOTA PARA O PROFESSOR: SE O SENHOR QUISER FAZER OS TESTES MAIS RÁPIDO, BASTA APERTAR ENTER QUE ELE VAI ATRIBUIR UM VALOR ALEATORIO AO INPUT


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_stock(stock):
    chars = list(string.ascii_uppercase)
    chars.remove("F")
    try:
        ch = (input("Insira a letra correspondente a ação, ou insira \'F\' para terminar\n").strip().upper())[0]
        if (ch.isalpha()) != True:
            raise Exception()
    except:
        clear_screen()
        ch = random.choice(chars)
        print("Erro, valor invalido! Valor aleatorio inserido: %c" % ch)
        stock.append(ch)
        return stock,False
    else:
        clear_screen()
        if ch == "F":
            return stock,True
        else:
            stock.append(ch)
            return stock,False

def get_prices(price_list,operation):
    try:
        n = float(input("Por favor insira o valor de %s da ação\n" % operation))
        if n <= 0:
            raise Exception()
    except:
        clear_screen()
        n = float(random.randint(1,1000)+(random.randint(0,99) % 100))
        print("Erro, valor invalido! Valor aleatorio inserido: %.2f" % n)
    else:
        clear_screen()
    price_list.append(n)
    return price_list

def get_values():
    stock,buy,sell = [],[],[]
    done = False
    while done != True:
        stock,done = get_stock(stock)
        if done == True:
            break
        buy = get_prices(buy,"compra")
        sell = get_prices(sell,"venda")
    return stock,buy,sell

def get_profit(stock,buy,sell):
    profit,count,total = [],[0,0], 0
    for i in range(len(stock)):
        val = sell[i]-buy[i]
        profit.append(val)
        if val < 200:
            count[0] += 1
        elif val > 1000:
            count[1] += 1
    for i in range(len(profit)):
        total += profit[i]
    return profit,count,total

def print_results(profit,count,total):
    for i in range(len(profit)):
        print("Lucro da ação numero %d: R$%.2f" % ((i+1),profit[i]))
    print("Total de ações com lucro abaixo de R$200: %d" % count[0])
    print("Total de ações com lucro acima de R$1000: %d" % count[1])
    print("Lucro total: %.2f" % total)

if __name__ == "__main__":
    clear_screen()
    stock,buy,sell = get_values()
    if len(stock) == 0:
        print("Nenhum valor inserido")
        sys.exit()
    else:
        profit,count,total = get_profit(stock,buy,sell)
        print_results(profit,count,total)
    #questão 32
    import os,random
from decimal import *

#NOTA PARA O PROFESSOR: SE O SENHOR QUISER FAZER OS TESTES MAIS RÁPIDO, BASTA APERTAR ENTER QUE ELE VAI ATRIBUIR UM VALOR ALEATORIO AO INPUT

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_input():
    nums,done = [],False
    while done != True:
        try:
            if len(nums) == 0:
                n = int(input("Insira um numero ou insira \'0\' para terminar\n"))
            else:
                n = int(input("Insira outro numero ou insira \'0\' para terminar\n"))
        except:
            clear_screen()
            n = random.randint(1,1000)
            nums.append(n)
            print("Erro, valor inserido invalido, inserindo valor aleatorio. Numero inserido: %d\n" % n)
        else:
            clear_screen()
            if n == 0:
                break
            else:
                nums.append(n)
    return nums

def op_A(nums):
    count = 0
    for i in nums:
        if i < 35:
            count += 1
    print("Quantidade de numeros menores que 35: %d" % count)

def op_B(nums):
    getcontext().prec = 2
    sum,count = 0,0
    for i in nums:
        if i > 0:
            sum += i
            count += 1
    if count == 0:
        print("Media dos numeros inteiros: 0")
    else:
        avg = Decimal(sum/count)
        print("Media dos numeros inteiros: %.2f" % avg)

def op_C(nums):
    count = 0
    getcontext().prec = 2
    for i in nums:
        if i >= 50 and i <= 100:
            count += 1
    res = Decimal((count/len(nums))*100)
    print("Porcentagem de numeros entre 50 e 100: %.2f%%" % (res))

def op_D(nums):
    count = [0,0]
    getcontext().prec = 2
    for i in nums:
        if i < 50:
            count[0] += 1
            if i >= 10 and i <= 20:
                count[1] += 1
    if count[0] == 0:
        print("Porcentagem de numeros menores que 50 que estão no intervalo [10,20]: 0%")
    else:
        res = Decimal((count[1]/count[0])*100)
        print("Porcentagem de numeros menores que 50 que estão no intervalo [10,20]: %.2f%%" % res)

if __name__ == "__main__":
    clear_screen()
    nums = get_input()
    if len(nums) == 0:
        print("Nenhum valor inserido")
    else:
        op_A(nums)
        op_B(nums)
        op_C(nums)
        op_D(nums)
#questão 33
import os,random,sys
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def menu_interaction():
    done = False
    while done != True:
        try:
            n = int(input("Menu de opções:\n1. Média aritmética\n2. Média ponderada\n3. Sair\nDigite a opção desejada\n"))
            match n:
                case 1|2|3:
                    clear_screen()
                    return n
                case _:
                    raise Exception()
        except:
            clear_screen()
            print("Erro, opção invalida\n")

def op_1():
    nums = []
    getcontext().prec = 2
    while len(nums) != 2:
        try:
            print("Média aritmética")
            n = int(input("Insira o %dº valor:\n" % (len(nums)+1)))
        except:
            clear_screen()
            print("Erro valor invalido\n")
        else:
            clear_screen()
            nums.append(n)
    avg = Decimal(sum(nums)/len(nums))
    print("Media aritmética dos numeros %d e %d: %.2f" % (nums[0],nums[1],avg))

def op_2():
    nums,weigth = [],[]
    getcontext().prec = 2
    while len(weigth) != 3:
        try:
            print("Média ponderada")
            if len(nums) == len(weigth):
                n = int(input("Insira o %dº valor:\n" % (len(nums)+1)))
                clear_screen()
                nums.append(n)
            else:
                x = float(input("Insira o %dº peso:\n" % (len(weigth)+1)))
                if x <= 0:
                    raise Exception()
                clear_screen()
                weigth.append(x)
        except:
            clear_screen()
            print("Erro valor invalido\n")
    for i in range(len(nums)):
        nums[i] *= weigth[i]
    avg = Decimal(sum(nums)/sum(weigth))
    print("Média ponderada dos numeros %d,%d e %d: %.2f" % (nums[0],nums[1],nums[2],avg))

if __name__ == "__main__":
    clear_screen()
    n = menu_interaction()
    match n:
        case 1:
            op_1()
        case 2:
            op_2()
        case 3:
            sys.exit()
#questão 34
import os,sys
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_input():
    votes = [0,0,0,0,0,0]
    done = False
    while done != True:
        try:
            for i in range(4):
                print("%d - Candidato %c" % (i+1,chr(65+i)))
            print("5 - Voto nulo\n6 - Voto em branco\n0 - Sair")
            n = int(input("Insira seu voto:\n"))
            match n:
                case 1|2|3|4|5|6: votes[n-1] += 1
                case 0: break
                case _: raise Exception()
            clear_screen()
        except:
            clear_screen()
            print("Valor invalido\n")
    clear_screen()
    return votes

def results(votes):
    print("Votos:")
    for i in range(4):
        print("Candidato %c: %d" % (chr(65+i),votes[i]))
    print("Branco: %d" % votes[4])
    print("Nulo: %d\n" % votes[5])

def percents(votes):
    getcontext().prec = 2
    p1 = Decimal((votes[4]/sum(votes))*100)
    p2 = Decimal((votes[5]/sum(votes))*100)
    print("Porcentagem de votos em branco: %.2f%%\nPorcentagem de votos nulos: %.2f%%\n" % (p1,p2))

if __name__ == "__main__":
    clear_screen()
    votes = get_input()
    if sum(votes) == 0:
        print("Nenhum voto")
        sys.exit()
    else:
        results(votes)
        percents(votes)
        pass
#questão 35
import os,sys

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_nums():
    done = False
    nums = []
    while done != True:
        try:
            n = int(input("Insira numeros positivos ou negativos.\nTotal de numeros inseridos: %d\n" % len(nums)))
            clear_screen()
            if n == 0:
                break
            else:
                nums.append(n)
        except:
            clear_screen()
            print("Erro, valor invalido\n")
    return nums

def results(nums):
    if len(nums) == 0:
        print("Nenhum numero inserido")
        sys.exit()
    pos = [x for x in nums if x > 0]
    neg = [x for x in nums if x < 0]
    s1,s2 = sum(pos),sum(neg)
    print("Soma dos numeros positivos: %d\nSoma dos numeros negativos: %d\nSoma dos numeros positivos e negativos: %d" % (s1,s2,(s1+s2)))

if __name__ == "__main__":
    clear_screen()
    nums = get_nums()
    results(nums)
#questão 36
import os,sys
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_age(age):
    try:
        n = int(input("Por favor digite sua idade, ou digite 0 para terminar\n"))
        clear_screen()
        if n <= 0:
            return age,True
        else:
            age.append(n)
            return age,False
    except:
        clear_screen()
        print("Erro, idade invalida\n")
        return age,False
    
def get_heigth(heigth):
    try:
        n = int(input("Por favor digite sua altura em cm\n"))
        clear_screen()
        if n <= 0 or n > 250:
            raise Exception()
        else:
            heigth.append(n)
            return heigth
    except:
        clear_screen()
        print("Erro, altura invalida\n")
        return heigth
    
def avg(age,heigth):
    x,count = 0,0
    for i in range(len(heigth)):
        if age[i] > 50:
            x += heigth[i]
            count += 1
    if count == 0:
        print("Nenhuma pessoa acima de 50 anos")
        sys.exit()
    else:
        getcontext().prec = 2
        avg = Decimal(x/count)
        print("Media de altura das pessoas com mais de 50 anos: %.2fcm" % avg)

def get_input():
    age,heigth = [],[]
    done = False
    while done != True:
        if len(age) == len(heigth):
            age,done = get_age(age)
            if done == True:
                break
        elif len(heigth) < len(age):
            heigth = get_heigth(heigth)
    return age,heigth

if __name__ == "__main__":
    clear_screen()
    age,heigth = get_input()
    avg(age,heigth)
#questão 37
import os,sys
from decimal import *

class divide_by_zero_exception(Exception):
    pass

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def menu_interaction():
    done = False
    while done != True:
        try:
            n = int(input("Menu de opções:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n0. Sair\nDigita a opção de sua escolha\n"))
            match n:
                case 1|2|3|4|0:
                    clear_screen()
                    return n
                case _:
                    raise Exception()
        except:
            clear_screen()
            print("Erro, opção invalida\n")

def get_nums(nums,op):
    while len(nums) != 2:
        try:
            n = int(input("Insira o %dº numero:\n" % (len(nums)+1)))
            if len(nums) == 1 and op == 4 and n == 0:
                raise divide_by_zero_exception()
            clear_screen()
            nums.append(n)
        except divide_by_zero_exception:
            clear_screen()
            print("Erro, impossivel dividir por zero, digite outro numero")
        except:
            clear_screen()
            print("Erro, valor invalido")
    return nums

def op_1():
    nums = []
    nums = get_nums(nums,1)
    print("Soma dos numeros %d e %d: %d" % (nums[0],nums[1],sum(nums)))

def op_2():
    nums = []
    nums = get_nums(nums,2)
    print("%d - %d: %d" % (nums[0],nums[1],(nums[0]-nums[1])))

def op_3():
    nums = []
    nums = get_nums(nums,3)
    print("%d multiplicado por %d: %d" % (nums[0],nums[1],(nums[0]*nums[1])))

def op_4():
    nums = []
    nums = get_nums(nums,4)
    getcontext().prec = 2
    div = Decimal(nums[0]/nums[1])
    if div == int(div):
        print("%d dividido por %d: %d" % (nums[0],nums[1],(div)))
    else:
        print("%d dividido por %d: %.2f" % (nums[0],nums[1],(div)))

def exit_prompt():
    done = False
    while done != True:
        try:
            ch = input("Digite \'SIM\' para continuar ou \'NÃO\' para terminar\n").strip().upper()
            match ch[:3]:
                case "SIM":
                    return False
                case "NÃO"|"NAO":
                    return True
                case _:
                    raise Exception()
        except:
            clear_screen()
            print("Erro, opção invalida\n")


if __name__ == "__main__":
    clear_screen()
    done = False
    while done != True:
        op = menu_interaction()
        clear_screen()
        match op:
            case 1: op_1()
            case 2: op_2()
            case 3: op_3()
            case 4: op_4()
            case 0: sys.exit()
        done = exit_prompt()
        clear_screen()
#questão 38
import os,sys
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def menu_interaction():
    done = False
    while done != True:
        try:
            n = int(input("Menu de opções:\n1. Novo Salário\n2. Férias\n3. Décimo terceiro\n4. Sair\nDigite a opção desejada\n"))
            match n:
                case 1|2|3|4:
                    return n
                case _:
                    raise Exception()
        except:
            clear_screen()
            print("Erro, valor invalido\n")

def get_salario():
    done = False
    while done != True:
        try:
            n = float(input("Insira o valor do salario:\n"))
            if n < 1:
                raise Exception()
            else:
                return n
        except:
            clear_screen()
            print("Erro, valor invalido\n")

def get_meses():
    done = False
    while done != True:
        try:
            n = int(input("Insira o numero de meses trabalhados:\n"))
            if n in range(1,13):
                return n
            else:
                raise Exception()
        except:
            clear_screen()
            print("Erro, valor invalido\n")

def op_1():
    getcontext().prec = 2
    salario = (get_salario())
    og_sal = salario
    if salario in range(1,350):
        salario = Decimal(salario*1.15)
    elif salario in range(350,601):
        salario = Decimal(salario*1.1)
    elif salario > 600:
        salario = Decimal(salario*1.05)
    print("Salario original: R$%.2f\nSalario novo: R$%.2f\n" % (og_sal,salario))

def op_2():
    getcontext().prec = 2
    salario = get_salario()
    ferias = Decimal(salario/3)
    print("Salario: R$%.2f\nFerias: R$%.2f\n" % (salario,ferias))

def op_3():
    salario = get_salario()
    meses = get_meses()
    decimo_terceiro = Decimal((salario*meses)/12)
    print("Salario: R$%.2f\nMeses trabalhados: R$%d\n13º: R$%.2f\n" % (salario,meses,decimo_terceiro))

def exit_prompt():
    done = False
    while done != True:
        try:
            s = input("Digite \"SIM\" para continuar ou \"NÃO\" para sair\n").strip().upper()
            match s[:3]:
                case "SIM": return False
                case "NAO"|"NÃO": return True
        except:
            clear_screen()
            print("Erro, valor invalido\n")

if __name__ == "__main__":
    done = False
    while done != True:
        clear_screen()
        op = menu_interaction()
        clear_screen()
        match op:
            case 1: op_1()
            case 2: op_2()
            case 3: op_3()
            case 4: sys.exit()
        done = exit_prompt()
#questão 39
import os,sys,multiprocessing
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_codigo(codigo):
    done = False
    while done != True:
        try:
            n = int(input("Insira o codigo do cliente:\n"))
            clear_screen()
            if n <= 0:
                return codigo,True
            else:
                codigo.append(n)
                return codigo,False
        except:
            clear_screen()
            print("Erro, valor invalido\n")

def get_tipo(tipo):
    done = False
    while done != True:
        try:
            n = int(input("Insira o tipo da conta:\n1. Poupança\n2. Poupança Plus\n3. Fundos de renda fixa\n"))
            match n:
                case 1|2|3:
                    clear_screen()
                    tipo.append(n)
                    return tipo
                case _: raise Exception()
        except:
            clear_screen()
            print("Erro, valor invalido\n")    

def get_investimento(investimento):
    done = False
    while done != True:
        try:
            n = float(input("Insira o valor do investimento:\n"))
            if n <= 0:
                raise Exception()
            else:
                investimento.append(n)
                return investimento
        except:
            clear_screen()
            print("Erro, valor invalido\n")

def get_values():
    done = False
    codigo,tipo,investimento = [],[],[]
    while done != True:
        codigo,done = get_codigo(codigo)
        if done == True:
            break
        tipo = get_tipo(tipo)
        investimento = get_investimento(investimento)
        clear_screen()
    return codigo,tipo,investimento

def total_value(investimento):
    print("Valor total investido: %.2f" % sum(investimento))

def juros(tipo,investimento):
    for i in len(investimento):
        match tipo[i]:
            case 1: investimento[i] *= (1*(15/1000))
            case 2: investimento[i] *= (1*(2/100))
            case 3: investimento[i] *= (1*(4/100))
    print("Juros: %.2f" % (sum(investimento)))

if __name__ == "__main__":
    clear_screen()
    codigo,tipo,investimento = get_values()
    proc = multiprocessing.Process(target=total_value,args=(investimento, ))
    proc2 = multiprocessing.Process(target=juros,args = (tipo,investimento, ))
    proc.start()
    proc2.start()
    proc2.join()
