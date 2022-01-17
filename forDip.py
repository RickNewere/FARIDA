from pyswip import Prolog
import utilities as ut

prolog = Prolog()
prolog.consult("myKB.pl")

#mostra la lista dei dipendenti, il loro numero e la lista delle posizioni non ricoperte
def listOfEmployee():
    myTrueQuery = "prop(X, list_of_employees, true)"
    myList = list(prolog.query(myTrueQuery))
    print("\nLista risorse umane: ")
    for elem in myList:
        nWorkers = list(prolog.query("prop(" + elem["X"] + ", availability, X)."))[0]['X']
        print("-" + elem["X"] + ": " + "n.ro " + str(nWorkers))
    myFalseQuery = "prop(X, list_of_employees, false)"
    nEmptyPosition= list(prolog.query(myFalseQuery))
    if nEmptyPosition:
        print("\nDovrai assumere le seguenti risorse umane:\n")
        for elem in nEmptyPosition:
            print("- "+ elem["X"])
    print()


#incrementa il numero del personale che andiamo a selezionare
def assunzione():
    listOfEmployee()
    check = True
    while (check):
        staffName = input("Inserisci la figura che si vuole assumere:\n").lower()
        queryStaff = "prop(" + str(staffName) + ",type,staff)"
        listEmployee = list(prolog.query(queryStaff))
        if (len(listEmployee) > 0):
            while(check):
                quantity = (input("Inserisci la quantita' (numerica):\n"))
                if(quantity.isnumeric()):
                    intQuantity = int(quantity)
                    myQuery = "prop(" + staffName + " , availability, X)"
                    initialStaff = list(prolog.query(myQuery))[0]['X']
                    prolog.retract("prop(" + staffName + " , availability," + str(initialStaff) + ")")
                    prolog.assertz("prop(" + staffName + " , availability," + str(initialStaff + intQuantity) + ")")
                    print("Sono stati aggiunti " + str(intQuantity) + " membri. Il numero di " + staffName + " adesso e' aggiornato!")
                    check = False
                else: print("Ti avevo chiesto di inserire un numero...")
        else:
            print("Errore nell'inserimento della figura. Questa figura non esiste all'interno della tua azienda...Ricontrolla ciò che hai inserito.")


#decrementa il numero del personale che andiamo a selezionare
def freePlaces():
    listOfEmployee()
    check = True
    while (check):
        staffName = input("Inserisci la figura di vuoi ridurne il numero:\n")
        queryStaff = "prop("+str(staffName)+",type,staff),prop("+str(staffName)+",list_of_employees, true)"
        listEmployee = list(prolog.query(queryStaff))
        if(len(listEmployee)>0):
            while(check):
                quantity = (input("Inserire la quantita' (numerica):\n"))
                if (quantity.isnumeric()):
                    intQuantity = int(quantity)
                    negativeQuantity = -abs(intQuantity)
                    myQuery = ("prop(" + staffName + " , availability, X)")
                    initialStaff = list(prolog.query(myQuery))[0]['X']
                    if (int(intQuantity) <= initialStaff):
                        prolog.retract("prop(" + staffName + " , availability," + str(initialStaff) + ")")
                        prolog.assertz("prop(" + staffName + " , availability," + str(initialStaff + negativeQuantity) + ")")
                        print("Sono stati liberati " + str(intQuantity) + " posti. Il numero di " + staffName + " adesso e' aggiornato!")
                        check = False
                    else:
                        print("La quantita' inserita deve essere minore o uguale dei posti occupati! Riesegui l'operazione...")
                else:
                    print("Ti avevo chiesto di inserire un numero...")
        else:
            print("Errore nell'inserimento della figura. Questa figura non esiste all'interno della tua azienda...Ricontrolla ciò che hai inserito.")
