from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

competenze = read_csv('../../PycharmProjects/FARIDA/salary.csv')
X = competenze.drop(columns=['salary'])
y = competenze['salary']

modello = DecisionTreeClassifier()
modello.fit(X.values, y.values)

def domanda():
    sex = ""
    age = 0
    yearsExperience = -1;
    result = True
    check = True
    while(sex != "maschio" and sex != "femmina"):
        sex = input("Inserisci il tuo sesso (maschio/femmina): ").lower()
        if(sex == "maschio"):
         firstParameter = 0
        elif(sex == "femmina"):
         firstParameter = 1
        else:
         print("Stai sbagliando qualcosa, rileggi attentamente ciò che ti viene chiesto!")
    while(age < 18 or age > 60 and True):
        try:
            while (result):
                age = (int)(input("Inserisci la tua eta' (intero): "))
                if(age < 18 or age > 60):
                    print("Non assumiamo personale con eta' < 18 o eta' > 60")
                    check=True
                    while(check):
                        userInput = input("Inserisci 'back' per tornare al menu' iniziale, 'retry' per proseguire:\n")
                        if(userInput == 'back'):
                            print("\nTorno alla Main Page!")
                            return None
                        elif(userInput == 'retry'):
                            check = False
                        else:
                            print("Stai sbagliando qualcosa, rileggi attentamente ciò che ti viene chiesto!")
                            check=True
                else:
                    result = False
        except ValueError:
                print("Ti avevo chiesto di inserire un numero...")
    while(yearsExperience < 0 or (age - yearsExperience) < 18 and True):
        try:
            yearsExperience = (float)(input("Inserisci gli anni di esperienza (es: 2/2.5/2.7): "))
            if(yearsExperience < 0 or (age - yearsExperience) < 18):
                print("La nostra azienda conta gli anni di esperienza solo dalla maggiore eta'")
        except ValueError:
            print("Ti avevo chiesto di inserire un numero...")
    salary = modello.predict([[firstParameter, age, yearsExperience]])
    for elem in salary:
     print("Il salario annuale a cui potresti ambire e': " + elem +"€ netti")
