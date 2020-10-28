import time
import math
#import memory_profiler

import numpy 
import math 
import time
    

    
def lireunfich(fichier):
    """
    Cette fonction permet de lire un fichier et de renvoyer les  deux séquences d'ADN qu'il contient sous forme de  liste
    """
    file=open(fichier)
    lines=file.readlines()
    list=[]
    for line in lines:
       list.append(line.split())
    return list[2:]
#________________________________________________________________________________________________________________________
                                        
                                            #TACHE A
#_________________________________________________________________________________________________________________________
def substitution(a,b):
    """
    Cette fonction calcule le coût de substitution de deux caractères a et b
    """
    if(a==b):
        return 0
    else:
        if((a=="C" and b=="G") or (a=="G" and b=="C") or (a=="A" and b=="T") or (a=="T" and b=="A")):
            return 3
        else:
            return 4
        
        
def DIST_NAIF_REC(x,y,i,j,c,dist):
    """
    x et y deux mots
    i un indice de [0..len(x)] et i un indice de [j..len(y)]
    c le coût de l'alignement de(x,y)
    dist le coût du meilleur alignement de (x,y) connu après cet appel
    """
    if(i==len(x) and j==len(y)): # le cas d'arret : on parcourut toutes les séquences x et y et on compare si le coût d'alignement est inferieur à la distance d'édition 
        if(c<dist):
            dist=c
    
    else: # On trois les trois cas possibles soit une insertion, suppression ou une substitution 
        if(i<len(x) and j<len(y)): 
         
            dist=DIST_NAIF_REC(x,y,i+1,j+1,c+substitution(x[i],y[j]),dist)
        
        if(i<len(x)):
            dist=DIST_NAIF_REC(x,y,i+1,j,c+2,dist)
    
        if(j<len(y)):
            dist=DIST_NAIF_REC(x,y,i,j+1,c+2,dist)
   
    return dist


def DIST_NAIF(x,y):
    """
    x et y deux mots
    Renvoie la distance d'édition de x à y
    """
    start_time = time.time()
    distance=DIST_NAIF_REC(x,y,0,0,0,math.inf)
    # Affichage du temps d execution 
    print("Temps d'exécution : %s secondes ---" % (time.time() - start_time))
    return distance

# temps d'exécutions des instances:
    #Inst_oooo10_44 (n=10,m=5): Temps d execution : 0.048039913177490234 secondes ---
    #Inst_oooo10_8 (n=10,m=9):  Temps d execution : 2.762869119644165 
    #Inst_oooo10_7 (n=10,m=10): Temps d execution : 6.7951085567474365 secondes --- 
    #Inst_oooo12_13 (n=12,m=9): Temps d execution : 11.958396434783936 secondes --- 
    #Inst_oooo12_32 (n=12,m=9): Temps d execution : 11.931615829467773 secondes --- 
    # On moins d'une minute, on peut executer que les instances(séquences  de taille <12)
    
    # Inst_0000013_45.adn'  Temps d execution : 816.9228141307831 secondes ---secondes --- 
    # Inst_0000014_83.adn                     222.39185375899999                                        
  



#_______________________________________________________________________________________________________________________________
#                             TACHE B
#_________________________________________________________________________________________________________________________________

#_______________________________________________________________________________________________________________________________
#                             DIST_1
#_________________________________________________________________________________________________________________________________

def DIST_1(x,y):
    """Un algorithme itératif qui prend en argument deux séquences , qui remplit le tableau à deux dimensions T
    avec toutes les valeurs de D et  renvoie la distance d'édition de ces deux mots
    """
     #Calcul du temps d'éxecution du programme
    start_time = time.time()
    T= [[0] *(len(y)+1) for i in range(len(x)+1)] # Initialisation de la matrice à 0
    for i in range(len(x)+1): # Parcours de la matrice
        
        for j in range(len(y)+1):
            if(i!=0 and j!=0):  # Calcul de D(i,j) avec j!=0 et i!=(0)  soit  par substitution ou insertion ou supprssion 
                T[i][j]=min([2+T[i][j-1],2+T[i-1][j],substitution(x[i-1],y[j-1])+T[i-1][j-1]]) 
            else:
                if(i==0):
                    T[i][j]=2*j  #Calcul de D(0,j): par des insertions successives
                if(j==0):
                    T[i][j]=2*i  # Calcul de D(i,0) :#Calcul de D(0,j): par des suppressions successives
    #Affichage du temps d'exécution
    print("Temps d'exécution : %s secondes ---" % (time.time() - start_time))
    return (T[len(x)][len(y)],T)
    

