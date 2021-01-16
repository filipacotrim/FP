#Filipa Cotrim 95572

##############################2_Projeto##############################
'''
---------------------------------------------------------------------
TAD posicao (2.1.1)
FUNCOES:
cria_posicao              : N --> posicao
cria_copia_posicao        : posicao --> posicao
obter_pos_x               : posicao --> N
obter_pos_y               : posicao --> N
eh_posicao                : universal --> booleano
posicoes_iguais           : posicao x posicao --> booleano
posicao_para_str          : posicao --> str
obter_posicoes_adjacentes : posicao --> tuplo de posicoes
Abstracao usada           : Listas
---------------------------------------------------------------------
'''

def cria_posicao(x,y):
 '''recebe coordenadas de uma posicao e devolve a posicao corres- \
 pondente'''
 if not (isinstance(x,int) and isinstance(y,int) and \
         x >= 0 and y >= 0):    
  raise ValueError ("cria_posicao: argumentos invalidos")
 posi = [x,y]      #uso de listas 
 return posi
    
def cria_copia_posicao(posi):
 '''recebe uma posicoa e devolve uma copia da mesma'''
 return cria_posicao(posi[0],posi[1])

def obter_pos_x(posi):
 '''recebe uma posicao valida e devolve a coordenada x'''
 return posi[0]

def obter_pos_y(posi):
 ''' recebe uma posicao valida e devolve a coordenada y'''
 return posi[1]

#-------------------------------Reconhecedor-----------------------------------

def eh_posicao(arg):
 '''funcao que recebe um argumento e verifica a sua validade, isto e \ 
 se se trata de uma posicao ou nao'''    #aqui tem de verificar se e tuplo???
 if not (isinstance(arg,list) and len(arg) == 2):
  return False
#o argumento tem de ser um tuplo com 2 coordenadas, x e y, necessariamente
 x = obter_pos_x(arg)
 y = obter_pos_y(arg)
 if not (isinstance(x,int) and isinstance(y,int) and \
         x >= 0 and y >= 0):
#as coordenadas da posicao tem de contar inteiros positivos
  return False
 return True
#-------------------------------Teste-----------------------------------------
def posicoes_iguais(posi1,posi2):
 '''funcao que recebe duas posicoes e compara-as verificando se \
 sao iguais ou nao'''
 if not (obter_pos_x(posi1) == obter_pos_x(posi2) and\
     obter_pos_y(posi1) == obter_pos_y(posi2)):
  return False
 return True

#-------------------------Transformador----------------------------------------

def posicao_para_str(posi):
 '''funcao que recebe uma posicao e devolve essa mesma posicao em string'''
 return ('(' + str(obter_pos_x(posi)) + ', ' + str(obter_pos_y(posi)) + ')')

#--------------------------Funcao de alto nivel--------------------------------

def obter_posicoes_adjacentes(posi):
 '''funcao que recebe um tuplo de coordenadas e devolve todas as suas adjacentes
 tendo em conta as condicionantes da posicao dela'''
 x = obter_pos_x(posi)
 y = obter_pos_y(posi)
 if (x == 0) and (y != 0):
     return ([x,y-1],[x+1,y],[x,y+1])
# sendo o x igual a zero entao vai pertencer ah primeira coluna, pelo que nao
#tem adjacentes a sua esquerda
 if (x != 0) and (y == 0):
     return ([x-1,y],[x+1,y],[x,y+1])
#sendo o y igual a zero entao vai pertencer ah a primeira linha, pelo que nao
#tem adjacentes em cima 
 if x > 0 and y > 0:
     return ([x,y-1],[x-1,y],[x+1,y],[x,y+1])
 #sendo ambas diferentes, e por consequentemente,maiores que zero, tem 4 
 #adjacentes, (em cima,baixo,esquerda e direita)
 if (x and y) == 0:
     return ([x+1,y],[x,y+1])
 #sendo ambas igual a zero entao vai estar na posicao (0,0) e so tem adjacente
 #a direita e em baixo
 
 '''
 --------------------------------------------------------------
 TAD unidade (2.1.2)
 FUNCOES
 cria_unidade         : posicao x N x N x str --> unidade
 cria_copia_unidade   : unidade --> unidade
 obter_posicao        : unidade --> posicao
 obter_exercito       : unidade --> str
 obter_forca          : unidade --> N
 obter_vida           : unidade --> N
 muda_posicao         : unidade x posicao --> unidade
 remove_vida          : unidade x N --> unidade
 eh_unidade           : universal --> booleano
 unidades_iguais      : unidade x unidade --> booleano
 unidade_para_char    : unidade --> str
 unidade_para_str     : unidade --> str
 unidade_ataca        : unidade x unidade --> booleano
 ordenar_unidades     : tuplo unidades --> tuplo unidades
 abstracao usada      : Listas
 -------------------------------------------------------------
 '''
 

