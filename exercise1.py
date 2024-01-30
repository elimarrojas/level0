#Desarrollador: Elimar Rojas
#Fecha:04/01/2023           
#Proyecto: Entry_level_0        

"""
1. Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions.

Author: @blindma1den
https://github.com/blindma1den/Programming-Skills-Level0
"""

class Entry:

  def banking_system():
    
    print("Bienvenid@ al Banco XYZ")
    
    assigned_user = "eliro"
    assigned_pass = 1234
    count = 0       
    
    while count < 3:
      user = str(input("Ingresa tu usuario: "))
      password = int(input(f"{user}, ingresa tu contraseña: "))     
      if (user == assigned_user) and (password == assigned_pass):
        print("Inicio de sesión exitoso\n")
        break        
      else:
        print("Usuario o contraseña incorrectos, intenta de nuevo")              
        print(f"Intentos restantes: {2 - count}\n")
        count += 1
        if count == 3:
          print("Has superado el número de intentos permitidos\nHasta pronto")
          return          
            
    while True:
      print(f"{user}, bienvenido al sistema")
      balance = 2000  
      print(f"Tu saldo es de {balance}$")
      option = ""
      while option != 5:
        print("¿Que operación deseas relizar?")
        print("1. Depositar\n2. Retirar\n3. Consultar\n4. Transferir\n5. Salir")
        option = int(input("Ingresa la opción: "))
        if option == 1:
          deposit = int(input("¿Cuánto deseas depositar?: "))
          if deposit > 0:
            balance += deposit
            print(f"Tu saldo es de {balance}$\n")
        elif option == 2:
          withdraw = int(input("¿cuánto deseas retirar?: "))
          if withdraw > 0:
            balance -= withdraw
            print(f"tu saldo es de {balance}$\n")
        elif option == 3:
          print(f"Tu saldo es de {balance}$\n")
        elif option == 4:
          transfer = int(input("¿Cuánto deseas trasferir?: "))
          if transfer > 0:
            balance -= transfer
            print(f"Tu saldo es de {balance}$\n")
        elif option == 5:
          print("Gracias por utilizar nuestros servicios")
          return
        else:
          print("Opción no válida")          
        
  banking_system()
   
 