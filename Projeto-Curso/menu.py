from Funcao import *
from banco_dados import *
from time import sleep

while True:
    print('\n===== Projeto Menu =====') 
    print('''
1- Inserir Tarefas
2- Remover Tarefas
3- Listar Tarefas
4- Marcar Tarefas concluidas
5- Exibir Tarefas 
6- Sair\n''')
    
    opcao = int(input('Digite uma opção: '))
    match opcao:
        case 1:
            adicionar_lista(lista)
        case 2:
            print('-='*20)
            print('>>>>>>Remover Tarefas<<<<<')
            print('-='*20)
            listar_lista(lista)
            Removed_list(lista)   
        case 3:
            print('-='*20)
            print('>>>>>>Lista de Tarefas<<<<<')
            print('-='*20)
            listar_lista(lista)
        case 4:
            print('-='*20)
            print('>>>>>>Marcar Tarefas<<<<<')
            print('-='*20)
            listar_lista(lista)
            sleep(1)
            marcar_lista(lista)
        case 5:
            exibir_Tarefas(lista)
        case 6:
            print('Saindo do programa.')
            break
        case _:
            print('Opção Invalida, Tente novamente.')
            

            