#   _____________________________________________________________________________________________________________________________
#                             Consommation de temps CPU 
#_________________________________________________________________________________________________________________________________


# Temps d'exécution des instances 
    #Inst_oooo10_44 (n=10,m=5):       Temps d execution :  8.487701416015625e-05 secondes ---    
    #Inst_oooo10_8 (n=10,m=9):        Temps d execution :  0.0001468658447265625 secondes ---    
    #Inst_oooo12_32 (n=12,m=9):       Temps d execution :  0.00014901161193847656 secondes ---     
    #Inst_oooo13_45 (n=13,m=12)       Temps d'exécution :  0.0001990795135498047 secondes --- 
    #Inst_oooo13_89 (n=13,m=12)       Temps d'exécution :  0.00023436546325683594 secondes ---   
    #Inst_oooo14_7 (n=14,m=12)        Temps d'exécution :  0.000217437744140625 secondes ---
    #Inst_oooo15_76 (n=15,m=13)       Temps d'exécution :  0.0002837181091308594 secondes ---
    #Inst_oooo50_9 (n=50,m=45)        Temps d'exécution :  0.0026171207427978516 secondes ---
    #Inst_ooo1000_23 (n=1000,m=887)   Temps d'exécution :  2.2866880893707275 secondes ---
    #Inst_ooo3000_10 (n=3000,m=2676)  Temps d'exécution :  7.138455152511597 secondes ---
    #Inst_ooo5000_33 (n=5000,m=4460)  Temps d'exécution : 19.771201610565186 secondes ---
    #Inst_oo10000_8 (n=10000,m=4460)  Temps d'exécution :  310.47955536842346 secondes ---
    # #Inst_oo15000_20 (n=15000,m=13359)  Temps d'exécution 202.496107339859 secondes ---
    # #Inst_oo15000_30 (n=15000,m=13360)  Temps d'exécution 199.54990816116333 secondes ---
    #Inst_oo20000_64                      Temps d'exécution 374.5727069377899 secondes ---
    #Inst_oo20000_5 (n=20000,m=17779) Temps d'exécution :  Le noyau est mort, redémarrage en cours
def minimum(T,i,j,x,y):
    """ rend le minimum de ces trois cases suivantes: T[i-1][j-1] et  T[i][j-1] et  T[i-1][j] 
    et les  coordonnées(indices) de cette case dans la matrice  T   
    """
    tmp=T[i-1][j-1] + substitution(x[i-1],y[j-1]) #substitution 
    indexX=i-1
    indexY=j-1
    if(tmp>=T[i-1][j]+2):#cas de suppression
        tmp=T[i-1][j]
        indexX=i-1
        indexY=j
    if(tmp>=T[i][j-1]+2):#cas d'insertion
        tmp=T[i][j-1]
        indexX=i
        indexY=j-1
    return (indexX,indexY)
                
def SOL_1(x,y,T):
    """ Cette foncton prend en argument deux séquences x et y et toutes les valeurs de D stockées dans une matrice de taille len(x)*len(y),
         et renvoie  un alignement optimal de ces deux séquences.
    """
    start_time=time.time();
    alignX=""  #pour stocker l'alignement
    alignY=""
    i=len(x)   # Afin de trouver un meilleur alignement, on parcourt la matrice T de la dernière case T[len(x)][len(y)]
    j=len(y)
    while(i>0 or j>0):
        (indexX,indexY)=minimum(T,i,j,x,y)  # Récuperer les indices d'une case de T qui contient une distance  minimale 
           
        if(indexX==i and indexY==j-1): # On vérifie s'il s'agit d'une insertion 
            alignX="_"+alignX
            alignY=y[j-1]+alignY
            
        else:      
           if(indexX==i-1 and indexY==j):   # On vérifie s'il s'agit d'une suppression 
               alignX=x[i-1]+alignX
               alignY="_" + alignY
           
           else:
                if(indexX==i-1 and indexY==j-1): # On vérifie s'il s'agit d'une substitution
                    alignX=x[i-1]+alignX
                    alignY=y[j-1]+alignY
      
                               
        i=indexX  # On passe à la case de meilleurs coût
        j=indexY
    print("Temps d execution : %s secondes ---" % (time.time() - start_time))
    return (alignX,alignY)
#____________________________________________________________________________________________________
           #       Consommation de temps CPU de  SOL_1
