from pyswip import Prolog

prolog = Prolog()
prolog.consult("myKB.pl")

#mostra la lista delle tecnologie e la lista dei tipi di tecnologia
def listOfTechnology():
    myQuery = "prop(X, subClassOf, itTechnology), prop(Y, type, X)."
    technology = list(prolog.query(myQuery))
    print("\nLista tecnologie:\n")
    for elem in technology:
        queryTechnologies = "- "+elem["Y"]+""
        print(queryTechnologies)
    print()
    print("Tipi di itTechnologies utilizzati:\n")
    myQuery2 = "prop(X,subClassOf,itTechnology)"
    query2 = list(prolog.query(myQuery2))
    for elem in query2:
        queryType = "- " + elem["X"] + ""
        print(queryType)


#aggiunge una nuova tecnologia
def addTechnology():
    technology = input("Specifica prima il tipo di tecnologia (ad es. language, database, framework...):\n").lower()
    queryCheck = "prop("+technology+ ",subClassOf, Y)"
    listTech = list(prolog.query(queryCheck))
    if(len(listTech)==0):
        myQuery = "prop(" + technology + ",subClassOf, itTechnology)"
        prolog.assertz(myQuery)
        nameOfTechnology = input("Specifica il nome della tecnologia (ad es. python):\n").lower()
        myQueryNameTech = "prop(" + nameOfTechnology + ",type,"+technology+")"
        prolog.assertz(myQueryNameTech)
        print("La tecnologia chiamata "+nameOfTechnology+" di tipo "+ technology+" e' stata aggiunta")
        print()
    else:
        nameOfTechnology = input("Specifica il nome della tecnologia (ad es. python):\n").lower()
        myQueryNameTech = "prop(" + nameOfTechnology + ",type," + technology + ")"
        prolog.assertz(myQueryNameTech)
        print("La tecnologia chiamata " + nameOfTechnology + " di tipo " + technology + " e' stata aggiunta")
        print()



