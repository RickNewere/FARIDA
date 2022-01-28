from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController

# Costruizione Rete Bayesiana Percentuale Assunzione

#titolo di studio posseduto fino a quel momento
titoloDiStudio = BbnNode(Variable(0, 'titolo di studio', ['laurea', 'diploma', 'titolo di studio inferiore']), [0.70, 0.25,
                                                                                                                0.05])
#l'utente ha mai lavorato in un'azienda?
esperienzaPregressa = BbnNode(Variable(1, 'esperienza pregressa', ['si', 'no']), [0.85, 0.15])
#nodo di presentazione principale (1-2)
valorePersonale = BbnNode(Variable(2, 'valore personale', ['ottimo', 'scarso']),
                          [0.98, 0.02, 0.75, 0.25, 0.6, 0.4, 0.51, 0.49, 0.15, 0.85, 0.05, 0.95])
#l'utente è appassionato?
passioneInformatica = BbnNode(Variable(3, 'passione informatica', ['si', 'no']), [0.85, 0.15])
#preferisce programmare front o back end?
sviluppoWeb = BbnNode(Variable(4, 'sviluppo web', ['back end', 'front end']), [0.71, 0.29])
#nodo di presentazione competenze informatiche (3-4)
valoreInformatico = BbnNode(Variable(5, 'valore informatico', ['ottimo', 'scarso']), [0.80, 0.20, 0.73, 0.27,
                                                                                      0.33, 0.67, 0.02, 0.98])
#nodo per un primo profilo dell'utente (2-5)
punteggioPersonale = BbnNode(Variable(6, 'punteggio personale', ['ottimo', 'scarso']), [0.99, 0.01, 0.72, 0.28, 0.32,
                                                                                        0.68, 0.02, 0.98])
#l'utente conosce Java come linguaggio di programmazione?
conoscenzaJava = BbnNode(Variable(7, 'conoscenza Java', ['si', 'no']), [0.93, 0.07])
#l'utente conosce Python come linguaggio di programmazione?
conoscenzaPython = BbnNode(Variable(8, 'conoscenza Python', ['si', 'no']), [0.85, 0.15])
#nodo per la conoscenza dei linguaggi (7-8)
conoscenzaLinguaggi = BbnNode(Variable(9, 'conoscenza linguaggi', ['ottima', 'scarsa']), [0.93, 0.07, 0.83, 0.17,
                                                                                          0.52, 0.48, 0.12, 0.88])
#l'utente sa usare MySQL?
conoscenzaMysql = BbnNode(Variable(10, 'conoscenza Mysql', ['si', 'no']), [0.95, 0.05])
#l'utente sa usare MongoDB?
conoscenzaMongo = BbnNode(Variable(11, 'conoscenza Mongo', ['si', 'no']), [0.85, 0.15])
#nodo per la conoscenza DB(10-11)
conoscenzaDB = BbnNode(Variable(12, 'conoscenza DB', ['ottima', 'scarsa']), [0.92, 0.08, 0.77, 0.23, 0.39, 0.61,
                                                                             0.16, 0.84])
#nodo per il vincolo lavorativo (9-12)
valoreLavorativo = BbnNode(Variable(13, 'valore lavorativo', ['ottimo', 'scarso']), [0.95, 0.05, 0.68, 0.32, 0.51,
                                                                                     0.49, 0.06, 0.94])
#previsione finale della % di essere assunti (6-13)
previsioneAssunzione = BbnNode(Variable(14, 'previsione assunzione', ['si', 'no']), [0.99, 0.01, 0.72, 0.28, 0.3, 0.7,
                                                                                     0.2, 0.8])

