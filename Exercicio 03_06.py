''' =======================================
ESAMC -  Faculdade de Sorocaba
Programa feito para a atividade do Chico. (Versão 3.0)
Disciplina 	: Lógica de Programação e Algoritmos
Professor	: Francisco Tesifom Munhoz
Data	: 1º semestre de 2020
===========================================
Atividade	: Exercício 05
Autor	: João Marcelo Gerenutti
Data	: 03/06/2020
Comentários	: "Deseja-se fazer uma pesquisa a respeito do consumo mensal de energia elétrica em uma determinada cidade.
 Para isso são obtidos os seguintes dados de vários consumidores numa entrevista:
quantidade de kWh consumidos durante o mês;
código do tipo de consumidor (residencial, comercial, industrial).
Para finalizar: digitar quantidade = 5312 e codigo = 5312.

Calcular:

o menor e o maior consumo de consumidor residencial.
o maior consumo dos consumidores comerciais e industriais;
o total de consumo para cada um dos tipos de consumidores;
a média geral de consumo industrial;"
============================================
'''

# DECLARAÇÂO DE VARIAVEL
contador_residencia = 0

quantidade_industrial = 0

kwh = 0
tipo_consumidor = 0

maior_residencial = 0
menor_residencial = 10000000000000000000000000000

menor_residencial_temporario = int

maior_comercial = 0

maior_industrial = 0

total_residencial = 0
total_comercial = 0
total_industrial = 0

total_geral = 0

# PROCESSAMENTO DE DADOS
while kwh != 5312 and tipo_consumidor != 5312:

    # SAIDA DE DADOS
    print("Para finalizar el programa: digitar quantidade = 5312 e codigo = 5312.")
    print("---------------------------------------------------------------------")

    # ENTRADA DE DADOS
    kwh = int(input("Digite a quantidade de kWh consumidos durante o mês: "))
    tipo_consumidor = (input("Digite o código do tipo de consumidor: (R)residencial, (C)comercial, (I)industrial: "))

    # PROCESAMIENTO DE DADOS
    if tipo_consumidor == "R" and kwh != 0:
        contador_residencia = contador_residencia + 1

        total_residencial = total_residencial + kwh

        menor_residencial_temporario = kwh

        if menor_residencial_temporario < menor_residencial:
            menor_residencial = menor_residencial_temporario

        if kwh > maior_residencial:
            maior_residencial = kwh

    elif tipo_consumidor == "C":
        total_comercial = total_comercial + kwh

        if kwh > maior_comercial:
            maior_comercial = kwh

    elif tipo_consumidor == "I":
        total_industrial = total_industrial + kwh

        quantidade_industrial = quantidade_industrial + 1

        if kwh > maior_industrial:
            maior_industrial = kwh

    else:
        # SALIDA DE DADOS
        print("Tipo do consumidor inválido! Listas dos já inseridos: ")

    # PROCESAMIENTO DE DADOS
    total_geral = total_geral + kwh

    # SALIDA DE DADOS
    print("---------------------------------------------------------------------")
    print("O maior consumo residencial: ", maior_residencial)

    # PROCESSAMENTO DE DADOS
    if contador_residencia >= 2:
        # SAIDA DE DADOS
        print("O menor consumo residencial: ", menor_residencial)
    else:
        # SAIDA DE DADOS
        print("O menor consumo residencial: 0 ")

    # SALIDA DE DADOS
    print("---------------------------------------------")
    print("O maior consumo comercial: ", maior_comercial)
    print("---------------------------------------------")
    print("O maior consumo industrial: ", maior_industrial)
    print("---------------------------------------------")
    print("O total de consumo residencial: ", total_residencial)
    print("O total de consumo comercial: ", total_comercial)
    print("O total de consumo industrial: ", total_industrial)
    print("---------------------------------------------------------------------")

# PROCESAMIENTO DE DATOS
if quantidade_industrial != 0:
    media_industrial = (total_industrial/quantidade_industrial)

    # SAIDA DE DADOS
    print("Media geral do consumo industrial: %.1f" % media_industrial)
    print("---------------------------------------------------------------------")
else:
    # SAIDA DE DADOS
    print("Impossivel calcular a média geral do consumo industrial!")
    print("---------------------------------------------------------------------")