#-------------------Construtor--------------------------------------

def cria_unidade(posi,vida,frc,cc):
 '''funcao que recebe uma posicao, vida, forca e cadeia de caracteres \
 e devolve a sua unidade, validando cada argumento'''
 if not (eh_posicao(posi) and isinstance(vida,int) and \
         vida > 0 and isinstance(frc,int) and frc > 0 and \
         isinstance(cc,str) and len(cc) > 0):     
  raise ValueError ("cria_unidade: argumentos invalidos")
 unidade = [posi,vida,frc,cc]
 return unidade

def cria_copia_unidade(u):
 '''funcao que recebe uma unidade valida e devolve uma copia da mesma'''
 return cria_unidade(cria_copia_posicao(obter_posicao(u)),obter_vida(u),\
                     obter_forca(u),obter_exercito(u))

#---------------------------Seletor---------------------------------
def obter_posicao(u):
 '''funcao que devolve a posicao de uma unidade'''
 return (u[0])

def obter_exercito(u):
 '''funcao que devolve o exercito de uma unidade'''
 return (u[3])

def obter_forca(u):
 '''funcao que devolve a forca de uma unidade'''
 return (u[2])

def obter_vida(u):
 '''funcao que devolve a vida de uma unidade'''
 return (u[1])

#-------------------------------Modificadores-----------------------

def muda_posicao(u,p):
 '''funcao que recebe uma unidade e uma posicao e devolve a unidade \
 com a posicao p'''
 nova_posi = p
 u[0] = nova_posi
 return u              #modifica u, mudando posicao

def remove_vida(u,v):
 '''funcao que recebe uma unidade e um valor de vida e devolve a unidade com \
 o valor de vida v'''
 vida = obter_vida(u) - v
 u[1] = vida
 return u             #modifica u, mudando vida de u por v

#-----------------------------Reconhecedor--------------------------

def eh_unidade(arg):
 '''funcao que recebe um argumento e verifica se se trata de uma unidade \
 valida, tendo em conta todas as condicionantes'''
 if not (isinstance(arg,list) and len(arg) == 4):
  return False    #len = 4 e list pois e necessariamente [posi,vida,frc,cc]
 posi = obter_posicao(arg) 
 vida = obter_vida(arg)                   
 frc = obter_forca(arg)                   
 cc = obter_exercito(arg)
 if not (eh_posicao(posi) and isinstance(vida,int) and \
     vida > 0 and isinstance(frc,int) and frc > 0 and \
     isinstance(cc,str) and len(cc) > 0):
  return False
 else:
  return True 
#------------------------Teste-------------------------------------
 
def unidades_iguais(u1,u2):
 '''funcao que recebe duas unidades e verifica se sao iguais ou nao'''
 if (posicoes_iguais(obter_posicao(u1),obter_posicao(u2)) \
     and obter_vida(u1) == obter_vida(u2) \
     and obter_forca(u1) == obter_forca(u2) \
     and obter_exercito(u1) == obter_exercito(u2)):
  return True       #tem de ter tds argumentos iguais 
 return False
#--------------------Transformador----------------------------------

def unidade_para_char(u):
 '''funcao que recebe uma unidade e devolve o primeiro caracter do seu \
 exercito em maiusculo'''
 e = obter_exercito(u) 
 return e[0].upper()

def unidade_para_str(u):
 '''funcao que recebe uma unidade e imprime a letra maiuscula do exercito \
 seguido do valor da sua vida e forca (em lista), de um '@' e da sua posicao \
 em tuplo'''
 posi = obter_posicao(u)  
 vida = obter_vida(u)
 forca = obter_forca(u)
 upper = unidade_para_char(u)
 lista_v_frc = [vida,forca]     #para o print da lista com a vida e forca
 return str(upper)+str(lista_v_frc)+'@'+ \
        ('(' + str(obter_pos_x(posi)) + ', ' + str(obter_pos_y(posi)) + ')')

#------------------Funcoes de alto nivel-------------------------

