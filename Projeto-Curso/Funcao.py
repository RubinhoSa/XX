def adicionar_lista(bd:list,status:bool=False) -> dict:
    while True:
        texto = input('Digite o Texto da tarefa: ')
        bd.append({'texto_tarefa':texto, 'status':status})
        print( f'\033[32mTarefa "{texto}" adicionada com sucesso!\033[m')
        continuar = input('Deseja continuar S/N: ')
        if continuar in 'Nn':
            break
        elif continuar in 'Ss':
            continue
        else:
            print('Opção invalida, Tente novamente.')
            continuar = input('Deseja continuar S/N: ')
        

def Removed_list(bd:list,status:bool=False) -> dict:
    while True:
        remover = input('Digite o Texto que deseja deletar: ')
        bd.remove({'texto_tarefa':remover, 'status':status})
        print(f'\033[31mTarefa "{remover}" Removido com sucesso!\033[m')
        continuar = input('Deseja continuar S/N: ')
        if continuar in 'Nn':
            break
        elif continuar in 'Ss':
            continue
        else:
            print('Opção invalida, Tente novamente.')
            continuar = input('Deseja continuar S/N: ')

def listar_lista (bd:list):
    count = 0
    for i in bd:
        count+= 1
        print(count,'-',i['texto_tarefa'])
        
def marcar_lista(bd: list, status: bool = False) -> dict:
    marcar = input('Qual item deseja marcar como concluido? ')
    for i in bd:
        if marcar == i['texto_tarefa']:
            i['status'] = True
            print(f'\x1b[9m {marcar} \x1b[0m')
            break
        
def exibir_Tarefas(bd: list) -> dict:
    for i in bd:
        if i["status"]:
            status = "Concluída"
        else:
            status = "Pendente"
        print(f'Tarefa: {i["texto_tarefa"]}, Status: {status}')


