from random import randint
from time import sleep

class carta:
    valor = 0
    naipe = ''
    simbolo = ''

asPaus = carta()
asPaus.valor = 14
asPaus.naipe = 'Paus'
asPaus.simbolo = 'A'

asCopas = carta()
asCopas.valor = 14
asCopas.naipe = 'Copas'
asCopas.simbolo = 'A'

asEspadas = carta()
asEspadas.valor = 14
asEspadas.naipe = 'Espadas'
asEspadas.simbolo = 'A'

asOuro = carta()
asOuro.valor = 14
asOuro.naipe = 'Ouro'
asOuro.simbolo = 'A'

reiPaus = carta()
reiPaus.valor = 13
reiPaus.naipe = 'Paus'
reiPaus.simbolo = 'K'

reiCopas = carta()
reiCopas.valor = 13
reiCopas.naipe = 'Copas'
reiCopas.simbolo = 'K'

reiEspadas = carta()
reiEspadas.valor = 13
reiEspadas.naipe = 'Espadas'
reiEspadas.simbolo = 'K'

reiOuro = carta()
reiOuro.valor = 13
reiOuro.naipe = 'Ouro'
reiOuro.simbolo = 'K'

damaPaus = carta()
damaPaus.valor = 11
damaPaus.naipe = 'Paus'
damaPaus.simbolo = 'Q'

damaCopas = carta()
damaCopas.valor = 12
damaCopas.naipe = 'Copas'
damaCopas.simbolo = 'Q'

damaEspadas = carta()
damaEspadas.valor = 12
damaEspadas.naipe = 'Espadas'
damaEspadas.simbolo = 'Q'

damaOuro = carta()
damaOuro.valor = 12
damaOuro.naipe = 'Ouro'
damaOuro.simbolo = 'Q'

valetePaus = carta()
valetePaus.valor = 11
valetePaus.naipe = 'Paus'
valetePaus.simbolo = 'J'

valeteCopas = carta()
valeteCopas.valor = 11
valeteCopas.naipe = 'Copas'
valeteCopas.simbolo = 'J'

valeteEspadas = carta()
valeteEspadas.valor = 11
valeteEspadas.naipe = 'Espadas'
valeteEspadas.simbolo = 'J'

valeteOuro = carta()
valeteOuro.valor = 11
valeteOuro.naipe = 'Ouro'
valeteOuro.simbolo = 'J'

dezPaus = carta()
dezPaus.valor = 10
dezPaus.naipe = 'Paus'
dezPaus.simbolo = '10'

dezCopas = carta()
dezCopas.valor = 10
dezCopas.naipe = 'Copas'
dezCopas.simbolo = '10'

dezEspadas = carta()
dezEspadas.valor = 10
dezEspadas.naipe = 'Espadas'
dezEspadas.simbolo = '10'

dezOuro = carta()
dezOuro.valor = 10
dezOuro.naipe = 'Ouro'
dezOuro.simbolo = '10'

novePaus = carta()
novePaus.valor = 9
novePaus.naipe = 'Paus'
novePaus.simbolo = '9'

noveCopas = carta()
noveCopas.valor = 9
noveCopas.naipe = 'Copas'
noveCopas.simbolo = '9'

noveEspadas = carta()
noveEspadas.valor = 9
noveEspadas.naipe = 'Espadas'
noveEspadas.simbolo = '9'

noveOuro = carta()
noveOuro.valor = 9
noveOuro.naipe = 'Ouro'
noveOuro.simbolo = '9'

oitoPaus = carta()
oitoPaus.valor = 8
oitoPaus.naipe = 'Paus'
oitoPaus.simbolo = '8'

oitoCopas = carta()
oitoCopas.valor = 8
oitoCopas.naipe = 'Copas'
oitoCopas.simbolo = '8'

oitoEspadas = carta()
oitoEspadas.valor = 8
oitoEspadas.naipe = 'Espadas'
oitoEspadas.simbolo = '8'

oitoOuro = carta()
oitoOuro.valor = 8
oitoOuro.naipe = 'Ouro'
oitoOuro.simbolo = '8'

setePaus = carta()
setePaus.valor = 7
setePaus.naipe = 'Paus'
setePaus.simbolo = '7'