def unidade_ataca(u1,u2):
 '''funcao que recebe duas unidades e simula o ataque da primeira ah segunda \
 devolvendo se a mesma foi destruida ou nao'''
 vida = obter_vida(u2)
 frc = obter_forca(u1)
 vida2 = vida - frc
 u2 = remove_vida(u2,frc)   #u2 eh modificado, subtraindo a frc de ataque de u1
 if vida2 <= 0:                       #ah vida do u2
  return True
 return False

def ordenar_unidades(t):
 '''funcao que recebe um conjunto de unidades e devolve o mesmo conjunto 
 mas ordenado seguindo a leitura do labirinto'''
 def aux(u):
  posi = obter_posicao(u)
  x = obter_pos_x(posi)
  y = obter_pos_y(posi)
  return (y, x)
 return tuple(sorted(t, key=aux))     #so assim organiza tendo em conta a ordem
                                    #do mapa, colunas e linhas

'''
------------------------------------------------------------------
TAD mapa (2.1.3)
FUNCOES
cria_mapa                 : tuplo x tuplo x tuplo x tuplo --> mapa
cria_copia_mapa           : mapa --> mapa
obter_tamanho             : mapa --> tuplo
obter_nome_exercitos      : mapa --> tuplo
obter_unidades_exercito   : mapa x str --> tuplo
obter_todas_unidades      : mapa --> tuplo
obter_unidade             : mapa x posicao --> unidade
eliminar_unidade          : mapa x unidade --> mapa
mover_unidade             : mapa x unidade x posicao --> mapa
eh_posicao_unidade        : mapa x posicao --> booleano
eh_posicao_corredor       : mapa x posicao --> booleano
eh_posicao_parede         : mapa x posicao --> booleano
mapas_iguais              : mapa x mapa --> booleano
mapa_para_str             : mapa --> str
obter_inimigos_adjacentes : mapa x unidade --> tuplo unidades
obter_movimento           : mapa x unidade --> posicao
abstracao usada           : listas
-------------------------------------------------------------------
'''


#-------------------------Construtor-------------------------------

def cria_mapa(d,w,e1,e2):    
 '''funcao que recebe uma dimensao, um conjunto de paredes, e 2 \
 tuplos de uma ou mais unidades de dois exercitos diferentes'''
 if not (isinstance(d,tuple) and len(d) == 2):
  raise ValueError ('cria_mapa: argumentos invalidos')
 nx = d[0]  #linhas do mapa
 ny = d[1]     #colunas do mapa
 if not (isinstance(nx,int) and isinstance(ny,int) \
         and nx >= 3 and isinstance(ny,int) \
         and ny >= 3 and \
         isinstance(w,tuple) and \
         isinstance(e1,tuple) and e1 != () and isinstance(e2,tuple) \
         and e2 != ()):
  raise ValueError ('cria_mapa: argumentos invalidos')
#d representa a dimensao do mapa em tuplo, com dimensao minima de 3x3
 for parede in w:
  if not (isinstance(parede,list) and parede[0] > 0 and parede[0] < (nx - 1) and \
          parede[1] > 0 and parede[1] < (ny - 1)): 
   #paredes sao listas pois sao posicoes
   raise ValueError ('cria_mapa: argumentos invalidos')
#w representa as paredes do mapa, no entando nao podem corresponder as dos
#limites do mapa
 for uni in e1:
  if not eh_unidade(uni):
   raise ValueError ('cria_mapa: argumentos invalidos')
#todas as unidades de e1 e e2 tem de ser argumentos validos
 for uni in e2:
  if not eh_unidade(uni):
   raise ValueError ('cria_mapa: argumentos invalidos')
 else:
  return [d,w,e1,e2]
 
 
def cria_copia_mapa(m):
 '''funcao que recebe um mapa valido e devolve uma copia do mesmo'''
 p = ()
 for paredes in m[1]:
  p += (cria_copia_posicao(paredes),)     #w pode ser tuplo vazio
 e1 = ()
 for u1 in m[2]:                       
  e1 += (cria_copia_unidade(u1),)      
 e2 = ()                       
 for u2 in m[3]:
  e2 += (cria_copia_unidade(u2),)
 return cria_mapa(obter_tamanho(m),p,e1,e2)
#nesta parte do projeto assume-se que os exercitos sao compostos por uma ou 
#mais unidades, no entanto, para a ultima funcao e relevante esta condicao
#pois ao simular a batalha eventualmente um exercito morre e fica um 
#tuplo vazio

#---------------------------Seletores---------------------------- 

def obter_tamanho(m):
 '''funcao que recebe um mapa e devolve o tamanho do mesmo'''
 return m[0]        #primeiro tuplo de m (d)