#___________________________________________________________________________________________________

    
    #Inst_oooo10_7 (n=10,m=10):             Temps d execution    0.00001219253540039062 secondes ---                  
    #Inst_oooo12_13 (n=12,m=9):             Temps d execution :  0.000020265579223632812 secondes ---                  
    #Inst_oooo13_45                         Temps d execution :   0.000019788742065429688 secondes ---      
    #Inst_oooo14_83                         Temps d execution    0.000030279159545898438 secondes ---
    #Inst_oooo15_4                          Temps d execution    0.00004935264587402344 secondes ---
    
    #Inst_oooo20_17                         Temps d execution   0.000030517578125 secondes ---
    #Inst_oooo50_3                          Temps d execution : 0.00006389617919921875 secondes --- 
    #Inst_ooo100_3                          Temps d execution : 0.0001823902130126953 secondes ---
     
     # Inst_ooo500_8                        Temps d execution :  0.0006706714630126953  secondes ---
     # Inst_oo1000_23                       Temps d execution    0.0017726421356201172  secondes ---
     #  Inst_oo2000_3                       Temps d execution   0.004521369934082031 secondes ---
     #Inst_0003000_10.adn                   Temps d execution : 0.0060446262359619145 secondes ---
     #Inst_0005000_33.adn                   Temps d execution :  0.010553359985351562 secondes ---
     
     #Inst_0008000_54.adn                   Temps d execution   0.017653703689575195  secondes----
     #Inst_0010000_7.adn                    Temps d execution   0.023798465728759766 
     #Inst_0015000_3.adn                    Temps d execution   3.1553030014038086 
     #Inst_0020000_5.adn                    Temps d execution: 6.0698840618133545 secondes ---
         
     
     
def PROG_DYN(x,y):
    """la fonction PROG_DYN prend en argument les deux séquences d'ADN x et y et renvoie la distance d(x,y) et un alignement optimal de ces deux séquences 
    """
    #Affichage du temps d'éxecution
    start_time = time.time()
    
    (dist,T)=DIST_1(x,y)  # récupérer la matrice D
    (alignX,alignY)=SOL_1(x,y,T) #construire l'alignement optimal par SOL_1
    
    print("Temps d execution : %s secondes ---" % (time.time() - start_time))
    return (dist)               
               
            
_#_____TEST___________________
#Alignements optimaux renvoyés par la fonction PROG_DYN
    
    #-------------------------------------------------------------------------------
    #Inst_oooo10_44 (n=10,m=5): disatance=5 Alignement_Optimal  'TATATGAGTC'      
    #                                                           'TAT_T___T_'
    #                                               Temps d execution :0.00012111663818359375 secondes ---
     
    #------------------------------------------------------------------------------
     
    #Inst_oooo10_8 (n=10,m=9):  distance=2  Alignement_Optimal  'AACTGTCTTT'
    #                                                           'AACTGT_TTT'
    #                                               Temps d execution : 0.00046443939208984375 secondes ---
    
    #------------------------------------------------------------------------------
    
    #Inst_oooo10_7 (n=10,m=10): distance =8 Alignement_Optimal 'TGGG_TGCTAT'
                    #                                          '_GGGGTTCTAT'
    #                                               Temps d execution : 0.00013136863708496094 secondes ---
                    
    #-------------------------------------------------------------------------------
    #Inst_oooo12_13 (n=12,m=9): distance=9 Alignement_Optimal  'CTGGAAAGTGCG'
    #                                                          'CTG_AA_CTG_G'
    #                                              Temps d execution : 0.00017189979553222656 secondes ---
    
    #-------------------------------------------------------------------------------
    
    #Inst_oooo12_32 (n=12,m=9): distance=6 Alignement_Optimal  'CCATTGATTTTC'
    #                                                          'C_ATTGATTT__'
    #                                             Temps d execution : 0.00011944770812988281 secondes ---
    
    #--------------------------------------------------------------------------------
    
    #Inst_oooo12_56 (n=12,m=11):distance=5 Alignement_Optimal  'GCTTAA_CTAACG'
    #                                                          'GCT_AAACTA_CT'
    #                                            Temps d execution : 0.00014543533325195312 secondes ---
   
    #---------------------------------------------------------------------------------
    
    #Inst_oooo14_83 (n=14,m=10):distance=6 Alignement_Optimal 'TGACTCACTCTTTC'
    #                                                         '__ACTCA_TCTT_C'
    #                                            Temps d execution : 0.0001537799835205078 secondes ---
    
    #---------------------------------------------------------------------------------
    #Inst_oooo20_17 (n=20,m=17):distance=14 Alignement_Optimal  'TTGGGGTGTGTTG_A_CCATCG'
    #                                                           'T_GGGG_GTGT_GGAAC_ATC_'
    #                                            Temps d execution :  0.00040841102600097656 secondes ---
    
    #---------------------------------------------------------------------------------
    #Inst_oooo20_32 (n=20,m=16):distance=8      Temps d execution :   0.00048661231994628906 secondes -
    #-------------------------------------------------------------------------------------
    
     #Inst_oooo50_3 (n=50,m=32):distance=26     Temps d execution :  0.0028896331787109375 secondes ---
    #-------------------------------------------------------------------------------------
    
     #Inst_ooo100_3                             Temps d execution : 0.00855112075805664 secondes ---
     
     # Inst_ooo500_8                            Temps d execution : 0.1871178150177002 secondes ---
     # Inst_oo1000_23                           Temps d execution  0.7802925109863281 secondes ---
     #  Inst_oo2000_3                           Temps d execution  3.269531726837158 secondes ---
     #Inst_0003000_10.adn                       Temps d execution : 7.33504056930542 secondes ---
     #Inst_0005000_33.adn                       Temps d execution : 22.756130933761597 secondes ---
     
     #Inst_0008000_54.adn                       Temps d execution   52.8333637714386 secondes ---
     #Inst_0010000_7.adn                        Temps d execution    82.76669502258301 secondes ---
     #Inst_0015000_3.adn                        Temps d execution 192.4584059715271 secondes ---   
      #Inst_0020000_5.adn                       Temps d executio 661.9248411655426 secondes --- KeyboardInterrupt
     
