from time import sleep
from termcolor import colored

def menu_hoje():
    print(colored('''---------------------
O que você vai fazer hoje?'
[1] Não tomar banho'
[2] Tomar banho
---------------------''', 'yellow'))

def menu_cel():
    print(colored('''----------------------
Onde você vai deixar o celular?'
[1] Fora do box
[2] Na báscula/janela
----------------------''', 'yellow'))    

def main():
    menu_hoje()
    escolha = int(input(" "))
    if escolha == 2:
        print(colored('OK, vamos tomar banho'))
        print('*pegando a toalha*')
        print('*pegando a roupa*')
        while True:
            resp_celular = str(input("Pegar celular? [S/N] ")).upper()[0]
            if resp_celular == 'S' or resp_celular == 'N':
                break
            else:
                print('Digite apenas S ou N')

        if resp_celular == 'S':
            print("Pegando celular")


            while True:
                resp_musica = str(input('Você vai ouvir música no banho? [S/N] ')).upper()[0]  
                if resp_musica == 'S' or resp_musica == 'N':
                    break
                else:
                    print('Digite apenas S or N')

            if resp_musica == 'S':
                menu_cel()

                while True:
                    resp_deixar_cel = int(input(" "))

                    if resp_deixar_cel == 1 or resp_deixar_cel == 2:
                        break
                    else:
                        print('Digite apenas 1 ou 2')

                if resp_deixar_cel == 2: 
                    print('\033[31mSeu celular caiu no chão e explodiu, causando a sua morte.\033[m')
                else:
                    print('Boa escolha, Mineirinho')          
    

main()
