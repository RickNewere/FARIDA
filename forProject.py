from pyswip import Prolog

prolog = Prolog()
prolog.consult("myKB.pl")

#mostra la lista di tutti i progetti. Permette, inoltre, di visualizzare le tecnologie utilizzate nel progetto passato
def listOfProject():
    result = True
    myQuery = "prop(X, subClassOf, project)."
    project = list(prolog.query(myQuery))
    print("Lista progetti:\n")
    for elem in project:
        queryProjects = "- "+elem["X"]+""
        print(queryProjects)
    while(result):
        nameOfProject = input("\nDigita il nome del progetto se vuoi avere piu' informazioni, 'back' per "
                              "tornare indietro:\n").lower()
        if(nameOfProject == 'back'):
            print("\nTorno alla Main Page!")
            return None
        else:
            languageUsed = "prop(" + nameOfProject + ", requires, Y)"
            listLanguage = list(prolog.query(languageUsed))
            if (len(listLanguage) > 0):
                print("\nTecnologie utilizzate:\n")
                for languages in listLanguage:
                    queryLanguages = "- "+languages["Y"]+""
                    print(queryLanguages)
            workers = "prop(Y, work,"+nameOfProject+")"
            listWorkers = list(prolog.query(workers))
            if (len(listWorkers) > 0):
                print("\nFigure impegnate nel progetto:\n")
                for work in listWorkers:
                    queryWorkers = "- "+work["Y"]+""
                    print(queryWorkers)
                return None
            else:
                print("\nNome del progetto inesistente, riprova...")
                result = True


#cerca un progetto in base alla tecnologia passata. Il programma mostra ogni occorrenza in base alla tecnologia cercata
def searchProject():
    technology = input("Inserisci il nome della tecnologia ricercata (ex. python):\n").lower()
    if(len(technology) > 0):
        query = "prop(" + technology + ", is_required, X)"
        myList = list(prolog.query(query))
        if myList:
            print("I progetti che fanno uso di "+technology+" sono:\n")
            for elem in myList:
                print("- " + elem["X"])
        else:
            print("Non ci sono progetti che usano "+technology+"!")
            print()
    else:
        print("Errore nella digitazione, riprova...")
        return None

#aggiunge un nuovo progetto in base alle tecnologie e alle figure che ci lavoreranno passate
def addProject():
    myQueryListProject = "prop(X, subClassOf, project)."
    project = list(prolog.query(myQueryListProject))
    print("Lista progetti esistenti:\n")
    for elem in project:
        queryProjects = "- " + elem["X"] + ""
        print(queryProjects)
    print()
    nameOfProject = input("Inserisci il nome del nuovo progetto:\n").lower()
    queryCheck = "prop(" + nameOfProject + ",subClassOf, project)"
    listProject = list(prolog.query(queryCheck))
    if (len(listProject) == 0):
        myQuery = "prop(" + nameOfProject + ",subClassOf, project)"
        prolog.assertz(myQuery)
        myQueryListTech = "prop(X, subClassOf, itTechnology), prop(Y, type, X)."
        technology = list(prolog.query(myQueryListTech))
        print("Lista tecnologie esistenti:\n")
        for elem in technology:
            queryTechnologies = "- " + elem["Y"] + ""
            print(queryTechnologies)
        print()
        controlInt=True
        while(controlInt):
         try:
            nOfTechUsed = (int)(input("Inserisci il numero di tecnologie che richiede il progetto:\n"))
            for i in range(nOfTechUsed):
                    check = True
                    while(check):
                        nameOfTechUsed = input("Inserisci il nome della della tecnologia utilizzata:\n").lower()
                        myQueryNameTech = "prop(X ,subClassOf, itTechnology), prop(" + nameOfTechUsed +",type, X)"
                        listTech = list(prolog.query(myQueryNameTech))
                        if(len(listTech) > 0):
                            creationQueryRequires = "prop(" + nameOfProject + ", requires," + nameOfTechUsed + ")"
                            listTechExists = list(prolog.query(creationQueryRequires))
                            if (len(listTechExists) == 0):
                                creationQueryIsRequired = "prop(" + nameOfTechUsed + ",is_required," + nameOfProject + ")"
                                prolog.assertz(creationQueryRequires)
                                prolog.assertz(creationQueryIsRequired)
                                print("Tecnologia aggiunta al progetto!")
                                check = False
                                controlInt = False
                            else:
                                print("Questa tecnologia e' gia' richiesta dal progetto, aggiungine una diversa!")
                        else:
                                print("Questa tecnologia non esiste! Creala prima di assegnarla ad un progetto!")
         except ValueError:
             print("Ti avevo chiesto di inserire un numero...")
        myTrueQuery = "prop(X, list_of_employees, true)"
        myList = list(prolog.query(myTrueQuery))
        print("\nLista Risorse Umane:\n")
        for elem in myList:
            print("- " + elem["X"] + "")
        print()
        controlInt = True
        while(controlInt):
            try:
             nOfFigureWorkIn = (int)(input("Inserisci il numero di figure che lavorano all'interno del progetto:\n"))
             for i in range(nOfFigureWorkIn):
                check = True
                while(check):
                    nameOfFigure = input("Inserisci il nome della figura che lavorera' al progetto:\n")
                    myQueryNameFigure = "prop(" + nameOfFigure + ", list_of_employees, true)"
                    listFigure = list(prolog.query(myQueryNameFigure))
                    if(len(listFigure)>0):
                        creationFigureQuery = "prop("+ nameOfFigure + ", work," + nameOfProject +")"
                        prolog.assertz(creationFigureQuery)
                        print("Figura aggiunta al progetto!")
                        check = False
                        controlInt = False
                    else:
                        print("Questa figura non esiste! Aggiungila prima di ripetere l'operazione!")
            except ValueError:
                    print("Ti avevo chiesto di inserire un numero...")
        print("Il progetto e' stato creato e inserito nella lista dei progetti!")
        print()
    else:
        print("Esiste già un progetto con quel nome! Prova a modificare quello.")
        print()