def DIST_2(x,y):
    """Un algorithme de calcul de la distance d'édition avec une complexité spatiale linéaire en O(len(y)) en modifiant légèrement l'algorithme DIST_1
    """
    
    start_time=time.time()
    
    tmp2=0  # variable temporelle 
    list=[]   #une liste(tableau) de taille len(y)  qui stockera la distance d'édition  pour chaque ligne i associée à la matrice D
    
    for k in range(len(y)+1):
        list.append(2*k)        # Calcul de D(0,k): le cas ou la taille de la séquence x est nulle et la taille de la séquence y >=0
        
    for i in range(1,len(x)+1): # Calcul de D(i,j), i>0 et j>=0
        
        for j in range(0,len(y)+1):  
            
            tmp1=list[j]    # Variable tomporelle
            if(j!=0):       # Calcul de D(i,j), i>0 et j>0
                
                mint=min([(2+list[j-1]),(tmp2+substitution(x[i-1],y[j-1])),(2+list[j])])   
                list=list[0:j]+[mint]+list[(j+1):]
                
            else:    #Cas où j=0 c_à_d Calcul de D(i,o)
                list=[2*i]+list[1:]
            tmp2=tmp1    # Variable tomporelle 
    print("Temps d execution : %s secondes ---" % (time.time() - start_time))
    return list[len(y)]

#____________________________________________________________________________________________________
           #    DIST2
#___________________________________________________________________________________________________
 #-------------------------------------------------------------------------------
    
    #Inst_oooo10_7 (n=10,m=10):  Temps d execution    0.000175885009765625 secondes ---
                    
    #-------------------------------------------------------------------------------
    #Inst_oooo12_13 (n=12,m=9): Temps d execution :  0.0001823223114013672 secondes ---
                    
    
     #Inst_oooo13_45        Temps d execution :   0.000216920166015625 secondes ---
    

    
    #Inst_oooo14_83         Temps d execution   0.000236402587890625 secondes ---
    #Inst_oooo15_4          Temps d execution   0.00035953521728515625 secondes ---
    
    #Inst_oooo20_17         Temps d execution  0.0003948211669921875 secondes ---
    #Inst_oooo50_3          Temps d execution : 0.0027022361755371094 secondes --- 
    #Inst_ooo100_3         Temps d execution : 0.01643991470336914 secondes ---
     
     # Inst_ooo500_8       Temps d execution :  0.9551939964294434 secondes ---
     # Inst_oo1000_23      Temps d execution   6.481737852096558 secondes ---
     #  Inst_oo2000_3      Temps d execution   54.134814500808716 secondes ---
     #Inst_0003000_10.adn  Temps d execution : 189.84318351745605 secondes ---
     #Inst_0005000_33.adn  Temps d execution : 201.23350429534912 secondes ---
     
    