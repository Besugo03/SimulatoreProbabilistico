import random
import threading

# variabili per creare la simulazione
creditiScelti = int(input('inserisci quanti crediti desideri avere : '))  # crediti massimi
scommessadefaultScelta = int(input('inserisci quanto vuoi scommettere : '))  # quantitá di scommessa
iterazioniScelte = int(input('scegli quante scommesse effettuare : '))  # quante scommesse fare per ogni generazione
probScelta = int(input('decidi le probabilitá di vittoria : '))  # quante probabilitá abbiamo di vincere
threadselezionati = int(input('quanti thread utilizzare per la simulazione? : '))  # quante probabilitá abbiamo di
# vincere
strategiaselezionata = str.upper(input('che strategia scegliere? M/K : '))

# variabili per calcolo finale

vittorietotali = 0
guadagnototale = 0
percentualevittoriaottenuta = 0
mediaguadagno = 0


# ciclo di simulazione
def generazionescommessemartingale(prob, crediti, iterazioni, scommessadefault):
    # parto da simulazione zero e creo variabili locali di crediti e scommessa
    nsim = 0
    creditigenerazione = crediti
    scommessagenerazione = scommessadefault
    iterazionigenerazione = iterazioni
    # inizio del ciclo di scommessa
    while iterazionigenerazione > 0:
        if scommessagenerazione > creditigenerazione:
            break
        if creditigenerazione - scommessagenerazione < creditiScelti and iterazionigenerazione == 1:
            iterazionigenerazione = iterazionigenerazione + 1
        else:
            x = random.randint(1, 100)  # estraggo un numero
            nsim = nsim + 1  # dichiaro l'inizio di una nuova simulazione di scommessa
            iterazionigenerazione = iterazionigenerazione - 1
            # se vinci :
            if x <= prob:
                creditigenerazione = creditigenerazione + scommessagenerazione
                scommessagenerazione = scommessadefault
            # se perdi :
            else:
                creditigenerazione = creditigenerazione - scommessagenerazione  # togli denaro
                scommessagenerazione = scommessagenerazione * 2  # raddoppia scommessa
                if creditigenerazione <= 0:  # se perdi abortisci scommesse
                    break
    print('hai terminato con : ', creditigenerazione, 'crediti. raggiunti in ', nsim, 'scommesse', 'guadagno')
    guadagnogenerazione = creditigenerazione - crediti
    if guadagnogenerazione >= 0:
        global vittorietotali
        vittorietotali = vittorietotali + 1
        global guadagnototale
        guadagnototale = guadagnogenerazione + guadagnototale
    else:
        guadagnototale = guadagnototale + guadagnogenerazione


# ciclo di simulazione
def generazionescommessekelly(prob, crediti, iterazioni, scommessadefault):
    # parto da simulazione zero e creo variabili locali di crediti e scommessa
    frazione = ((1*prob-(100-prob))/1)
    annullamento = 0
    print(frazione)
    nsim = 0
    creditigenerazione = crediti
    iterazionigenerazione = iterazioni
    # inizio del ciclo di scommessa
    if prob <= 50:
        print("probabilitá non sufficienti per la strategia kelly.")
        annullamento = 1
    while iterazionigenerazione > 0:
        if annullamento == 1:
            break
        # aggiorno quantita di scommessa
        scommessagenerazione = (creditigenerazione/(100/frazione))
        print(scommessagenerazione)
        if scommessagenerazione > creditigenerazione:  # evita di andare sotto
            break
        if creditigenerazione - scommessagenerazione < creditiScelti and iterazionigenerazione == 1:
            iterazionigenerazione = iterazionigenerazione + 1
        else:
            x = random.randint(1, 100)  # estraggo un numero
            nsim = nsim + 1  # dichiaro l'inizio di una nuova simulazione di scommessa
            iterazionigenerazione = iterazionigenerazione - 1
            # se vinci :
            if x <= prob:
                creditigenerazione = creditigenerazione + scommessagenerazione
            # se perdi :
            else:
                creditigenerazione = creditigenerazione - scommessagenerazione  # togli denaro
                if creditigenerazione <= 0:  # se perdi abortisci scommesse
                    break
    print('hai terminato con : ', creditigenerazione, 'crediti. raggiunti in ', nsim, 'scommesse', 'guadagno')
    guadagnogenerazione = creditigenerazione - crediti
    if guadagnogenerazione >= 0:
        global vittorietotali
        vittorietotali = vittorietotali + 1
        global guadagnototale
        guadagnototale = guadagnogenerazione + guadagnototale
    else:
        guadagnototale = guadagnototale + guadagnogenerazione


# threading del ciclo
if strategiaselezionata == 'M':
    for i in range(threadselezionati):
        threading.Thread(
            target=generazionescommessemartingale(probScelta, creditiScelti, iterazioniScelte, scommessadefaultScelta))
elif strategiaselezionata == 'K':
    for i in range(threadselezionati):
        threading.Thread(
            target=generazionescommessekelly(probScelta, creditiScelti, iterazioniScelte, scommessadefaultScelta))

print('\n')
print('------------------------------------------------------------')
print('guadagno medio : ', guadagnototale / threadselezionati)
print('------------------------------------------------------------')
