from socket import *
import sys
import time

#Req1: O cliente deverá receber como entrada um endereço ip (ou nome de host) e um número de porta. 

def  conecta_server(): #criação de função para conectar com servidor
    serverName = input("Entre com o endereço do servidor") or "localhost"
    serverPort = int(input("Entre com a porta do servidor"))

    #criacao do socket
    clientSocket = socket(AF_INET, SOCK_STREAM,0)

    # Conexao com o servidor
    clientSocket.connect((serverName,serverPort))

    return clientSocket


#Req2: . Enquanto o servidor aguarda completar quatro jogadores, o cliente deverá exibir uma mensagem na tela informando o jogador dessa situação.

class Jogador:  #classe jogador para armazenar nome e conexão

	def __init__(self, nomeJogador, conexao, bytesRecebidos):
		self.nomeJogador = nomeJogador
		self.conexao = conexao
		self.bytesRecebidos = bytesRecebidos #número de bytes recebidos pela conexão  


#Função para realizar a leitura correta das mensagens recebidas.
def ler_msg(bytesRecebidos,data):
    qtdArmazenada = bytesRecebidos #quantidade de bytes já recebidos por aquela conexão  
    qtdRecebida = len(data) # contar quantidades de bytes (atual msgs_antigas+msg_nova)

    data = data.decode() # passando mensagem em bytes para string
    
    msgEsperada = data[(qtdArmazenada-1):] #corta a string a partir da quantidade ja recebida até o final
    return msgEsperada


mesaJogadores = [] #array para montar a mesa da partida
numMinJogadores = 3 #variavel auxiliar no controle de jogadores


for i in range(0,4):

    #### REALIZANDO CONEXÃO E ARMAZENANDO JOGADOR 
    nome = input('Digite seu nome: ')
    conexao = conecta_server() #realiza conexão com servidor 
    j = Jogador(nome, conexao, 0) #cria jogador
    autorizacao = conexao.recv(4096) #autorização do server se o jogo deve começar ou não
    j.bytesRecebidos = j.bytesRecebidos+len(autorizacao) #armazenando a quantidade de bytes recebidos
    mesaJogadores.append(j) #mesa recebe jogadores

    ### VERIFICAÇÃO SE TODOS OS JOGADORES ESTÃO ONLINE
    if (autorizacao==b'0'):
        print('A mesa ainda não está completa. Aguardando mais',numMinJogadores,'jogadores...')
        numMinJogadores=numMinJogadores-1
        
    if (autorizacao==b'1'):
        print('Vamos começar!')
        fimJogo=False #variável de permissão para iniciar o jogo no cliente 
        
		

while (fimJogo==False):
    
    cont = 0
    for i in mesaJogadores: #For para exibir as cartas
        data = i.conexao.recv(4096) #cliente escuta servidor
        print (mesaJogadores[cont].nomeJogador, ',sua mão é ', data , '\n') #exibe última mensagem
        mesaJogadores[cont].bytesRecebidos += len(data)
        cont +=1
        
    cont = 0
    time.sleep(1) #Delay para receber o VIra  
    for i in mesaJogadores: #For para exibir o vira
        data = i.conexao.recv(4096) #cliente escuta servidor
        print('\n',mesaJogadores[cont].nomeJogador,',o Vira é ', data) 
        mesaJogadores[cont].bytesRecebidos += len(data)
        cont +=1
    
        
    for i in range(0,4): #Escolher uma carta da mão
        print('')
        print('----MENU------')
        print(mesaJogadores[i].nomeJogador,', escolha uma opção abaixo:')
        print('1) Escolher uma carta')
        print('2) Truco')
        escolha = int(input("Informe sua opção: "))
        if (escolha == 1):
            cartaEscolhida = int(input("Escolha uma carta (1 a 3): "))
            visibilidade = int(input("Digite 0 para aberta e 1 para fechada:"))
            ''' A ídeia é que concatene as 2 opções, por exemblo, se a escolha for
            a carta 2 e que ela seja fechada, passaria para o servidor o valor 20
            '''
            escolhafinal = str(cartaEscolhida)+str(visibilidade) #Concatenar as strings
            mesaJogadores[i].conexao.send(escolhafinal.encode('utf-8')) #Enviar para o servidor
        else:
            mesaJogadores[i].conexao.send(str(escolha).encode('utf-8')) #Se escolher o 2 é truco
    cont=0
    print('------- Cartas escolhidas --------')    
    for i in mesaJogadores: #Mostar as cartas que foram escolhidas
        data = i.conexao.recv(4096) #cliente escuta servidor
        print(mesaJogadores[cont].nomeJogador, data, '\n')
        mesaJogadores[cont].bytesRecebidos += len(data)
        cont+=1
    cont = 0
    print('------- Ganhador da rodada --------')
    for i in mesaJogadores: #Mostar quem ganhou a rodada
        data = i.conexao.recv(4096) #cliente escuta servidor
        print(mesaJogadores[cont].nomeJogador, data, '\n')
        mesaJogadores[cont].bytesRecebidos += len(data)
        ++cont
    print('---------------')
    time.sleep(1) #Delay 
