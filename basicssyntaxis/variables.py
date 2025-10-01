a = 10
b = 3.5
name = "JAZMANY"
is_active=True
print(a,b,name,is_active)

print(type(a))
print(type(name))
print(type(is_active))

device = 'router'
id = 101
print(f'Device: {device} and ID: {id}')

#ARTIHMENTIC OPERATIONS
numbera=2
numberb=3

result = numbera + numberb
print(f'The Sum is: {result}')

print("The result of adding two numbers is: ", numbera + numberb)
print("The result of substracction is: ", numbera - numberb)
print("The Sum is: ", numbera * numberb)
print("The Sum of power to any number is: ", numbera ** numberb)
print("The Sum is: ", numbera / numberb)
print("The Sum is: ", numbera // numberb)

#STRINGS
print("#STRINGS")
name="jazmany sumi"
print(name.upper())
print(name.capitalize())
name2=name.upper()
print(name2.lower())

lenguage="PYTHON"
print(lenguage[0])
print(lenguage[-1])
print(len(lenguage))


#LISTS
print("#LISTS")
devices=['router','switch',"cable",45,True,False]
print(len(devices))

print(devices[0])
print(devices[-1])

devices.append("Server")
print(devices)

names=list()
names.append("Jazmany")
names.append("Maria")
names.append("Ana")
names.append("Julio")
print(names)
names[1]='Sebastian'
print(names)
print(names.pop())
print(names)

numbers=list(range(10))
print(numbers)
elementosseleccionados=numbers[2:4]
print(elementosseleccionados)

print(numbers[:-1])
print(numbers[:3])

numbers[1:3]=[100,100]
print(numbers)


#TUPLES
print("#TUPLES")

containertuple=(10,20,30)
print(containertuple[0])

containertuplelist = list(containertuple)
print(type(containertuple))


#DICTIONARIES
print("#DICTIONARIES")
animals={'dog':'nice','cat':'pretty','monkey':'black'}
print(animals['dog'])

animals['cat']='small'
print(animals)

print('cat' in animals)

del animals['monkey']
print(animals)
animals['monkey']='ugly'
animals['fish']='gold'
animals['bird']='colorful'

for item in animals:
    print(animals[item])

#New Dictionary
print("#New Dictionary")
mydictionary=dict()
mydictionary['humans']=2
mydictionary['cats']=4
mydictionary['spider']=8

for clave in mydictionary:
    data=mydictionary[clave]
    print('The %s has %d' % (clave, data))

#LOOPS

counter=0
while counter<10:
    print(counter)
    counter+=1

name=input('Enter your name: \n')
print(f'Hello {name}')

#Contenedor lista
mylista=list(range(1,101))
vacia=[]
for numero in mylista:
    if numero%2==0:
        vacia.append(numero)
print(vacia)

#Lista de numeros usando LOOPS de 1 a 100 elevado al mismo numero
numbers=[]
for numero in range(1,101):
    numbers.append(numero**numero)
print(numbers)

def greeting():
    return 
print('ok!!!')

#crear una lista con 10 elementos, guardar numeros que consideremos de cualquier cantidad del 1 al 20 ejemplo saltandose del 5 al 10 al 15 y asi, un codigo que me permita buscar el numero maximo que esta dentro de tal lista
#Crear una lista y guardar numeros, identificar el numero mayor
mylist=(range(1,90))
for number in mylist:
    if number%5!=0:
        print(number)

#Funcion greeting
print("***********************")
print("Function greeting")
def greeting(name):
    print(f'Hello {name}')
    return

greeting('Jazmany')

#Calculadora con 2 numeros
while True:
    numero1=int(input("Ingrese el primer numero: \n"))
    numero2=int(input("Ingrese el segundo numero: \n"))
    operationType=input("Ingrese la operacion a realizar (1. suma, 2. resta, 3. multiplicacion, 4. division): \n")
    if operationType=='1':
        print(f'El resultado de la suma es: {(numero1)+(numero2)}')
    elif operationType=='2':
        print(f'El resultado de la resta es: {(numero1)-(numero2)}')
    elif operationType=='3':
        print(f'El resultado de la multiplicacion es: {(numero1)*(numero2)}')
    elif operationType=='4':
        print(f'El resultado de la division es: {(numero1)/(numero2)}')
    else:
        print("Operacion no valida")