#modifica un progetto esistente
def modifyProject():
    myQueryListProject = "prop(X, subClassOf, project)."
    project = list(prolog.query(myQueryListProject))
    print("Lista progetti esistenti:\n")
    for elem in project:
        queryProjects = "- " + elem["X"] + ""
        print(queryProjects)
    nameOfProject = input("\nInserisci il nome del progetto che si vuole modificare:\n").lower()
    queryCheck = "prop(" + nameOfProject + ",subClassOf, project)"
    listProject = list(prolog.query(queryCheck))
    if (len(listProject) > 0):
        queryRetract = "prop(" + nameOfProject + ", requires, X)"
        prolog.retractall(queryRetract)
        myQuery = "prop(" + nameOfProject + ",subClassOf, project)"
        prolog.retract(myQuery)
        queryRetractFigure = "prop(Y, work,"+nameOfProject+")"
        prolog.retractall(queryRetractFigure)
        queryRetractIsRequired = "prop(X,is_required," + nameOfProject + ")"
        prolog.retractall(queryRetractIsRequired)
        prolog.assertz(myQuery)
        myQueryListTech = "prop(X, subClassOf, itTechnology), prop(Y, type, X)."
        technology = list(prolog.query(myQueryListTech))
        print("Lista tecnologie esistenti:\n")
        for elem in technology:
            queryTechnologies = "- " + elem["Y"] + ""
            print(queryTechnologies)
        print()
        controlInt = True
        while (controlInt):
            try:
                nOfTechUsed = input("Inserisci il numero di tecnologie che richiede il progetto:\n")
                for i in range(int(nOfTechUsed)):
                    check = True
                    while (check):
                        nameOfTechUsed = input("Inserisci il nome della della tecnologia utilizzata:\n").lower()
                        myQueryNameTech = "prop(X ,subClassOf, itTechnology), prop(" + nameOfTechUsed + ",type, X)"
                        listTech = list(prolog.query(myQueryNameTech))
                        if (len(listTech) > 0):
                            creationQueryRequires = "prop(" + nameOfProject + ", requires," + nameOfTechUsed + ")"
                            listTechExists = list(prolog.query(creationQueryRequires))
                            if (len(listTechExists) == 0):
                                creationQueryIsRequired = "prop(" + nameOfTechUsed + ",is_required," + nameOfProject + ")"
                                prolog.assertz(creationQueryRequires)
                                prolog.assertz(creationQueryIsRequired)
                                print("Tecnologia aggiunta al progetto!")
                                check = False
                                controlInt = False
                            else:
                                print("Questa tecnologia e' gia' richiesta dal progetto, aggiungine una diversa!")
                        else:
                            print("Questa tecnologia non esiste! Creala prima di assegnarla ad un progetto!")
            except ValueError:
                    print("Ti avevo chiesto di inserire un numero...")
        myTrueQuery = "prop(X, list_of_employees, true)"
        myList = list(prolog.query(myTrueQuery))
        print("\nLista Risorse Umane:\n")
        for elem in myList:
            print("- " + elem["X"] + "")
        print()
        controlInt=True
        while (controlInt):
            try:
                nOfFigureWorkIn = (int)(input("Inserisci il numero di figure che lavorano all'interno del progetto:\n"))
                for i in range(nOfFigureWorkIn):
                    check = True
                    while (check):
                        nameOfFigure = input("Inserisci il nome della figura che lavorera' al progetto:\n")
                        myQueryNameFigure = "prop(" + nameOfFigure + ", list_of_employees, true)"
                        listFigure = list(prolog.query(myQueryNameFigure))
                        if (len(listFigure) > 0):
                            creationFigureQuery = "prop(" + nameOfFigure + ", work," + nameOfProject + ")"
                            prolog.assertz(creationFigureQuery)
                            print("Figura aggiunta al progetto!")
                            check = False
                            controlInt = False
                        else:
                            print("Questa figura non esiste! Aggiungila prima di ripetere l'operazione!")
            except ValueError:
                    print("Ti avevo chiesto di inserire un numero...")
        print("Il progetto e' stato modificato correttamente!")
        print()
    else:
        print("Non esiste un progetto con quel nome! Prova a crearlo!")
        print()

