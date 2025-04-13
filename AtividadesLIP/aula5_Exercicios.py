import locale
import math
import time
import os
import pyautogui as gui

locale.setlocale(locale.LC_NUMERIC, 'pt-BR.UTF-8')

'''
Exercício 1:
Escreva um programa em python que leia dois números decimais, leia a operação desejada 
dentre adição, subtração, multiplicação ou divisão e mostre o seu resultado com duas casas 
decimais. Não permita a possibilidade do sistema tentar calcular uma divisão por zero ou a
leitura de caracteres que não possam ser números.
'''
'''
tentativa = 3
loop = 0

while True:
    if loop == 0:
        try:
            num_1 = input("Digite um número que contenha decimais: ")
            num_2 = input("Digite outro número que contenha decimais: ")
            num_1 = num_1.replace(',','.')
            num_2 = num_2.replace(',', '.')
            num_1 = float(num_1)
            num_2 = float(num_2)

            oper = input("Digite uma das seguintes operações matemáticas: +, -, * ou /: ")
            match oper:
                case "+":
                    soma = num_1 + num_2
                    soma_form = locale.format_string("%.2f", soma, grouping=True)
                    print("o resultado da adição é, aproximadamente: {}".format(soma_form))
                case "-":
                    sub = num_1 - num_2
                    sub_form = locale.format_string("%.2f", sub, grouping=True)
                    print("o resultado da subtração é, aproximadamente: {}".format(sub_form))
                case "*":
                    mult = num_1 * num_2
                    mult_form = locale.format_string("%.2f", mult, grouping=True)
                    print("o resultado da multiplicação é, aproximadamente: {}".format(mult_form))
                case "/":
                    div = num_1 / num_2
                    div_form = locale.format_string("%.2f", div, grouping=True)
                    print("o resultado da divisão é, aproximadamente: {}".format(div_form))
                case _:
                    print("Este tipo de operação não existe")
            loop = 1

        except ValueError:
            if tentativa > 1:
                tentativa -= 1
                print("\nValor inválido! Por favor, digite os valores corretamente")
                print("Você tem mais {} tentativa(s)\n".format(tentativa))
            else:
                print("\nO número de tentativas foi excedido. O programa foi encerrado")
                break

        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário")
            break

    else:
        try:
            repetir_prog = int(input("\nDeseja repetir o processo? Digite '1' para confirmar ou qualquer outro para encerrar o programa: "))
            if repetir_prog == 1:
                tentativa = 3
                loop = 0
            else:
                print("\nO programa foi encerrado")
                break
        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break
'''
'''
Exercício 2:
Escreva um programa em python para calcular os valores de imc a partir de entradas de 
dados específicos como peso e altura da pessoa. Não permita a entrada de valores que não 
possam ser números. O sistema deve trazer o resultado escrito do IMC e não o cálculo.
Não permita que o usuário entre com valores que não possam ser números
IMC = Peso[kg] ÷ (Altura²[m]) 
baixo peso < 18,5
18,5 >= peso normal < 25
25 >= pre obesidade < 30
30 >= obesidade grau 1 < 35
35 >= obesidade grau 2 < 40 
obesidade mórbida >= 40
'''
'''
tentativa = 3
loop = 0

while True:
    if loop == 0:
        try:
            peso = input("Digite o valor aproximado do seu peso em kg: ")
            altura = input("Digite o valor aproximado de sua altura em m: ")
            peso = peso.replace(',','.')
            altura = altura.replace(',','.')
            peso = float(peso)
            altura = float(altura)

            IMC = peso / altura**2
            IMC_form = locale.format_string("%.2f", IMC)

            if IMC < 18.5:
                print("Seu IMC é de {}. CUIDADO!!! Você está abaixo do peso normal".format(IMC_form))
            elif 18.5 <= IMC < 25:
                print("Seu IMC é de {}. Você está com o peso saudável".format(IMC_form))
            elif 25 <= IMC < 30:
                print("Seu IMC é de {}. CUIDADO!!! Você está na faixa de pré-obesidade".format(IMC_form))
            elif 30 <= IMC < 35:
                print("Seu IMC é de {}. CUIDADO!!! Você está na faixa de obesidade grau I".format(IMC_form))
            elif 35 <= IMC < 40:
                print("Seu IMC é de {}. CUIDADO!!! Você está na faixa de obesidade grau II".format(IMC_form))
            elif IMC >= 40:
                print("Seu IMC é de {}. CUIDADO!!! Você está na faixa de obesidade mórbida".format(IMC_form))
            loop = 1

        except ValueError:
            if tentativa > 1:
                tentativa -= 1
                print("\nValor inválido! Por favor, digite os valores corretamente")
                print("Você tem mais {} tentativa(s)\n".format(tentativa))
            else:
                print("\nO número de tentativas foi excedido. O programa foi encerrado")
                break

        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário")
            break

    else:
        try:
            repetir_prog = int(input("\nDeseja repetir o processo? Digite '1' para confirmar ou qualquer outro para encerrar o programa: "))
            if repetir_prog == 1:
                tentativa = 3
                loop = 0
            else:
                print("\nO programa foi encerrado")
                break
        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break
'''
'''
Exercício 3:
Calcule um polinômio do segundo grau através da fórmula de bhaskara ax²+ bx + c. Não 
permita o sistema tentar calcular divisão por zero, raiz negativa ou entrada de valores 
que não sejam números. Mostrar quantas raízes o sistema deve gerar: nenhuma(se for numero
complexo com raiz negativa, uma ou duas) e seus valores sempre com duas casas decimais.
'''
'''
tentativa = 3
loop = 0

while True:
    if loop == 0
        try:
            a = float(input("Defina um valor para 'a': "))
            b = float(input("Defina um valor para 'b': "))
            c = float(input("Defina um valor para 'c': "))

            if a == 0:
                print("A equação não pode ser realizada pois o divisor é zero!")
                continue

            delta = (b ** 2) - (4 * a * c)
            delta_form = locale.format_string("%.2f", delta)

            if delta < 0:
                print("Há raízes negativas nessa operação. Tente novamente com outros valores.")
                continue

            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x1_form = locale.format_string("%.2f", x1)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            x2_form = locale.format_string("%.2f", x2)

            print("O delta é aproximadamente: {}".format(delta_form))
            print("As raízes do polinômio são aproximadamente:\n x1 = {}\n x2 = {}".format(x1_form, x2_form))
            loop = 1

        except ValueError:
            if tentativa > 1:
                tentativa -= 1
                print("\nValor inválido! Por favor, digite os valores corretamente")
                print("Você tem mais {} tentativa(s)\n".format(tentativa))
            else:
                print("\nO número de tentativas foi excedido. O programa foi encerrado")
                break

        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break

    else:
        try:
            repetir_prog = int(input("\nDeseja repetir o processo? Digite '1' para confirmar ou qualquer outro para encerrar o programa: "))
            if repetir_prog == 1:
                tentativa = 3
                loop = 0
            else:
                print("\nO programa foi encerrado")
                break
        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break
'''
'''
Exercício 4:
 O software deve permitir a leitura de um código cifrado (protocolo) que contenha 10 caracteres,
de uma estação meteorológica, a principio esse código deve trazer os seguintes dados:
zona de medição = 02 caracteres ==> 01 sul 02 norte 03 leste 04 oeste
temperatura     = 04 caracteres ==> 0321 ==> temperatura + 32,1ºC ou 1321 temperatura -32,1ºC
pluviometria    = 04 caracteres ==> 0400 ==> índice pluviométrico 400mm 
Exemplo se o código recebido for 0402980010 seu software deve decodificar a seguinte informação:
Campinas, região: Norte,  Temperatura: 29,8ºC, Índice pluviométrico:10mm 
Não permita que seja digitado um código de menos de 10 caracteres e que não seja um numero
decimal
'''
'''
tentativa = 3
loop = 0
while True:
    if loop == 0:
        try:
            protocolo = input("Digite o número do protocolo (10 dígitos): ")
            if not protocolo.isdigit or (protocolo) != 10:
                print("")
                loop = 1

            if loop == 0:
                zona_cod = protocolo[:2]
                temp_cod = protocolo[2:6]
                chuva_cod = protocolo[6:]

                if zona_cod == "01":
                    zona = "sul"
                elif zona_cod == "02":
                    zona = "norte"
                elif zona_cod == "03":
                    zona = "leste"
                elif zona_cod == "04":
                    zona = "oeste"

                if temp_cod[0] == "1":
                    sinal = "- "
                elif temp_cod[0] == "0":
                    sinal = "+ "

                temp = f"{sinal}{int(temp_cod[1:]) / 10:.1f} ºC"
                temp = temp.replace('.',',')
                chuva = f"{int(chuva_cod)} mm"

                print("\nA zona a qual foram obtidas as medições foi: Zona {}".format(zona))
                print("\nA temperatura medida foi de: {}".format(temp))
                print("\nA precipitação medida foi de: {}".format(chuva))
                loop = 2

        except (NameError, IndexError):
            if tentativa > 1:
                tentativa -= 1
                print("Protocolo inválido! Por favor, digite os valores corretamente")
                print("Você tem mais {} tentativa(s)\n".format(tentativa))
            else:
                print("O número de tentativas foi excedido. O programa foi encerrado")
                break

        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break
    elif loop == 1:
        if tentativa > 1:
            tentativa -= 1
            print("Protocolo inválido! O protocolo deve conter exclusivamente 10 dígitos inteiros")
            print("Você tem mais {} tentativa(s)\n".format(tentativa))
            loop = 0
        else:
            print("O número de tentativas foi excedido. O programa foi encerrado")
            break

    elif loop == 2:
        try:
            repetir_prog = int(input("\nDeseja repetir o processo? Digite '1' para confirmar ou qualquer outro para encerrar o programa: "))
            if repetir_prog == 1:
                tentativa = 3
                loop = 0
            else:
                print("\nO programa foi encerrado")
                break
        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break
'''
'''
Exercício 5
5) Escreva um programa para aprovar  o empréstimo bancário para compra de uma casa. O programa
deve perguntar o valor da casa, o salário, e a quantidade de anos a pagar. O valor da prestação 
mensal não pode ser maior que 30% do salario. Calcule o valor da prestação como sendo o valor 
da casa dividido pelo numero de meses a pagar. Não permita o empréstimo se a condição citada 
não for atendida. 
Não permita a entrada de valores que não sejam números.
'''
'''
tentativa = 3
loop = 0

while True:
    if loop == 0:
        try:
            valor_casa = float(input("Digite o valor da casa a ser pago: R$ "))
            valor_salario = float(input("Digite o valor do salário mensal: R$ "))
            anos_pagar = int(input("Digite a quantidade de anos à pagar a casa: "))

            valor_salario_form = locale.format_string("%.2f", valor_salario)
            valor_casa_form = locale.format_string("%.2f", valor_casa)

            num_prestacoes = anos_pagar * 12
            valor_prestacao = valor_casa / num_prestacoes
            lim_valor_prestacao = valor_salario - ((valor_salario * 30) / 100)

            valor_prestacao_form = locale.format_string("%.2f", valor_prestacao)
            lim_valor_prestacao_form = locale.format_string("%.2f", lim_valor_prestacao)

            if valor_prestacao > lim_valor_prestacao:
                print("O empréstimo não pode ser realizado pois a prestação mensal é maior do que 30% do salário")
                print("O valor da prestação é de R$ {}".format(valor_prestacao_form))
                print("O valor equivalente a 30% do salário é R$ {}".format(lim_valor_prestacao_form))
            else:
                print("O empréstimo pode ser realizado")
                print("O valor da prestação é de R$ {}".format(valor_prestacao_form))
                print("O valor equivalente a 30% do salário é R$ {}".format(lim_valor_prestacao_form))
            loop = 1

        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break

        except ValueError:
            if tentativa > 1:
                tentativa -= 1
                print("\nValor inválido! Por favor, digite os valores corretamente")
                print("Você tem mais {} tentativa(s)\n".format(tentativa))
            else:
                print("\nO número de tentativas foi excedido. O programa foi encerrado")
                break

    else:
        try:
            repetir_prog = int(input("\nDeseja repetir o processo? Digite '1' para confirmar ou qualquer outro para encerrar o programa: "))
            if repetir_prog == 1:
                tentativa = 3
                loop = 0
            else:
                print("\nO programa foi encerrado")
                break
        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break
'''

