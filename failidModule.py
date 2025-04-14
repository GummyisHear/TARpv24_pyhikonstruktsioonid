from random import *

def loeFail(fail:str)->list:
    jarjend = []
    with open(fail, 'r', encoding="utf-8-sig") as f:
        for line in f:
            jarjend.append(line)
    return jarjend

def kirjutaFail(fail:str, jarjend:list):
    f = open(fail, 'w', encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+"\n")
    f.close()

def failToDict(f:str): 
    riik_pealinn = {}#sõnastik {"Riik": "Pealinn"} 
    pealinn_riik = {}#sõnastik {"Pealinn": "Riik"}
    file = open(f, 'r', encoding="utf-8-sig") 

    for line in file: 
        k,v = line.strip().split('-') #k-võti, v-väärtus 
        riik_pealinn[k] = v #täidame riik_pealinn 
        pealinn_riik[v] = k #täidame pealinn_riik
    file.close() 
    return riik_pealinn, pealinn_riik 