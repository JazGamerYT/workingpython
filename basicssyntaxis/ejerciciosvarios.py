# print("========================================================")
# number=int(input('Escriba un numero para saber si es par: \n'))
# if number % 2==0:
#         print(f'El numero {number} es par')
# else:
#     print(f'El numero {number} es impar')
#     print("========================================================")


#Validar usuario y contraseña
# while True:
#     print("========================================================")
#     usuariodefault='admin'
#     passworddefault='123'
#     usuario=input('Ingrese su usuario: \n')
#     password=input('Ingrese su contraseña: \n')
#     if usuario==usuariodefault and password==passworddefault:
#         print(f'Bienvenido {usuario}')
#     else:
#         print('Usuario o contraseña incorrecta, intente de nuevo')
#     print("========================================================")


# repository=list()
# ramdonNumber=int(input('Ingrese un numero por favor: \n'))
# suma=0

# for i in range(ramdonNumber):
#     repository.append(i)
# for i in repository:
#     suma=suma+i
# print('La suma total es: ', suma)


#Menu de banco, opciones, depositar, retirar, chequear saldo, salir
# saldo=0
# deposito=0
# retiro=0
# while True:
#     print("===================== Bienvenido a su banco ======================")
#     choice=input('1. Depositar\n2. Retirar\n3. chequear saldo\n4. Salir\n')
#     choice=int(choice)
#     if choice==1:
#         deposito=int(input('Ingrese la cantidad a depositar: \n'))
#         saldo+=deposito
#         print(f'Su nuevo saldo es: {saldo}')
#     elif choice==2:
#         retiro=int(input('Ingrese la cantidad a retirar: \n'))
#         if retiro>saldo:
#             print('Fondos insuficientes')
#         else:
#             saldo-=retiro
#             print(f'Su nuevo saldo es: {saldo}')
#     elif choice==3:
#         print(f'Su saldo actual es: {saldo}')
#     elif choice==4:
#         print('Gracias por usar nuestro banco')
#         break
#     else:
#         print('Opcion no valida, intente de nuevo')


#CLases
# class Students:
#     def __init__(self, name, course='AI'):
#         print('the student has been registrered... ')
#         self.name=name
#         self.course=course
#     def dataStudent(self):
#         print(f'Name is: {self.name} and the course is: {self.course}')
    
# student1=Students('Jazmany')
# student2=Students('Carlos', 'Distributed systems')

# student1.dataStudent()
# student2.dataStudent()

#Ejemplo pasando argumentos

# class Students:
#     def __init__(self, name, course='AI'):
#         print('the student has been registrered... ')
#         self.name=name
#         self.course=course
#     def dataStudent(self,status='No active'):
#         print(f'Name is: {self.name} and the course is: {self.course}')
    
# student1=Students('Jazmany')
# student2=Students('Carlos', 'Distributed systems')

# student1.dataStudent()
# student2.dataStudent()

#App banco con clases
class banco:
    def __init__(self, titular, saldo, deposito, retiro):
        print('Bienvenido a su banco')
        self.titular=titular
        self.saldo=saldo
        self.deposito=deposito
        self.retiro=retiro
    def menu(self):
        while True:
            print("===================== Bienvenido a su banco ======================")
            choice=input('1. Depositar\n2. Retirar\n3. chequear saldo\n4. Salir\n')
            choice=int(choice)
            if choice==1:
                self.deposito=int(input('Ingrese la cantidad a depositar: \n'))
                self.saldo+=self.deposito
                print(f'Su nuevo saldo es: {self.saldo}')
            elif choice==2:
                self.retiro=int(input('Ingrese la cantidad a retirar: \n'))
                if self.retiro>self.saldo:
                    print('Fondos insuficientes')
                else:
                    self.saldo-=self.retiro
                    print(f'Su nuevo saldo es: {self.saldo}')
            elif choice==3:
                print(f'Su saldo actual es: {self.saldo}')
            elif choice==4:
                print('Gracias por usar nuestro banco')
                break
            else:
                print('Opcion no valida, intente de nuevo')