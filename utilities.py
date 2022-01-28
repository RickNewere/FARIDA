from pyswip import Prolog
from pyswip.prolog import PrologError

prolog = Prolog()
prolog.consult("myKB.pl")

#messaggio di saluto
def helloMessage():
    print("Ciao! Sono FARIDA, il tuo assistente personale! Come posso aiutarti?")

#mostra l'elenco dei comandi ammessi
def helpMain():
  print("\n|--------------------------------------- SEZ.PROGETTI ----------------------------------------------|\n"
          "|'lista_progetti' - mostra la lista dei progetti disposizione                                       |\n"
          "|'cerca_progetto' - mostra tutti i progetti che contengono la tecnologia passata                    |\n"
          "|'aggiungi_progetto' - aggiunge un nuovo progetto                                                   |\n"
          "|'modifica_progetto' - modifica un progetto esistente                                               |\n"
          "|--------------------------------------- SEZ.TECNOLOGIE --------------------------------------------|\n"
          "|'lista_tecnologie' - mostra la lista delle tecnologie presenti                                     |\n"
          "|'aggiungi_tecnologia' - aggiunge una tecnologia                                                    |\n"
          "|--------------------------------------- SEZ.DIPENDENTI --------------------------------------------|\n"
          "|'lista_dipendenti' - mostra le risorse umane dell'azienda e il loro numero                         |\n"
          "|'assumi' - incrementa il numero della figura aziendale in base alla quantita' passata              |\n"
          "|'licenzia' - decrementa il numero della figura aziendale in base alla quantita' passata            |\n"
          "|--------------------------------------- ALTRI COMANDI ---------------------------------------------|\n"
          "|'esempio_query' - mostra un esempio di query possibile                                             |\n"
          "|'query prop(query)' - permette di effettuare una query                                             |\n"
          "|'probabilita_assunzione' - prevede la probabilità di essere assunti in base alle proprie capacita' |\n"
          "|'calcola_salario' - prevede l'eventuale stipendio in caso di assunzione                            |\n"
          "|'accuratezza_classificatore' - calcola l'accuratezza del classificatore                            |\n"
          "|'esci' - esce dal programma                                                                        |\n"
          "|---------------------------------------------------------------------------------------------------|\n")


#stampa i risultati di una query
def query(string):
    try:
        myList = list(prolog.query(string))
        print("Risultato(i):\n")
        for elem in myList:
            print(elem)
    except PrologError:
        print(string + " <-- c'e' qualcosa che non va nel formato della query! Controllala prima di continuare! Consulta il comando 'esempio_query' per avere un aiuto!")

#mostra il messaggio di aiuto all'utente
def helpMessage():
     print("\nDigita 'help' per scoprire i comandi: ")


#mostra un esempio di query
def queryExample():
    myQuery = "prop(X,type,staff)"
    staffFigure = list(prolog.query(myQuery))
    print("\nUn esempio di query e' il seguente: query prop(X,type,staff)\n")
    print("Il risultato di questa query e' il seguente:\n")
    for elem in staffFigure:
        print(elem)
    print()
    print("Sono ammesse anche query concatenate! Utilizza piu' variabili e usa la ',' tra una query e l'altra!")