def obter_nome_exercitos(m):  
 '''funcao que recebe um mapa e devolve o nome dos dois exercitos existentes'''
 if m[2] and m[3] == ():
  return ('','')
 if m[2] == () and m[3] != ():
  return tuple(sorted(('',m[3][0][3])))
 if m[2] != () and m[3] == ():
  return tuple(sorted(('',m[2][0][3]))) 
 #ate aqui o codigo desta funcao so e relevante para a ultima funcao pois,
 #novamente, ate aqui se assume que ambos os exercitos nao podem ser 
 #tuplos vazios
 else:
  nome_e1 = m[2][0][3]   
  nome_e2 = m[3][0][3]    
  t = (nome_e1,nome_e2)
  return tuple(sorted(t))

def obter_unidades_exercito(m,e):
 '''funcao que recebe um mapa e um exercito e devolve todas as unidades do \
 mapa que per tencem a esse mesmo exercito'''
 #linhas de codigo seguintes sao novamente apenas necessarias para simular
 #batalhas, mais especificamente quando um dos exercitos morre, isto e 
 #fica sem unidades
 if len(m[2]) == 0 and len(m[3]) == 0:
  return ()
 #se ambos ficarem sem unidades
 
 if len(m[2]) == 0:
  if obter_exercito(m[3][0]) != e:
   return ()
#se e1 ficar sem unidades e exercito e for igual ao exercito de e2
  
  else:
   return ordenar_unidades(m[3])  
 #se e1 ficar sem unidades mas exercito e e igual ao exercito de e1
 
 elif len(m[3]) == 0:
  if obter_exercito(m[2][0]) != e:
   return ()
  else:
   return ordenar_unidades(m[2])  
 
 #considerar para esta parte do projeto a partir daqui
 if obter_exercito(m[2][0]) != e:
  return ordenar_unidades(m[3])
 else:
  return ordenar_unidades(m[2])
 #o exercito e esta necessariamente ou no primeiro exercito do mapa ou no 
 #segundo 
  

 
def obter_todas_unidades(m):
 '''funcao que recebe um mapa e devolve todas as unidades desse mapa'''
 e1 = m[2]
 e2 = m[3]
 todas_u = e1+e2
 #todas_u representa unidades dos 2 exercitos, e1 e e2, porem nao ordenadas
 return ordenar_unidades(todas_u)    #ja ordenadas segundo a ordem do labirinto

def obter_unidade(m,p):
 '''funcao que recebe um mapa e uma posicao e devolve a unidade ocupada \
 por essa posicao'''
 e1 = m[2]
 e2 = m[3]
 for u1 in e1:
  if p in u1:
   return u1
#percorre as unidades pertencentes ao primeiro exercito e verifica se ha 
#alguma unidade com a posicao p 
 for u2 in e2:
  if p in u2:
   return u2
#mesmo procedimento para o segundo exercito

#----------------------Modificadores-----------------------------
#Auxiliar
def filtra(tst,lst):
 res = []
 for e in lst:
  if tst(e):
   res = res + [e]
 return tuple(res)

def eliminar_unidade(m,u):
 '''funcao que recebe um mapa e uma unidade e elimina essa unidade 
 do mapa, devolvendo o novo mapa com a unidade ja eliminada'''
 e1 = filtra(lambda x: x!= u, m[2])  #se u estiver no primeiro exercito, 
 #recorre se a funcao filtra para elimina-lo do mesmo
 e2 = filtra(lambda x: x!= u, m[3])
 #o mesmo ocorre para se a unidade estiver no segundo exercito
 m[2] = e1
 m[3] = e2
 return m

def mover_unidade(m,u,p):
 '''funcao que recebe um mapa, uma unidade e uma posicao e devolve 
 o mapa com a unidade u e a posicao p no mapa, devolvendo o proprio 
 mapa'''
 e1 = list(m[2])
 e2 = list(m[3])
 for uni in e1:
  if uni == u:
   muda_posicao(uni,p)
   return m
 for uni in e2:
  if uni == u:
   muda_posicao(uni,p)    #maltera mapa
   return m 
   
   
#-------------------------Reconhecedores--------------------------

def eh_posicao_unidade(m,p):
 '''funcao que recebe um mapa e uma posicao e devolve true se a 
 posicao esta ocupada por alguma unidade e false caso contrario'''
 if isinstance(obter_unidade(m,p),list):
  return True
 return False          
