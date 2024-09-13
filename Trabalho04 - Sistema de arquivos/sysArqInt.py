arqSys = arquivos()
while True:
    inp = input(f"J {arqSys.obterPathAtual()}> ")
    if inp == "exit":
        break
    else:
        com = inp.split(" ")

        if len(com) < 2 and com[0] not in ("dir", "help"):
            print(f"comando '{com[0]}' inválido, digite 'help' para mais informações")
        else:
            match com[0]:
                case "cd":
                    if len(com) == 2:
                        arqSys.moverParaDiretorio(com[1])
                    else:
                        print(f"comando '{com[0]}' inválido, digite 'help' para mais informações")
               
                case "mkdir":
                    if len(com) == 2:
                        arqSys.criaDiretorio(com[1])
                    else:
                        print(f"comando '{com[0]}' inválido, digite 'help' para mais informações")
                
                case "mk":
                    if len(com) == 2:
                        arqSys.criaArquivo(com[1])
                    else:
                        print(f"comando '{com[0]}' inválido, digite 'help' para mais informações")
                
                case "dir":
                    arqSys.listarItensDirAtual()
                
                case "mv":
                    if len(com) == 3:
                        arqSys.moverItens(com[1], com[2])
                    else:
                        print(f"comando '{com[0]}' inválido, digite 'help' para mais informações")

                case "rm":
                    if len(com) == 2:
                        arqSys.removerItens(com[1])
                    elif len(com) == 3:
                        arqSys.removerItens(com[1],com[2])
                    else:
                        print(f"comando '{com[0]}' inválido, digite 'help' para mais informações")

                case "wa":
                    if len(com) >= 3:
                        iindex = 0
                        findex = 0
                        for i in com:
                            if i.__contains__("\""):
                                iindex = com.index(i)
                                break
                        if iindex != 0:
                            for i in com[::-1]:
                                if i.__contains__("\""):
                                    findex = com.index(i)
                                    break
                            texto = " ".join(com[iindex:findex+1])
                            arqSys.escreverNoArquivo(com[1], texto)
                        else:
                            print(f"comando '{com[0]}' inválido, digite 'help' para mais informações")
                    else:
                        print(f"comando '{com[0]}' inválido, digite 'help' para mais informações")

                case "ra":
                    if len(com) == 2:
                        arqSys.lerArquivo(com[1])
                    else:
                        print(f"comando '{com[0]}' inválido, digite 'help' para mais informações")

                case "help":
                    help = {
                        "cd": "utilize 'cd [diretório de destino]' para ir ao local de destino, pode ser usado path relativo/absoluto",
                        "mkdir": "utilize 'mkdir [nome do diretório]' para criar um novo diretório no diretório atual",
                        "mk": "utilize 'mk [nome do arquivo]' para criar um arquivo .txt, ou especifique a extensão na criação",
                        "dir": "utilize 'dir' para listar todos os arquivos/diretórios no diretório atual",
                        "mv": "utilize 'mv [path do arquivo] [diretório de destino]' para mover um arquivo do diretório atual para o diretório de destino",
                        "rm": "utilize 'rm [path do arquivo/diretório]' para remover um arquivo/diretório",
                        "wa": "utilize 'wa [path do arquivo] [texto entre aspas]' para inserir dados dentro de um arquivo",
                        "ra": "utilize 'ra [path do arquivo]' para visualizar o conteúdo de um arquivo"
                    }
                    for cmd, descricao in help.items():
                        print(f"comando {cmd:6} {descricao}")
