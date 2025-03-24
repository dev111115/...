print("Bem Vindo ao Menu Principal")
print(20*"==")
op = ''
while op != 3:
    print("Digite (1) para Aprender")
    print("Digite (2) para Quiz")
    print("Digite (3) para Encerrar o programa")
    op = int(input("Digite :"))
    if op != 1 and op != 2 and op != 3:
        print("Digite um número entre 1 e 3")
    if op == 1 :
        for i in range(0,2):
            op1 = str(input("Deseja aprender INPUT ou PRINT ?:")).upper().strip()
            if op1 == "INPUT":
                print("A função input() em Python é usada para receber dados do usuário.\nEx: input('Digite sua idade')")
            elif op1 == "PRINT":
                print("A função print() em Python é usada para exibir informações na tela.Ex: print('Olá Mundo')")
            else:
                print("Digite um Valor válido, print ou input")
            print(20*'==')
    elif op == 2:
    
        print("O que é Python ?")
        print("A) Linguagem de Progamação")
        print("B) Marca de Carro")
        print("C) Esporte")
        quiz = ''
        while quiz != 'A':
           quiz = str(input("Digite a alternativa correta:")).upper().strip()
           if quiz == 'A':
              print('Correto')
           elif quiz == 'B':
             print("ERRADO , TENTE NOVAMENTE")
           elif quiz == 'C':
             print("ERRADO , TENTE NOVAMENTE")
           else : 
                print('Insira um valor válido')
                
        print(20*'==')
        print(20*'==')
        print("Em que ano o Python foi inventado ?")
        print("A) 1980")
        print("B) 2000")
        print("C) 1991")
        quiz_2 = ''
        while quiz_2 != 'C':
           quiz_2 = str(input("Digite a alternativa correta:")).upper().strip()
           if quiz_2 == 'A':
              print('ERRADO , TENTE NOVAMENTE')
           elif quiz_2 == 'B':
             print("ERRADO , TENTE NOVAMENTE")
           elif quiz_2 == 'C':
             print("Correto")
           else : 
                print('Insira um valor válido')
    elif op == 3:
        print("Programa Encerrado")
