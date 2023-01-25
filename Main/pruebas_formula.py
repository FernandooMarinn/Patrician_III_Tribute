def prueba(opcion):
    if opcion == 1:
        print("Soy un uno")
        opcion = 2
    if opcion == 2:
        print("Soy un dos")
        opcion = 3
    if opcion != 1 and opcion != 2:
        print("No soy ni un uno ni un dos")

prueba(1)