#a funcao obter_unidade apenas retorna algo(uma unidade) se a posicao p 
#estiver ocupada por uma unidade do mapa m, essa unidade e representada por
#uma lista

def eh_posicao_corredor(m,p):
 '''funcao que recebe um mapa e uma posicao e devolve true se a 
 posicao p corresponde a um corredor no labirinto'''
 x = obter_pos_x(p)
 y = obter_pos_y(p)
 nx = obter_tamanho(m)[0]
 ny = obter_tamanho(m)[1]
 w = m[1]
 if not (x != 0 and x != (nx-1) and y != 0 and y != (ny-1)):
  return False
 #condicoes que verificam se a posicao p nao corresponde as paredes dos limites 
 #do mapa, pois so assim pode ser corredor
 for parede in w:
  if parede == p:
   return False
  #w representa paredes (nao dos limites do mapa), entao se p for igual a 
  #alguma dessas paredes entao nao eh corredor
 return True


def eh_posicao_parede(m,p):
 '''funcao que recebe um mapa e uma posicao e devolve true se se p 
 corresponder a uma parede no labirinto'''
 if eh_posicao_corredor(m,p):
  return False
 #se nao e corredor e necessariamente parede
 return True

#-------------------------------Teste-----------------------------

def mapas_iguais(m1,m2):           
 '''funcao que recebe dois mapas e devolve true se estes
 forem iguais'''
 if (obter_tamanho(m1) == obter_tamanho(m2) and \
     obter_todas_unidades(m1) == obter_todas_unidades(m2) \
     and m1[1] == m2[1]):
  return True
 #para serem mapas iguais tem de ter d,w,e1,e2 necessariamentes iguais
 return False

#-----------------------------Transformador------------------------

def mapa_para_str(m):
 '''funcao que recebe um mapa e devolve uma cadeia de caracteres que
 representa o mapa com as unidades representadas pela sua 
 representacao externa'''
 dim = obter_tamanho(m)
 col = dim[0]      
 linhas = dim[1]     
 str_1 = ''
 e1 = obter_unidades_exercito(m,obter_nome_exercitos(m)[1])
 e2 = obter_unidades_exercito(m,obter_nome_exercitos(m)[0])
 for l in range(linhas):
  for c in range(col):
   p = cria_posicao(c,l)
   if eh_posicao_parede(m,p):
    str_1 = str_1 + '#'  #correspondem a paredes
   else:                     
    if eh_posicao_corredor(m,p) and not \
       eh_posicao_unidade(m,p):
     str_1 = str_1 + '.'   
#se p corresponder a um corredor entao representa-se como '.'
    else:                   
     u = obter_unidade(m,p)
     if u in e1:
      str_1 = str_1 + unidade_para_char(u)  #imprime a maiuscula do exercito
     else:
      str_1 = str_1 + unidade_para_char(u)               
  str_1 = str_1 + '\n'
 return str_1 [:-1]
 

def obter_inimigos_adjacentes(m,u):
 '''funcao que recebe um mapa e uma unidade e devolve as unidades 
 inimigas adjacentes a unidade u'''
 e_u = obter_exercito(u)
 e1e2 = obter_nome_exercitos(m)
 posi_u = obter_posicao(u)
 todas_uni = obter_todas_unidades(m)
 uni_e = obter_unidades_exercito(m,e_u)
 adjs = []
 if e_u not in e1e2[0]:     #avaliacao de qual exercito e o inimigo
  for uni in obter_unidades_exercito(m,e1e2[0]):
   #sabendo as unidades inimigas de u, percorro-as com uni
   posi_uni = obter_posicao(uni)    #obtenho posicao de cada unidade
   if posi_uni in obter_posicoes_adjacentes(posi_u):
    #se a posicao da unidade estiver nas posicoes adjacentes de u, \
    #entao e inimigo adjacente
    adjs = [uni] + adjs
 else:                
  for uni in obter_unidades_exercito(m,e1e2[1]):
   #se o exercito da unidade u for e1e2[0] entao percorre-se as unidades de
   #e1e2[1], sendo necessariamente as unidades inimigas
   posi_uni = obter_posicao(uni)
   if posi_uni in obter_posicoes_adjacentes(posi_u):
    adjs = [uni] + adjs   
 return ordenar_unidades(adjs)



def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)

#--------------------Funcoes adicionais------------------------------
'''
calcula_pontos    : mapa x str --> int
simula_turno      : mapa --> mapa
simula_batalha    : str x booleano --> str
'''

