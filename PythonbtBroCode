
---
#### Type
A container for a value

Function type is using to type what character we will use, example
```
name = "Bro"

print(type(name))

#print("Hello " + name)
```

R :<class 'str'> this is the type of name
#### int = integer (a whole number)
string is diferent of a int, strings is using for characters and int for whole number
```
#age = 21

#age +=2

#print("Yout age is: " + str(age))

#print(type(age))
```

#### float = floating poit number (a decimal number)


#### Boolean True Or False
```
#Human = "Bro"  
#age = 21
#attractive = True
#Human, age, attractive = "Bro", 22, True
#print(Human)
#print(age)
#print(attractive)
```

#### len lenght of the string
```
name = "Bro Code"
#print(len(name))
#print(name.find("C"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower()+ " " +name.upper())
#print(name.isdigit())
#print(name.isalpha()) # -> True without space, False with space (Alphabetical lethers)
#print(name.count("o")) # -> How many caracters are to our string
#print(name.replace("o","a"))  # -> Replace caracters
#print(name*2)
```

```
texto = "12345"
resultado = texto.isdigit()
print(resultado)  # Esto imprimirá True, ya que todos los caracteres son dígitos numéricos.

texto = "abc123"
resultado = texto.isdigit()
print(resultado)  # Esto imprimirá False, ya que hay caracteres no numéricos en la cadena.

```

----

#### len lenght of the string
```
name = "Bro Code"
#print(len(name))
#print(name.find("C"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower()+ " " +name.upper())
#print(name.isdigit())
#print(name.isalpha()) # -> True without space, False with space (Alphabetical lethers)
#print(name.count("o")) # -> How many caracters are to our string
#print(name.replace("o","a"))  # -> Replace caracters
#print(name*2)
```

```
texto = "12345"
resultado = texto.isdigit()
print(resultado)  # Esto imprimirá True, ya que todos los caracteres son dígitos numéricos.

texto = "abc123"
resultado = texto.isdigit()
print(resultado)  # Esto imprimirá False, ya que hay caracteres no numéricos en la cadena.

```

---
#### Type casting
Convert the data type of a value to another data type

```
x = 1 #int
y = 22.3 #float
z = "5" #str

#x = str(x)
#y = str(y)
#z = str(z)

print("X is "+str(x))
print("Y is "+str(y))
print(3*z+ " " +str(y))
```

---
#### User Input 

```
name = input("Whats your name?: ")

age = int(input("How old are you?: "))
height  = float(input("How tall are you: "))
country = input("From what contry are you?: ")

print("Hello "+name)
print("You are "+str(age)+"years old")
print("You are "+str(height)+"cm tall")
print("You are from "+str(country)+"You speak "+str(country))
```

---
#### Math Fuctions
```
import math

pi = 3.14
x = 1
y = 2
z = 3


#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi)) # -> absolute
#print(pow(pi,2)) # -> to the power of 2
#print(math.sqrt(5)) # -> radacina patrata
#print(max(x,y,z))
#print(min(x,y,z))
```

---
#### Strings Slicing
Create a substring by extracting elements from another string

```
#   indexing[] or slice()
#   [start:stop:step]
#name = "Bro Code"
#first_name = name[0:3]
#last_name = name[4:7]
#dx_name = name[1:0:2]
#reverse_name = name=[0:0:0]
  
#print(reverse_name)

website = "http://google.com"
website2 = "http://wikipedia.com"

slice= slice(7, -4)

print(website[slice])
print(website2[slice])
```

```
1. `slice = slice(7, -4)`:
    
    - Aquí, estás creando un objeto `slice` con dos argumentos, 7 y -4. El primer argumento (7) representa el índice de inicio, y el segundo argumento (-4) representa el índice de parada. Esto significa que se va a crear un slice que incluye caracteres desde el índice 7 hasta el índice -4 (en sentido inverso).
2. `website = "http://google.com"` y `website2 = "http://wikipedia.com"`:
    
    - Estás definiendo dos cadenas de caracteres, `website` y `website2`, que contienen URLs.
3. `print(website[slice])` y `print(website2[slice])`:
    
    - Estás aplicando el objeto `slice` previamente definido a las cadenas `website` y `website2`. Esto significa que estás extrayendo una porción de cada cadena según el slice definido. El resultado impreso será la parte de la cadena que va desde el índice 7 hasta el índice -4 (sin incluir el índice -4) en ambas cadenas.
```

---
#### if statements
is a block of code that will  execute only if it's a true condition

```
age = int(input("How old are you: "))

if age == 100:
    print("You are a century old!")
elif age >= 13:
    print("You are an adult!")
elif age < 0:
    print("You haven't born")
else:
    print("You are a child")
```

---
#### Logical Operations
Use to check if one or more if statements is  true with (and,or, not)

```
#temp = int(input("Whats is the temperature outside?")) 

#if  not (temp >= 0 and temp <= 30):
    #print("The temp is bad today")
    #print("Stay Inside")

#elif not (temp < 0 or temp > 30):
    #print("The temperature is good Today" + " " + str(temp))
    #print("Go outside")

min = int(input("What time is it: "))

if (min >= 15 and min <= 20):
    print("You are in time")
    print("Stay down")

elif ( min <= 15 ):
    print("You are have time!")

elif ( min < 0 or min > 20 ):
    print("You are late!")
    print("Go up")
```

---
#### while loop
A statement that will execute it's blok of code, as loog as it's condition remains true

```
#while 1==1:
    #print("Help, i'm stuck in a loop!")

name = ""  
while len(name) == 0:
    name = input("Enter your name: ")
    print("Hello "+name)
```
---
#### For Loop
a statement that will execute it's block of code a limited amount of times
while loop = unlimited, for loop = limited

```
import time
import math

total = 0

for seconds in range(10,0,-1):
    print(seconds)
    print("The sum for the  number is:", total)
    total +=seconds
    time.sleep(1)

print("Happy")
print("The sum for the total numbers is:", total)
```
---
#### nested loops
The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"
```
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
```
out:
```
$$$$$$
$$$$$$
$$$$$$
$$$$$$
$$$$$$
```

```
import time
from pwn import *

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: " + str(rows) + "<-Your Rows/"))
symbol = input("Enter a symbol to use: ")

p1 = log.progress("TIPYING")
p1.status("Stargting Typing")
  
time.sleep(1)
for a in range(rows):
    for b in range(columns):
        print(symbol, end= " ")
        time.sleep(0.1)
    print()
    p1.status(print())
```

---
#### Loop Control Statements 
change a loops execution it's normal sequence
break = user to terminate the loop entirely 
continue = skips to the next integration of the loop
pass = does nothing, acts as a placeholder

```
1. `for i in phone_number:`: Este bucle `for` itera a través de cada carácter en la cadena `phone_number`. En este caso, `i` representa el carácter actual en cada iteración del bucle.
    
2. `if i == "-":`: Esta línea verifica si el carácter actual `i` es igual a un guion "-". La expresión `i == "-"` es una condición que se evalúa como Verdadera (True) cuando el carácter actual es un guion.
    
3. `continue`: Si se cumple la condición (es decir, si `i` es un guion), se ejecuta la instrucción `continue`, que salta al siguiente ciclo de iteración del bucle `for`, sin ejecutar las instrucciones siguientes en el bucle. En otras palabras, ignora el guion y pasa al siguiente carácter.
    
4. `print(i, end="")`: Si la condición no se cumple (cuando `i` no es un guion), se imprime el carácter `i` en la consola. La expresión `end=""` se utiliza para evitar que `print` agregue un salto de línea al final de cada impresión, lo que significa que los caracteres se imprimirán en la misma línea sin espacios ni saltos de línea entre ellos.
```

```
#break
#while True:

#    name = input("Enter you name: ")
#    if name != "":
#        break

#phone_number = "123-456-789"
#for i in phone_number:
 #   if i == "-":
  #      continue
   # print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i, end=" ")
```
---
#### list
Used to store multiples item in a single variable

```
food = ["pizza","hamburger","hotdog","spaghetti"]
 
#food[2] = "bread"
#print(food[2])  

#food.append("ice cream")
#food.remove("hotdog")
#food.pop() #remove last
#food.insert(5,"cake")
#food.sort() # sort the list
#food.clear()

for x in food:
    print(x,end="/")
```
---
#### 2D lists

a list o lists
```
  

drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice cream"]

food = [drinks, dinner, dessert]

print(food[2][1])
```
---
#### tuples
collection which is ordered and unchangeable used to group together related data

```
student = ("Bro","Bro",21,"male")

print(student.count("Bro")) # 2
print(student.index("male"))
  
for x in student:
    print(x)

if 21 in student:
    yos = int(student[2])
    print("Bro is here!")
    yos += 1
    print("The next year the student will have: " + str(yos))
```
---
#### set
collection which is unordered, unindexed. No duplicate value (No se duplica en la lista)

```
utensils = {"fork","spoon","knife","knife","3"}
dishes = {"1","2","3","4"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dishes.update(utensils)
dinner_table = utensils.union(dishes) 

#for x in dinner_table:
#    print(x)  

#for x in dishes:
#    print(x, end = " ")
 

#print(utensils.difference(dishes))
print(dishes.difference(utensils))
#print(utensils.intersection(dishes))
```

```
1. El conjunto `dishes` contiene los elementos `{'1', '2', '3', '4'}`.
2. El conjunto `utensils` contiene los elementos `{'fork', 'knife', '3', 'spoon'}`.
3. Cuando utilizas `dishes.difference(utensils)`, estás buscando los elementos que están en `dishes` pero no en `utensils`.
4. Los elementos en `dishes` que no están en `utensils` son `{'1', '2', '4'}`. El elemento `'3'` está en ambos conjuntos, por lo que no se incluye en el resultado.
```
---
#### dictionary
A changeable, unordered collection of unique key: valuea pairs. Fast because they use hashing, allow us to access a value quickly
```
capitals = {'USA':'Washinton DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}  

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
capitals.clear()

#print(capitals['Germany'])
print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items()) 

for key,value in capitals.items():
    print(key,value)
```
---
#### index operator []
gives access to a sequence's element (str,list,tuples)
```
name = "bro code!" 

#if(name[0].islower()):
    #name = name.capitalize()
 

first_name = name[0:3].upper()
second_name = name[4:8].lower()
last_character = name[-2].upper()
 

print(first_name)
print(second_name)
print(last_character)
```
---
#### Functions
A block of code which is executed only when it is called.
```
def hello(first_name, last_name, age):
    print("hello! "+ first_name + " " + last_name+ " " + str(age))
    print("Have a nice day!")
    print(str(age))

age = 21 # def age 

hello("Bro","Code",age) # se pueden definir aqui tambien las variantes

age += 1 #Incrementa en 1
print(str(age))
```
---
#### Return Statement
Function send Python values/objects back to the caller.
There Values/objects are known as the function's return value
```
def multiply(number1,number2):
 result = number1 *number2
 return result

x = multiply(6,8)
#print(multiply(6,8))
print(x)
```
---
#### keword arguments 
Arguments preceded by an identifier when we pass the to a function. The order of the arguments doesn't matter, unlike positional a arguments, Python knows the name of the arguments that our function receives.

