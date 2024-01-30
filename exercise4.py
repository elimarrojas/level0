#Desarrollador: Elimar Rojas
#Fecha: 09/01/2024
#Proyecto: Entry_level_0

"""
4. Create an online shipping system with the following features:

*The system has a login that locks after the third failed attempt.
*Display a menu that allows: Sending a package, exiting the system.
*To send a package, sender and recipient details are required.
*The system assigns a random package number to each sent package.
*The system calculates the shipping price. $2 per kg.
*The user must input the total weight of their package, and the system should display the amount to pay.
*The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.

Author: @blindma1den
https://github.com/blindma1den/Programming-Skills-Level0
"""

import random as r

class Entry:

  def shipping_system():

    print("Bienvenido al sistema de envío XYZ")
    assigned_user = "admin"
    assigned_passwword = 123
    attempts = 0
    package_number = r.randint(10000,99999)
    
    while attempts < 3:
      user = str(input("Ingrese su usuario: "))
      password = int(input("Ingrese su contraseña: "))
      if (user == assigned_user) and (password == assigned_passwword):
        print("Inicio de sesión exitoso\n")
        break
      else:
        attempts += 1
        print("Usuario o contraseña incorrectos\nIntente de nuevo")
        if attempts == 3:
          print("Ha excedido el número máximo de intentos")
          print("Usuario bloqueado")
          return

    while True:
      print("Seleccione una opción: ")
      print("1. Enviar paquete")
      print("2. Salir")
      option = int(input("Ingrese una opción: "))
      if option == 1:
        sender_name = input("Ingrese el nombre del remitente: ")
        sender_address = input("Ingrese la dirección del remitente: ")
        recipient_name = input("Ingrese el nombre del destinatario: ")
        recipient_address = input("Ingrese la dirección del destinatario: ")
        print(f"El número de su paquete es {package_number}")
        weight = float(input("Ingrese el peso del paquete (en kg): "))
        shipping_price = weight*2
        print(f"El precio de envío es: $ {shipping_price}\n")
        print("¿Desea realizar otra operación?")
        print("1. Si")
        print("2. No")
        option = int(input("Ingrese una opción: "))
        if option == 1:
          continue          
        elif option == 2:
          print("Gracias por utilizar el sistema de envío XYZ")
          return
        else:
          print("Ingrese un valor válido\nIntente nuevamente")
      elif option == 2:
          print("Gracias por usar el sistema de envío XYZ")
          return
      else:
        print("Ingrese una opción válida\nIntente de nuevo")
         
  shipping_system()
   