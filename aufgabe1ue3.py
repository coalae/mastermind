# -*- coding: utf-8 -*-
"""
@author: cordula eggerth (00750881)

aufgabe 1 / uebung 3: spiel mastermind 

"""
import numpy as np

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

# maximale anzahl von rateversuchen (lt. angabe):
maxVersuche = 12

# rateversuche-liste
rateversuchliste = list()

# tipp-liste (= zum speichern der hinweise, die dem user gegeben werden)
tippliste = list()


################################################################
## START DES SPIELS ############################################
################################################################

# ZU ERRATENDEN ZIEL-FARBCODE SETZEN 
zielCode = (np.random.choice(farbcodes,4)).tolist()

# USER MACHT RATEVERSUCHE UND BEKOMMT HINWEISE:
for i in range(0,maxVersuche):
    
    ###### USER-EINGABE ##### 
    
    # user gibt rateversuch ein
    for a in range(0,rateversuchLaenge):
        rateversuch[a] = input(str(a+1) + ". Buchstabe. Bitte 1 Grossbuchstabe aus R, G, B, L, O, P eingeben: ")
        
    # eingabe pruefen und korrigieren, falls zeichen nicht in erlaubten zeichen enthalten
    # korrektur: es wird mittels random funktion ein zufaelliges korrektes zeichen gezogen
    for j in range(0,rateversuchLaenge):
        if not(rateversuch[j] in farbcodes):
            # 1 zufaellige farbe auswaehlen und damit eingabe korrigieren
            zufallsCode = (np.random.choice(farbcodes, 1)).tolist() # generiert 1 zuefaelliges zeichen als liste
            rateversuch[j] = zufallsCode[0] # setze als character
    
    # rateversuch dieser iteration in rateversuche-liste einfuegen
    aktuellerVersuch = str(rateversuch[0]) + str(rateversuch[1]) + str(rateversuch[2]) +str(rateversuch[3])
    rateversuchliste.append(aktuellerVersuch)
    
    # CHECK print
    print("\n Das war der " + str(i+1) + ". Rateversuch:" + str(rateversuch))
            
    
    ###### VERGLEICHE USER-EINGABE MIT ZIELCODE #####
    
    # leere liste fuer aktuellen tipp anlegen
    aktuellerTipp = list()
    
    # tipp (hinweis) zum aktuellen rateversuch geben
    # X ... farbe und position richtig
    # O ... farbe richtig, position falsch
    # F ... farbe und position falsch
    for c in range(0, len(aktuellerVersuch)):
        if(aktuellerVersuch[c] == zielCode[c]):
            aktuellerTipp.append("X") # farbe richtig, position richtig
        elif((aktuellerVersuch[c] != zielCode[c]) and (aktuellerVersuch[c] in zielCode)):
            aktuellerTipp.append("O") # farbe richtig,  position falsch
        else: 
            aktuellerTipp.append("F") # farbe falsch, position falsch
    
    # string des aktuellenTipp anlegen und zu tippliste hinzufuegen
    aktuellerTippStr = str(aktuellerTipp[0]) + str(aktuellerTipp[1]) + str(aktuellerTipp[2]) + str(aktuellerTipp[3])
    tippliste.append(aktuellerTippStr)

    
    ##### TIPPS- und EINGABE-ZUSAMMENFASSUNG FUER USER ANZEIGEN ##### 
    
    # fuer alle versuchsdurchlaeufe den jeweiligen eintrag von der rateversuchliste und
    # von der tippliste ausgeben 
    for d in range(0, i+1):
        # ANZEIGEFORMAT (z.B.): 3. Rateversuch: AAAA ; Tipp: XXOF
        print("\n" + str(d+1) + ". Rateversuch: " + rateversuchliste[d] + "; Tipp dazu: " + tippliste[d] + " \n")


    ##### GEWONNEN / VERLOREN ANZEIGE
    
    # falls in 12. versuch nicht erraten: SPIEL VERLOREN (ende der versuchschleife)
    if((i == 11) and not(all(x == "X" for x in aktuellerTippStr))):
        print("\n SPIEL VERLOREN! \n Der Zielcode war: " + str(zielCode) + ".")
    
    # falls vor 12. versuch erraten: SPIEL GEWONNEN (versuchschleife verlassen)
    if((i < 11) and (all(x == "X" for x in aktuellerTippStr))):
        print("\n SPIEL GEWONNEN! \n Der Zielcode war: " + str(zielCode) + ".")
        break # schleife verlassen
    
    
    
    