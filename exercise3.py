#Desarrollador: Elimar Rojas
#Fecha: 12/01/2024
#Proyecto: Entry_level_0
"""
3. Create an university enrollment system with the following characteristics:

* The system has a login with a username and password.
* Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
* The user must input their first name, last name, and chosen program.
* Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
* If login information is incorrect three times, the system should be locked.
* The user must choose a campus from three cities: London, Manchester, Liverpool.
* In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
* If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.

Author: @blindma1den
https://github.com/blindma1den/Programming-Skills-Level0

"""

def enrollment_system():

  print("Bienvenido al sistema de matrícula U")
  
  while True:  
    
    students = []
      
    student = {
      'nombre': '',
      'apellido': '',
      'programas': [], 
      'program_campus': []
    }

    assigned_user = str(input("Ingrese su usuario: "))
    assigned_pass = int(input("Ingrese su contraseña: "))
    count = 0
    
    #validando credenciales del usuario hasta 3 intentos
    while count < 3:
      user = str(input("Por favor, confirme su usuario: "))
      password = int(input("Por favor, confirme su contraseña: "))
      if (user == assigned_user) and (password == assigned_pass):
        print("Inicio de sesión exitoso\n")
        break
      else:
        count += 1
        print("Usuario o contraseña incorrectos\nIntente de nuevo")
        if count == 3:
          print("Ha excedido el número máximo de intentos")
          print("Usuario bloqueado")
          return

    #ingresando al sistema y registrando al usuario     
    print(f"Bienvenido {user}")
    print("Por favor, ingrese su nombre y apellido")
    name = str(input("Nombre: "))
    last_name = str(input("Apellido: "))
    programs = []
    campus_reg = []
    num_program = 0    
    slots_1 = {'1': 1, '2': 1, '3': 1, '4': 1}
    slots_2 = {'1': 3, '2': 3, '3': 3, '4': 3}
    slots_3 = {'1': 1, '2': 1, '3': 1, '4': 1}

    #validando que el usuario ingrese un número válido
    ver = False
    while ver == False:
      program = ""
      answer = "s"
      while program != 5 or answer == "s":
        print("Menú de programas")
        print("1: Informática")
        print("2: Medicina")
        print("3: Marketing")
        print("4: Artes")
        print("5. Salir")
        program = input("Seleccione una opción: ")     
        if program == "1" or program == "2" or program == "3" or program == "4":        
          programs.append((program))
          #print(programs)
          break
        elif program == "5":
          print("Gracias por usar la plataforma de matrícula U")
          return
        else:
          print("Opción inválida, por favor intente nuevamente")        
             
      campus = 0
        
      while campus > 3 or campus < 1:
        print("Por favor, ingrese el campus al que desea matricularse")
        print("1. Londres")
        print("2. Manchester")
        print("3. Liverpool")
        campus = int(input("Ingrese el número del campus: "))
        campus_site = str(campus)           
        if campus == 1:
          campus_site = "londres"
          print(f"Campus seleccionado: {campus_site}\n")       
          if slots_1[program] == 0:
            print("No hay suficientes plazas disponibles en Londres")
            print("Plazas disponibles en Manchester: {}".format(slots_2[program]))
            print("Plazas disponibles en Liverpool: {}".format(slots_3[program]))
            print("¿Desea matricularse en otro campus? (s/n)")
            answer = input()
            if answer == "s":
              campus = 0            
            elif answer == "n":
              print("Gracias por utilizar el sistema de matrícula U")
              return
            else:
              print("Por favor, ingresa una opción correcta")
          else:
            for i in range(len(programs)):
              for k, v in slots_1.items():
                if programs[i] in slots_1:
                  if slots_1[programs[i]] > 0:
                    print(f"El registro de {program} ha sido exitoso")                 
                    slots_1[programs[i]] -= 1
                    #print(slots_1[programs[i]])
                    #print(slots_1)
            campus_reg.append((program, campus_site))
            print(campus_reg)
        elif campus == 2:
          campus_site = "Manchester"
          print(f"Campus seleccionado: {campus_site}\n")
          if slots_2[program] == 0:
            print("No hay suficientes plazas disponibles en Londres")
            print("Número de plazas disponibles en Londres: {}".format(slots_2[program]))
            print("Número de plazas disponibles en Liverpool: {}".format(slots_3[program]))
            print("¿Desea matricularse en otro campus? (s/n)")
            answer = input()
            if answer == "s":
              campus = 0             
            elif answer == "n":
              print("Gracias por utilizar el sistema de matrícula U")
              return
            else:
              print("Por favor, ingresa una opción correcta")              
          else:
            #validación de duplicado de programas            
            if (len(programs) >= 2) and (programs.count(program) > 1):
              print("Ya has inscrito este programa")
              programs.remove(program)
              num_program -= 1                         
              break
            for i in range(len(programs)):
              for k, v in slots_2.items():
                if programs[i] in slots_2:
                  if slots_3[programs[i]] > 0:
                    print(f"El registro de {program} ha sido exitoso")                 
                    slots_2[programs[i]] -= 1
                    #print(slots_2[programs[i]])
                    #print(slots_2)
                    break
            campus_reg.append((program, campus_site))
            print(campus_reg)
        elif campus == 3:
          campus_site = "Liverpool"
          print(f"Campus seleccionado: {campus_site}\n")       
          if slots_3[program] == 0:
            print("No hay suficientes plazas disponibles en Londres")
            print("Plazas disponibles en Manchester: {}".format(slots_2[program]))
            print("Plazas disponibles en Liverpool: {}".format(slots_1[program]))
            print("¿Desea matricularse en otro campus? (s/n)")
            answer = input()
            if answer == "s":
              campus = 0            
            elif answer == "n":
              print("Gracias por utilizar el sistema de matrícula U")
              return
            else:
              print("Por favor, ingresa una opción correcta")
          else:
            for i in range(len(programs)):
              for k, v in slots_3.items():
                if programs[i] in slots_3:
                  if slots_3[programs[i]] > 0:
                    print(f"El registro de {program} ha sido exitoso")                 
                    slots_3[programs[i]] -= 1
                    #print(slots_3[programs[i]])
                    #print(slots_3)
            campus_reg.append((program, campus_site))
            #print(campus_reg)
        else:
         print("Por favor, ingrese una opción válida")  
              
      print("¿Desea añadir otro programa? (s/n)")
      answer = input()
      num_program += 1
      ver = False
      print(num_program)
      if answer == "s":
        print(f"Programa: {program}")                
      elif answer == "n":       
        print(f"La carga académica de estudiante {i+1} es:")
        student['nombre'] = name
        student['apellido'] = last_name
        student['programas'] = programs                 
        student['program_campus'] = campus_reg
        for k in student:
          print(k, ":", student[k])                
        for student.items in students:          
          students.append((student.items))
          count += 1
          print(students)
        print("\n")  
        break  
      else:
        print("Por favor ingrese una opción válida")
             
enrollment_system()
