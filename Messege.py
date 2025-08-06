def Menu():
    print("Paquetería BingBong")
    print("1.Ingresar repartidores: ")
    print("2.Mostrar repartidores desordenados")
    print("3.Mostrar repartidores ordenados")
    print("4.Buscar repartidor")
    print("5.Estadisticas generales")
    print("6.Salir")
allow = False
messengers = {}
while allow == False:
    Menu()
    opt = int(input("Ingrese la opción que desee: "))
    print(" ")
    match opt:
        case 1:
            num = int(input("Cuantos repartidores participaron? "))
            if num <= 0:
                print("La cantidad ingresada no es valida")
            else:
                for i in range(num):
                    name = input("Ingrese el nombre del repartidor: ")
                    deliver = int(input("Cuantos paquetes entregó: "))
                    zone = input("Zona asiganda: ")
                    messengers[name] = {'Entregas':deliver,'Zona':zone}
        case 2:
            for code,value in messengers.items():
                print(f"Nombre del repartidor: {code},Cantidad de entregas: {value['Entregas']},Zona: {value['Zona']}")
        case 3:
            print("Mostrar ")
        case 4:
            look = input("Ingrese el nombre del repartidor que busca: ")
        case 5:
            print("Mostrar ")
        case 6:
            print("Gracias por utilizar el programa")
            break
        case _:
            print("La opción seleccionada no es valida")