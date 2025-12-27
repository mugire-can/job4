## job 1

def my_print_hello():
    print("Hello world")

my_print_hello()

## job 2

def My_print_name(name):
    print(name)

My_print_name("Can")
My_print_name("Han")
My_print_name("Zam")


## job 3

def Add(a,b):
    result = a+ b
    print(result)

Add(5, 6)
Add(8, 7)
Add(1, 97)

## job 4


def GetHello():
    print("Hello La Platforme")

GetHello()


## job 5

def calcule(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operator == "%":
        result = num1 % num2
    else:
        result = "Unknown operator"
    print(result)

calcule(5, "+", 6)
calcule(8, "-", 7)
calcule(1, "*", 97)


## job 6 

def nombre(x):
    if x< 0:
        print ("negatif")
    elif x>0:
        print ("pozitif")
    
nombre(-58)
nombre(63)
nombre(632)
nombre(-214)

## job 7

def langage(x):

    if x == "JavaScript":
        print ("tu es en developper web")
    elif x == "Python":
        print ("tu es un developper IA")
    elif x == "java":
        print ("tu es un developper logiciel")
    elif x == "reactjs":
        print("tu es un developper mobile")
    else:
        print("un jour, je serai le meilleur developper ... ")

langage("java")
langage("Python")
langage("Data")
langage("reactjs")

## job 8

def my_function(type, saison):
    if type == "fruit" and saison == "hiver":
        print("orange, mandarine, et kiwi")
    elif type == "fruit" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine,navet")

my_function("fruit", "hiver")
my_function("legume", "ete")
my_function("fruit", "ete")
my_function("legume", "hiver")


## job 9

def moyenne(x, y, z):
    result = (x + y +z) / 3

    if 14<result<21:
        print("moyenne_etudiant:","Très bon élève")
    elif 10<result<15:
        print("moyenne_etudiant:","Bon élève")
    elif 7 <result < 11:
        print("moyenne_etudiant:", "Élève moyen")
    elif 0 <=result<8:
        print("moyenne etudiant:", "Élève devant faire des efforts")
    else:
        print("non classifie")

moyenne(12, 18 ,15)
moyenne(45, 15 ,15)
moyenne(8, 10 ,6)
moyenne(12, 18 ,11)
moyenne(7, 8 ,5)


## job 10

def nombre(x):
    if x % 2 == 0:
        print("pair")
    elif x % 2 != 0:
        print("impair")

nombre(-74)
nombre(15)
nombre(54)

## job 11

def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    print(f"{heures} heures et {minutes_restantes} minutes")


time_to_text(125)
time_to_text(90)
time_to_text(45)
time_to_text(0)



## job 12

def inverser_chaine(chaine):
    return chaine[::-1]

print(inverser_chaine("nikana"))
print(inverser_chaine("bonjour"))
print(inverser_chaine("Python"))






