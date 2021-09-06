
#Função que recebe um número int e retorna o mesmo em String, formatada
#com pontos separando as centenas
def int_to_string(num):
    #Conversao inteiro para string
    numero = str(int(num))
    #Armazena tamanho do numero que será formatado
    tamanho = len(numero)
    
    #Caso não seja necessário adicionar pontos no meio do número (números de três dígitos)
    if tamanho <= 3:
        return numero
    
    #Caso o tamanho do número não seja divisível por três, separa o número em duas partes
    if tamanho % 3 != 0:
        numero_parte01 = numero[:tamanho % 3] + '.'

    else:
        numero_parte01 = ''

    numero_parte02 = numero[tamanho % 3:]
    
    #Calcula o número de substrings (com tamanho fixo de 3 dígitos) que surgirão da string inicial 'numero'
    n_intervalos = len(numero_parte02) // 3
    
    #Inicializa as variáveis necessárias
    cont = 0
    substrings = []
    numero_atualizado_parte02 = ''
    
    #Faz a divisão da string inicial em substrings de acordo com 'n_intervalos'
    while cont < n_intervalos:
        substrings.append(numero_parte02[cont*3:(cont+1)*3])
        cont += 1
    
    #Concatena as substrings em uma string, separadas por '.'
    for string in substrings:
        if len(numero_atualizado_parte02) != 0:
            numero_atualizado_parte02 = numero_atualizado_parte02 + '.' + string
        else:
            numero_atualizado_parte02 = numero_atualizado_parte02 + string

    #Retorna o número formatado
    return numero_parte01 + numero_atualizado_parte02


#Caso tenha apenas um dígito, formata o número para dois dígitos. Ao final, retorna o número atualizado como string.
def formata_numero(numero):
    string = str(numero)
    
    if len(string) == 1:
        string = '0' + string

    return string