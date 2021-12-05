# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

#1
def getLinha(linha):
    novaLinha=linha.strip("\n")
    campos=novaLinha.split(",")
    atleta=[]
    atleta.append("emd"+str(int(campos[1])+1))
    for i in range(2,len(campos)):
        atleta.append(campos[i])

    
      
    return atleta


def lerDataset(fnome):
    f = open(fnome, encoding= "utf-8")
    bd = []
    f.readline()
    for linha in f:
        bd.append(getLinha(linha))
    #...
    return bd

BD = []
BD = lerDataset("c:/Users/Asus/Desktop/ATP2021/emd.csv")  
#2
def chaveOrd(atleta):
    return atleta[1]


def listarDataset(bd):
    bd.sort(key=chaveOrd, reverse= True)
    lista=[]
    lista.append("      id        |       data         |         nome           |        apto        ")
    lista.append("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for atleta in bd:
        lista.append(atleta[0] + "  |  " + atleta[1] + "   |   "  + atleta[3]+ " " + atleta[2]+ "    |    " + atleta[11])
    return lista


#4

def modalidades(bd):
    modalidades={}
    listaMod=[]
    for atleta in bd:
        if atleta[7] not in listaMod:
            listaMod.append(atleta[7])
    listaMod.sort()
    return listaMod



#5

def distribPorModalidade(bd):
    # Escreve aqui o teu código
    distribuicaoM={}
    lista=[]
    for atleta in bd:
        if atleta[7] in distribuicaoM.keys():
            distribuicaoM[atleta[7]] = distribuicaoM[atleta[7]] + 1
        else:
            distribuicaoM[atleta[7]] = 1
    

    return distribuicaoM


print(distribPorModalidade(BD))
#6
def distribPorClube(bd):
    # Escreve aqui o teu código
    distribuicaoC={}
    lista=[]
    for atleta in bd:
        if atleta[8] in distribuicaoC.keys():
            distribuicaoC[atleta[8]] = distribuicaoC[atleta[8]] + 1
        else:
            distribuicaoC[atleta[8]] = 1
    
    
    return distribuicaoC


# 66
def distrib(bd,parametro):
    
    distribuicaoP={}
    if parametro == 1:
       for atleta in bd:
        if atleta[1][:4] in distribuicaoP.keys():
            distribuicaoP[atleta[1][:4]] = distribuicaoP[atleta[1][:4]] + 1
        else:
            distribuicaoP[atleta[1][:4]] = 1
       return distribuicaoP
    else:
        for atleta in bd:
         if atleta[parametro] in distribuicaoP.keys():
            distribuicaoP[atleta[parametro]] = distribuicaoP[atleta[parametro]] + 1
         else:
            distribuicaoP[atleta[parametro]] = 1
        return distribuicaoP
  
#7
def distribPorAno(bd):
    distribuicaoA={}
    lista=[]
    for atleta in bd:
        if atleta[1][:4] in distribuicaoA.keys():
            distribuicaoA[atleta[1][:4]] = distribuicaoA[atleta[1][:4]] + 1
        else:
            distribuicaoA[atleta[1][:4]] = 1
    

    return distribuicaoA



#8
def plotDistribPorModalidade(distribuicao):
    x=[]
    for i in range(len(distribuicao)):
        x.append(i+1)
    y=[]
    tick_label=[]
    for chave in distribuicao:
        y.append(distribuicao[chave])
        tick_label.append(chave)
    
    plt.bar(x, y, tick_label = tick_label,
        width = 0.8, color = ['orange', 'green',"yellow","black"])
 
    plt.xlabel('Modalidades')
    plt.ylabel('Número de atletas')
    plt.title('Atletas por modalidades')
 

    plt.show()
   
    
#9

def plotDistrib(distribuicao):
    
    x=[]
    for i in range(len(distribuicao)):
        x.append(i+1)
    y=[]
    tick_label=[]
    for chave in distribuicao:
        y.append(distribuicao[chave])
        tick_label.append(chave)
    
    plt.bar(x, y, tick_label = tick_label,
        width = 0.8, color = ['orange', 'green',"yellow","black"])
 
    plt.xlabel('Parametro')
    plt.ylabel('Número de atletas')
    plt.title('Atletas por parametro')
 

    plt.show()

 
