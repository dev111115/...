op = ''
while op != 3:
    print(20*"=","BEM VINDO AO MENU PRINCIPAL","="*20)
    print(20*"-","Digite (1) para Aprender","-"*20)
    print(20*"-","Digite (2) para fazer o Quiz","-"*20)
    print(20*"-","Digite (3) para encerrar o programa","-"*20)
    op = str(input("\nDigite :"))
    if op != "1" and op != "2" and op != "3":
        print("VALOR INVALIDO!, DIGITE UMA VALOR ENTRE 1 E 3")
    if op == "1":
        op1 = ''
        while op1 != "SAIR":
           print('\n',20*"=","BEM VINDO AO MENU APRENDER","="*20)
           print(16*'-',"Aqui você aprenderá sobre Input ou Print",16*'-')
           print(16*'-',"Digite 'SAIR' se desejar sair do Menu Aprender",16*'-')
           op1 = str(input("\nDeseja Aprender Input ou Print ? :")).upper()
           if op1 == "INPUT":
                print("\n----------------------------INPUT---------------------------------")
                print("\nInput tem a função de receber dados do usuario. \nEx : input('Digite seu nome')\n")
                print("---------------------------------------------------------------\n")
           elif op1 == "PRINT":
                print("\n----------------------------PRINT---------------------------------")
                print("\nPrint tem a função de imprimir algum texto\nEx : print('Ola Mundo')\n")
                print("---------------------------------------------------------------\n")
           elif op1 == "SAIR":
                print("Encerrou o programa Menu Aprender\n")
           else:
                print("\n====================VALOR INVALIDO!, DIGITE PRINT ou INPUT====================\n")
    elif op == '2':
        quiz = ''
        while quiz != 'A':
            print("\n============================01 Pergunta============================")
            print("\nO que é Python ?")
            print("A) Linguagem de Programação.")
            print("B) Esporte.")
            print("C) Marca de Carro.")
            print("D) Tipo de Sofware.")
            quiz = str(input("\nDigite a Alternativa Correta :")).upper()
            if quiz == "A":
                print("\nAternativa correta!\n")
                print('======================================================================')
            elif quiz == "B":
                print("Alternativa ERRADA!, TENTE NOVAMENTE")
            elif quiz == "C":
                print("Alternativa ERRADA! , TENTE NOVAMENTE")
            elif quiz == "D":
                print("Alternativa ERRADA! , TENTE NOVAMENTE")
            else:
                print("VALOR INVÁLIDO, DIGITE NOVAMENTE\n")
                print(20*'==')
            
        quiz_1 = ''
        while quiz_1 != 'D':
            print("\n============================02 Pergunta============================")
            print("\nQual a função do Print ?")
            print("A) Abrir o navegador.")
            print("B) Deletar o Windows.")
            print("C) Receber dados.")
            print("D) Imprimir algum texto.")
            quiz_1 = str(input("\nDigite a Alternativa Correta :")).upper()
            if quiz_1 == "A":
                print("Alternativa ERRADA!, TENTE NOVAMENTE")
            elif quiz_1 == "B":
                print("Alternativa ERRADA!, TENTE NOVAMENTE")
            elif quiz_1 == "C":
                print("Alternativa ERRADA! , TENTE NOVAMENTE")
            elif quiz_1 == "D":
                print("\nAlternativa correta!")
                print('======================================================================')
            else:
                print("VALOR INVÁLIDO, DIGITE NOVAMENTE\n")
                print(20*'==')
        quiz_2 = ''        
        while quiz_2 != 'C':
            print("\n============================03 Pergunta================================")
            print("\nQual a função do Input ?")
            print("A) Imprimi um texto.")
            print("B) Deletar o Windows.")
            print("C) Receber dados.")
            print("D) Abrir o navegador.")
            quiz_2 = str(input("\nDigite a Alternativa Correta :")).upper()
            if quiz_2 == "A":
                print("Alternativa ERRADA!, TENTE NOVAMENTE")
                break
            elif quiz_2 == "B":
                print("Alternativa ERRADA!, TENTE NOVAMENTE")
            elif quiz_2 == "C":
                print("\nAternativa correta!\n")
                print('======================================================================')
            elif quiz_2 == "D":
                print("Aternativa ERRADA! , TENTE NOVAMENTE")
            else:
                print("VALOR INVÁLIDO, DIGITE NOVAMENTE\n")
                print(20*'==')
    elif op == '3':
            print("Programa Encerrado")
