import filecmp
import os
import shutil


# Repertoires

r1 = 'C:/Users/USER/PycharmProjects/scriptSNH/r1/'      # exemple : C:/Users/USER/PycharmProjects/scriptSNH/r1/
r2 = 'C:/Users/USER/PycharmProjects/scriptSNH/r2/'      # exemple : C:/Users/USER/PycharmProjects/scriptSNH/r2/


# fonction qui vérifie si une variable a est dans une liste b

def estDans(a,b):
    for tmp in b:
        if(tmp == a):
            return True
    return False


# fonction principale

def fonction(r1,r2):


    # 1ere étape : distinguer les fichiers des dossiers

    fichiersR1 = []
    dossiersR1 = []
    fichiersR2 = []
    dossiersR2 = []

    for tmp in os.listdir(r1):
        if(os.path.isdir(r1 + '' + tmp) == True):
            dossiersR1.append(tmp)
        else:
            fichiersR1.append(tmp)
            
    for tmp in os.listdir(r2):
        if(os.path.isdir(r2 + '' + tmp) == True):
            dossiersR2.append(tmp)
        else:
            fichiersR2.append(tmp)


    # 2eme étape : Copie des fichiers absents

    if ((fichiersR1 != []) and (fichiersR2 != [])):
        for tmp in fichiersR1:
            if(estDans(tmp,fichiersR2) == False):
                shutil.copy(r1 + '' + tmp, r2)
    else:
        for tmp in fichiersR1:
            shutil.copy(r1 + '' + tmp, r2)


    # 3eme étape : Copie des fichiers manquant dans le repertoire 2

    if((fichiersR1 != []) and (fichiersR2 != [])):
        for tmp in fichiersR1:
            for tmp2 in fichiersR2:
                if (tmp2 == tmp):
                    if (filecmp.cmp(r1 + '' + tmp, r2 + '' + tmp2) == True):
                        break
                    else:
                        shutil.copy(r1 + '' + tmp, r2)
                        break


    # 4eme étape : Copie des repertoires fils manquant dans les repertoires parent

    for tmp in dossiersR1:
        if( estDans(tmp,dossiersR2) == False ):
            # On copie le repertoire fils du repertoire R1 dans R2 #
            shutil.copytree(r1 + '' + tmp, r2+''+tmp)


    # 5eme étape : fin

    for i,j in zip(dossiersR1,dossiersR2):
        r11 = r1 + '' + i + '/'
        r22 = r2 + '' + j + '/'
        fonction(r11, r22)

    print('Fonction bien exécutée')


# Exécution de la fonction

fonction(r1,r2)