def calcula_pontos(m,e):
 '''funcao que recebe um mapa e uma cadeia de caracteres correspondente \
 a um exercito e devolve a soma das vidas das unidades desse mesmo exercito'''
 u_e = obter_unidades_exercito(m,e)   #unidades de m do exercito recebido
 if len(u_e) == 0:
  return 0
 vidas = 0
 for uni in u_e:
  #percorro as unidades de m do exercito recebido e obtenho o valor da vida
  #de cada uma, somando-as
  v_uni = obter_vida(uni)
  vidas += v_uni
 return vidas

def simula_turno(m):
 '''funcao que recebe um mapa e simula um turno de batalha completo'''
 for uni in obter_todas_unidades(m):
  vida = obter_vida(uni) 
  if vida > 0:          #unidades so existem se tiverem vida positiva
   mov = obter_movimento(m,uni)
   mapa = mover_unidade(m,uni,mov)
   inimigos_adjs = obter_inimigos_adjacentes(m,uni)
   if inimigos_adjs != ():        
 #se houverem inimigos adjacentes entao sucede-se um ataque e verifica-se
 #com a funcao eliminar_unidade se a unidade foi destruida ou nao
    if unidade_ataca(uni,inimigos_adjs[0]):
     m = eliminar_unidade(m,inimigos_adjs[0])
     
 return m    

def simula_batalha(cc,valor):
 f = open(cc)
 linhas = f.readlines()
 f.close()
 dim = eval(linhas[0])
 car_e1 = eval(linhas[1])
 car_e2 = eval(linhas[2])
 pos_paredes = eval(linhas[3])
 pos_e1 = eval(linhas[4])
 pos_e2 = eval(linhas[5])
 paredes = ()
 #codigo em respeito a abertura e leitura do ficheiro 
 for p in pos_paredes:
  paredes += (cria_posicao(obter_pos_x(p),obter_pos_y(p)),)
 #criacao das paredes
 e1 = tuple(cria_unidade(cria_posicao(obter_pos_x(p),obter_pos_y(p)),car_e1[1],car_e1[2],car_e1[0]) for p in pos_e1)
 e2 = tuple(cria_unidade(cria_posicao(obter_pos_x(p),obter_pos_y(p)),car_e2[1],car_e2[2],car_e2[0]) for p in pos_e2)
 m = cria_mapa(dim,paredes,e1,e2)
 nomes = obter_nome_exercitos(m)
 pontuacao1 = calcula_pontos(m,nomes[0])
 pontuacao2 = calcula_pontos(m,nomes[1])
#calculo das pontuacoes de ambos os exercitos pois a batalha vai decorrendo por
#turnos enquanto ambas as pontuacoes forem maior que zero
 print(mapa_para_str(m))       #mapa inical
 print('[ '+str(nomes[0]) + ':' + str(pontuacao1) + ' ' \
       + str(nomes[1]) + ':' + str(pontuacao2) + ' ]')
 #pontuacoes e nomes iniciais

 while pontuacao1 > 0 and pontuacao2 > 0:
  m_anterior = cria_copia_mapa(m)
  m = simula_turno(m)
  pontuacao1 = calcula_pontos(m,nomes[0])
  pontuacao2 = calcula_pontos(m,nomes[1])
  if mapas_iguais(m,m_anterior):
 #mapas_iguais identica o caso em que depois de um simula_turno os mapas nao se
 #alteraram, isto e, nenhuma unidade se alterou. pelo que ocorre um empate.
   print(mapa_para_str(m))
   print('[ '+str(nomes[0]) + ':' + str(pontuacao1) + ' ' \
         + str(nomes[1]) + ':' + str(pontuacao2) + ' ]')  
   return 'EMPATE'
  if valor:
#se valor for true entao imprime-se os varios turnos ate algum ser destruido
   print(mapa_para_str(m))
   print('[ '+str(nomes[0]) + ':' + str(pontuacao1) + ' ' \
         + str(nomes[1]) + ':' + str(pontuacao2) + ' ]')  
 if not valor:
#se o valor for false entao imprime se apenas o mapa inicial e final, pelo q 
#se encontra fora do ciclo 
  print(mapa_para_str(m))
  print('[ '+str(nomes[0]) + ':' + str(pontuacao1) + ' ' \
        + str(nomes[1]) + ':' + str(pontuacao2) + ' ]')    
 if pontuacao1 < pontuacao2:
#se a pontuacao 1 e menor entao o e2 ganhou
  return nomes[1]
 else:
  return nomes[0]
