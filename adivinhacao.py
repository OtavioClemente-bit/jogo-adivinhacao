import random
import time
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def perguntar_novo_jogo():
    while True:
        operação = input("\nDigite 1 para jogar novamente ou 2 para sair: ")
        if operação == "1":
            return True
        elif operação == "2":
            limpar_tela()
            return False
        limpar_tela()
        print("Valor inválido, tente novamente.")
        time.sleep(1)
        limpar_tela()

def jogar(escolha_dificuldade, numero_secreto):
    limpar_tela()
    print(f"\nESCOLHA UM NÚMERO DE 1 A {escolha_dificuldade}!")
    tentativas = 0
    while True:
        try:
            palpite = int(input("\nDigite seu palpite: "))
        except ValueError:
            limpar_tela()
            print ("Digite um número valido!")
            time.sleep(2)
            limpar_tela()
            continue
        tentativas += 1
        if palpite > numero_secreto:
            limpar_tela()
            print ("Número escolhido maior! Tente novamente")
            time.sleep(0.5)
            limpar_tela()
        elif palpite < numero_secreto:
            limpar_tela()
            print ("Número escolhido menor! Tente novamente")
            time.sleep(0.5)
            limpar_tela()
        elif palpite == numero_secreto:
            limpar_tela()
            print ("  PARABÉNS VOCÊ ACERTOU !!!  ")
            if tentativas == 1:
                print ("\n Você acertou de primeira!!")
            else:
                print (f"\n Você tentou um total de {tentativas} tentativas.")
            break

NIVEIS = {'1': 10, '2': 50, '3': 100}

if __name__ == "__main__":
    while True:
        limpar_tela()
        print("=========================================")
        print("=========== BEM-VINDO AO JOGO ===========")
        print("=========================================")
        time.sleep(1)
        while True:
            limpar_tela()
            dificuldade = input("\nEscolha a dificuldade (1-Fácil, 2-Médio, 3-Difícil): ")
            if dificuldade in NIVEIS:
                escolha_dificuldade = NIVEIS[dificuldade]
                numero_secreto = random.randint(1, escolha_dificuldade)
                limpar_tela()
                if escolha_dificuldade == 10:
                    print("Você escolheu o nível Fácil!")
                elif escolha_dificuldade == 50:
                    print("Você escolheu o nível Médio!")
                elif escolha_dificuldade == 100:
                    print("Você escolheu o nível Difícil!")
                time.sleep(1)
                jogar(escolha_dificuldade, numero_secreto)
                break
            else:
                limpar_tela()
                print("Opção inválida, tente novamente.")
                time.sleep(1)
        if not perguntar_novo_jogo():
            limpar_tela()
            print("=========================================")
            print("=========== FIM DO JOGO =================")
            print("=========================================")
            break