'''
Exercicio 6 ==> Faça o usuário entrar com dois valores valor mínimo e valor máximo
O seu algoritmo deverá decidir se a contagem que será feita é crescente ou decrescente que será mostrada ao usuário,
se o 1 º numero digitado for maior que o 2 º então a contagem é decrescente e se
acontecer o contrário, crescente
'''
'''
tentativa = 3
loop = 0
while True:
    if loop == 0:
        try:
            var_1 = int(input("Digite um valor para a 1ª variável: "))
            var_2 = int(input("Digite um valor para a 2ª variável: "))
            if var_1 > var_2:
                print("\nA contagem será decrescente de {} a {}".format(var_1, var_2))
                for num in range(var_1, var_2, -1):
                    print(num, "- ", end="")
                    time.sleep(.8)
                print(var_2)
            elif var_1 < var_2:
                print("\nA contagem será crescente de {} a {}".format(var_1, var_2))
                for num in range(var_1, var_2, 1):
                    print(num, "- ", end="")
                    time.sleep(.8)
                print(var_2)
            else:
                print("\nOs valores digitados são iguais")
            loop = 1
        except KeyboardInterrupt:
            gui.hotkey('shift', 'c')
            print("\n\nO programa foi interrompido pelo usuário!")
            break
        except ValueError:
            if tentativa > 1:
                tentativa -= 1
                print("\nValor inválido! Por favor, digite apenas números inteiros")
                print("Você tem mais {} tentativa(s)\n".format(tentativa))
            else:
                gui.hotkey('shift', 'c')
                print("\nO número de tentativas foi excedido. O programa foi encerrado")
                break
    else:
        try:
            repetir_prog = int(input("\nDeseja repetir o processo? Digite '1' para confirmar ou qualquer outro para encerrar o programa: "))
            if repetir_prog == 1:
                tentativa = 3
                loop = 0
            else:
                print("\nO programa foi encerrado")
                break
        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break
'''

