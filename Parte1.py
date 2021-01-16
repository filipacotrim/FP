 #Filipa Cotrim, 95572

def eh_labirinto(maze):
 '''funcao que recebe qualquer tipo de argumento e devolve True or False, se 
 esse argumento corresponder a um labirinto ou nao,respetivamente, e tendo em 
 conta todas as condicionantes(paredes,tamanhos,caracteres,...''' 
 if not isinstance(maze,tuple):    #maze tem de ser tuplo
     return False
 if not len(maze)>=3:        #maze tem de ser constituido por pelo menos
     return False              #tres tuplos
 for t in maze:
     if not (isinstance(t,tuple)\
             and len(t)>=3):  #cada t (equivalente a linhas) tem de ter 
         return False              #comprimento maior que tres                   
     for i in t:
         if i != 1 and i != 0 or not isinstance(i,int):
             return False    #tem de ter exclusivamente 0's e 1's (inteiros)
 col = len(maze[0])
 for i in range(1, len(maze)):    # igual nr de linhas, isto e, comprimen-
     if not col == len(maze[i]):   #to de cada tuplo igual ao longo
         return False                        #do maze
 i = 0
 tuplo1 = ()
 while i != col:     #diferente de len(maze[0]) pois os comprimentos vao ser              
     tuplo1 = tuplo1 + (1,)        #iguais, isto e, maze[0]=maze[1]=(...)
                         #logo queria criar um tuplo que representasse as 
     i += 1              #paredes de cada maze, dependendo do seu tamanho
 
 if maze[0] != tuplo1 or maze[-1] != tuplo1: 
                                    #maze[0] eh a primeira coluna e
     return False                  #e maze[-1] eh a ultima coluna pelo que
                              #tem necessariamente de ser paredes, isto eh,
 for i in maze[1:(len(maze)-1)]:      #tem de ter apenas 1s
     if i[0] != 1 and i[-1] != 0:     #Todos os tuplos dentro do maze,isto eh
         return False              #todos as colunas tem de comecar e acabar 
                                        #por 1's                                                                 
 else:
     return True
    

def eh_posicao(coord):
 '''funcao que recebe um tuplo de coordenadas e devolve True or False se 
 respeitar as condicionantes referidas (tuplo de 2 inteiros positivos)'''
 if not isinstance(coord,tuple):     #coordenadas tem de ser tuplo
     return False
 if not len(coord) == 2:         #coordenadas com apenas (x,y)
     return False
 for k in coord:
     if not isinstance(k, int) or k < 0:   
         return False       #as oordenadas tem de ser inteiros positivos
 else:
     return True

def eh_conj_posicoes(unidades):  
 ''' funcao que recebe um conjunto de coordenadas e avalia, uma a uma, se 
 corresponde a um tuplo de coordenadas valido a partir da funcao anterior'''
 if not isinstance(unidades,tuple):     #tem de ser tuplo
  return False
 for i in unidades:
  if not isinstance(i,tuple):
   return False
  if eh_posicao(i) is False:
   return False
 if not len(tuple(set(unidades))) == len(unidades):    #nao pode haver coordenadas iguais nas
   return False                      #unidades e cada coordenada tem             
 else:                                #de se verificar ser posicao pela 
  return True                          #funcao anterior
        
def tamanho_labirinto(maze): 
 '''funcao que recebe um labirinto, que tem de se verificar ser verdadeiro
 e devolve o seu tamanho em que a ordenada x corresponde ao numero de colunas
 e y ao numero de linhas'''
 if eh_labirinto(maze) is False:  #maze tem de ser labirinto valido
     raise ValueError('tamanho_labirinto: argumento invalido')
 for t in maze:
     return (len(maze),len(t))   #vai devolver 
                              #(numero de colunas, numero de linhas)
                                   
def eh_mapa_valido(maze,unidades):
 ''' funcao que recebe um labirinto, necessariamente verdadeiro caso contrario
 da erro, e um conjunto de coordenadas e verifica se cada uma se verifica ser 
 posicao, isto e, se nao corresponde a nenhuma parede no maze valido dado''' 
 if eh_labirinto(maze) is False:      #maze tem de ser labirinto valido
     raise ValueError('eh_mapa_valido: algum dos argumentos e invalido')
 if eh_conj_posicoes(unidades) is False:  
     raise ValueError('eh_mapa_valido: algum dos argumentos e invalido')
 #todas as coordenadas do conjunto de coords tem de ser validas
 else:
     tuplos = unidades[:]
     for i in tuplos:               
         if not i[0] <= len(maze): 
             return False               
         if not i[0] > 0:    
             return False 
    #a ordenada x tem de corresponder a uma coluna do maze, logo nao pode  
  #ultrapassar o seu comprimento que,por sua vez, tambem nao pode ser menor que
  #zero sendo que nao eh possivel nr de colunas negativo             
         for t in maze:          
             if not i[1] <= len(t) or i[1] == 0: 
                 return False    
             x = i[0]
             y = i[1]
             if not maze[x][y]==0:
                 return False       #nao pode corresponder a uma parede
 #a ordenada y tem de corresponder a uma linha do maze,pelo q nao pode exceder
       #o seu comprimento,que, por sua vez, nao pode ser menor que zero   
                                           
     else:
         return True

