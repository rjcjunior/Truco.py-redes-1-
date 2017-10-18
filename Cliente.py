from socket import *


#Req1: O cliente deverá receber como entrada um endereço ip (ou nome de host) e um número de porta. 

def  conecta_server(): #criação de função para conectar com servidor
    serverName = input('Digite o IP do servidor:')
    serverPort = int(input('Digite a porta do servidor:'))

    #criacao do socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Conexao com o servidor
    clientSocket.connect((serverName,serverPort))

    return clientSocket


#Req2: . Enquanto o servidor aguarda completar quatro jogadores, o cliente deverá exibir uma mensagem na tela informando o jogador dessa situação.

class Jogador:  #classe jogador para armazenar nome e conexão

	def __init__(self, nomeJogador, conexao):
		self.nomeJogador = nomeJogador
		self.conexao = conexao



mesaJogadores = [] #array para montar a mesa da partida
aux = 3 #variavel auxiliar no controle de jogadores

for i in range(0,4):

    nome = input('Digite seu nome: ')
    conexao = conecta_server()
    j = Jogador(nome, conexao)
    mesaJogadores.append(j) #mesa recebe jogadores 
    #verificar autorização de início do jogo 
    autorizacao = conexao.recv(1024) #autorização do server se o jogo deve começar ou não
    if (autorizacao==b'0'):
        print('A mesa ainda não está completa. Aguardando mais',aux,'jogadores...')
        aux=aux-1

    if (i==3):
        fimJogo=False


while (fimJogo==False):
    for i in mesaJogadores:
        print (i.conexao.recv(1024))
    
#print('Vamos começar!')
#toda a lógica do jogo aqui.

	


	




