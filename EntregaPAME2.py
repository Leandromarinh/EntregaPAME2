# Leandro Serra da Silva Marinho
# Segunda entrega do PAME 2020.2

class Lutador:

    def __init__(self, nome, idade, peso, forca, faixa, artemarcial):

        if isinstance(nome, str) and isinstance(idade, int) and isinstance(float(peso), float) and isinstance(float(forca), float) and isinstance(faixa, str) and isinstance(artemarcial, str):

            if idade >= 21 and peso >= 70.0 and forca >= 100.0:
                self.nome = nome
                self.idade = idade
                self.peso = peso
                self.forca = forca
                self.faixa = faixa
                self.artemarcial = artemarcial

            else:
                print( "alguma informação do lutador não atende os critérios minimos")
                print( " lembrando que o lutador tem que ter, no mínimo, 21 anos, 70.0 de peso e 100.0 de força" )

        else:
            print( "alguma informação do lutador não é válida")
            print( "lembrando que o nome do lutador tem que estar entre aspas e a idade tem que ser um número inteiro" )
            
            

    def __str__(self):
        return f" Lutador: nome: {self.nome} ,idade :{self.idade}, peso: {self.peso}, força: {self.forca}, faixa: {self.faixa}, arte macial: {self.artemarcial}"

class Torneio:

    faixas = ["branca", "azul", "marrom", "livre"] # todos os torneios terão todas essas faixas
    pesos = [[70,80],[80,90],[90,100],[100,120]] # todos os torneios terão esse categorias de peso
    

    def __init__(self, nometorneio, artemarciais ):

      if isinstance( nometorneio, str) and isinstance( artemarciais, str):
          self.nometorneio = nometorneio
          self.artemarciais = artemarciais
          
        
      else:
          print( "alguma informação do torneio não é válida")
          print( "lembrando que o nome do torneio e a arte marcial tem que estar entre aspas" )

    def __str__(self):
        return f" Torneio: nome: {self.nometorneio}, arte marcial:{self.artemarciais}, faixas: {self.faixas}, pesos: {self.pesos}"

    def __setLutador__(self,lutadores):

        if isinstance(lutadores, list):
            self.lutadores = lutadores

        else:
            print("tipo inválido")
        
