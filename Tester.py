from ABRRN import *
import numpy as np
from timeit import default_timer as timer
from decimal import *
import matplotlib.pyplot as plt

getcontext().prec = 4

def main():
    abr = ABR()
    rn = RN()

    #SVANTAGGI DI ABR
    ###########################################################
    N = 10
    count = 0
    ordVect = np.arange(N)
    revVect = np.arange(N*99, N*98, -1)
    step = np.full((N,), N)
    recAbr = {}
    recRn = {}
    searchAbr = {}
    searchRn = {}

    #INSERIMENTO VALORI CRESCENTI  E RICERCA DELL'ULTIMO VALORE INSERITO
    while (count < 99): #inserisco 10 elementi tutti insieme e controllo i tempi di inserimento, viene eseguito 99 volte
        #ABR
        start = Decimal(timer())
        for i in ordVect:
            abr.insert(i)
        end = Decimal(timer())
        recAbr[N*count] = end - start                #la chiave indica il numero di elementi già nell'albero al momento dell'inserimento

        start = Decimal(timer())
        abr.find((N * (count + 1)) - 1)
        end = Decimal(timer())
        print(":>Abr trova l'ultimo valore in ", N * (count + 1), " elementi (ordinati) in ", end - start, "s.")
        searchAbr[N * (count + 1)] = end - start

        #ABRRN
        start = Decimal(timer())
        for i in ordVect:
            rn.insert(i)
        end = Decimal(timer())
        recRn[N * count] = end - start

        start = Decimal(timer())
        rn.find((N*(count+1))-1)
        end = Decimal(timer())
        print(":>Rn trova l'ultimo valore in ", N*(count+1)," elementi (ordinati) in ", end - start,"s.")
        searchRn[N * (count + 1)] = end - start

        # aggiornamento dei valori
        count += 1
        if (count < 99):
            np.add(ordVect, step)  # ...ma anche per aumentare i valori di ordVect...
            np.subtract(revVect, step)  # ...e diminuire quelli di revVect.

    print("Abr e ordinato:>", recAbr)
    print("Rn e ordinato:>", recRn)
    #GRAFICO INSERIMENTO VALORI ORDINATI#
    x = recAbr.keys()
    y_abr = recAbr.values()
    y_rn = recRn.values()
    plt.plot(x, y_abr)
    plt.plot(x, y_rn)
    plt.xlabel('Numero di elementi precedentemente inseriti')
    plt.ylabel('Tempo richiesto')
    plt.legend(['ABR', 'ARN'])
    plt.title('Inserimento di valori ordinati')
    plt.show()
    #GRAFICO RICERCA VALORI ORDINATI
    x1 = searchAbr.keys()
    y_abr = searchAbr.values()
    y_rn = searchRn.values()
    plt.plot(x1, y_abr)
    plt.plot(x1, y_rn)
    plt.xlabel('Dimensione dell albero')
    plt.ylabel('Tempo richiesto')
    plt.legend(['ABR', 'ARN'])
    plt.title('Ricerca in valori ordinati')
    plt.show()

    abr = ABR()
    rn = RN()
    count = 0
    recAbr = {}
    recRn = {}


    #INSERIMENTO VALORI COSTANTI  E RICERCA DELL'ULTIMO VALORE INSERITO
    while(count < 99):
        #ABR
        start = Decimal(timer())
        for i in step:                  #step è usato come vettore di valori costanti...
            abr.insert(i)
        end = Decimal(timer())
        recAbr[N * count] = end - start  # la chiave indica il numero di elementi già nell'albero al momento dell'inserimento

        start = Decimal(timer())
        abr.find((N * (count + 1)) - 1)
        end = Decimal(timer())
        print(":>Abr trova l'ultimo valore in ", N * (count + 1), " elementi (costanti) in ", end - start, "s.")
        searchAbr[N * (count + 1)] = end - start

        #ABRRN
        start = Decimal(timer())
        for i in step:
            rn.insert(i)
        end = Decimal(timer())
        recRn[N * count] = end - start

        start = Decimal(timer())
        rn.find((N * (count + 1)) - 1)
        end = Decimal(timer())
        print(":>Rn trova l'ultimo valore in ", N * (count + 1), " elementi (costanti) in ", end - start,"s.")
        searchRn[N * (count + 1)] = end - start

        # aggiornamento dei valori
        count += 1
        if (count < 99):
            np.add(ordVect, step)  # ...ma anche per aumentare i valori di ordVect...
            np.subtract(revVect, step)  # ...e diminuire quelli di revVect.

    print("Abr e costante:>", recAbr)
    print("Rn e costante:>", recRn)
    #GRAFICO INSERIMENTO VALORI COSTANTI#
    y_abr = recAbr.values()
    y_rn = recRn.values()
    plt.plot(x, y_abr)
    plt.plot(x, y_rn)
    plt.xlabel('Numero di elementi precedentemente inseriti')
    plt.ylabel('Tempo richiesto')
    plt.legend(['ABR', 'ARN'])
    plt.title('Inserimento di valori costanti')
    plt.show()
    #GRAFICO RICERCA VALORI COSTANTI#
    y_abr = searchAbr.values()
    y_rn = searchRn.values()
    plt.plot(x1, y_abr)
    plt.plot(x1, y_rn)
    plt.xlabel('Dimensione dell albero')
    plt.ylabel('Tempo richiesto')
    plt.legend(['ABR', 'ARN'])
    plt.title('Ricerca in valori costanti')
    plt.show()

    abr = ABR()
    rn = RN()
    count = 0
    recAbr = {}
    recRn = {}

    #INSERIMENTO VALORI CASUALI E RICERCA DELL'ULTIMO VALORE INSERITO
    while(count < 99):
        rndVect = np.random.random((N * (count+1),))
        #ABR
        start = Decimal(timer())
        for i in rndVect:
            abr.insert(i)
        end = Decimal(timer())
        recAbr[N * count] = end - start  # la chiave indica il numero di elementi già nell'albero al momento dell'inserimento

        start = Decimal(timer())
        abr.find((N * (count + 1)) - 1)
        end = Decimal(timer())
        print(":>Abr trova l'ultimo valore in ", N * (count + 1), " elementi (casuali) in ", end - start,"s.")
        searchAbr[N * (count + 1)] = end - start

        #ABRRN
        start = Decimal(timer())
        for i in rndVect:
            rn.insert(i)
        end = Decimal(timer())
        recRn[N * count] = end - start

        start = Decimal(timer())
        rn.find((N * (count + 1)) - 1)
        end = Decimal(timer())
        print(":>Rn trova l'ultimo valore in ", N * (count + 1), " elementi (casuali) in ", end - start,"s.")
        searchRn[N * (count + 1)] = end - start

        #aggiornamento dei valori
        count += 1
        if(count < 99):
            np.add(ordVect, step)       #...ma anche per aumentare i valori di ordVect...
            np.subtract(revVect, step)  #...e diminuire quelli di revVect.

    print("Abr e casuale:>", recAbr)
    print("Rn e casuale:>", recRn)
    #GRAFICO INSERIMENTO VALORI CASUALI#
    y_abr = recAbr.values()
    y_rn = recRn.values()
    plt.plot(x, y_abr)
    plt.plot(x, y_rn)
    plt.xlabel('Numero di elementi precedentemente inseriti')
    plt.ylabel('Tempo richiesto')
    plt.legend(['ABR', 'ARN'])
    plt.title('Inserimento di valori casuali')
    plt.show()
    #GRAFICO RICERCA VALORI CASUALI#
    y_abr = searchAbr.values()
    y_rn = searchRn.values()
    plt.plot(x1, y_abr)
    plt.plot(x1, y_rn)
    plt.xlabel('Dimensione dell albero')
    plt.ylabel('Tempo richiesto')
    plt.legend(['ABR', 'ARN'])
    plt.title('Ricerca in valori casuali')
    plt.show()

if __name__ == "__main__":
    main()