x = 0
y = 0
desconto = 0.05
clientes = []
passagens = []
aviao = []
tripulacao = []

while True:
    try:
        print("\nSeja Bem vindo ao painel de passagens!\n\nPara começar, selecione alguma das opções abaixo:\n")

        x=int(input("1- Cadastros\n" "2- Relatórios\n" "0- Encerrar e sair\n\n"))
        
        if x == 0:
            print("Encerrando. Até logo!")
            break
#-------------------------------------------------------------------------------------------------------        
        if x == 1:
            print("\nMuito bem! Preencha com todas as informações solicitadas:\n")
            print("-----Cadastro Cliente-----")
            nome = input("Digite seu primeiro nome: ")
            sobrenome = input("Digite seu sobrenome: ")
            rg = input("Digite seu RG: ")
            cpf = input("Digite seu CPF: ")
            endereço = input("Digite seu endereço: ")
            telef = input("Digite seu telefone: ")
            idd = input("Digite sua idade: ")

            cliente = {'Nome': nome, 'Sobrenome': sobrenome, 'RG': rg, 'CPF': cpf
                       , 'Endereço': endereço, 'Telefone': telef, 'Idade': idd
                       }
            clientes.append(cliente)
            print("\nCadastro do cliente completo!\n")
 #-------------------------------------------------------------------------------------------------------               
            print("-----Cadastro Passagem-----")
            destino = input("Digite o destino: ")
            origem = input("Digite a origem: ")
            duração_voo = input("Duração do voo: ")
            valorpassagem = float(input("Valor da passagem: "))
            print("Desconto (5%): ",(valorpassagem-valorpassagem*desconto))
            passagem = valorpassagem-valorpassagem*desconto
            
            passagens1 = {'Destino': destino, 'Origem': origem, 'Duração do voo': duração_voo,
                         'Valor da passagem':passagem
                         }
            passagens.append(passagens1)
            print("\nCadastro da passagem completo!\n")
#-------------------------------------------------------------------------------------------------------                    
            print("-----Cadastro Avião-----")
            modelo = input("Digite o modelo do avião: ")
            ano = input("Digite o ano (Ex. 01/01/2001): ")
            horas_voo = input("Horas de voo: ")
            cor_aviao = input("Cor do avião: ")
            qntd_passageiros = input("Quantidade de passageiros: ")

            cadastro_aviao = {'Modelo do avião': modelo, 'Ano': ano, 'Horas de voo': horas_voo, 'Cor do avião': cor_aviao,
                              'Quantidade de passageiros': qntd_passageiros
                              }
            aviao.append(cadastro_aviao)
            print("Cadastro dos dados do avião completos!\n")
#-------------------------------------------------------------------------------------------------------                        
            print("-----Cadastro Tripulação-----")
            name = input("Digite seu nome: ")
            cargo = input("Digite seu cargo: ")
            idade = input("Digite sua idade: ")
            data_admissao = input("Data de admissão: ")
            telefone = input("Telefone para contato: ")

            cadastro_tripulacao = {"Nome": name, "Cargo": cargo, "Idade": idade,
                                   "Data de admissão": data_admissao, "Telefone": telefone
                                   }
            tripulacao.append(cadastro_tripulacao)
            print("Cadastro dos dados da tripulação completos!\n")
            print("Dados cadastrados com sucesso! Retornando ao menu principal.\n")
#-------------------------------------------------------------------------------------------------------
        if x == 2:
            print("\nMuito bem! Aqui está um relatório geral:\n")

            if len(clientes) == 0:
                print("Nenhum cliente cadastrado.\n")
                print("Deseja realizar o cadastro agora? Digite '1' para 'Sim' ou '2' para 'Não':")
                resposta = input()

                if resposta == "1":
                    continue
                elif resposta == "2":
                    print("\nOk. Voltando ao menu principal")

            else:
                print("\n-----CLIENTES-----")  
                for c in clientes:
                    print(f"Nome: {c['Nome']} {c['Sobrenome']}")
                    print(f"RG: {c['RG']}")
                    print(f"CPF: {c['CPF']}")
                    print(f"Endereço: {c['Endereço']}")
                    print(f"Telefone: {c['Telefone']}")
                    print(f"Idade: {c['Idade']}")
                    print("----------------------------")
            
            
                print("\n-----PASSAGENS-----")
                for p in passagens:
                    print(f"Destino: {p['Destino']}")
                    print(f"Origem: {p['Origem']}")
                    print(f"Duração: {p['Duração do voo']}")
                    print(f"Valor Passagem com desconto (5%): {p['Valor da passagem']}")
                    print("----------------------------")
            
            
                print("\n-----AVIÕES-----")
                for a in aviao:
                    print(f"Modelo do avião: {a['Modelo do avião']}")
                    print(f"Ano: {a['Ano']}")
                    print(f"Horas de voo: {a['Horas de voo']}")
                    print(f"Cor do avião: {a['Cor do avião']}")
                    print(f"Quantidade de passageiros: {a['Quantidade de passageiros']}")
                    print("----------------------------")
            
            
                print("\n-----TRIPULAÇÃO-----")
                for t in tripulacao:
                    print(f"Nome: {t['Nome']}")
                    print(f"Cargo: {t['Cargo']}")
                    print(f"Idade: {t['Idade']}")
                    print(f"Data de Admissão: {t['Data de admissão']}")
                    print(f"Telefone: {t['Telefone']}")
                    print("----------------------------")
                    
        print("\nRelatórios gerados, retornando ao menu principal.")
                    
    except ValueError:
        print("Opção inválida ou inexistente. Digite uma das opções amostra.")