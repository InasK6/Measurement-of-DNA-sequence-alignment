#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:07:15 2019

@author: inas
"""
def lire_un_fich(fichier):
    f=open(fichier)
    l=f.readlines()
    x=""
    y=""
    for k in l[2].split():
        x=x+k
    for k in l[3].split():
        y=y+k
    return (x,y)

def C_sub(a,b):
    if(a==b):
        return 0
    if((a=='A' and b=='T') or (a=='T' and b=='A') or (a=='G' and b=='C') or (a=='C' and b=='G') ):
        return 3
    else: 
        return 4

#Question 21:

def mot_gaps(k):
    s=''
    for i in range (k):
        s+="-"
        
    return s

#Question 22
#Entrées: x un mot de longueur 1
#         y un mot de longueur quelconque
def align_lettre_mot(x,y):
    c=''   #j'hésite si je dois mettre c='' ou c=""
    i=0
    ly=len(y)
    #On fait des insertions 
    while ( i<ly and x[0]!=y[i]):

        c=c+'-'
        i=i+1
    #On sort de la boucle si on a trouvé un élément en commun entre x et y
    # Ou si on a finit de parcourir tout le tableau 
    # Dans le premier cas, on fait des insertions avec les éléments restants du 
    # tableau
    s=''
   
    if(i<ly and x[0]==y[i] ):
        for k in range((i+1),ly):
            s=s+'-'
            k=k+1
        c=c+x+s

    #sinon on aura fait des insertions tout le long, l'élément de x
    # n'est pas dans y, on doit faire une substitution
    else:
        c=c[0:(ly-1)]+x
      
    return (c,y)
    
    
#On suppose qu'on dispose d'une fonction de coupure 
"""def coupure(x,y):
    i=len(x)/2
    ly=len(y)
    tab=[0 for k in range(ly+1)]
    j=0
    if(len(x)>1 and len(y)>=1):
        return j
    return j"""


        
#Question 25
def coupure(x,y):
    ly=len(y)
    lx=len(x)
    I=[[0]*(ly+1),[0]*(ly+1)]
    for j in range(ly+1):
        I[0][j]=j
        I[1][j]=j
    D=[[],[]]
    for j in range(ly+1):
        D[0]=D[0]+[j*2]
        D[1]=D[1]+[0]
    for i in range (1,lx+1):
        D[1][0]=2*i
        for j in range(1,ly+1):
            D[1][j]=min([2+D[1][j-1],2+D[0][j],C_sub(x[i-1],y[j-1])+D[0][j-1]])
        
        if(i>(lx//2)):
             for j in range(ly+1):
                 if(D[1][j]==2+D[1][j-1]) :
                     I[1][j]=I[1][j-1]
                 
                 else:
                     if(D[1][j]==2+D[0][j]):
                         I[1][j]=I[1][j]
            
                     else:
                         if (D[1][j]==(C_sub(x[i-1],y[j-1])+D[0][j-1])):
                             I[1][j]=I[0][j-1]

        for j in range(ly+1):
            D[0][j]=D[1][j]
        if(i>(lx//2)):
               for j in range(ly+1):
                   I[0][j]=I[1][j]
       
    return I[1][ly]

#Question 24
def SOL_2(x,y):
    lx=len(x)
    ly=len(y)
    i=lx//2
    if(ly==0):
        return (x,mot_gaps(len(x)))
    if(lx==1):
        return align_lettre_mot(x,y)
    else:
        j=coupure(x,y)
        A=SOL_2(x[0:(i)],y[0:(j)])
        B=SOL_2(x[(i):lx],y[(j):ly])
        return (A[0]+B[0], A[1]+B[1])