```
def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(last="Bro",middle="Dude",first="Code")
```
---
#### Nested funciton calls
function inside other function calls, innermost function calls are resolved first, returned value is use as argument for the next outer funciton.

```
num = input("Enter a whole positive number: ") #Curently is a string
#num = float(num)
#num = abs(num)
#num = round(num)

#print(num)
print(round(abs(float(input("Enter a whole positive number: "))))) #Curently is a string
```
---
#### Scope
The region that a variable is recognized. A variable is only available from inside the region it is created. A global and locally scoped versions of a variable can be created.

```
#LEGB

name = "BRO" # Global scope (avaiable inside & ouside funcitons)  

def display_name():
    name = "Code" # Local scope (avaiable only inside this function)
    print(name)

display_name()

print(name)
```
---
#### Args
parameter that will pack all  arguments into a tuple. useful so that a function can accept a varying amount of arguments
```
#def add(*args):
def add(*stuff):    
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0 #este es el primer argumento 0 = 2 entonces, 2 + 1 + 2 + 3

    for i in stuff:
        sum += i
        #sum -= i
        #sum +- i
    return sum

print(add(1,2,3))
```
or
```
*#def add(*args):
def add(*stuff):    
    sum = 0
    stuff = list(stuff)
    stuff[0] = 4 # el primer argumenteo 0 = 2
    stuff[1] = 1
    
    for i in stuff:
        sum += i
        #sum -= i
        #sum +- i
    return sum

print(add(1,2,4))
```
---
#### kawrgs
Parameter that will pack al arguments into a dictionary useful so that a function can accept a varying amount of keyword arguments.

```
#def hello(first, last):
#    print("hello" + firts + " " + last)

#hello(first="Bro",middle="Who",last="Code")

def hello(**kwargs): # any word can be replaced by kwargs
    #print("hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end= " ")
    for key,value in kwargs.items():
        print(value,end= " ")

  
hello(title="Mr.",first="Bro",middle="Who",last="Code")
```
```
El bucle `for key, value in kwargs.items():` itera a través de este diccionario y en cada iteración, `key` toma el nombre del argumento de palabra clave y `value` toma el valor asociado a ese argumento. En tu ejemplo, la función imprimirá:
```
```
Donde:

- `key` en la primera iteración será "title" y `value` será "Mr."
- En la segunda iteración, `key` será "first" y `value` será "Bro"
- En la tercera iteración, `key` será "middle" y `value` será "Who"
- En la cuarta iteración, `key` será "last" y `value` será "Code"
```
---
#### str.format
optional method that gives users more control when displaying output 
```
#animal = "Cow"
#item = "Moon"
  
#print("The "+animal+" Jumped over the " +item)
#print("The {} jumped over the {}".format("cow","moon"))
#print("The {1} jumped over the {1}".format(animal,item)) #positional argument
#print("The {item} jumped over the {animal}".format(animal="Cow",item="Moon")) # keyboard argument 

#text = "the {} jumped over the {}"
#print(text.format(animal,item))  

#name = "Bro"
#item = "Vasile"
#print("Hello, my name is {}",format(name))
#print("Hello, my name is {:10}. Nice to meet you {}".format(name,item))
#print("Hello, my name is {:>10}. Nice to meet you {}".format(name,item))
#print("Hello, my name is {:^10}. Nice to meet you {}".format(name,item))

#number = 3.14159
#print("The number pi is {:.2f} ".format(number))
#print("The number pi is {:.3f} ".format(number))


number = 1000
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:x}".format(number))
print("The number is {:X}".format(number))
print("The number is {:e}".format(number))
print("The number is {:E}".format(number))
```
---
#### random numbers
```
import random

x = random.randint(1,6)
y = random.random()

myList = ['rock','paper', 'scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
  
print(x)
print(y)
print(z)
print(cards)
```
---
#### Exception
events detected during execution that interrupt the flow of a program
```
try:
    numerator = int(input("Enter a number to divide "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator  

except ValueError as e:
   print("Enter only numbers Please")
   print(e)  

except ZeroDivisionError as e:
    print("You cand divide by 0 :()")
    print(e)
  

except Exception as x:
    print("Somnetihng went wrong")
    print(x)  

else:
    print(result)
finally:
    print("This will always execute")
```
---
#### file detection
```
import os

path = "C:\\Users\\Adrian\\Desktop\\folder" 

if os.path.exists(path):
    print("That location exists!!")
    if os.path.isfile(path):
        print("That is afile")
    elif os.path.isdir(path):
        print("That is a direcory")

else:
    print("That location doesn't exist")
```
---
#### read file 
```
try:
    with open('G:\\Practice\\test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")

#print(file.close)
```
---
#### write a file
```
#test = "\nBy adrian\n1997"

# There are too, r , w, a and x to traverse the file, just inspect.  

#with open('test.txt','w') as file:
#    file.write(test)
# Add a new line

test = "\nBy adrian\n1998 new line"

with open('test.txt','a') as file:
    file.write(test)
```
---
#### Copy a file
```
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination ca be a direcotry
# copy2() = copy + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('test.txt','copy.txt') #source, destination #or path #i was make a copy and after that i was pass the copy with another name
```
---
#### move a file
In the same partition
```
import os

source = "test.txt"
destination = "G:\\Practice\\1\\test.txt" 

try:
    if os.path.exists(destination):
        print("There is alreadey a file there")
    else:
        os.replace(source,destination)
        print(source+ " was moved")
except FileNotFoundError:
    print(source+" wa not found")
```


The os.replace(source, destination) method in Windows can only move files within the same drive. If you are trying to move files between different drives, you must copy the file and then delete it from the source.
```
import os
import shutil  

source = "test.txt"
destination = "C:\\Users\\Adrian\\Desktop\\1\\test.txt"

try:
    if os.path.exists(destination):
        print("There is alreadey a file there")
    else:
        shutil.copy2(source, destination)  # Copia el archivo
        os.remove(source)  # Elimina el archivo de origen
        print(source+ " was moved")
except FileNotFoundError:
    print(source+" wa not found")
except Exception as e:
    print("An error occurred:", e)
```