def eh_posicao_livre(maze,unidades,coords):
 '''funcao que recebe um labirinto,unidades(conjunto de coordenadas) e coordena
 -das, avaliando cada um delas pelas funcoes anteriores e devolve true ou false
 se as coordenadas no maze corresponderem a espacos nao ocupados por unidades
 nem por paredes'''
 if eh_labirinto(maze) is False:
     raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')
 if eh_conj_posicoes(unidades) is False:
     raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
 if eh_posicao(coords) is False:
     raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
 if eh_mapa_valido(maze,unidades) is False:
     raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
 for t in unidades:
     if not t != coords:   #coords nao podem corresponder a unidades
         return False
     x = coords[0]
     y = coords[1]
     if not maze[x][y] == 0: #coords nao podem corresponder a paredes no maze
         return False
 else:
     return True
    
def posicoes_adjacentes(coords):
 '''funcao que recebe um tuplo de coordenadas e devolve todas as suas adjacentes
 tendo em conta as condicionantes da posicao dela'''
 if eh_posicao(coords) is False:
     raise ValueError('posicoes_adjacentes: argumento invalido')
 x = coords[0] 
 y = coords[1]   
 if (x == 0) and (y != 0):
     return ((x,y-1),(x+1,y),(x,y+1))
# sendo o x igual a zero entao vai pertencer ah primeira coluna, pelo que nao
#tem adjacentes a sua esquerda
 if (x != 0) and (y == 0):
     return (x-1,y),(x+1,y),(x,y+1)  
#sendo o y igual a zero entao vai pertencer ah a primeira linha, pelo que nao
#tem adjacentes em cima 
 if x > 0 and y > 0:
     return ((x,y-1),(x-1,y),(x+1,y),(x,y+1)) 
 #sendo ambas diferentes, e por consequentemente,maiores que zero, tem 4 
 #adjacentes, (em cima,baixo,esquerda e direita)
 if (x and y) == 0:
     return ((x+1,y),(x,y+1))
 #sendo ambas igual a zero entao vai estar na posicao (0,0) e so tem adjacente
 #a direita e em baixo

def mapa_str(maze,unidades):
 '''funcao que recebe um labirinto e um conjunto de coordenadas e devolve a 
 representacao grafica do mesmo com as unidades ocupadas representadas'''
 if eh_labirinto(maze) is False or eh_conj_posicoes(unidades) is False:
     raise ValueError('mapa_str: algum dos argumentos e invalido')
 if eh_mapa_valido(maze,unidades) is False:
     raise ValueError('mapa_str: algum dos argumentos e invalido')
 dimensao = tamanho_labirinto(maze)
 col = dimensao[0]       #sendo q todas as colunas tem igual tamanho
 linhas = dimensao[1]     #sendo q todas as linhas tem igual tamanho
 str_1 = ''
 for k in range(linhas):
     for l in range(col):
         if maze[l][k] == 1:
             str_1 = str_1 + '#'  #se as coordenadas no maze for 1 equivale
         else:                     #uma parede, pelo que se torna '#'
             if (l,k) not in unidades:
                 str_1 = str_1 + '.'      #se uma posicao no maze nao estiver
             else:                   #referida nas unidades equivale a um'.'
                 str_1 = str_1 + 'O'   #caso contrario, identifica-se a 
     str_1 = str_1 + '\n'                #posicao como 'O'
 str_1 = str_1 [:-1]
 return str_1