seteCopas = carta()
seteCopas.valor = 7
seteCopas.naipe = 'Copas'
seteCopas.simbolo = '7'

seteEspadas = carta()
seteEspadas.valor = 7
seteEspadas.naipe = 'Espadas'
seteEspadas.simbolo = '7'

seteOuro = carta()
seteOuro.valor = 7
seteOuro.naipe = 'Ouro'
seteOuro.simbolo = '7'

seisPaus = carta()
seisPaus.valor = 6
seisPaus.naipe = 'Paus'
seisPaus.simbolo = '6'

seisCopas = carta()
seisCopas.valor = 6
seisCopas.naipe = 'Copas'
seisCopas.simbolo = '6'

seisEspadas = carta()
seisEspadas.valor = 6
seisEspadas.naipe = 'Espadas'
seisEspadas.simbolo = '6'

seisOuro = carta()
seisOuro.valor = 6
seisOuro.naipe = 'Ouro'
seisOuro.simbolo = '6'

cincoPaus = carta()
cincoPaus.valor = 5
cincoPaus.naipe = 'Paus'
cincoPaus.simbolo = '5'

cincoCopas = carta()
cincoCopas.valor = 5
cincoCopas.naipe = 'Copas'
cincoCopas.simbolo = '5'

cincoEspadas = carta()
cincoEspadas.valor = 5
cincoEspadas.naipe = 'Espadas'
cincoEspadas.simbolo = '5'

cincoOuro = carta()
cincoOuro.valor = 5
cincoOuro.naipe = 'Ouro'
cincoOuro.simbolo = '5'

quatroPaus = carta()
quatroPaus.valor = 4
quatroPaus.naipe = 'Paus'
quatroPaus.simbolo = '4'

quatroCopas = carta()
quatroCopas.valor = 4
quatroCopas.naipe = 'Copas'
quatroCopas.simbolo = '4'

quatroEspadas = carta()
quatroEspadas.valor = 4
quatroEspadas.naipe = 'Espadas'
quatroEspadas.simbolo = '4'

quatroOuro = carta()
quatroOuro.valor = 4
quatroOuro.naipe = 'Ouro'
quatroOuro.simbolo = '4'

tresPaus = carta()
tresPaus.valor = 3
tresPaus.naipe = 'Paus'
tresPaus.simbolo = '3'

tresCopas = carta()
tresCopas.valor = 3
tresCopas.naipe = 'Copas'
tresCopas.simbolo = '3'

tresEspadas = carta()
tresEspadas.valor = 3
tresEspadas.naipe = 'Espadas'
tresEspadas.simbolo = '3'

tresOuro = carta()
tresOuro.valor = 3
tresOuro.naipe = 'Ouro'
tresOuro.simbolo = '3'

doisPaus = carta()
doisPaus.valor = 2
doisPaus.naipe = 'Paus'
doisPaus.simbolo = '2'

doisCopas = carta()
doisCopas.valor = 2
doisCopas.naipe = 'Copas'
doisCopas.simbolo = '2'

doisEspadas = carta()
doisEspadas.valor = 2
doisEspadas.naipe = 'Espadas'
doisEspadas.simbolo = '2'

doisOuro = carta()
doisOuro.valor = 2
doisOuro.naipe = 'Ouro'
doisOuro.simbolo = '2'