```
The except Exception as e: block catches any exception of type Exception or subclasses of Exception. In Python, Exception is the base class for all exceptions, so catching Exception is a general way to handle any type of error that may occur.

The as e allows you to assign the instance of the exception to a variable named e, which can then be used to access information about the error, such as the error message, the cause of the error, the type of error, etc. By printing "An error occurred:", e, you are displaying a generic error message along with the specific error information that was caught.

This is useful because it allows you to catch unexpected errors and provide useful information about the error, making it easier to debug and understand why the error occurred. Without this part of the code, unexpected errors could go undetected and be more difficult to fix.
```
---
#### Delete a file
```
import os
import shutil

path = 'G:\\Practice\\empty_folder'

try:
    #os.remove(path) #delete files
    #os.rmdir(path) #delete direcotries
    shutil.rmtree(path) #delete directories with something inside !!DANGEROUS!!

except FileNotFoundError:
    print("That file does not found")
except PermissionError:
    print("You dont have permission to delete GAY!")
except OSError:
    print("Check the folder please, there are something inside")
else:
    print(path+" was deleted")
```
---
#### Modules
A file containing python code. May contain functions, classes, etc. Used with modular programming, which is to separate a program into parts. [AlltheModulesOfPython](https://docs.python.org/3/py-modindex.html)
###### imports
----
###### But in this part we has created  one module named, messages and after that we has imported the module:
messages:
```
def hello():
    print("[+]Have a nice day")

def bye():
    print("[-]Bye Have a wonderful time!")
```
---
##### Our Script
In this script we has named the module messages, that was created by as:
```
import messages
  
messages.hello()
messages.bye()

import messages as msg
msg.hello()
msg.bye()

from messages import hello,bye
hello()
bye()
 

from messages import *
hello()
bye()

help("modules")
```
---
#### Rock, paper, scissors game!
```
import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices) #the choises of the computer
    player = None 
    
    while player not in choices:
        player = input("rock paper or scissors?: ").lower() #key insesitive
  
    if player == computer:
            print("Computer: ", computer)
            print("player: ", player)
            print("TIE!")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("player: ", player)
            print("YOU LOSE")
        if computer == "scissors":
            print("Computer: ", computer)
            print("player: ", player)
            print("YOU WIN")
    elif player == "scissors":
        if computer == "rock":
            print("Computer: ", computer)
            print("player: ", player)
            print("YOU LOSE")
        if computer == "paper":
            print("Computer: ", computer)
            print("player: ", player)
            print("YOU WIN")
    elif player == "paper":
        if computer == "rock":
            print("Computer: ", computer)
            print("player: ", player)
            print("YOU LOSE")
        if computer == "scissors":
            print("Computer: ", computer)
            print("player: ", player)
            print("You lose!")
    play_again = input("Play again?(Y/n): ").lower()
    #if play_again in ["y", "yes", "claro", "si", "campeon"]: #Tryed
    if play_again != "yes":   #!= not equal yes
            break
print("Bye!")
```
[TrySpokeEdition](https://realpython.com/python-rock-paper-scissors/) 

---
#### Quiz Game
```
1. `for i in options[question_num-1]:`: Inicia otro bucle que itera a través de las opciones disponibles para la pregunta actual. La variable `question_num` se utiliza para acceder a la lista de opciones correspondiente a la pregunta actual.
```
The ex:
```
#------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print(f"\n-------------")
        print(key)
        for i in options[question_num-1]: #Separe and filter only the
            print(i)
            
        guess = input("Enter (A, B, C or D):  ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses, guesses)

#------------------------

def check_answer(answer, guess): # retorna un 1 o un 0 si es correcto o no!
    if answer == guess:
       print("CoRRECt")
       return 1
    else:
       print("WrONg!")
       return 0
#------------------------

def display_score(correct_guesses, guesses):
    print("-----------")
    print("RESULTS")
    print("Answers: ", end=" ")
    for i in questions:
            print(questions.get(i), end=" ")
    print()    
    print("-----------")
    print("RESULTS")
    print("Guesses: ", end=" ")
    for i in guesses:
            print(i, end=" ")
print()   

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

#------------------------

def play_again(): 
    reponse = input("Do you want to play again?: (Y/n): ")
    reponse= reponse.upper()

    if reponse == "Y":
         return True
    else:
         return False
#------------------------   
questions = {
    "Who created Python?:": "A",
    "What year was python created?": "B",
    "Python is tributed to which comedy group?": "C",
    "Is the Earth round?: ": "A"
}
 
options =  [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Your mother"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]


new_game()
	 while play_again():
     new_game()

print("Gobay")
```
---
#### Object Oriented Programming (OOP)
```
# Clase Car
class Car:
    # Constructor de la clase
    def __init__(self, make, model, year, color):
        self.make = make   # Atributo make
        self.model = model  # Atributo model
        self.year = year   # Atributo year
        self.color = color  # Atributo color

    # Método drive
    def drive(self):
        print("This " + self.model + " car is driving")  # Imprime un mensaje que incluye el modelo del coche

    # Método stop
    def stop(self):
        print("This car is stopped")  # Imprime un mensaje que indica que el coche se detuvo

# Importar la clase Car desde el archivo car.py
from car import Car

# Crear dos instancias de la clase Car
car_1 = Car("Chevy", "Corvette", 2021, "Blue")
car_2 = Car("Ford", "Mustang", 2022, "Red")

# Acceder a los atributos de car_1 y car_2 e imprimirlos
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

# Llamar al método drive() y stop() en car_1
car_1.drive()
car_1.stop()

# Acceder a los atributos de car_2 e imprimirlos
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

# Llamar al método drive() y stop() en car_2
car_2.drive()
car_2.stop()

```
----
#### Class Variables
```
# Clase Car
class Car:
    # Variable de clase
    wheels = 4  # Todos los objetos de la clase Car comparten esta variable

    # Constructor de la clase
    def __init__(self, make, model, year, color):
        # Atributos de instancia (valores únicos para cada objeto)
        self.make = make    # Marca del automóvil
        self.model = model  # Modelo del automóvil
        self.year = year    # Año del automóvil
        self.color = color  # Color del automóvil

# Importar la clase Car desde el archivo car.py
from car import Car

# Crear dos instancias de la clase Car
car_1 = Car("Chevy", "Corvette", 2021, "Blue")
car_2 = Car("Ford", "Mustang", 2022, "Red")

# Cambiar el valor de la variable de clase 'wheels' para toda la clase Car
Car.wheels = 2

# Acceder a la variable 'wheels' a través de las instancias car_1 y car_2
print(car_1.wheels)  # Imprime 2, ya que se modificó la variable de clase para toda la clase Car
print(car_2.wheels)  # Imprime 2, también refleja el cambio

# Nota: car_1.wheels = 4 establecería una variable 'wheels' específica para car_1, no afectaría a car_2 ni al valor de la clase.

```
---
#### inhertiance
receive as an heir the death of the previous holder (como herencia)
```
I. Herencia en Python - Permite que una clase hija herede atributos y métodos de una clase padre. - Proporciona una forma de reutilizar y extender el código de una clase existente. II. Sobrescritura de Métodos - Cuando una clase hija hereda un método de la clase padre, puede: a. Utilizarlo tal como está. b. Proporcionar su propia implementación del método. c. Llamar al método de la clase padre utilizando `super()`.
```

```
class Animal:

    alive = True

	def eat(self):
       print("This animal is eating")  

    def sleep(self):
        print("This animal is sleeping")
  

# As if each had every attribute of the class Animal 

class Rabbit(Animal): #rabbit is the child class, the animal is the parent class
   def run(self):
       print("This rabbit is running")

class Fish(Animal): #fish is the child class, the animal is the parent class
    def swim(self):
        print("This fish is swmming")  

class Hawk(Animal): #hawk is the child class, the animal is the parent class
    def fly(self):
        print("This hawk is flying")
    def eat(self):
        print("WORK?")
        super().eat() # llamar a la funcion fuera de esta funcion (llamar a la funcion padre de fuera)
  

# Crear instancias de las clases Rabbit, Fish y Hawk
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()  

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()
 

#Ejecucion de los metodos de cada instancia
rabbit.run()
fish.swim()
hawk.fly()
hawk.eat()
```
Another example:
```
import math

class Animal:
    alive = True

    def eat(self):
       print("This animal is eating")
    def sleep(self):
       return 21
# As if each had every attribute of the class Animal


class Rabbit(Animal): #rabbit is the child class, the animal is the parent class
   def run(self):
       print("This rabbit is running")

class Fish(Animal): #fish is the child class, the animal is the parent class

    def swim(self)
        print("This fish is swmming")  

class Hawk(Animal): #hawk is the child class, the animal is the parent class
    def fly(self):
        print("This hawk is flying")
    def eat(self):
        print("WORK?")
        super().eat() # llamar a la funcion fuera de esta funcion (llamar a la funcion padre de fuera)
 

# Crear instancias de las clases Rabbit, Fish y Hawk
rabbit = Rabbit()
fish = Fish()
hawk = Hawk(
  

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()
 

a = 2 

class Math:
    def my_sum(self, hawk, a):
        zum = hawk.sleep() + a
        print(int(zum)) 

#Ejecucion de los metodos de cada instancia
rabbit.run()
fish.swim()
hawk.fly()
hawk.sleep()


math_obj = Math()

  
math_obj.my_sum(hawk, a)
```


---
#### Multilevel inheritance
```
class Organism:

    alive = True 

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")
        
dog = Dog()

print(dog.alive)
dog.eat()
dog.bark()
```
---
#### Multiple Inheritance
when a child class is derived from more than one parent class
```
class Prey:
    def flee(self):
        print("This animals flees")
        
class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pas

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
  
#rabbit.flee()
#hawk = Hawk()
#fish = Fish()

fish.flee()
fish.hunt()
```
---
#### Method overriding (Subclass)
```
class Animal:

    def eat(self):
       print("This animal is eating")

class Rabbit(Animal):  

    def eat(self):
        print("This rabbit is eating carrot!")
  
  

rabbit = Rabbit()
rabbit.eat() #This is asosiated specificly for rabbits
```
---
#### Method Chaining 
calling multiple methods sequentially each call perform an action on the same objects an returns self
```
class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You step on the brakes")
        return self  

    def turn_off(self):
        print("You turn off the engine")
        return self
  

car = Car()

#car.turn_on().drive()
#car.brake().turn_off()
car.turn_on()\
    .drive()\
    .brake()\
```
Mas ejemplos, comparten el mismo elemento:
```
class Car:
    def __init__(self, make, model):
        self.make = make  # 1. Creación de atributo 'make' en la instancia
        self.model = model  # 1. Creación de atributo 'model' en la instancia

    def start(self):
        print(f"Starting the {self.make} {self.model}.")  # 2. Acceso a 'make' y 'model'

class Computer:
    def __init__(self, brand):
        self.brand = brand  # 1. Creación de atributo 'brand' en la instancia

    def boot(self):
        print(f"Booting the {self.brand} computer")  # 2. Acceso a 'brand'
 

class CombinedObject:
    def __init__(self, car, computer):
        self.car = car  # 3. Combinación de objetos 'car' y 'computer'
        self.computer = computer  # 3. Combinación de objetos 'car' y 'computer'

    def operate(self):
        self.car.start()  # 4. Llamada al método 'start' en 'car'
        self.computer.boot()  # 4. Llamada al método 'boot' en 'computer'

car_obj = Car("Mandrila", "Camry")  # 5. Creación de instancia de 'Car'
Computer_obj = Computer("Dell")  # 5. Creación de instancia de 'Computer'

combined = CombinedObject(car_obj, Computer_obj)  # 6. Creación de instancia 'combined'
combined.operate()  # 6. Llamada al método 'operate' en 'combined'
```
---
#### Super function
Function user to give access to the methods of a parent class.
Returns a temporary object of a partent class when used.

```
class Rectangle:
    def __init__(self, length, width):
        self.length = length  # Inicializa el atributo 'length'
        self.width = width  # Inicializa el atributo 'width'

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)  # Llama al constructor de la clase base 'Rectangle'
    
    def area(self):
        return self.length * self.width  # Calcula el área del cuadrado

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)  # Llama al constructor de la clase base 'Rectangle'
        self.height = height  # Inicializa el atributo 'height'

    def volume(self):
        return self.length * self.width * self.height  # Calcula el volumen del cubo

square = Square(3, 3)  # Crea una instancia de 'Square'
cube = Cube(3, 3, 3)  # Crea una instancia de 'Cube'

print(square.area())  # Calcula y muestra el área del cuadrado
print(cube.volume())  # Calcula y muestra el volumen del cubo

```
---
#### Abstract classes
Prevents a user from creating an object of that class + compels a user to override abstract methods in a child class
abstract class = a class which contains one or more a that has declaration but does not have an implementation.
abstract method = a method that has declaration but does no have an implementation
```
from abc import ABC, abstractmethod # creating an abstract class abc = abstractmetod

class Vehicle(ABC):
   @abstractmethod # cualquier clase derivada de vehicle
   def go(self):
    pass
    
   @abstractmethod
   def stop(self):
      pass

class Car(Vehicle):

    def go(self):
        print("You drive a car")
  

    def stop(self):
	  print("This car is stopped")
	  
class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")
  

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()


#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
```
---
#### Objects as arguments

```
class Car:
    color = None

class Motorcycle:
    color = None
  

def change_color(vehicle, color):
    vehicle.color = color 

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle

change_color(car_1,"red")
change_color(car_2,"iron")
change_color(car_3,"yellow")
change_color(bike_1,"back")
  

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)
```
---
#### Duck typing
Concept where the class of an object is less important than the methods class type is not checked if minimum methods/attributes are present 
 ```
 class Duck:

    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is quaking")
  

class Chicken:

    #def walk(self):
    #    print("This chiken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person(): 

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
```
---
#### walrus operator
:= assignment expressions aka walrus operator
assigns values to variables as part of a larger expression
```
#happy = True
#print(happy)

#print(happy := True)  

#foods = list()
#while True:
#    food = input("What food do you like?: ")
#    if food == 'quit':
#        break
#    foods.append(food) 

foods = list()
while food := input("What food do you like?:") != "quit":
    foods.append(food)
```
---
#### Function to variables
```
#def hello():
#    print("hello")  

#hi = hello
#hi()
#hello()

#print(hello)
#print(hi)

say = print
say("Function?: ")
```
---
#### Higher order Functions
A function that either:
1. accepts a function as an argument or return a function (In python, functions are also treated as objects)

```
#def loud(text):
    #return text.upper()

#def quiet(text):
    #return text.lower()  

#def hello(func):
    #text = func("Heloo")
    #print(text)

#hello(quiet)
#hello(loud)

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(3))
```
---
#### lambda function
function written in 1 line using lambda keyword, accepts any number of arguments, but only has one expression.
(think of it as a shortcut) (useful if needed for a short period of time, throw-away)
```
#lambda parameters:expression 

#def double(x):
#    return x * 2
#print(double(5))

double = lambda x:x *2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name : first_name+" "+last_name
age_check = lambda age:True if age >= 18 else False
print(age_check(18))
```
---
#### Sort
sort() method = used with lists
sort() function = user with iterables
```
#students = ("Vasile","John","Ioan","Patrunjel","Bob")

#students.sort(reverse=True)

#sorted_students = sorted(students, reverse=True) #sorted_students is a list,  sorted(students) will return a lists

#for i in students:
#    print(i)

#students = [("Vasile","F", 50),
#            ("John", "M", 30),
#            ("Ioan", "F",16),
#            ("Patrunjel", "F", 30)]

students =(("Vasile","F", 50),
            ("John", "M", 30),
            ("Ioan", "F",16),
            ("Patrunjel", "F", 30))

age = lambda ages:ages[2]
#students.sort(key=age) # key = keyword agument
sorted_students = sorted(students,key=age)

for i in sorted_students:
    print(i)
```
#### map
applies a function to each item in a iterable (list, tuple, etc.)
map( function, iterable)
```
store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]


to_euros = lambda data: (data[0], data[1]*0.82)
to_dolars = lambda data: (data[0], data[1]/0.82)



store_euros = list(map(to_euros, store))
store_dolars = list(map(to_dolars, store))  

for i in store_euros:
    print(i)

for g in store_dolars:
    print("Dolars")
    print(g)
```
---
#### Filter
filter() = creates a collection of elements from an iterable for which a funciton returns 
filter(function, iterable)
```
friends =  [("Vasile","F", 50),
            ("John", "M", 21),
            ("Ioan", "F",16),
            ("Patrunjel", "F", 18)]

age = lambda data:data[2] >=18
drinking_dubbies = list(filter(age, friends))

for i in drinking_dubbies:
    print(i)
```
---
#### Reduce() 
Apply a function to an iterable and reduce it to a single cumulate value. Performs function on first two elements and repeats the process until 1 value remains

reduce(function, iterable)

```
import functools  # Importa el módulo functools para acceder a la función reduce.

letters = ["H", "E", "L", "L", "O"]  # Define una lista llamada 'letters' que contiene las letras "H", "E", "L", "L", "O".

# Utiliza functools.reduce para concatenar las letras en la lista 'letters' y almacenar el resultado en la variable 'word'.
word = functools.reduce(lambda x, y: x + y, letters)
print(word)  # Imprime la variable 'word' que contendrá la cadena resultante "HELLO".

factorial = [5, 4, 3, 2, 1]  # Define una lista llamada 'factorial' que contiene los números del 5 al 1 en orden descendente.

# Utiliza functools.reduce nuevamente, pero esta vez para calcular el factorial de un número.
# La función lambda toma dos argumentos 'x' e 'y' y multiplica 'x' por 'y'.
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)  # Imprime la variable 'result' que contendrá el resultado del factorial, en este caso, 120.

```

---
#### list comprehensions
a way to create a new list with less syntax. Can mimic certain lambda functions, easier to read
list = expression for item in iterable
list = expression for item in iterable if conditional
list = expression if/else for item in iterable if conditional
```
squares = []   # create an empty list
for i in range(1,11): # create a loop
    squares.append(i * i) # define what each loop iteration should do
print(squares) 

squares = [i * i for i in range(1,11)]
print(squares) 

students = [100,20,80,70,60,50,40,30,0]
#passwd_students = list(filter(lambda x: x >= 60, students))

#passwd_studens = [i for i in students if i >=60]

passwd_studens = [i if i >= 60 else "Failed" for i in students]
print(passwd_studens)
```

---
#### dictionary comprehensions
dictionary = {key: expression for (key,value) in iterable}
```
#cities_in_C = {'Cluj': 11, 'Turda': 300, 'Medias': 4, 'Lodroman': 16}
#cities_in_F = {key: ((value+32)/(9/5)) for (key,value) in cities_in_C.items()}
#print(cities_in_F)

#weather = {'Valea Lunga':"Ninge", 'Blaj':"Ploua", 'Boston':"Soare", 'Turda': "Gropi"}
#Soare_weather = {key: value for (key,value) in weather.items() if value == "Soare"}
#print(Soare_weather)

#cities_in_C = {'Cluj': 11, 'Turda': 300, 'Medias': 4, 'Lodroman': 16}
#desc_cities = {key: ("Warm" if value >= 15 else "CoLd") for (key,value) in cities_in_C.items()}
#print(desc_cities)


def check_temp(value):
    if value >=14:
        return "Hot"
    elif 16>= value >=20:
        return "Warm"
    else:
        return "Cold" 

cities_in_C = {'Cluj': 11, 'Turda': 300, 'Medias': 4, 'Lodroman': 16}
desc_cities = {key: check_temp(value) for (key,value) in cities_in_C.items()}
print(desc_cities)
```

---
#### zip function
agregate elements from two or more iterables (list, tuples, sets, etc.)
creates a zip object paired elements stored in tuples for each elements
```
usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@sswords", "abc123", "guest")

users = dict(zip(usernames, passwords))  

print(type(users))
for i in users:
    print(i)

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@sswords", "abc123", "guest")
users = dict(zip(usernames, passwords))

for key,value in users.items():
    print(key+" : "+value)
```
---
#### 
```
if __name__ == '__main__':
```
```
# Importa el módulo Hello2
import Hello2

# Imprime el valor de __name__ en el script actual
print(__name__)

# Imprime el valor de __name__ en el módulo Hello2
print(Hello2.__name__)

# Verifica si el script se está ejecutando directamente
if __name__ == '__main__':
    print("running this directly")
else:
    print("running other module indirectly")

# Define una función llamada main que imprime "Hello"
def main():
    print("Hello")

# Verifica nuevamente si el script se está ejecutando directamente
if __name__ == '__main__':
    # Llama a la función main si el script se está ejecutando directamente
    main()

```
1. `import Hello2`: Importa el módulo llamado `Hello2`.
    
2. `print(__name__)`: Imprime el valor de `__name__` en el script actual. Cuando se ejecuta directamente, esto imprimirá `'__main__'`. Si se importa como un módulo, imprimirá el nombre del módulo.
    
3. `print(Hello2.__name__)`: Imprime el valor de `__name__` en el módulo `Hello2`.
    
4. `if __name__ == '__main__':`: Verifica si el script se está ejecutando directamente. Si es así, ejecuta el bloque de código dentro del `if`. Si se importa como un módulo, ejecuta el bloque dentro del `else`.
    
5. `print("running this directly")`: Imprime si el script se está ejecutando directamente.
    
6. `else:`: Si el script se está ejecutando como un módulo, este bloque se ejecutará.
    
7. `print("running other module indirectly")`: Imprime si el script se está ejecutando como un módulo.
    
8. `def main(): print("Hello")`: Define una función llamada `main` que imprime "Hello".
    
9. `if __name__ == '__main__':`: Verifica nuevamente si el script se está ejecutando directamente.
    
10. `main()`: Llama a la función `main()` si el script se está ejecutando directamente. En este caso, imprimirá "Hello".
    

Este script sirve como un ejemplo de cómo estructurar código en Python para que ciertas partes se ejecuten solo cuando el script se inicia directamente y no cuando se importa como un módulo. Este enfoque es útil para modularizar y reutilizar código en diferentes contextos.

---
#### time module
epoch = a date and time from which a computer measures system time
[Strftime](https://www.freecodecamp.org/news/strftime-in-python/) [StrfTimePython](https://docs.python.org/3/library/datetime.html)
```
import time

#print(time.ctime(10000000))    # convert a time expressed in seconds since epoch to a readable string, epoch when your computer thinks time began (reference point)

#print(time.time()) # return current seconds since epoch

#print(time.ctime(time.time())) # current local time


#time_object =  time.localtime()
#time_object = time.gmtime()
#print(time_object)
#local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
#print(local_time)

#time_string = "20 April, 2020"
#time_object =  time.strptime(time_string,"%d %B, %Y")
#print(time_object)

# year, month, day, hours, minutes, secs, # day of the week, #day of the year, dst
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0)


# time.mktime() requiere una tupla en formato (year, month, day, hour, minute, second, day of week, day of year, daylight saving flag)

# Pero day of week y day of year son opcionales
time_seconds = time.mktime((time_tuple[0], time_tuple[1], time_tuple[2], time_tuple[3], time_tuple[4], time_tuple[5], -1, -1, -1))

# Convierte los segundos a un objeto time.struct_time
struct_time = time.localtime(time_seconds)

# Convierte el objeto time.struct_time a una cadena de tiempo legible
time_string = time.asctime(struct_time)

print(time_string)
```
---
#### thread
a flow of execution. Like a separate order of instructions.
1. However each and thread takes a turn running to achieve concurrency
2. GIL = (global interpreter lock)
3. allow only one thread to hold the control of the Python interpreter at any one time
4. cpu bound = program/task spends most of it's time waiting for internal events (CPU insentive use multiprocessing)
5. io bound = program/task spends most of it's time waiting for external events (user input, web scraping)  use multitreading

```
import threading
import time

# Definición de funciones para realizar tareas específicas
def eat_breakfast():
    time.sleep(3)
    print("You eat Breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You finish studying")

# Creación de objetos Thread para cada tarea
x = threading.Thread(target=eat_breakfast, args=())
y = threading.Thread(target=drink_coffee, args=())
z = threading.Thread(target=study, args=())

# Inicio de los hilos
x.start()
y.start()
z.start()

# Espera a que cada hilo termine antes de continuar con el siguiente
x.join()
y.join()
z.join()

# Impresión de información sobre los hilos y el tiempo de ejecución
print(threading.active_count())  # Número de hilos activos
print(threading.enumerate())     # Lista de hilos activos
print(time.perf_counter())        # Tiempo de ejecución desde el inicio del programa

```
1. **Definición de funciones:**
    
    - Se definen tres funciones (`eat_breakfast`, `drink_coffee`, `study`) que simulan diferentes tareas, cada una de las cuales toma un cierto tiempo para completarse (`time.sleep` simula la duración de la tarea).
2. **Creación de objetos Thread:**
    
    - Se crean tres objetos `Thread` (`x`, `y`, `z`) para representar cada tarea. Se especifica la función objetivo (`target`) y se proporcionan los argumentos necesarios (`args`).
3. **Inicio de los hilos:**
    
    - Se inician los hilos utilizando el método `start()`. Cada hilo ejecutará la función asociada en paralelo con otros hilos.
4. **Espera a que cada hilo termine:**
    
    - Se utiliza el método `join()` para esperar a que cada hilo termine su ejecución antes de pasar al siguiente. Esto garantiza que la impresión al final del programa no se mezcle con la salida de los hilos.
5. **Impresión de información sobre los hilos:**
    
    - `threading.active_count()`: Muestra el número de hilos activos en el momento actual.
    - `threading.enumerate()`: Devuelve una lista de todos los objetos Thread que están actualmente activos.
    - `time.perf_counter()`: Devuelve el tiempo de ejecución desde el inicio del programa en segundos.

---
#### daemon threads
a thread that runs in the background, not important for program to run you program will not wait for daemon threads to complete before exiting non-daemon threads cannot normally be killed, stay alive until task is complete

ex. background tasks, garbage collection, wait for input, long running process
```
import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged for: ",count,"seconds")

x = threading.Thread(target=timer, daemon=True) # con daemon, estamos haciendo que cuando el proceso de pare matemos al demonio de la ejecucion
x.start()  

#set.Daemon(True)
print(x.isDaemon()) # check if the thread is a daemon or not.

answer = input("Do you wish to exit?")
```
---
#### multiprocessing
Runing tasks in parallel on different cpu cores, bypasses GIL used for threading 
multiprocessing = better for cpu bound tasks (heavy cpu usage)
multithreading = better for io bound tasks (waiting around)
```
from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    # Imprime el número de núcleos de CPU disponibles
    print("Número de núcleos de CPU disponibles:", cpu_count())
    
    # Crea cuatro procesos, cada uno ejecutando la función counter con el argumento 5000000000
    a = Process(target=counter, args=(5000000000,))   
    b = Process(target=counter, args=(5000000000,))
    c = Process(target=counter, args=(5000000000,))   
    d = Process(target=counter, args=(5000000000,))

    # Comentado: Inicia los procesos concurrentes
    # a.start()
    # b.start()
    # c.start()
    # d.start()

    # Espera a que cada proceso termine antes de continuar
    a.join()
    b.join()
    c.join()
    d.join()

    # Imprime el tiempo total de ejecución
    print("Tiempo de ejecución total:", time.perf_counter(), "segundos")

if __name__ == '__main__':
    main()

```
```
Este código en Python utiliza el módulo `multiprocessing` para realizar cuatro procesos concurrentes que ejecutan una función llamada `counter`. La función `counter` simplemente incrementa una variable en un bucle hasta alcanzar un valor específico.

Aquí hay una descripción detallada del código:

1. Se importan las clases `Process` y `cpu_count` del módulo `multiprocessing` y la función `time` para medir el tiempo de ejecución.
    
2. La función `counter(num)` incrementa una variable `count` en un bucle while hasta que `count` alcanza el valor proporcionado como argumento `num`.
    
3. En la función `main()`:
    
    - Se imprime el número de núcleos de CPU disponibles utilizando `cpu_count()`.
        
    - Se crean cuatro objetos `Process` (a, b, c, y d), cada uno destinado a ejecutar la función `counter` con el argumento `5000000000`.
        
    - Se comentan las líneas `a.start()`, `b.start()`, `c.start()`, y `d.start()`. Estas líneas iniciarían los procesos concurrentes.
        
    - Se utilizan las funciones `a.join()`, `b.join()`, `c.join()`, y `d.join()` para esperar a que cada proceso termine antes de continuar.
        
    - Se imprime el tiempo total de ejecución utilizando `time.perf_counter()`.
        
4. La condición `if __name__ == '__main__':` asegura que el código dentro de `main()` se ejecute solo si el script se está ejecutando como un programa principal y no siendo importado como un módulo.
    

Es importante destacar que el código actualmente está comentado en las líneas que inician los procesos (`start()`). Si se descomentan esas líneas, los procesos se ejecutarán en paralelo, incrementando la variable `count` simultáneamente en cada proceso. Puedes observar cómo el tiempo de ejecución disminuiría debido a la ejecución concurrente en múltiples núcleos de CPU.
```
---
#### Gui Windows Grafical User Interface
widgets = GUI elements: buttons, textboxes, labels, images
windows = server as containter to hold or contain there widgets
```
from tkinter import *

window = Tk() #instantiate and instance of a window
window.geometry("420x420")
window.title("Bro Code first GUI Program")

#icon = PhotoImage(file='IMG_4725.jpg')
#window.iconphoto(True,icon)

window.config(background="#5cfcff")

window.mainloop() # place windows computer screen, listen for events
```
---
#### labels
label = an area widget that holds text and/or an image within a window
```
from tkinter import *

window = Tk()

photo = PhotoImage(file='IMG_4725.jpg')

label = Label(window,
              text="Hello World",
              font=('Arial',40,'bold'),
              fg='#00ff00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='buttom')

label.pack()
#label.place(x=0,y=0)

window.mainloop()
```
---
#### buttons
```
from tkinter import *

count = 0
def click():
    global count
    count+=1
    print("You clicked the button")
    print(count)


window = Tk()

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00ff00",
                bg="black",
                activeforeground="#00ff00",
                activebackground="black",
                state=ACTIVE,)
                #image='IMG_4725.jpg',
                #compound=TOP) # Activve or disable


button.pack()

window.mainloop()
```
---
#### entryBox
entry widget = text box that accepts a single line of user input
```
from tkinter import *

# Función que se ejecuta cuando se hace clic en el botón "submit"
def submit():
   # Obtiene el contenido del Entry (cuadro de entrada)
   username = entry.get()
   
   # Imprime un saludo con el nombre ingresado en la consola
   print("Hello " + username)
   
   # Deshabilita la entrada para que no se pueda modificar después de hacer clic en "submit"
   entry.config(state=DISABLED)

# Función que se ejecuta cuando se hace clic en el botón "delete"
def delete():
   # Borra todo el contenido del Entry
   entry.delete(0, END)

# Función que se ejecuta cuando se hace clic en el botón "backspace"
def backspace():
   # Borra el último carácter en el Entry
   entry.delete(len(entry.get()) - 1, END)

# Crear la ventana principal
window = Tk()

# Crear un Entry (cuadro de entrada) con algunas configuraciones
entry = Entry(window,
              font=("Arial", 50),
              fg="#00ff00",  # Color del texto (verde)
              bg="orange",   # Color de fondo (naranja)
              show="g")      # Muestra la letra "g" en lugar de los caracteres reales (puede ser útil para contraseñas)

# Empaqueta el Entry en la ventana
entry.pack(side=LEFT)

# Crear un botón "submit" que llama a la función submit cuando se hace clic
submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

# Crear un botón "delete" que llama a la función delete cuando se hace clic
delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side=RIGHT)

# Crear un botón "backspace" que llama a la función backspace cuando se hace clic
backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)

# Iniciar el bucle principal de la interfaz gráfica de usuario (GUI)
window.mainloop()

```
---
#### check box
```from tkinter import *

window = Tk()

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree :(")

x = IntVar()

python_photo = PhotoImage(file='Python-logo-notext.svg.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='green',
                           background='yellow',
                           activebackground='#00ff00',
                           activeforeground='black',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound='left')

  
check_button.pack()
window.mainloop()
```

```
from tkinter import *

window = Tk()

def display():
    if(x.get()):
        print("You agree!")
    else:
        print("You don't agree :(")

x = BooleanVar()

python_photo = PhotoImage(file='Python-logo-notext.svg.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue="YES",
                           offvalue="NO",
                           command=display,
                           font=('Arial',20),
                           fg='green',
                           background='yellow',
                           activebackground='#00ff00',
                           activeforeground='black',
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound='left')

check_button.pack()
window.mainloop()
```
---
#### Radio Buttons
a similar to checkbox, but you can only select one from a group.
```
from tkinter import *

food = ["Pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("You ordered Pizza")
    elif(x.get()==1):
        print("You ordered hamburger")
    elif(x.get()==2):
        print("You ordered hotdog")
    else:
        print("Huh??!")

window = Tk()

x = IntVar()

for index in  range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], # adds text to radio buttons
                              variable=x, # groups radiobuttons together if they share the same baraible
                              value=index, # assingns each readiobutton a different value
                              padx=25, #adds padding on x-axis
                              font=("Impact",20), # fount and size
                              command=order # set command of radiobutton to funciton
                              )
    radiobutton.pack(anchor=W)

window.mainloop() 
```
---
#### scale

```
from tkinter import *

def submit():
    print("The temperature is: "+str(scale.get())+ " degrees C")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL, #orie orientation of scale
              font = ('Arial',20),
              tickinterval= 10, #adds numeric indicator for value
              showvalue= 0,
              troughcolor= '#69EAFF',
              fg= '#FF1C00',
              bg='orange') #hide current value
scale.set(((scale['from']-scale['to'])/2)+scale['to'])

scale.pack()

button = Button(window,
                text='submit',
                command=submit)
button.pack()

window.mainloop()
```
Ex
```
from tkinter import *

def submit():
    print("The temperature is: "+str(scale.get())+ " degrees C")
    if(scale.get() < 50):
        print("Cold")
        scale.config(bg='orange') # Cambia el color de fondo a rojo para temperaturas frías
    elif(scale.get() > 50):
        print("Hot")
        scale.config(bg='blue')  # Cambia el color de fondo a azul para temperaturas calientes
    else:
        print("HUH?")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL, #orie orientation of scale
              font = ('Arial',20),
              tickinterval= 10, #adds numeric indicator for value
              showvalue= 0,
              troughcolor= '#69EAFF',
              fg= '#FF1C00',
              )#bg=str(scale.get)) #hide current value
              
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

button = Button(window,
                text='submit',
                command=submit,
                )      
button.pack()

window.mainloop()
```
---
#### list box
listbox = A list of selectable text items within it's own containter
```
from tkinter import *

  

def submit():

    food = []

  

    for index in listbox.curselection(): # Scroll through the indexes of the selected elements

        food.insert(index,listbox.get(index)) # add elements to the list foods

  

    print("You have ordered: ")

    #print(listbox.get(listbox.curselection())) # submmit one selection

    for index in food:

        print(index)

  
  

def add():

    listbox.insert(listbox.size(),entryBox.get()) # add elements to the lists foods

    listbox.config(height=listbox.size(listbox.size(),entryBox.get())) # ajust the number of the elements

  

def delet():

    for index in listbox.curselection(): # delete more seledction

        listbox.delete(index)   # delete more selection

    #listbox.delete(listbox.curselection()) # delete one selection

    listbox.config(height=listbox.size())  # Ajust the size after delet the items

  
  
  

window = Tk() # Configuration about the principal window

  

#Window Creation

listbox = Listbox(window,

                  bg='#ffae00',

                  font=('Consatntia',12),

                  width=12,

                  selectmode=MULTIPLE) # Do permitions to select multiple elements

  

listbox.pack() # list of products

  

listbox.insert(1,"pizza")

listbox.insert(2,"pasta")

listbox.insert(3,"shaorma")

listbox.insert(4,"potato")

listbox.insert(5,"salad")

listbox.insert(6,"tortellini")

listbox.insert(7,"water")

listbox.insert(8,"Coca-Cola?")

  

listbox.config(height=listbox.size())

  
  

#Entry Box

entryBox = Entry(window)

entryBox.pack()

  
  

submitButton = Button(window,text="submit",command=submit) # submitbutton

submitButton.pack()

  

addButton = Button(window,text="Add",command=add) # addbutton

addButton.pack()

  

deletButton = Button(window,text="Delete",command=delet) # delete button

deletButton.pack()

  

window.mainloop()
```
---
#### messagebox
```
from tkinter import *

from tkinter import messagebox # import mesaggebox librari

  

def click():

    #messagebox.showinfo(title='This is an info message box',message='You are a person')

    #while(True):

        #messagebox.showwarning(title='Warning',message='Virus')

    #messagebox.showerror(title='Something',message='Error')

    #if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):

    #    print('You did a Think!')

    #else:

    #    print("You canceled a thing!")

  

    #if messagebox.askretrycancel(title='ask ok cancel',message='Do you want retry the thing?'):

    #    print('You retried a Think!')

    #else:

    #    print("You canceled a thing!")

  

    #if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):

    #    print("I like cake too")

    #else:

    #    print("Why do you not like cake?")

  

    #answer =  messagebox.askquestion(title='ask question',message='Do you like pie?')

    #if(answer == 'yes'):

    #    print('I like pie too')

    #else:

    #    print('I don\'t like too')

  

    answer = messagebox.askyesnocancel(title='Yes no cances',message='Do you like too?',icon='question' or 'error')

    if(answer == True):

        print('I like too')

    elif(answer ==  False ):

        print('Then why are you watching')

    else:

        print("You have dodged the question")

  
  

window = Tk()

  

button = Button(window,command=click,text='click me')

button.pack()

  
  

window.mainloop()
```

---
#### colorchooser
```from tkinter import *

from tkinter import colorchooser #submodule

  

def click():

   color = colorchooser.askcolor()

   #print(color)

   #colorHex = color[1]

   #print(colorHex)

   #window.config(bg=colorHex) #change background color

   window.config(bg=color[1]) #change background color

  

window = Tk()

window.geometry("420x420")

button = Button(text='click me', command=click)

button.pack()

  

window.mainloop()
```
---
#### text area
text widget = functions like a text area, you can enter multiple lines of text
```
from tkinter import *

  

def submit():

    input = text.get("1.0",END)

    print(input)

  

window = Tk()

  

text = Text(window,

            bg="light yellow",

            font=("Ink Free",15),

            padx=20,

            pady=20,

            fg="purple")

text.pack()

button = Button(window,text="submmit",command=submit)

button.pack()

  

window.mainloop()
```
---
#### open a file (File dialog)

```
from tkinter import *

from tkinter import filedialog

  

def openFile():

    filepath = filedialog.askopenfilename(initialdir="G:\\Practice\\text.txt",

                                          title="Ooen file?",

                                          filetypes= (("text files","*.txt"),

                                          ("all files","*.*")))

  

    file = open(filepath,'r')

    print(file.read())

    file.close()

  
  

window = Tk()

  

button = Button(text="Open",command=openFile)

button.pack()

  

window.mainloop()
```

---
#### Save a file (File dialog)
```
from tkinter import *

from tkinter import filedialog

  

def saveFile():

    file = filedialog.asksaveasfile(initialdir='G:\\Practice\\1',

                                    defaultextension='.txt',

                                    filetypes=[

                                        ("Text file",".txt"),

                                        ("HTML file",".html"),

                                        ("All file",".*")

                                    ])

    if file is None: # The Error that i was need to correct but in a simply line

        return

    #filetext = str(text.get(1.0,END)) # Use the window

    filetext = input("Enter Some Text: ") # Use the Console

    file.write(filetext)

    file.close

    print("You has saved a file")

  
  
  

window = Tk()

button = Button(text='save',command=saveFile)

button.pack()

text = Text(window)

text.pack()

  
  

window.mainloop()
```
---
#### Menu Bar
```
from tkinter import *

  

def openFile():

    print("File has been opened")

  

def saveFile():

    print("File has been saved")

  

def cut():

    print("[!] You cuted some text~")

  

def copy():

    print("[-] You copied some text~")

  

def paste():

    print("[+] You pasted some text~")

  

window = Tk()

  

openImage = PhotoImage(file='Python-logo-notext.svg.png')

  

menubar = Menu(window)

window.config(menu=menubar)

  

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))

menubar.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')

fileMenu.add_command(label="Save",command=saveFile)

fileMenu.add_separator()

fileMenu.add_command(label="Exit",command=quit)

  

editMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))

menubar.add_cascade(label="Edit",menu=editMenu)

editMenu.add_command(label="Cut",command=cut)

editMenu.add_command(label="Copy",command=copy)

editMenu.add_command(label="Paste",command=paste)

  

window.mainloop()
```
---
#### frames (Button)
frame = a rectangular container to group and hold widgets
```
from tkinter import *

  

window = Tk()

  

frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)

#frame.pack(side=BOTTOM)

frame.place(x=0,y=0) # place of the frame in the window

  

Button(frame,text="W",font=("Consolar",12),width=3).pack(side=TOP)

Button(frame,text="A",font=("Consolar",12),width=3).pack(side=LEFT)

Button(frame,text="S",font=("Consolar",12),width=3).pack(side=LEFT)

Button(frame,text="D",font=("Consolar",12),width=3).pack(side=LEFT)

  
  

window.mainloop()
```
---
#### NewWindow
```
from tkinter import *

  

def create_window():

    new_window = Tk()     # TopLevel() = new window 'on top' of another window, linked to a 'bottom' window # it's a mother proccess if you close a window this will close it tpp

                                # Tk() = new independent window, logien screen ex.

  

    old_window.destroy()  # close out of old window

  

old_window = Tk()

  

Button(old_window,text="New Window",command=create_window).pack()

  

old_window.mainloop()
```
---
#### Windows Tabs
```
from tkinter import *

from tkinter import ttk

  

window = Tk()

  
  

notebook = ttk.Notebook(window) # widget that manages a collection of windows/displays

  

tab1 = Frame(notebook) # new frame for tab 1

tab2 = Frame(notebook) # new frame for tab 2

  

notebook.add(tab1,text="Tab 1")

notebook.add(tab2,text="Tab 2")

notebook.pack(expand=True,fill="both") #expand = expand to fill any space not otherwise used

                                       # fill = fill spae on x and axis # to stay in the center of the window

Label(tab1,text="Hello this is tab number 1",width=50,height=25).pack()
Label(tab2,text="Tab nr.2",width=50,height=25).pack()

window.mainloop()
```
---
#### Grid (Insert Data)
grid() = geometry manager that organizes widgets in a table-like structure in a parent.
Think like excel to configure the window
```
from tkinter import *

  

window = Tk()

  

titleLabel = Label(window,text="Enter Your info",font=("Console",12)).grid(row=0,column=0,columnspan=2)

  

firstNameLabel = Label(window,text="First name: ",width=15,bg="#37984e").grid(row=1,column=0) #think in excel to configure the window

firstNameEntry = Entry(window).grid(row=1,column=1) #think in excel to configure the window

  

lastNameLabel = Label(window,text="Last name: ",bg="#37987e").grid(row=2,column=0) #think in excel to configure the window

lastNameEntry = Entry(window).grid(row=2,column=1) #think in excel to configure the window

  

emailNameLabel = Label(window,text="Email: ",bg="#378298",width=30).grid(row=3,column=0) #think in excel to configure the window

emailNameEntry = Entry(window).grid(row=3,column=1) #think in excel to configure the window

  

submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2) #poner en medio

  
  

window.mainloop()
```
---
#### Progress Bar
```
from tkinter import *

from tkinter.ttk import *

import time

  

def start():

    tasks = 100

    x = 0 #Start a variable

    speed = 1 # represent the cantiti of the cases that will need to complete

    while(x<tasks):

        time.sleep(0.05)

        bar['value']+=(speed/tasks)*100 # Update the value of the progress

        x+=speed  # Increment the progress acording to the total progress

        percent.set(str(int((x/tasks)*100))+"%") # Increment the progress completed on the interface

        text.set(str(x)+"/"+str(tasks)+" tasks comleted") #Updates the text

        window.update_idletasks() # Update de GUI to reflect the  changes

  

window = Tk()

  

percent = StringVar() # To store and track you the progress the percent

text = StringVar() #To store and track you the progress the text

  

bar = Progressbar(window,orient=HORIZONTAL,length=300) # Crea un barra orizontal

bar.pack(pady=10)

  

percentLabel = Label(window,textvariable=percent).pack()

taskLabel = Label(window,textvariable=text).pack()

  
  

button = Button(window,text="Download",command=start).pack()

  

window.mainloop()
```
---
#### Canvas
widget that is used to draw graphs, plots, images and a window
```
from tkinter import *

  

window = Tk()

  

canvas = Canvas(window,height=500,width=500)

blueLine = canvas.create_line(0,0,500,500,fill="blue",width=2) # simple line

redLine = canvas.create_line(0,500,500,0,fill="red",width=2)

canvas.create_rectangle(50,50,250,250,fill="purple")

points = [250,0,500,500,0,500]

canvas.create_polygon(points,fill="yellow",outline="black",width=0.1)

canvas.create_arc(0,0,500,500,fill="green",style=ARC,start=180,extent=180)

canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)

canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)

canvas.create_oval(190,190,310,310,fill="white",width=10)

  

canvas.pack()

  
  

window.mainloop()
```
---
#### keyboard events
```
from tkinter import *

  

def doSomething(event):

    #print("You pressed: " + event.keysym)

    label.config(text=event.keysym)

  

window = Tk()

  

window.bind("<Key>",doSomething)

  

label = Label(window,font=("Helvetica",100))

label.pack()

  

window.mainloop()
```
---
#### mouse events
```
from tkinter import *

  

def doSomething(event):

    print("Mouse cordinates: " + str(event.x)+","+str(event.y))

  

window = Tk()

  

#window.bind("<Button-1>",doSomething) # left click

#window.bind("<Button-2>",doSomething) # wheel click

#window.bind("<Button-3>",doSomething) # right click

#window.bind("<Button-3>",doSomething)

#window.bind("<ButtonRelease>",doSomething)

#window.bind("<Enter>",doSomething)  # Where you enter on the window

#window.bind("<Leave>",doSomething) # where you leave the window

#window.bind("<Motion>",doSomething) # where the mouse move

  

window.mainloop()
```
---
#### Drag and drop
``` 
from tkinter import *

  

def drag_start(event):

    widget = event.widget

    widget.startX = event.x

    widget.startY = event.y

  

def drag_motion(event):

    widget = event.widget

    x = widget.winfo_x() - widget.startX + event.x

    y = widget.winfo_y() - widget.startY + event.y

    widget.place(x=x,y=y)

  
  

window = Tk()

  

label = Label(window,bg="red",width=10,height=5)

label.place(x=0,y=0)

  

label2 = Label(window,bg="blue",width=10,height=5)

label2.place(x=100,y=100)

  

label.bind("<Button-1>",drag_start)

label.bind("<B1-Motion>",drag_motion)

  

label2.bind("<Button-1>",drag_start)

label2.bind("<B1-Motion>",drag_motion)

  
  

window.mainloop()
```
---
#### Move Imagines
```
from tkinter import *

  

def move_up(event):

    label.place(x=label.winfo_x(),y=label.winfo_y()-10) # move the imagine with (w)

  

def move_down(event):

    label.place(x=label.winfo_x(),y=label.winfo_y()+10)

  

def move_left(event):

    label.place(x=label.winfo_x()-10,y=label.winfo_y())

  

def move_right(event):

    label.place(x=label.winfo_x()+10,y=label.winfo_y())

  

window= Tk()

window.geometry("500x500")

  

window.bind("<w>",move_up) # Pushing (W)

window.bind("<s>",move_down)

window.bind("<a>",move_left)

window.bind("<d>",move_right)

  

window.bind("<Up>",move_up) # Pushing (W)

window.bind("<Down>",move_down)

window.bind("<Left>",move_left)

window.bind("<Right>",move_right)

  

myimage = PhotoImage(file='Python-logo-notext.svg.png')

label = Label(window,image=myimage,bg="red")

label.place(x=0,y=0)

  
  

window.mainloop()
```
---
#### 2D animations in python
```
from tkinter import *

import time

from PIL import Image

  

WIDTH = 800

HEIGHT = 800

xVelocity = 1

yVelocity = 1

  

window = Tk()

  

canvas = Canvas(window,width=WIDTH,height=HEIGHT)

canvas.pack()

  

photo_image = PhotoImage(file='a8e11d39-ab9d-4136-90a6-60f0574969d6.png',height=100,width=100)

my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

  

image_width = photo_image.width()

image_height = photo_image.height()

  

while True:

    coordinates = canvas.coords(my_image)

    print(coordinates)

    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<=0):

        xVelocity = -xVelocity

    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<=0):

        yVelocity = -yVelocity    

    canvas.move(my_image,xVelocity,yVelocity)

    window.update()

    time.sleep(0.01)

  
  

window.mainloop()
```

#### multiple animations
class Ball
```
class Ball:

  

    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):

        self.canvas = canvas

        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)

        self.xVelocity = xVelocity

        self.yVelocity = yVelocity

  

    def move(self):

        cordinates = self.canvas.coords(self.image)

        print(cordinates)

        if(cordinates[2]>=(self.canvas.winfo_width()) or cordinates[0]<0):

            self.xVelocity = -self.xVelocity

        if(cordinates[3]>=(self.canvas.winfo_height()) or cordinates[1]<0):

            self.yVelocity = -self.yVelocity

  

        self.canvas.move(self.image,self.xVelocity,self.yVelocity)
```
Function
```
from tkinter import *

import time

from Ball import Ball

  

window = Tk()

  

WIDTH = 500

HEIGHT = 500

  

canvas = Canvas(window,width=WIDTH,height=HEIGHT)

canvas.pack()

  

volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "white")

tennis_ball = Ball(canvas, 0, 0, 50, 4, 2, "yellow")

  

while True:

    volley_ball.move()

    tennis_ball.move()

    window.update()

    time.sleep(0.01)

  

  

window.mainloop()
```
---
#### Clock Program
```
from tkinter import *

from time import *

  

def update():

    time_string = strftime("%I:%M:%S %p")

    time_label.config(text=time_string)

  

    day_string = strftime("%A")

    day_label.config(text=day_string)

    date_string = strftime("%B %d,%Y")

    date_label.config(text=date_string)

  
  

    window.after(1000,update)

  
  

window = Tk()

  

time_label = Label(window,font=("Adrial",50),fg="#00ff00",bg="black")

time_label.pack()

  

day_label = Label(window,font=("Ink Free",40),fg="#00ff00",bg="black")

day_label.pack()

  

date_label = Label(window,font=("Ink Free",40),fg="#00ff00",bg="black")

date_label.pack()

  

update()

  

window.mainloop()
```

---
#### Send an email
```

import smtplib

  

sender = "sender@gmail.com"

reciver = "reciver@gmail.com"

password = "password1234"

subject = "Python email test"

body = "I wrote an email"

  

#header

message = f"""From: Snoop Dogg{sender}

To: Nicolas Cage{reciver}

Subject: {subject}\n

{body}

"""     #Can spend multiple own of text

  

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

  
  
  

try:    

    server.login(sender,password)

    print("Logged in...")

    server.sendmail(sender, reciver, message)

    print("Email has been sent!")

  

except smtplib.SMTPServerDisconnected:

    print("unable to sing in")

# You need to turn on the less secure app acces of secure acount of google
```
---
#### run with command prompt

```
print("Hello !")


name = input("What's yout name?")


print("Hello " + name)
```
---
### pip to download packages and modules
```
help : pip
update : pip install --upgrade pip
installed packages: pip list
check outdated packages: pip list --outdated
update a package: pip install "package name" --upgrade
isntall a package pip install "package"
pypi.org
```

----
#### py to exe
```
to conver an image in ico file doy have icoconvert.com
```
```
pyinstaller -F -w -i icoFile
```
```
 -w do you do not need a terminal window 
 -i icon.ico
```
```
pyinstaller -F -w Hello.py
```
---
#### Basic Calculator program
```
from tkinter import *

  

def button_press(num): #Define una función llamada button_press que toma un argumento num. Esta función se activa cuando se presiona un botón en la calculadora.

    global equation_text #Declara que la variable equation_text es global, lo que permite acceder y modificar su valor tanto dentro como fuera de la función.

  

    equation_text = equation_text + str(num) #Actualiza la variable equation_text concatenando un string con el número ingresado y establece el valor de la etiqueta equation_label con el contenido actualizado de equation_text.

    equation_label.set(equation_text)

  

def equals(): #Dentro de la función equals, intenta evaluar la expresión en equation_text como una operación matemática. Si tiene éxito, muestra el resultado en la etiqueta equation_label. Si hay un error de sintaxis, imprime "Syntax error" y muestra "Syntax Error" en la etiqueta.

    global equation_text

  

    try:

        total = str(eval(equation_text))

  

        equation_label.set(total)

  

        equation_text = total

    except SyntaxError:

        print("Syntax error")

        equation_label.set("Syntax Error")

  

def clear(): # Dentro de la función clear, borra el contenido de equation_label y establece equation_text como una cadena vacía.

    global equation_text

  

    equation_label.set("")

  

    equation_text = ""

  

window = Tk()

window.title("Calculator")

window.geometry("600x600")

  

equation_text = "" # Inicializa las variables equation_text como una cadena vacía y equation_label como una variable de control para la etiqueta.

equation_label = StringVar()

  

label = Label(window, textvariable=equation_label, font=('consolas',20),bg="white",width=24,height=2)

label.pack()

  

frame = Frame(window)

frame.pack()

  

button1 = Button(frame, text=1, height=4, width=9, font=35

                 , command= lambda:button_press(1))

button1.grid(row=0,column=0)

  

button2 = Button(frame, text=2, height=4, width=9, font=35

                 , command= lambda:button_press(2))

button2.grid(row=0,column=1)

  

button3 = Button(frame, text=3, height=4, width=9, font=35

                 , command= lambda:button_press(3))

button3.grid(row=0,column=2)

  

button4 = Button(frame, text=4, height=4, width=9, font=35

                 , command= lambda:button_press(4))

button4.grid(row=1,column=0)

  

button5 = Button(frame, text=5, height=4, width=9, font=35

                 , command= lambda:button_press(5))

button5.grid(row=1,column=1)

  

button6 = Button(frame, text=6, height=4, width=9, font=35

                 , command= lambda:button_press(6))

button6.grid(row=1,column=2)

  

button7 = Button(frame, text=7, height=4, width=9, font=35

                 , command= lambda:button_press(7))

button7.grid(row=2,column=0)

  

button8 = Button(frame, text=8, height=4, width=9, font=35

                 , command= lambda:button_press(8))

button8.grid(row=2,column=1)

  

button9 = Button(frame, text=9, height=4, width=9, font=35

                 , command= lambda:button_press(9))

button9.grid(row=2,column=2)

  

button0 = Button(frame, text=0, height=4, width=9, font=35

                 , command= lambda:button_press(9))

button0.grid(row=3,column=0,columnspan=3)

  

plus = Button(frame, text="+", height=4, width=9, font=35

                 , command= lambda:button_press('+'))

plus.grid(row=3,column=0,columnspan=1)

  

minus = Button(frame, text="-", height=4, width=9, font=35

                 , command= lambda:button_press('-'))

minus.grid(row=3,column=2,columnspan=6)

  

multiply = Button(frame, text="*", height=4, width=9, font=35

                 , command= lambda:button_press('*'))

multiply.grid(row=4,column=2,columnspan=6)

  

divisor = Button(frame, text="/", height=4, width=9, font=35

                 , command= lambda:button_press('/'))

divisor.grid(row=4,column=1,columnspan=1)

  

equal = Button(frame, text="=", height=4, width=9, font=35

                 , command= equals)

equal.grid(row=5,column=0,columnspan=1)

  

decimal = Button(frame, text=",", height=4, width=9, font=35

                 , command= lambda:button_press(','))

decimal.grid(row=4,column=0,columnspan=1)

  

clear = Button(window, text="clear", height=4, width=12, font=35

                 , command= clear)

clear.pack()

  

window.mainloop()
```
---
#### Text Editor
```
import os

from tkinter import *

from tkinter import filedialog, colorchooser, font

from tkinter.messagebox import *

from tkinter import *

  

def change_color():

    color = colorchooser.askcolor(title="Pick a Color")

    text_area.config(fg=color[1])

  

def change_font(*args):

    text_area.config(font=(font_name.get(), size_box.get()))

  

def new_file():

    window.title("Untitled")

    text_area.delete(1.0, END)

  

def open_file():

  

    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=(("All Files", "*.*"), ("Text Documents", "*.txt")))

    try:

        window.title(os.path.basename(file))

        text_area.delete(1.0, END)

  

        file = open(file, "r")

  

        text_area.insert(1.0, file.read())

  

    except SyntaxError:

        print("Couldn't read file")

  

    finally:

        file.close()

  

def save_file():

    file = filedialog.asksaveasfilename(initialfile='untitled.txt',

                                        defaultextension=".txt",

                                        filetypes=[("All Files", "*.*"),

                                                   ("Text Documents", "*.txt")])

    if file is None:

        return

  

    else:

        try:

            window.title(os.path.basename(file))

            file = open(file, "w")

  

            file.write(text_area.get(1.0, END))

        except Exception:

            print("Couldn't sabe file")

  

        finally:

            file.close()

  

def cut():

    text_area.event_generate("<<Cut>>")

  
  

def copy():

    text_area.event_generate("<<Copy>>")

  
  

def paste():

    text_area.event_generate("<<Paste>>")

  

def about():

    showinfo("About this program", "This is a program written about Barman")

  

def quit():

    window.destroy()

  
  

window = Tk()

window.title("Notepad Program")

file = None

  

window_width = 500

window_height = 500

screen_width = window.winfo_screenwidth()

screen_height = window.winfo_screenheight()

  

x = int((screen_width / 2 - window_width / 2))

y = int((screen_height / 2 - window_height / 2))

  

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

  

font_name = StringVar(window)

font_name.set("Arial")

  

font_size = StringVar(window)

font_size.set("25")

  

text_area = Text(window, font=(font_name.get(), font_size.get()))

  

scroll_bar = Scrollbar(text_area) #scroll Barr

window.grid_rowconfigure(0, weight=1)

window.grid_columnconfigure(0, weight=1)

text_area.grid(sticky=N + E + S + W)

scroll_bar.pack(side=RIGHT, fill=Y)

text_area.config(yscrollcommand=scroll_bar.set)

  
  

frame = Frame(window)

frame.grid()

  

color_button = Button(frame, text="color", command=change_color)

color_button.grid(row=0, column= 0)

  

font_box = OptionMenu(frame, font_name, *font.families(),command=change_font)

font_box.grid(row=0, column=1)

  

size_box = Spinbox(frame, from_=1, to=25, textvariable=font_size, command=change_font)

size_box.grid(row=4, columns=2, columnspan=2)

  

menu_bar = Menu(window)

window.config(menu=menu_bar)

  

file_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)

file_menu.add_command(label="Open", command=open_file)

file_menu.add_command(label="Save", command=save_file)

file_menu.add_separator()

file_menu.add_command(label="Exit", command=quit)

  

edit_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut", command=cut)

edit_menu.add_command(label="Copy", command=copy)

edit_menu.add_command(label="Paste", command=paste)

  

help_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(label="About", command=about)

  

window.mainloop()
```
---
#### tick tack toe Game
```
from tkinter import *
import random

# Función para manejar el turno del jugador en el botón seleccionado
def next_turn(row, column):
    global player
    
    # Verifica si el botón está vacío y no hay un ganador aún
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            # Turno del primer jugador (jugador X)
            buttons[row][column]['text'] = player

            if check_winner() is False:
                # Cambia al turno del segundo jugador (jugador O)
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                # Si hay un ganador, muestra quién ganó
                label.config(text=players[0]+" Wins")

            elif check_winner() == "Tie":
                # Si hay empate, muestra un mensaje de empate
                label.config(text="Tie!")

        else:
            # Turno del segundo jugador (jugador O)
            buttons[row][column]['text'] = player

            if check_winner() is False:
                # Cambia al turno del primer jugador (jugador X)
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                # Si hay un ganador, muestra quién ganó
                label.config(text=players[1]+" Wins")

            elif check_winner() == "Tie":
                # Si hay empate, muestra un mensaje de empate
                label.config(text="Tie!")

# Función para verificar si hay un ganador
def check_winner():
    # Verifica si hay un ganador en filas
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            # Marca los botones que forman la fila ganadora en verde
            buttons[row][0].config(bg='green')
            buttons[row][1].config(bg='green')
            buttons[row][2].config(bg='green')
            return True
        
    # Verifica si hay un ganador en columnas
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            # Marca los botones que forman la columna ganadora en verde
            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green')
            return True
    
    # Verifica si hay un ganador en diagonales
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        # Marca los botones que forman la diagonal ganadora en verde
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        # Marca los botones que forman la diagonal ganadora en verde
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True
    
    elif empty_spaces() is False:
        # Si no hay más espacios disponibles, se declara empate
        return "Tie"
    
    else:
        return False

# Función para verificar si hay espacios vacíos en el tablero
def empty_spaces():
    spaces = 9

    # Cuenta los espacios vacíos en el tablero
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1
    if spaces == 0:
        return False
    else:
        return True

# Función para iniciar un nuevo juego
def new_game():
    global player
    
    # Inicia un nuevo juego con un jugador aleatorio
    player = random.choice(players)

    label.config(text=player + " Turn")

    # Reinicia todos los botones del juego
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#f0f0f0")


# Configuración de la interfaz gráfica usando tkinter
window = Tk()
window.title("X|O")
players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + "Turn", font=('Consolas', 40))
label.pack(side="top")

reset_button = Button(text="Restart Game", font=('Consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

# Creación de botones para el tablero usando un bucle
for row in range(3):
    for column in range(3):
        # Configuración de cada botón y su función al hacer clic
        buttons[row][column] = Button(frame,
                                      text="",
                                      font=('Consolas', 40),
                                      width=4,
                                      height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()

```
---
#### Snake Game
```
from tkinter import *
import random

# Definición de constantes para el juego
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 10
BODY_PARTS = 3
SNAKE_COLOR = 'blue'
FOOD_COLOR = 'red'
BACKGROUD_COLOR = 'black'

# Definición de la clase Snake
class Snake():
    
    def __init__(self):
        # Inicialización de la serpiente con un cuerpo de tamaño BODY_PARTS
        self.body = BODY_PARTS
        self.coordinates = []
        self.squares = []
        
        # Creación de las coordenadas iniciales de la serpiente
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Creación de los cuadrados que representan el cuerpo de la serpiente en la interfaz
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Definición de la clase Food
class Food():
    
    def __init__(self):
        # Inicialización de la comida en una posición aleatoria
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        # Creación del óvalo que representa la comida en la interfaz
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# Función para avanzar al siguiente turno del juego
def next_turn(snake, food):
    
    x, y = snake.coordinates[0]

    # Movimiento de la serpiente según la dirección actual
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Actualización de las coordenadas de la serpiente
    snake.coordinates.insert(0, (x, y))

    # Creación de un nuevo cuadrado en la interfaz para representar la nueva posición de la cabeza de la serpiente
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    # Agregar el nuevo cuadrado a la lista de cuadrados que representan el cuerpo de la serpiente
    snake.squares.insert(0, square)

    # Comprobación de si la serpiente ha alcanzado la comida
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        # Incrementar la puntuación y actualizar la etiqueta de puntuación
        score += 1
        label.config(text="Score:{}".format(score))
        # Eliminar la comida actual
        canvas.delete("food")
        # Crear una nueva instancia de Food para generar una nueva comida
        food = Food()
    else:
        # Si no se ha alcanzado la comida, eliminar la cola de la serpiente
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Comprobación de colisiones
    if check_colitions(snake):
        game_over()
    else:
        # Programar la siguiente llamada a la función next_turn después de un tiempo especificado por SPEED
        window.after(SPEED, next_turn, snake, food)

# Función para cambiar la dirección de la serpiente
def change_direction(new_direction):
    global direction
    # Cambiar la dirección si la nueva dirección no es opuesta a la dirección actual
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

# Función para verificar colisiones de la serpiente
def check_colitions(snake):
    x, y = snake.coordinates[0]

    # Comprobación de colisiones con los bordes de la pantalla
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    # Comprobación de colisiones con el cuerpo de la serpiente
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("Game Over")
            return True

    return False

# Función para manejar el final del juego
def game_over():
    # Eliminar todos los elementos en la interfaz y mostrar el texto "GAME OVER"
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('Consolas', 50), text="GAME OVER", fill='red', tag="game over")

# Creación de la ventana principal del juego
window = Tk()
window.title("SnakeGame")
window.resizable(False, False)  # No permitir cambiar el tamaño de la ventana

# Inicialización de variables y configuración de la interfaz
score = 0
direction = 'down'
label = Label(window, text="Score:{}".format(score), font=('Consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUD_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Configuración de la ventana
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Configuración de la entrada del teclado para cambiar la dirección de la serpiente
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Creación de instancias de Snake y Food
snake = Snake()
food = Food()

# Inicio del juego llamando a la función next_turn
next_turn(snake, food)

# Inicio del bucle principal de la interfaz gráfica
window.mainloop()


```
