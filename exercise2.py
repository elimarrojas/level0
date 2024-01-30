#Desarrollador: Elimar Rojas
#Fecha: 10/01/2024
#Proyecto: Entry_level_0

"""
2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:

* The user must choose their initial currency and the currency they want to exchange to.
* The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
* If the user decides to withdraw the funds, the system will charge a 1% commission.
* Set a minimum and maximum amount for each currency, it can be of your choice.
* The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.

Author: @blindma1den
https://github.com/blindma1den/Programming-Skills-Level0
"""

class Entry:
  
  def exchange():
    print("Bienvenido al conversor de divisas XYZ")    
  
    menu = ""
    while menu != "n" or menu != "N":
      init_currency = int(input("Indique la moneda inicial:\n 1.CLP\n 2.ARS\n 3.USD\n 4.EUR\n 5.TRY\n 6.GBP\n Ingrese su respuesta: "))
      #validando el ingreso del init_currency
      while init_currency < 1 or init_currency > 6:
        print ("Ingrese una número entre 1 y 6, intente de nuevo")
        init_currency = int(input("Indique la moneda inicial:\n 1.CLP\n 2.ARS\n 3.USD\n 4.EUR\n 5.TRY\n 6.GBP\n Ingrese su respuesta: "))

      
      exchan_currency = int(input("Indique la moneda a la que desea cambiar:\n 1.CLP\n 2.ARS\n 3.USD\n 4.EUR\n 5.TRY\n 6.GBP\n Ingrese su respuesta: "))
      #validando el ingreso del exchan_currency
      while exchan_currency < 1 or exchan_currency > 6:
        print ("Ingrese una número entre 1 y 6, intente de nuevo")
        exchan_currency = int(input("Indique la moneda a la que desea cambiar:\n 1.CLP\n 2.ARS\n 3.USD\n 4.EUR\n 5.TRY\n 6.GBP\n Ingrese su respuesta: "))
        ver = False
           
      balance = 0.0
                     
      if init_currency == 1:
        clp = int(input("Ingrese la cantidad de CLP a cambiar: "))  
        if exchan_currency == 1:
          print(f"El valor en CLP es: {clp}")
        elif exchan_currency == 2:
          balance = round((clp*0.0059),2)
          print(f"El valor en ARS es: {balance}")
        elif exchan_currency == 3:
          balance = round((clp*0.00026),2)
          print(f"El valor en USD es: {balance}")
        elif exchan_currency == 4:
          balance = round((clp*0.00022),2)
          print(f"El valor en EUR es: {balance}")
        elif exchan_currency == 5:
          balance = round((clp*0.0069),2)
          print(f"El valor en TRY es: {balance}")
        elif exchan_currency == 6:
          balance = round((clp*0.00016),2)
          print(f"El valor en GBP es: {balance}")
        else:
          print("Ingrese una opción válida")
      elif init_currency == 2:
        ars = int(input("Ingrese la cantidad de ARS a cambiar: "))
        if exchan_currency == 1:
          balance = round((ars*0.0059),2)    
          print(f"El valor en CLP es: {balance}") 
        elif exchan_currency == 2:
          print(f"El valor en ARS es: {ars}")
        elif exchan_currency == 3:
          balance = round((ars*0.00024),2)
          print(f"El valor en USD es: {balance}")
        elif exchan_currency == 4:
          balance = round((ars*0.0021),2)
          print(f"El valor en EUR es: {balance}")
        elif exchan_currency == 5:
          balance = round((ars*0.0027),2)
          print(f"El valor en TRY es: {balance}")
        elif exchan_currency == 6:
          balance = round((ars*0.0017),2)
          print(f"El valor en GBP es: {balance}")
        else:
          print("Ingrese una opción válida")
      elif init_currency == 3:
        usd = int(input("Ingrese la cantidad de USD a cambiar: "))
        if exchan_currency == 1:
          balance = round((usd*4.013),2)
          print(f"El valor en CLP es: {balance}")
        elif exchan_currency == 2:
          balance = round((usd*39.98),2)
          print(f"El valor en ARS es: {balance}")
        elif exchan_currency == 3:
          print(f"El valor en USD es: {usd}")
        elif exchan_currency == 4:
          balance = round((usd*0.84),2)
          print(f"El valor en EUR es: {balance}")
        elif exchan_currency == 5:
          balance = round((usd*7.61),2)
          print(f"El valor en TRY es: {balance}")
        elif exchan_currency == 6:
          balance = round((usd*0.72),2)
          print(f"El valor en GBP es: {balance}")
        else:
          print("Ingrese una opción válida")
      elif init_currency == 4:
        eur = int(input("Ingrese la cantidad de EUR a cambiar: "))
        if exchan_currency == 1:
          balance = round((eur*4.463),2)
          print(f"El valor en CLP es: {balance}")
        elif exchan_currency == 2:
          balance = round((eur*44.63),2)
          print(f"El valor en ARS es: {balance}")
        elif exchan_currency == 3:
          balance = round((eur*1.19),2)
          print(f"El valor en USD es: {balance}")
        elif exchan_currency == 4:
          print(f"El valor en EUR es: {eur}")
        elif exchan_currency == 5:
          balance = round((eur*8.78),2)
          print(f"El valor en TRY es: {balance}")
        elif exchan_currency == 6:
          balance = round((eur*0.87),2)
          print(f"El valor en GBP es: {balance}")
        else:
          print("Ingrese una opción válida")
      elif init_currency == 5:
        try_ = int(input("Ingrese la cantidad de TRY a cambiar: "))
        if exchan_currency == 1:
          balance = round((try_*0.11),2)
          print(f"El valor en CLP es: {balance}")
        elif exchan_currency == 2:
          balance = round((try_*3.66),2)
          print(f"El valor en ARS es: {balance}")
        elif exchan_currency == 3:
          balance = round((try_*0.13),2)
          print(f"El valor en USD es: {balance}")
        elif exchan_currency == 4:
          balance = round((try_*0.12),2)
          print(f"El valor en EUR es: {balance}")
        elif exchan_currency == 5:    
          print(f"El valor en TRY es: {try_}")
        elif exchan_currency == 6:
          balance = round((try_*0.10),2)
          print(f"El valor en GBP es: {balance}")
        else:
          print("Ingrese una opción válida")
      elif init_currency == 6:
        gbp = int(input("Ingrese la cantidad de GBP a cambiar: "))
        if exchan_currency == 1:
          balance = round((gbp*6.652),2)    
          print(f"El valor en CLP es: {balance}")
        elif exchan_currency == 2:
          balance = round((gbp*100.00),2)
          print(f"El valor en ARS es: {balance}")
        elif exchan_currency == 3:
          balance = round((gbp*1.37),2)
          print(f"El valor en USD es: {balance}")
        elif exchan_currency == 4:
          balance = round((gbp*1.16),2)
          print(f"El valor en EUR es: {balance}")
        elif exchan_currency == 5:
          balance = round((gbp*15.54),2)
          print(f"El valor en TRY es: {balance}")
        elif exchan_currency == 6:
          print(f"El valor en GBP es: {gbp}")
        else:
          print("Ingrese una opción válida")
      else:
        print("Ingrese una opción válida")
               
      min = balance*0.1
      max = balance*0.8
      ver = False
      while ver == False:          
        operation = str(input("¿Desea retirar su dinero?(S/N): "))         
        if operation == "S" or operation == "s":  
          withdraw = float(input("Ingrese la cantidad a retirar: "))
          if withdraw > balance:
            print("No tiene suficientes fondos")
            ver = False
          elif withdraw < min:
            print(f"El mínimo a retirar es: {min}")
            ver = False
          elif withdraw > max:
            print(f"El máximo a retirar es: {max}")
            ver = False
          else:
            print("Retire su dinero")
            commission = withdraw*0.01
            balance = balance - withdraw - commission    
            print(f"Su nuevo saldo es: {balance}")              
            menu = str(input("¿Desea realizar otra operación?(S/N): "))
            if menu == "S" or menu == "s":
              ver = False
            elif menu == "N" or menu == "n":
              print("...Saliendo del sistema")
              print("Gracias por utilizar nuestros servicios")              
              return             
            else:
              print("Ingrese una opción correcta")
              ver = False
        elif operation == "N" or operation == "n":
          print("Retornando al menú principal")            
          ver = True
        else:
          print("Ingrese una de las opciones válidas")
          ver = False
    
  exchange()
    