def main():

    lutadores = []
    lista_torneios = []
    lutadores_torneio = []
    print(" Bem vindo ao torneio de artes marciais" )
    print()
    print( " Escolha o menu desejado a sguir...")
    print( " Digite 1 para visualizar o menu de lutadores")
    print( " Digite 2 para visualizar o menu de torneios")
    print( " Digite 3 para criar um torneio aleatório")
    menu = int(input(" Digite aqui: "))
    
    if menu == 1:
        def primeiro_menu():

            count = 0
            print()
            print (" Aqui você pode cadastrar um lutador ou visualizar um já cadastrado")
            print(" Para cadastrar um lutador, digite 1")
            print(" Para ver um lutador, digite 2 ")
            menu_lutador = int(input(" Digite aqui: "))

            if menu_lutador == 1:

                print()
                print(" Determine as informações sobre o lutador")
                print()
                nome_lutador = str(input(" Diga o nome do lutador( deve ter no mínimo o nome e um sobrenome): "))
                print()
                idade_lutador = input(" Diga a idade do lutador( idade mínima de 21 anos): ")
                print()
                peso_lutador = input(" Diga o peso do lutador em kg( peso mínimo de 70 kg e máximo de 120): ")
                print()
                forca_lutador = input(" Diga a força do lutador( força mínima de 100): ")
                print()
                faixa_lutador = str(input(" Diga a faixa do lutador: "))
                print()
                arte_lutador = str(input(" Diga a arte marcial praticada pelo lutador: "))
                lutador_cadastrado =[]
                lutador_cadastrado.append(Lutador.nome_lutador)
                lutador_cadastrado.append(Lutador.idade_lutador)
                lutador_cadastrado.append(Lutador.peso_lutador)
                lutador_cadastrado.append(Lutador.forca_lutador)
                lutador_cadastrado.append(Lutador.faixa_lutador)
                lutador_cadastrado.append(Lutador.arte_lutador)
                lutadores.append(lutador_cadastrado)
                count += 1

                print(" Para voltar ao menu principal, digite 1")
                print(" Para voltar ao menu de lutadores, digite 2")
                caminho = int(input(" Digite aqui: "))

                if caminho == 1:
                    return main()

                elif caminho == 2:
                    return priemiro_menu()
                    

            elif menu_lutador == 2:

                if count == 0:

                    print(" Não há lutadores cadastrado no torneio")

                else:

                    print(lutadores)

                print(" Para voltar ao menu principal, digite 1")
                print(" Para voltar ao menu de lutadores, digite 2")
                caminho = int(input(" Digite aqui: "))

                if caminho == 1:
                    main()

                elif caminho == 2:
                    priemiro_menu()

            else:

                print(" opção inválida")

    primeiro_menu()            


    if menu == 2:

        def segundo_menu():

            count = 0
            print( " Aqui você pode criar um torneio ou visualizar um já existente e modificá-lo")
            print( " Para criar um torneio, digite 1")
            print( " Para ver/editar um torneio, digite 2")
            menu_torneio = int(input(" Digite aqui: "))

            if menu_torneio == 1:

                print(" Determine algumas informações sobre o seu torneio...")
                nome_torneio = str(input("Dê um nome ao torneio: "))
                print()
                print(" Determine a arte marcial do torneio")
                print(" As opções são: jiu-jítsu, karatê e judo ")
                arte_torneio = str(input("Digite a opção desejada: "))
                torneio_criado = []
                torneio_criado.append(Torneio.nome_torneio)
                torneio_criado.append(Torneio.arte_torneio)
                lisa_torneio.append(torneio_criado)
                count += 1

            elif menu_torneio == 2:

                if count == 0:

                    print ( " não há torneios exitentes, crie-os para que seja possível visualizar-los" )

                else:

                    ok = 1
                    print(lista_torneios)
                    print(" Escolha um torneio, sendo o primeiro o conjunto que está dentro do primeiro colchetes, o segundo,o seguinte e assim em diante")

                    while ok <= count:

                        print( "o" + ok + "torneio é" + lista_torneio[ok - 1] )
                        ok += 1

                    print()
                    torneio_escolhido = input ( " O torneio desejado é:  ")
                    print()
                    print (" O que você deseja fazer nesse torneio ?" )
                    print()
                    print ("  Para ver o ranking, digite 1")
                    print ("  Para inscrever um lutador, digite 2") 
                    print ("  Para ver o lutadores inscritos e/ou fazer uma luta entre dois, digite 3")
                    print()
                    escolha = input(" Digite aqui: ")

                    if escolha == 1 :

                        if lutadores_torneio == []:

                            print ( " Não há lutadores cadastrados nesse torneio")

                        else:
                            print()
                            # fazer o ranking dos lutadores

                    elif escolha == 2:

                        if lutadores != []:
                            print(" Escolha um jogador para inscrevê-lo: ")
                            print(lutadores)
                            lutador_escolhido = str(input(" Digite aqui o nome do lutador escolhido: "))
                            for i in lutadores :
                                #for j in i :
                                if i[0] == lutador_escolhido:
                                    lutadores_torneio.append(lutador_escolhido)
                                else:
                                    print(" O lutador escolhido não é cadastrado")
                                    print()
                                    print(" Para cadastrá-lo, vá para o menu de lutadores")
                                    print()
                                    print(" Para voltar ao menu de lutadores, digite 1")
                                    print(" Para voltar ao menu de torneios, digite 2")
                                    volta = int(input(" Digite aqui: "))

                                    if volta == 1:
                                        primeiro_menu()

                                    if volta == 2:
                                        segundo_menu()

                                    else:
                                        print(" Número invàlido")

                        else:
                            print(" Não há lutadores cadastrados nesse torneio")
                            

                                    
                    elif escolha == 3 :

                        if lutadores_torneio == []:

                            print ( "não há lutadores cadastrados nesse torneio")

                        else:

                            print( lutadores_torneio )
                            print( "Escolha dois lutadores dentre os que estão na lista")
                            primeiro_lutador = input( " O primeiro será: ")
                            segundo_lutador = input (" O segundo será: ")
                            #fazer a luta e o criterio de vitória

        segundo_menu()            

    
        

                        


                        
                    



                                      
                
                                
                
                
                
main()












