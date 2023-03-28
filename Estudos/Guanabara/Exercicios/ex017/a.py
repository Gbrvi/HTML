from time import sleep
g = d = 0
b = c = e = f = 'n'
w1 = 0
def fazer_hoje():
    print('O que você vai fazer hoje?')
    print('[1] Não tomar banho')
    print('[2] Tomar banho')
    a = int(input(''))
    if a == '2':
        w1 = 0
        sleep(1.5)
        print('OK, vamos tomar banho')
        sleep(1.5)
        print('*pegando a toalha*')
        sleep(1.5)
        print('*pegando a roupa*')
        sleep(1.5)
        b == 'n'
        b = input('Pegar o celular? [Sim/Não] ')
        w2 = 0
        while w2 == 0:
            try:
                if b.lower() == 's':
                    sleep(1.5)
                    print('*pegando o celular*')
                    sleep(1.5)
                    e == 'n'
                    e = input('Você vai ouvir música no banho? [Sim/Não] ')
                    w3 = 0
                    while w3 == 0:
                        try:
                            if e.lower() == 'n':
                                sleep(1.5)
                                f == 'n'
                                f = input('Você quer colocar o celular pra carregar? [Sim/Não] ')
                                w4 = 0
                                while w4 == 0:
                                    try:
                                        if f.lower() == 'n':
                                            sleep(1.5)
                                            print('Pegou celular pra quê então?')
                                            w4 += 1
                                            return False
                                        elif f.lower() == 's':
                                            sleep(1.5)
                                            print('\033[31mSeu celular é Samsung, ele explodiu e você morreu.\033[m')
                                            w1 += 1
                                            return False
                                    except:
                                        print('\033[33mValor inválido, tente novamente.\033[m')
                                        w4 = 0
                            if e.lower() == 's':
                                sleep(1.5)
                                print('Onde você vai deixar o celular?')
                                print('[1] Fora do box')
                                print('[2] Na báscula/janela')
                                g = int(input(''))
                                w5 = 0
                                while w5 == 0:
                                    try:
                                        if g == '2':
                                            print('\033[31mSeu celular caiu no chão e explodiu, causando a sua morte.\033[m')
                                            w1 += 1
                                            return False
                                        elif g == '1':
                                            print('Boa escolha.')
                                            w5 += 1
                                    except:
                                        print('\033[33mValor inválido, tente novamente.\033[m')
                                        w5 = 0
                            sleep(1.5)
                            c1 == 's'
                            c1 = input('Você vai se depilar hoje? [Sim/Não] ')
                            w6 = 0
                            while w6 == 0:
                                try:
                                    if c1.lower() == 's':
                                        sleep(1.5)
                                        print('O que você vai usar?')
                                        print('[1] Máquina')
                                        print('[2] Prestobarba')
                                        d = int(input(''))
                                        w6 += 1
                                    elif c1.lower() == 'n':
                                        sleep(1.5)
                                        print('\033[31mSeu pelo encravou, gerando uma infecção que atingiu a corrente sanguínea, você desenvolveu septicemia e morreu.\033[m')
                                        w1 += 1
                                        return False
                                except:
                                    print('\033[33mValor inválido, tente novamente.\033[m')
                                    w6 = 0
                        except:
                            print('\033[33mValor inválido, tente novamente.\033[m')
                            w3 = 0        
                elif b.lower() == 'n':
                    sleep(1.5)
                    c2 == 's'
                    c2 = input('Você vai se depilar hoje? [Sim/Não] ')
                    while w6 == 0:
                        if c2.lower() == 's':
                            sleep(1.5)
                            print('O que você vai usar?')
                            print('[1] Máquina')
                            print('[2] Prestobarba')
                            d = int(input(''))
                            w6 += 1
                        if c2.lower() == 'n':
                            sleep(1.5)
                            print('\033[31mSeu pelo encravou, gerando uma infecção que atingiu a corrente sanguínea, você desenvolveu septicemia e morreu.\033[m')
                            w1 += 1
                            return False
            except:
                print('Valor inválido, tente novamente.')
                w2 = 0
    elif a == '1':
        sleep(1.5)
        print('\033[31mApós 1 semana sem tomar banho, você desenvolveu uma infecção e morreu.\033[m')
        w1 += 1
        return False
def fim():
    sleep(1.5)
    if g == '1' and d == '1':
        sleep(1.5)
        print('*ligando o chuveiro*')
        sleep(1.5)
        print('*se molhando*')
        sleep(1.5)
        print('*se ensaboando*')
        sleep(1.5)
        print('*ligando a máquina*')
        sleep(1.5)
        print('*começando a se depilar*')
        sleep(1.5)
        print('*a água entrou na máquina*')
        sleep(1.5)
        print('\033[31mVocê morreu eletrocutado.\033[m')
        w1 += 1
        return False
    if g == '1' and d == '2':
        sleep(1.5)
        print('*ligando o chuveiro*')
        sleep(1.5)
        print('*se molhando*')
        sleep(1.5)
        print('*se ensaboando*')
        sleep(1.5)
        print('*pegando o prestobarba*')
        sleep(1.5)
        print('*começando a se depilar*')
        sleep(1.5)
        print('*terminando de se depilar*')
        sleep(1.5)
        print('*se limpando*')
        sleep(1.5)
        print('*pegando a toalha*')
        sleep(1.5)
        print('*se secando*')
        sleep(1.5)
        print('*colocando a roupa*')
        sleep(1.5)
        print('*FIM*')
        w1 += 1
        return False

fazer_hoje()