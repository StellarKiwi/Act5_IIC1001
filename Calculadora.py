Conf_Digito_1 = True
Conf_Digito_2 = True

while True:
    while Conf_Digito_1:
        Digito_1 = (input("Ingrese el primer dígito a operar \n"))
        if Digito_1.isdecimal() == False:
            print("Por favor, ingrese un número válido")
        else:
            Digito_1 = int(Digito_1)
            Conf_Digito_1 = False
    Operador = input("Ingrese el operador: \n + (Suma) \n - (Resta) \n * (Multiplicación) \n  / (División) \n")
    Confirm_Operador = Operador == "+" or Operador == "-" or Operador == "*" or Operador == "/"
    if Confirm_Operador == False:
        while True:
            Operador = input("Por favor, ingrese un operador válido \n")
            Confirm_Operador = Operador == "+" or Operador == "-" or Operador == "*" or Operador == "/"
            if Confirm_Operador == True:
                break
    while Conf_Digito_2:
        Digito_2 = (input("Ingrese el segundo dígito a operar \n"))
        if Digito_2.isdecimal() == False:
            print("Por favor, ingrese un número válido")
        else:
            Digito_2 = int(Digito_2)
            Conf_Digito_2 = False
    Confirmacion = (input(f"¿Quiere operar {Digito_1} {Operador} {Digito_2}? (Y/N) \n"))
    if Confirmacion == "Y" or Confirmacion == "y":
        if Operador == "+":
            print(f"El Resultado es = {Digito_1+Digito_2}")
        elif Operador == "-":
            print(f"El Resultado es = {Digito_1-Digito_2}")
        elif Operador == "*":
            print(f"El Resultado es = {Digito_1*Digito_2}")
        elif Operador == "/":
            print(f"El Resultado es = {Digito_1/Digito_2}")
        Seguir = input("¿Desea realizar otra operación? (Y/N) \n")
        if Seguir == "N" or Seguir == "n":
            break
    Conf_Digito_1 = True
    Conf_Digito_2 = True
print("¡Muchas gracias por usar la calculadora!")