bbn = Bbn() \
    .add_node(titoloDiStudio) \
    .add_node(esperienzaPregressa) \
    .add_node(valorePersonale) \
    .add_node(passioneInformatica) \
    .add_node(sviluppoWeb) \
    .add_node(valoreInformatico) \
    .add_node(punteggioPersonale) \
    .add_node(conoscenzaJava) \
    .add_node(conoscenzaPython) \
    .add_node(conoscenzaLinguaggi) \
    .add_node(conoscenzaMysql) \
    .add_node(conoscenzaMongo) \
    .add_node(conoscenzaDB) \
    .add_node(valoreLavorativo) \
    .add_node(previsioneAssunzione) \
    .add_edge(Edge(titoloDiStudio, valorePersonale, EdgeType.DIRECTED)) \
    .add_edge(Edge(esperienzaPregressa, valorePersonale, EdgeType.DIRECTED)) \
    .add_edge(Edge(passioneInformatica, valoreInformatico, EdgeType.DIRECTED)) \
    .add_edge(Edge(sviluppoWeb, valoreInformatico, EdgeType.DIRECTED)) \
    .add_edge(Edge(valorePersonale, punteggioPersonale, EdgeType.DIRECTED)) \
    .add_edge(Edge(valoreInformatico, punteggioPersonale, EdgeType.DIRECTED)) \
    .add_edge(Edge(conoscenzaJava, conoscenzaLinguaggi, EdgeType.DIRECTED)) \
    .add_edge(Edge(conoscenzaPython, conoscenzaLinguaggi, EdgeType.DIRECTED)) \
    .add_edge(Edge(conoscenzaMysql, conoscenzaDB, EdgeType.DIRECTED)) \
    .add_edge(Edge(conoscenzaMongo, conoscenzaDB, EdgeType.DIRECTED)) \
    .add_edge(Edge(conoscenzaLinguaggi, valoreLavorativo, EdgeType.DIRECTED)) \
    .add_edge(Edge(conoscenzaDB, valoreLavorativo, EdgeType.DIRECTED)) \
    .add_edge(Edge(valoreLavorativo, previsioneAssunzione, EdgeType.DIRECTED)) \
    .add_edge(Edge(punteggioPersonale, previsioneAssunzione, EdgeType.DIRECTED))

# Conversione da bbn ad albero
treeCopy = InferenceController.apply(bbn)

#Setta il valore scelto in base alla risposta data
def insertDefinedValue(tree, nodeName, optionName, value):
    ev = EvidenceBuilder() \
        .with_node(tree.get_bbn_node_by_name(nodeName)) \
        .with_evidence(optionName, value) \
        .build()
    tree.set_observation(ev)

