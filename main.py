import forProject as fp
import forDip as fd
import utilities as ut
import forPrediction as fpr
import forTech as ft
import classifier as cl

#Parser dei comandi
def command(input):
    try:
        commands = input.split(" ")
        if commands[0] == 'help':
            ut.helpMain()
        elif commands[0] == 'lista_progetti':
            fp.listOfProject()
            ut.helpMessage()
        elif commands[0] == 'cerca_progetto':
            fp.searchProject()
            ut.helpMessage()
        elif commands[0] == 'aggiungi_progetto':
            fp.addProject()
            ut.helpMessage()
        elif commands[0] == 'modifica_progetto':
            fp.modifyProject()
            ut.helpMessage()
        elif commands[0] == 'lista_tecnologie':
            ft.listOfTechnology()
            ut.helpMessage()
        elif commands[0] == 'aggiungi_tecnologia':
            ft.addTechnology()
            ut.helpMessage()
        elif commands[0] == 'lista_dipendenti':
            fd.listOfEmployee()
            ut.helpMessage()
        elif commands[0] == 'assumi':
            fd.assunzione()
            ut.helpMessage()
        elif commands[0] == 'licenzia':
           fd.freePlaces()
           ut.helpMessage()
        elif commands[0] == 'query':
            ut.query(input[5:])
            ut.helpMessage()
        elif commands[0] == 'esempio_query':
            ut.queryExample()
            ut.helpMessage()
        elif commands[0] == 'probabilita_assunzione':
            fpr.prediction()
            ut.helpMessage()
        elif commands[0] == 'calcola_salario':
            cl.domanda()
            ut.helpMessage()
        elif commands[0] == 'esci':
            print("A presto!")
            return 0
        else:
            print("Non riesco a trovare questo comando! Consulta la lista dei comandi tramite 'help' e riprova...")
    except ValueError as err:
        print("Attenzione!", err)
        print("Riesegui l'azione!\n")
    except IndexError:
        print("Rispetta gli argomenti prima di andare avanti!")

#start main con messaggi di benvenuto + messaggio di aiuto
if __name__ == '__main__':
    ut.helloMessage()
    ut.helpMessage()
    startInput = None
    while (startInput != 'esci'):
        string = input("")
        startInput = string
        if(startInput.split()[0] == 'query'):
            command(startInput)
        else:
            startInput = string.lower()
            command(startInput)




