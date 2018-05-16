# -*- coding: utf-8 -*-
"""
@author: cordula eggerth (00750881)

aufgabe 2 / uebung 3: strategie 1 und strategie 2 mastermind 

"""
import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations

# ---------------------------------------------------------------------------------------------------------------


# STRATEGIE 1 (GLEICHVERTEILTE ZUFALLSCODES OHNE BERÜCKSICHTIGUNG DER HINWEISE)
def simuliereSpielStrategie1():
    """
    funktion simuliert eine spielrunde mit strategie 1, bis der code erraten wird
    (ziehen gleichverteilter zufallsfarbcodes)
    returnwert: anzahl der notwendigen schritte bis zum erraten des codes 
    """
    # erlaubte 6 farbcodes anlegen:
    #  R ... rot
    #  G ... gruen
    #  B ... blau
    #  L ... lila
    #  O ... orange
    #  P ... pink
    farbcodes = ["R", "G", "B", "L", "O", "P"]
    
    # input anlegen (mit neutralem buchstabe initialisiert):
    rateversuch = ["A", "A", "A", "A"]
    rateversuchLaenge = 4
    
    # zaehlervariable fuer anzahl der schritte bis zum erraten
    counter = 0
    
    # anfangswert aktuellerVersuch
    aktuellerVersuch = "AAAA"
    
    ################################################################
    ## START DES SPIELS ############################################
    ################################################################
    
    # ZU ERRATENDEN ZIEL-FARBCODE SETZEN 
    zielCode = (np.random.choice(farbcodes,4)).tolist()
    zielCodeStr = str(zielCode[0]) + str(zielCode[1]) + str(zielCode[2]) + str(zielCode[3]) 
    
    # RATEVERSUCHE MITTELS ZIEHEN VON GLEICHVERTEILTEN ZUFALLSFARBCODES
    # UND DARAUFFOLGEND HINWEISE:
    while( zielCodeStr != aktuellerVersuch ):
                    
        ##### ZUFALLSCODES GENERIEREN #####
        # es wird mittels random funktion ein zufaelliges korrektes zeichen gezogen pro stelle
        for j in range(0,rateversuchLaenge):
            # 1 zufaellige farbe auswaehlen pro stelle des rateversuchs
            zufallsCode = (np.random.choice(farbcodes, 1)).tolist() 
            rateversuch[j] = zufallsCode[0] # setze als character
        
        aktuellerVersuch = str(rateversuch[0]) + str(rateversuch[1]) + str(rateversuch[2]) +str(rateversuch[3])
        
        # CHECK print
        # print("\n Das war der " + str(counter+1) + ". Rateversuch:" + str(rateversuch))
        
        ##### COUNTER #####
        # anzahl der schritt um 1 erhöhen
        counter += 1
   
    # CHECK: anzahl der schritte bis erraten ausgeben
    # print("\n Anzahl der Schritte bis zum Erraten: " + str(counter))
       
    ##### RETURN #####
    return counter
        
# ---------------------------------------------------------------------------------------------------------------