def obter_objetivos(maze,unidades,coords):
 '''recebe um labirinto, um conjunto de coordenadas e um tuplo de coordenadas 
 que tem necessariamente de estar nas unidades e vai devolver todos os possiveis
 objetivos, isto e, as adjacentes das unidades diferentes das coords'''
 if eh_labirinto(maze) is False:
     raise ValueError('obter_objetivos: algum dos argumentos e invalido')
 if eh_conj_posicoes(unidades) is False:
     raise ValueError ('obter_objetivos: algum dos argumentos e invalido')
 if eh_posicao(coords) is False:
     raise ValueError('obter_objetivos: algum dos argumentos e invalido')
 if eh_mapa_valido(maze,unidades) is False:
     raise ValueError('obter_objetivos: algum dos argumentos e invalido')
 if coords not in unidades:
     raise ValueError('obter_objetivos: algum dos argumentos e invalido')
 p_origem = ()
 for posicoes in unidades:
     if posicoes != coords:
         p_origem = p_origem + posicoes     
 #filtrar o tuplo q eh igual as coords, e p_origem vai ser o novo conjunto sem o
 #tuplo repetido
 else:
     t_origens = ()
     for i in range(0,len(p_origem),2):
         t_origens = t_origens + ((p_origem[i],p_origem[i+1]),)
#conversao do conjunto para tuplo de tuplos
 adjacentes = ()
 for i in range(len(t_origens)):
     adjacentes = posicoes_adjacentes(t_origens[i]) + adjacentes
# adjacentes e o tuplo de todas as posicoes adjacentes dos tuplos de t_origens
 #incluindo algumas que possam nao ser validas(pertencer a paredes,...)

 objetivos = ()
 for k in adjacentes:
     if eh_posicao_livre(maze,unidades,k) is True and k not in objetivos:
             objetivos = objetivos + (k,)
 return objetivos   
#vai retornar todas as adjacentes que correspondem a posicoes livres


def obter_caminho(maze,unidades,coords):
 '''funcao que recebe um labirinto, um conjunto de coordenadas e um tuplo
 de coordenadas e devolve o caminho do mesmo ao objetivo'''
 if eh_labirinto(maze) is False or eh_conj_posicoes(unidades) is False\
    or eh_posicao(coords) is False:
     raise ValueError('obter_caminho: algum dos argumentos e invalido')
 if eh_mapa_valido(maze,unidades) is False:
     raise ValueError('obter_caminho: algum dos argumentos e invalido')
 if coords not in unidades:
  raise ValueError('obter_caminho: algum dos argumentos e invalido')
 pos_visitadas = ()
 pos_inicial = coords
 lst_de_exploracao = [[pos_inicial,()]]      
 objetivos = obter_objetivos(maze,unidades,coords)
 while lst_de_exploracao != []:
     pos_atual = lst_de_exploracao[0][0]
     caminho_atual = lst_de_exploracao[0][1]     #algoritmo bfs, 
     if pos_atual not in pos_visitadas:            #instrucoes dadas
         pos_visitadas += (pos_atual,)
         caminho_atual += (pos_atual,)
         if pos_atual in objetivos:        
          return caminho_atual
         else:
             adjacentes = posicoes_adjacentes(pos_atual)
             for t in adjacentes:
                 if eh_posicao_livre(maze,unidades,t) is True:
                     lst_de_exploracao += [(t,caminho_atual),]            
     del(lst_de_exploracao[0])      

 return ()

def mover_unidade(maze,unidades,coords):
 '''funcao que recebe um labirinto,um conjunto de coordenadas e coordenadas que
 permite mover as unidades ate que estas mesmas sejam adjacentes'''
 if eh_labirinto(maze) is False or eh_conj_posicoes(unidades) is False or eh_posicao(coords) is False:
     raise ValueError('mover_unidade: algum dos argumentos e invalido')
 if eh_mapa_valido(maze,unidades) is False:
     raise ValueError('mover_unidade: algum dos argumentos e invalido') 
 if coords not in unidades: 
     raise ValueError('mover_unidade: algum dos argumentos e invalido')
 if (coords,) == unidades:
  return unidades
 caminho = obter_caminho(maze,unidades,coords)
 tds_adjs = ()
 for i in range(len(unidades)):      
     if unidades[i] == coords:      #identificacao do indice das unidades
         indice = i
     if caminho == ():
      return unidades         
     else:
         adjs = posicoes_adjacentes(unidades[i])  #calculo das adjacentes do
                                      #da unidade identificada
         for k in range(len(adjs)):                 
             if adjs[k] not in tds_adjs:   
                 tds_adjs = (adjs[k],) + tds_adjs
 if coords in tds_adjs:     #se a unidade identificada estiver adjacente
     return unidades          #ah outra entao nao se move pois
                            #a posicao ja esta ocupada com a unidade

 novas_unidades = unidades[:indice] + (caminho[1],) + unidades[indice+1:]
 return novas_unidades
    
    




                        
            
    
                    
    