def JogarBlackJack():
    asPaus.valor = 11
    asCopas.valor = 11
    asEspadas.valor = 11
    asOuro.valor = 11
    reiPaus.valor = 10
    reiCopas.valor = 10
    reiEspadas.valor = 10
    reiOuro.valor = 10
    damaPaus.valor = 10
    damaCopas.valor = 10
    damaEspadas.valor = 10
    damaOuro.valor = 10
    valetePaus.valor = 10
    valeteCopas.valor = 10
    valeteEspadas.valor = 10
    valeteOuro.valor = 10

    global soma
    global soma1
    global soma2
    global somaC
    global numero
    global numeroC
    global numero1
    global numero2
    global computador
    global jogador
    global jogador1
    global jogador2
    global contadorAs
    global contadorAsC
    global contadorAs1
    global contadorAs2
    global cartasRestantes
    global cartas
    global resp1
    global resp2

    soma = 0
    soma1 = 0
    soma2 = 0
    somaC = 0
    numero = 0
    numeroC = 0
    numero1 = 0
    numero2 = 0
    computador = []
    jogador = []
    jogador1 = []
    jogador2 = []
    resp1 = 0
    resp2 = 0
    contadorAs = 0
    contadorAsC = 0
    contadorAs1 = 0
    contadorAs2 = 0
    cartasRestantes = 51

    cartas = [doisOuro, doisEspadas, doisCopas, doisPaus, tresOuro, tresEspadas, tresCopas, tresPaus, quatroOuro, quatroEspadas, quatroCopas, quatroPaus, cincoOuro, cincoEspadas, cincoCopas, cincoPaus, seisOuro, seisEspadas, seisCopas, seisPaus, seteOuro, seteEspadas, seteCopas, setePaus, oitoOuro, oitoEspadas, oitoCopas, oitoPaus, noveOuro, noveEspadas, noveCopas, novePaus, dezOuro, dezEspadas, dezCopas, dezPaus, valeteOuro, valeteEspadas, valeteCopas, valetePaus, damaOuro, damaEspadas, damaCopas, damaPaus, reiOuro, reiEspadas, reiCopas, reiPaus, asOuro, asEspadas, asCopas, asPaus]  
    modoJogo = input("Escolha o modo de jogo:\n (1)Jogador 1 Vs. CPU\n (2)Jogador 1 Vs. Jogador 2\n ")
    
    if modoJogo == "1":
        while True: 
            randomC = randint(0, cartasRestantes)
            computador.append(cartas[randomC])
            cartas.remove(cartas[randomC])
            
            while contadorAsC < len(computador):
                testeAs = computador[contadorAs].simbolo
                somaAs = somaC + computador[-1].valor
                if testeAs == 'A':
                    if somaAs > 21:
                        somaC = somaC - 10
                contadorAsC += 1 
            somaC = somaC + computador[-1].valor           
            numeroC += 1
            cartasRestantes -= 1
            if somaC >= 17:
                break
            if numeroC >= 5:
                break
            while True:
                random = randint(0, cartasRestantes)
                jogador.append(cartas[random])
                sleep(0.4)
                print("\nVocê recebeu um {} de {}".format(cartas[random].simbolo, cartas[random].naipe))
                cartas.remove(cartas[random])
                
                while contadorAs < len(jogador):
                    testeAs = jogador[contadorAs].simbolo
                    somaAs = soma + jogador[-1].valor
                    if testeAs == 'A':
                        if somaAs > 21:
                            soma = soma - 10
                    contadorAs += 1                    
                soma = soma + jogador[-1].valor                
                if soma > 21:
                    sleep(0.4)
                    print("Você Perdeu, estourou 21\n")
                    continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                    if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                    else:
                        Menu()
                        break
                if soma == 21 and somaC<21:
                    sleep(0.4)
                    print("Você Ganhou com 21\n")
                    continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                    if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                        JogarBlackJack()
                        break
                    else:
                        Menu()
                        break
                numero += 1
                cartasRestantes -= 1                
                if numero >= 5:
                    sleep(0.4)
                    print("Você chegou no limite de 5 cartas.")
                    if somaC > 21:
                        sleep(0.4)
                        print("Você Ganhou, o adversário estourou 21\n")
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    if soma > somaC:
                        sleep(0.4)
                        print("Você Ganhou com {} contra os {} do adversário.\n".format(soma, somaC))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    elif somaC > soma:
                        sleep(0.4)
                        print("Você Perdeu com {} contra os {} do adversário.\n".format(soma, somaC))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    else:
                        sleep(0.4)
                        print("Vocês empataram com {}.\n".format(soma))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                sleep(0.4)
                print ("Pontos:{}".format(soma))
                if soma >= 17:
                    sleep(0.4)
                    print("Você chegou a 17 pontos e não pode acertar mais cartas.")
                    if somaC > 21:
                        sleep(0.4)
                        print("Você Ganhou, o adversário estourou 21\n")
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    if soma > somaC:
                        sleep(0.4)
                        print("Você Ganhou com {} contra os {} do adversário.\n".format(soma, somaC))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    elif somaC > soma:
                        sleep(0.4)
                        print("Você Perdeu com {} contra os {} do adversário.\n".format(soma, somaC))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    else:
                        sleep(0.4)
                        print("Vocês empataram com {}.\n".format(soma))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                        
                resp = input("ENTER para Acertar ou 0 para Parar:\n")               
                if resp == "0":
                    if somaC > 21:
                        sleep(0.4)
                        print("Você Ganhou, o adversário estourou 21\n")
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    if soma > somaC:
                        sleep(0.4)
                        print("Você Ganhou com {} contra os {} do adversário.\n".format(soma, somaC))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    elif somaC > soma:
                        sleep(0.4)
                        print("Você Perdeu com {} contra os {} do adversário.\n".format(soma, somaC))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    else:
                        sleep(0.4)
                        print("Vocês empataram com {}.\n".format(soma))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
    elif modoJogo == "2":
        def AcertarJogador1():
                global contadorAs1
                global soma1
                global cartasRestantes                  
                random1 = randint(0, cartasRestantes)
                jogador1.append(cartas[random1])
                sleep(0.4)
                print("\nJogador 1 recebeu um {} de {}".format(cartas[random1].simbolo, cartas[random1].naipe))
                cartas.remove(cartas[random1])
                while contadorAs1 < len(jogador1):
                    testeAs1 = jogador1[contadorAs1].simbolo
                    somaAs1 = soma1 + jogador1[-1].valor
                    if testeAs1 == 'A':
                        if somaAs1 > 21:
                            soma1 = soma1 - 10
                    contadorAs1 += 1
                soma1 = soma1 + jogador1[-1].valor
                cartasRestantes -= 1
        def AcertarJogador2():
                global contadorAs2
                global soma2
                global cartasRestantes
                random2 = randint(0, cartasRestantes)
                jogador2.append(cartas[random2])
                sleep(0.4)
                print("Jogador 2 recebeu um {} de {}\n".format(cartas[random2].simbolo, cartas[random2].naipe))
                cartas.remove(cartas[random2])
                while contadorAs2 < len(jogador2):
                    testeAs2 = jogador2[contadorAs2].simbolo
                    somaAs2 = soma2 + jogador2[-1].valor
                    if testeAs2 == 'A':
                        if somaAs2 > 21:
                            soma2 = soma2 - 10
                    contadorAs2 += 1
                soma2 = soma2 + jogador2[-1].valor
                cartasRestantes -= 1
        while True:
                if resp1 == 0 or resp1 == '':
                    AcertarJogador1()
                if resp2 == 0 or resp2 == '':
                    AcertarJogador2()                
                if soma1 > 21:
                    sleep(0.4)
                    print("Jogador 1 Perdeu, estourou 21\n")
                    continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                    if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                    else:
                        Menu()
                        break
                if soma2 > 21:
                    sleep(0.4)
                    print("Jogador 2 Perdeu, estourou 21\n")
                    continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                    if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                        JogarBlackJack()
                        break
                    else:
                        Menu()
                        break
                if soma1 == 21 and soma2<21:
                    sleep(0.4)
                    print("Jogador 1 Ganhou com 21\n")
                    continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                    if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                        JogarBlackJack()
                        break
                    else:
                        Menu()
                        break
                if soma2 == 21 and soma1<21:
                    sleep(0.4)
                    print("Jogador 2 Ganhou com 21\n")
                    continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                    if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                        JogarBlackJack()
                        break
                    else:
                        Menu()
                        break
                numero1 += 1
                numero2 += 1              
                if numero1 >= 5:
                    sleep(0.4)
                    print("Jogador 1 chegou no limite de 5 cartas.")
                    if soma1 > 21:
                        sleep(0.4)
                        print("Jogador 2 Ganhou, o adversário estourou 21\n")
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    if soma2 > 21:
                        sleep(0.4)
                        print("Jogador 1 Ganhou, o adversário estourou 21\n")
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    if soma1 > soma2:
                        sleep(0.4)
                        print("Jogador 1 Ganhou com {} contra os {} do adversário.\n".format(soma1, soma2))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    elif soma2 > soma1:
                        sleep(0.4)
                        print("Jogador 2 Ganhou com {} contra os {} do adversário.\n".format(soma2, soma1))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    else:
                        sleep(0.4)
                        print("Vocês empataram com {}.\n".format(soma1))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                if numero2 >= 5:
                    sleep(0.4)
                    print("Jogador 2 chegou no limite de 5 cartas.")
                    if soma1 > 21:
                        sleep(0.4)
                        print("Jogador 2 Ganhou, o adversário estourou 21\n")
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    if soma2 > 21:
                        sleep(0.4)
                        print("Jogador 1 Ganhou, o adversário estourou 21\n")
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    if soma1 > soma2:
                        sleep(0.4)
                        print("Jogador 1 Ganhou com {} contra os {} do adversário.\n".format(soma1, soma2))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    elif soma2 > soma1:
                        sleep(0.4)
                        print("Jogador 2 Ganhou com {} contra os {} do adversário.\n".format(soma2, soma1))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    else:
                        sleep(0.4)
                        print("Vocês empataram com {}.\n".format(soma1))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                sleep(0.4)
                print ("\nJogador 1 tem {} pontos.".format(soma1))
                print ("Jogador 2 tem {} pontos.\n".format(soma2))
                if soma1 >= 17:
                    sleep(0.4)
                    print("O Jogador 1 chegou a 17 pontos e não pode acertar mais cartas.")
                    if soma1 > 21:
                        sleep(0.4)
                        print("Jogador 2 Ganhou, o adversário estourou 21\n")
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    if soma2 > 21:
                        sleep(0.4)
                        print("Jogador 1 Ganhou, o adversário estourou 21\n")
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    if soma1 > soma2:
                        sleep(0.4)
                        print("Jogador 1 Ganhou com {} contra os {} do adversário.\n".format(soma1, soma2))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    elif soma2 > soma1:
                        sleep(0.4)
                        print("Jogador 2 Ganhou com {} contra os {} do adversário.\n".format(soma2, soma1))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    else:
                        sleep(0.4)
                        print("Vocês empataram com {}.\n".format(soma1))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                if soma2 >= 17:
                    sleep(0.4)
                    print("O Jogador 2 chegou a 17 pontos e não pode acertar mais cartas.")
                    if soma1 > 21:
                        sleep(0.4)
                        print("Jogador 2 Ganhou, o adversário estourou 21\n")
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    if soma2 > 21:
                        sleep(0.4)
                        print("Jogador 1 Ganhou, o adversário estourou 21\n")
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    if soma1 > soma2:
                        sleep(0.4)
                        print("Jogador 1 Ganhou com {} contra os {} do adversário.\n".format(soma1, soma2))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    elif soma2 > soma1:
                        sleep(0.4)
                        print("Jogador 2 Ganhou com {} contra os {} do adversário.\n".format(soma2, soma1))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    else:
                        sleep(0.4)
                        print("Vocês empataram com {}.\n".format(soma1))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                def Jogador1Acertar():
                    global resp1
                    resp1 = input("Jogador 1, Pressione ENTER para Acertar ou 0 para Parar:\n")
                    if resp1 == "0":
                        def AcertarJogador1():
                            resp1 = 1
                        def Jogador1Acertar():
                            resp1 = 1                       
                def Jogador2Acertar():
                    global resp2
                    resp2 = input("Jogador 2, Pressione ENTER para Acertar ou 0 para Parar:\n")
                    if resp2 == "0":
                        def AcertarJogador2():
                            resp2 = 1
                        def Jogador2Acertar():
                            resp2 = 1
                if resp1 == 0 or resp1 == '':
                    Jogador1Acertar()
                if resp2 == 0 or resp2 == '':
                    Jogador2Acertar()                        
                if resp1 == "0" and resp2 == "0":
                    if soma1 > soma2:
                        sleep(0.4)
                        print("Jogador 1 Ganhou com {} contra os {} do adversário.\n".format(soma1, soma2))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    elif soma2 > soma1:
                        sleep(0.4)
                        print("Jogador 2 Ganhou com {} contra os {} do adversário.\n".format(soma2, soma1))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
                    else:
                        sleep(0.4)
                        print("Vocês empataram com {}.\n".format(soma1))
                        continuar = input("Deseja Continuar Jogando BlackJack?\n(1)Sim\n(2)Não\n ").upper().strip()
                        if continuar == "SIM" or continuar == "SIM." or continuar == "1":
                            JogarBlackJack()
                            break
                        else:
                            Menu()
                            break
JogarBlackJack()