# STRATEGIE 2 ("EINFACHE" STRATEGIE)       
def simuliereSpielStrategie2():
    """
    funktion simuliert eine spielrunde mit strategie 2, bis der code erraten wird
    (siehe angabe "einfache" strategie)
    returnwert: anzahl der notwendigen schritte bis zum erraten des codes 
    """
    # erlaubte 6 farbcodes anlegen:
    #  R ... rot
    #  G ... gruen
    #  B ... blau
    #  L ... lila
    #  O ... orange
    #  P ... pink
    farbcodes = ["R", "G", "B", "L", "O", "P"]
        
    # zaehlervariable fuer anzahl der schritte bis zum erraten
    counter = 0
    
    # anfangswert aktuellerVersuch
    aktuellerVersuch = "A"
    
    # richtige farben liste
    richtigeFarben = list()
        
    ################################################################
    ## START DES SPIELS ############################################
    ################################################################
    
    # ZU ERRATENDEN ZIEL-FARBCODE SETZEN 
    zielCode = (np.random.choice(farbcodes,4)).tolist()
    zielCodeStr = str(zielCode[0]) + str(zielCode[1]) + str(zielCode[2]) + str(zielCode[3]) 
    
    # RATEVERSUCHE MITTELS "EINFACHER STRATEGIE"
    # solange farben testen, bis man die farbkombination richtig hat:
    while( len(richtigeFarben) < 4 ):
             
        # variable fuer anzahl der vorkommenden elemente mit dieser farbe
        vorkommenDieserFarbcode = 0
        
        # zu testende farbe
        aktuellerVersuch = str(farbcodes[counter]) 
        
        # ermitteln, wie oft die derzeitige farbe im zielCode vorkommt
        for c in range(0,len(zielCode)):
            if(aktuellerVersuch == zielCode[c]):
                vorkommenDieserFarbcode += 1
        
        # anzahl des vorkommens der farbe als code an richtigeFarben anhaengen
        for c in range(0,vorkommenDieserFarbcode):
            richtigeFarben.append(aktuellerVersuch)
  
        # anzahl der schritte um 1 erhoehen
        counter += 1
    
    richtigeFarbenStr = str(richtigeFarben[0]) + str(richtigeFarben[1]) + \
                        str(richtigeFarben[2]) + str(richtigeFarben[3])
                        
    if(richtigeFarbenStr != zielCodeStr):
        # anzahl der tausche umordnungen ermitteln
        anordnungen = list(permutations(richtigeFarben))
        
        # unique elemente in liste ermitteln
        anordnungen_unique = list(set(anordnungen))

        # richtige anordnung der farbcodes ermitteln
        for i in range(0,len(anordnungen_unique)):
            anordnung = anordnungen_unique[i] #i
            anordnungStr = str(anordnung[0]) + str(anordnung[1]) + \
                        str(anordnung[2]) + str(anordnung[3])
            if(anordnungStr != zielCodeStr):
                counter += 1
            if(anordnungStr == zielCodeStr):
                break
                
    ##### RETURN: anzahl der schritte bis code erraten
    return counter


# ---------------------------------------------------------------------------------------------------------------


# SIMULATION der GEWAEHLTEN STRATEGIE FUER UEBERGEBENE N DURCHLAEUFE 
def simuliereSpieldurchlaeufeStrategie(n=1000, strategie="strategie1"):
    """
    funktion simuliert fuer n spieldurchlaeufe die anzahl der schritte, die 
    notwendig sind, um jeweils den zielcode zu erraten
    (ziehen gleichverteilter zufallsfarbcodes)
    returnwert: liste der anzahl der notwendigen schritte bis zum erraten 
    des codes fuer n simulationsdurchlaeufe 
    """
    # liste fuer spielergebnisse anlegen
    spielergebnisliste = list()

    # fuer n durchlaeufe von spielen die anzahl der schritte bis erraten sammeln
    for i in range(0,n):
        if(strategie == "strategie1"):
            anzahlSchritte = simuliereSpielStrategie1()
            spielergebnisliste.append(anzahlSchritte)
        else: 
            anzahlSchritte = simuliereSpielStrategie2()
            spielergebnisliste.append(anzahlSchritte)
            

    # return: liste von spielergebnissen
    return spielergebnisliste

   
# ---------------------------------------------------------------------------------------------------------------


# FUNKTION ZUR BERECHNUNG DES ERWARTUNGSWERTES DER SPIELLAENGE
def erwartungswertSpiellaengeBerechnen(simulationsergebnisse):
    
    erwartungswert = float(sum(simulationsergebnisse)) / len(simulationsergebnisse)

    return erwartungswert


# ---------------------------------------------------------------------------------------------------------------


# FUNKTION ZUR BERECHNUNG DER WAHRSCHEINLICHKEIT IN MAX. X-FACHEM RATEVERSUCHEN ZU GEWINNEN
def wahrschBerechnen(simulationsergebnisse, xlist):
    
   wahrschListe = list()
   
   for i in range(0,len(xlist)):   
       count = 0
       for j in range(0,len(simulationsergebnisse)):
           if(simulationsergebnisse[j] <= xlist[i]): 
               count+=1
       wahrscheinlichkeit = float(count) / float(len(simulationsergebnisse))
       wahrschListe.append(wahrscheinlichkeit)
   
   return wahrschListe