'''
Exercicio 7 ==> Faça um algoritmo que leia 4 números inteiros e através de uma 
rotina de repetição e decisão se consiga mostrar na tela os números organizados de forma 
crescente. Por enquanto não usar listas, conjuntos ou vetores, usar decisões e 
repetições somente pra resolver essa questão.
'''
''' 
tentativa = 3
loop = 0
while True:
    if loop == 0:
        try:
            num_1 = int(input("Declare o 1º numero: "))
            num_2 = int(input("Declare o 2º numero: "))
            num_3 = int(input("Declare o 3º numero: "))
            num_4 = int(input("Declare o 4º numero: "))
            while not num_1 <= num_2 <= num_3 <= num_4:
                if num_1 > num_2:
                    num_1, num_2 = num_2, num_1
                if num_2 > num_3:
                    num_2, num_3 = num_3, num_2
                if num_3 > num_4:
                    num_3, num_4 = num_4, num_3
            print("Os números digitados serão dispostos a seguir em ordem crescente:\n")
            time.sleep(.8)
            print(num_1, end=" - ", flush=True)
            time.sleep(.8)
            print(num_2, end=" - ", flush=True)
            time.sleep(.8)
            print(num_3, end=" - ", flush=True)
            time.sleep(.8)
            print(num_4)
            loop = 1
        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break
        except ValueError:
            if tentativa > 1:
                tentativa -= 1
                print("\nValor inválido! Por favor, digite apenas números inteiros")
                print("Você tem mais {} tentativa(s)\n".format(tentativa))
                time.sleep(3)
                os.system('cls')
            else:
                os.system('cls')
                print("\nO número de tentativas foi excedido. O programa foi encerrado")
                break
    else:
        try:
            repetir_prog = int(input("\nDeseja repetir o processo? Digite '1' para confirmar ou qualquer outro para encerrar o programa: "))
            if repetir_prog == 1:
                tentativa = 3
                loop = 0
                os.system('cls')
            else:
                os.system('cls')
                print("\nO programa foi encerrado")
                break
        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break
'''
'''
Exercício 8 ==> Repita o exercício, porém agora o usuário pode escolher se
organizado de forma crescente ou decrescente
'''
'''  
tentativa = 3
loop = 0
while True:
    if loop == 0:
        try:
            num_1 = int(input("Declare o 1º numero: "))
            num_2 = int(input("Declare o 2º numero: "))
            num_3 = int(input("Declare o 3º numero: "))
            num_4 = int(input("Declare o 4º numero: "))
            while not num_4 <= num_3 <= num_2 <= num_1:
                if num_4 > num_3:
                    num_3, num_4 = num_4, num_3
                if num_3 > num_2:
                    num_2, num_3 = num_3, num_2
                if num_2 > num_1:
                    num_1, num_2 = num_2, num_1
            print("Os números digitados serão dispostos a seguir em ordem decrescente:\n")
            time.sleep(.8)
            print(num_1, end=" - ", flush=True)
            time.sleep(.8)
            print(num_2, end=" - ", flush=True)
            time.sleep(.8)
            print(num_3, end=" - ", flush=True)
            time.sleep(.8)
            print(num_4)
            loop = 1
        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break
        except ValueError:
            if tentativa > 1:
                tentativa -= 1
                print("\nValor inválido! Por favor, digite apenas números inteiros")
                print("Você tem mais {} tentativa(s)\n".format(tentativa))
                time.sleep(3)
                os.system('cls')
            else:
                os.system('cls')
                print("\nO número de tentativas foi excedido. O programa foi encerrado")
                break
    else:
        try:
            repetir_prog = int(input("\nDeseja repetir o processo? Digite '1' para confirmar ou qualquer outro para encerrar o programa: "))
            if repetir_prog == 1:
                tentativa = 3
                loop = 0
                os.system('cls')
            else:
                os.system('cls')
                print("\nO programa foi encerrado")
                break
        except KeyboardInterrupt:
            print("\n\nO programa foi interrompido pelo usuário!")
            break
'''
'''          
Exercício 9 ==> Faça um contador de minutos e segundos com 02 casas decimais de
formatação se assemelhando ao mostrador de um relógio XX:XX. O programa deve durar 
1 minuto e os segundos do dia de seu aniversário. Pesquise uma forma de apagar o 
console através de comando no interpretador python para que funcione da seguinte 
forma:
00:00 ==> 1 segundo ==> apaga ==> 00:01 ==> 1 segundo ==> apaga ==> 00:02 ...
'''
tentativa = 3
loop = 0
while True:
    if loop == 0:
        try:
            dia = int(input("Digite o número do dia de seu aniversário: "))
            if 0 < dia <= 31:
                cont = 60 + dia
                for i in range(cont):
                    min = i // 60
                    seg = i % 60
                    time.sleep(1)
                    os.system('cls')
                    print("O contador irá parar com 1 minuto e o dia de seu aniversário:\n")
                    print(f"{min:02}:{seg:02}")
                print(f"{min}:{dia}")
                loop = 1
            else:
                if tentativa > 1:
                    tentativa -= 1
                    print("\nO número do dia não existe! Por favor, digite um dia válido")
                    print("Você tem mais {} tentativa(s)\n".format(tentativa))
                    time.sleep(3)
                    os.system('cls')
                else:
                    os.system('cls')
                    print("\nO número de tentativas foi excedido. O programa foi encerrado")
                    break

        except KeyboardInterrupt:
            print("\nO programa foi interrompido pelo usuário!")
            break
        except ValueError:
            if tentativa > 1:
                tentativa -= 1
                print("\nValor inválido! Por favor, digite apenas números inteiros")
                print("Você tem mais {} tentativa(s)\n".format(tentativa))
                time.sleep(3)
                os.system('cls')
            else:
                os.system('cls')
                print("\nO número de tentativas foi excedido. O programa foi encerrado")
                break
    else:
        try:
            repetir_prog = int(input("\nDeseja repetir o processo? Digite '1' para confirmar ou qualquer outro para encerrar o programa: "))
            if repetir_prog == 1:
                tentativa = 3
                loop = 0
                os.system('cls')
            else:
                os.system('cls')
                print("O programa foi encerrado")
                break
        except KeyboardInterrupt:
            os.system('cls')
            print("O programa foi interrompido pelo usuário!")
            break