#Desarrollador: Elimar Rojas
#Fecha: 10/01/2024
#Proyecto: Entry_level_0

"""
5. Develop a finance management application with the following features:

* The user records their total income.
* There are categories: Medical expenses, household expenses, leisure, savings, and education.
* The user can list their expenses within the categories and get the total for each category.
* The user can obtain the total of their expenses.
* If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
* If the user spends less than they earn, the system displays a congratulatory message on the screen.
* If the user spends more than they earn, the system will display advice to improve the user's financial health.

Author: @blindma1den
https://github.com/blindma1den/Programming-Skills-Level0
"""
import operator
import tkinter as tk
import tkinter.messagebox as tkmb


class Entry:

  def finance_management():
    
    print("Bienvenid@ a la aplicación de gestión de finanzas XYZ")
    print("Por favor introduce tu ingreso total")
    income = float(input())    
    expenses = {}
    total_expenses = 0
    
    for category in ['Gastos médicos', 'Gastos domésticos', 'Ocio', 'Ahorro', 'Educación']:
      print("Por favor registra tus gastos para {}".format(category))
      expenses_item = {}
      #agregando los gastos (item) dentro de cada categoría
      while True: 
        print("Por favor ingresa el item de gasto")
        item = input()
        print("Por favor ingresa la cantidad del gasto")
        amount = float(input())
        expenses_item[item] = amount
        print("¿Deseas añadir otro gasto? (s/n)")
        answer = input()
        if answer == "n":
          break
      
      total_item = sum(expenses_item.values())
      expenses[category] = expenses_item
      #print("Your expenses list are: " + str(expenses_list))
      print(f"Tus gastos por item son: {expenses[category]}")      
      print("Tu total de gastos por item es: ${}".format(total_item))
      print("\n")
      total_expenses += total_item
        
    for category in expenses:
      print("Tus gastos por {} son: ${}".format(category, sum(expenses[category].values())))
    print("Tus gastos totales son: ${}".format(total_expenses))    
    print("\n")
    if total_expenses > income:
      print("Estás gastando más de lo que ganas")
      print("Aquí tienes algunos consejos para mejorar tu salud financiera:")
      print("1. Vivir dentro de tus posibilidades")
      print("2. Controlar los gastos")
      print("3. Evitar los gastos hormiga")
      print("4. Reducir o eliminar las deudas")
      print("5. Ahorrar/Acumular un fondo para emergencias")      
    elif total_expenses < income:
      print("Estás gastando menos de lo que ganas")
      #código para que salga un pop up, pero no funciona je
      master = tk.Tk()
      info_message = "Felicitaciones! Que bien administras tus finanzas!"
      tkmb.showinfo("Output", info_message)
      master.mainloop()    
    else:
      print("Estás gastando la misma cantidad que ganas")
      #buscando la key con el valor más alto
      max_category = max(expenses, key=lambda k: sum(expenses[k].values()))
      print(f"Debes reducir tus gastos en {max_category}")   

  finance_management()