# ---------------------------------------------------------------------------------------------------------------


##### STRATEGIE 1 AUSFÜHREN, SIMULATIONSERGEBNISSE GENERIEREN UN VISUALISIEREN #####
   
# liste von simulationsergebnissen
ergebnisseStrat1 = simuliereSpieldurchlaeufeStrategie(500,"strategie1")
# erwartungswert 
erwartungswertStrat1 = erwartungswertSpiellaengeBerechnen(ergebnisseStrat1)
# gewinnwahrscheinlichkeit bei max. x-fachem raten
xlist = [5, 10, 20, 50, 100, 200, 500, 700, 1000]
wahrscheinlichkeitenStrat1 = wahrschBerechnen(ergebnisseStrat1, xlist)

# line plot der ergebnisseStrat1
plt.plot(ergebnisseStrat1, c="c", alpha=0.55)
plt.title("Ergebnisse von Strat. 1")
plt.axhline(erwartungswertStrat1, color='r', linestyle='dashed', linewidth=2)
plt.text(erwartungswertStrat1-1000,1555,'Erwartungswert',rotation=1, color="black")
plt.xlabel("Simulationen von Spielrunden")
plt.ylabel("Anzahl der Schritte bis Erraten des Farbcodes")
plt.show()

# histogram plot der ergebnisseStrat1
plt.hist(ergebnisseStrat1, bins=20, color='c', edgecolor='k', alpha=0.55)
plt.title("Histogramm der Ergebnisse von Strat. 1")
plt.xlabel("Schritte")
plt.ylabel("Häufigkeit")
plt.axvline(erwartungswertStrat1, color='k', linestyle='dashed', linewidth=2)
plt.text(erwartungswertStrat1+65,90,'Erwartungswert',rotation=90)
plt.show()

# boxplot 
plt.boxplot(ergebnisseStrat1)
plt.title("Boxplot der Ergebnisse von Strat. 1")
plt.ylabel("Anzahl der Schritte bis Erraten")
plt.show()

# ---------------------------------------------------------------------------------------------------------------


##### STRATEGIE 2 AUSFÜHREN, SIMULATIONSERGEBNISSE GENERIEREN UN VISUALISIEREN #####
   
# liste von simulationsergebnissen
ergebnisseStrat2 = simuliereSpieldurchlaeufeStrategie(500,"strategie2")
# erwartungswert 
erwartungswertStrat2 = erwartungswertSpiellaengeBerechnen(ergebnisseStrat2)
# gewinnwahrscheinlichkeit bei max. x-fachem raten
xlist2 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
wahrscheinlichkeitenStrat2 = wahrschBerechnen(ergebnisseStrat2, xlist2)

# line plot der ergebnisseStrat2
plt.plot(ergebnisseStrat2, c="g", alpha=0.55)
plt.title("Ergebnisse von Strat. 2")
plt.axhline(erwartungswertStrat2, color='r', linestyle='dashed', linewidth=2)
plt.text(erwartungswertStrat2-30,1555,'Erwartungswert',rotation=1, color="black")
plt.xlabel("Simulationen von Spielrunden")
plt.ylabel("Anzahl der Schritte bis Erraten des Farbcodes")
plt.show()

# histogram plot der ergebnisseStrat1
plt.hist(ergebnisseStrat2, bins=20, color='g', edgecolor='k', alpha=0.55)
plt.title("Histogramm der Ergebnisse von Strat. 2")
plt.xlabel("Schritte")
plt.ylabel("Häufigkeit")
plt.axvline(erwartungswertStrat2, color='k', linestyle='dashed', linewidth=2)
plt.text(erwartungswertStrat2+1,60,'Erwartungswert',rotation=90)
plt.show()

# boxplot 
plt.boxplot(ergebnisseStrat2)
plt.title("Boxplot der Ergebnisse von Strat. 2")
plt.ylabel("Anzahl der Schritte bis Erraten")
plt.show()


# ---------------------------------------------------------------------------------------------------------------
 