#predizione: domande da fare all'utente
def prediction():
    tree = treeCopy.__copy__()

    while True:
        value = input(
            "Indicare il proprio titolo di studio:\n"
            "Risposte possibili: (laurea) (diploma) (titolo di studio inferiore) (dato mancante)\n").lower()
        if value in ["laurea", "diploma", "titolo di studio inferiore"]:
            insertDefinedValue(tree, "titolo di studio", value, 1.0)
            break
        elif value in ["dato mancante"]:
            info(0)

    while True:
        value = input(
            "Indicare se si possiedono esperienze pregresse in aziende informatiche:\n"
            "Risposte possibili: (si) (no) (dato mancante)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "esperienza pregressa", value, 1.0)
            break
        elif value in ["dato mancante"]:
            info(1)

    while True:
        value = input("Ti affascina il mondo dell'informatica:\n"
                      "Risposte possibili: (si) (no) (dato mancante)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "passione informatica", value, 1.0)
            break
        elif value in ["dato mancante"]:
            info(2)

    while True:
        value = input("Preferisci:\n"
                      "Risposte possibili: (back end) (front end) (dato mancante)\n").lower()
        if value in ["back end", "front end"]:
            insertDefinedValue(tree, "sviluppo web", value, 1.0)
            break
        elif value in ["dato mancante"]:
            info(3)

    while True:
        value = input("Hai conoscenze del linguaggio Java:\n"
                      "Risposte possibili: (si) (no) (dato mancante)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "conoscenza Java", value, 1.0)
            break
        elif value in ["dato mancante"]:
            info(4)

    while True:
        value = input("Hai conoscenze del linguaggio Python:\n"
                      "Risposte possibili: (si) (no) (dato mancante)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "conoscenza Python", value, 1.0)
            break
        elif value in ["dato mancante"]:
            info(5)

    while True:
        value = input("Sai usare MySQL:\n"
                      "Risposte possibili: (si) (no) (dato mancante)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "conoscenza Mysql", value, 1.0)
            break
        elif value in ["dato mancante"]:
            info(6)

    while True:
        value = input("Sai usare MongoDB:\n"
                      "Risposte possibili: (si) (no) (dato mancante)\n").lower()
        if value in ["si", "no"]:
            insertDefinedValue(tree, "conoscenza Mongo", value, 1.0)
            break
        elif value in ["dato mancante"]:
            info(7)

    print("Analisi delle tue risposte...")
    outputPrediction(tree)


#stampa la probabilità di essere assunti e,in base alla probabilità, stampa un messaggio/consiglio
def outputPrediction(tree):
    for node, posteriors in tree.get_posteriors().items():
        if node == 'previsione assunzione':
            max, min = posteriors.items()
            print(f'[{node} : {max[1]*100:.0f}%]')
            if max[1] < 0.26:
                print("Probabilità di assunzione: bassa.\nTi consiglio fortemente di investire nella tua formazione.\n"
                      "Ad oggi le tue competenze ed esperienze non sono idonee per ricoprire un eventuale posto di lavoro!\n"
                      "Ti consiglio di seguire corsi specializzati in modo da arricchire le tue competenze!")
            elif max[1] < 0.4:
                print("Probabilità di assunzione: medio-bassa.\nTi consiglio di investire nella tua formazione.\n"
                      "Ti consiglio di seguire corsi specializzati in modo da arricchire le tue competenze!")
            elif max[1] < 0.5:
                print("Probabilità di assunzione: media.\nIl sapere non è mai abbastanza. \nTi consiglio comunque "
                      "di accrescere la propria formazione e arricchire le tue esperienze!")
            elif max[1] < 0.7:
                print("Probabilità di assunzione: medio-alta.\nÈ probabile che tu sia assunto!\nTi consiglio di accrescere "
                      "la propria formazione e arricchiere le tue esperienze!")
            else:
                print("Probabilità di assunzione: alta.\nÈ molto probabile che tu sia assunto!\n"
                      "Con queste conoscenze ed esperienze essere assunti sarà un gioco da ragazzi!")


def info(number):
    if number == 0:
        print("Devi inserire il tuo titolo di studio, cioe indicare se sei laureato, diplomato o hai un titolo di studio inferiore\n")
    elif number == 1:
        print("Devi indicare se hai avuto in passato altre esperienze lavorative nel campo informatico:"
              " 'si' se hai gia esperienze lavorative nel mondo informatico, 'no' altrimenti\n")
    elif number == 2:
        print("Devi indicare se sei appassionato per tutto cio che riguarda l'informatica: 'si' se sei appassionato, 'no' altrimenti\n")
    elif number == 3:
        print("Il backend, denominato anche “lato server”, è la parte del sito web che non puoi vedere e con cui non"
              " puoi interagire. Fondamentalmente, tutto ciò che accade dietro le quinte può essere attribuito allo sviluppo web back-end\n"
              "Il frontend è la parte del sito web che puoi vedere e con cui puoi interagire direttamente per ricevere"
              " le funzionalità di backend del sistema. Coinvolge tutto ciò che l’utente può vedere, toccare e sperimentare.\n"
              "Scegli quello che ti appassiona di piu!\n")
    elif number == 4:
        print("Java è un linguaggio di programmazione generico utilizzato per lo sviluppo web. Java è uno dei linguaggi "
              "di programmazione più popolari in uso, in particolare per le applicazioni web client-server.\n"
              "Indicare con 'si' se sai usare java, 'no' altrimenti\n")
    elif number == 5:
        print("Python è un linguaggio di programmazione orientato agli oggetti noto per la sua chiarezza, "
              "potenza e flessibilità. Si tratta di un linguaggio interpretato, il che significa che un interprete legge"
              " ed esegue il codice direttamente, senza compilazione.\n"
              "Indicare con 'si' se sai usare python, 'no' altrimenti\n")
    elif number == 6:
        print("MySQL è un RDBMS (Relational Database Management System) open source disponibile gratuitamente che utilizza Structured Query Language (SQL).\n"
              "Indicare con 'si' se sai usare MySQL, 'no' altrimenti\n")
    elif number == 7:
        print("MongoDB è un database scalabile e ad alte prestazioni progettato per gestire l'archiviazione orientata"
              " ai documenti. Classificato come noSQL, multipiattaforma, gratuito e open source, MongoDB è stato scritto"
              " in C++ nel 2007 originariamente come parte principale di un prodotto PaaS (Platform as a Service),"
              " per poi essere rilasciato come progetto open source nel 2009.\n"
              "Indicare con 'si' se sai usare mongoDB, 'no' altrimenti")


