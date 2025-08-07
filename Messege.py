from contextlib import nullcontext


def Menu():
    print("Paquetería BingBong")
    print("1.Ingresar repartidores: ")
    print("2.Mostrar repartidores desordenados")
    print("3.Mostrar repartidores ordenados")
    print("4.Buscar repartidor")
    print("5.Estadisticas generales")
    print("6.Salir")
def Q_S(Sorted):
    Lower = {}
    Same = {}
    Upper = {}
    if len(Sorted) <= 1:
        return Sorted
    for code,value in Sorted.items():
        Check = value['Entregas']
        break
    for code, value in Sorted.items():
        if value['Entregas'] < Check:
            Lower[code] = {'Entregas': value['Entregas'],'Zona': value['Zona']}
        if value['Entregas'] == Check:
            Same[code] = {'Entregas': value['Entregas'],'Zona': value['Zona']}
        if value['Entregas'] > Check:
            Upper[code] = {'Entregas': value['Entregas'], 'Zona': value['Zona']}
    return {**Q_S(Upper), **Same, **Q_S(Lower)}
def Bus_Sec(Looking,Find):
    for code,value in Looking.items():
        Name = code.lower()
        Find = Find.lower()
        if Name == Find:
            return Name
    return -1
def Total(Dict,T):
    if len(Dict) == 0:
        return T
    else:
        for code,value in Dict.items():
           T = T + value['Entregas']
    return T
allow = False
allow1 = False
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
                    if name not in messengers:
                        deliver = int(input("Cuantos paquetes entregó: "))
                        if deliver <= 0:
                            print("Cantidad no valida")
                        else:
                            zone = input("Zona asiganda: ")
                            if zone == "":
                                print("La zona no puede quedar vacía")
                            else:
                                messengers[name] = {'Entregas': deliver, 'Zona': zone}
                    else:
                        print("No se pueden repetir nombres")
                allow1 = True
        case 2:
            if allow1 == False:
                print("Aún no hay datos que ingresar")
            else:
                cont = 1
                for code,value in messengers.items():
                    print(f"Repartidor {cont}:")
                    print(f"Nombre del repartidor: {code},Cantidad de entregas: {value['Entregas']},Zona: {value['Zona']}")
                    print(" ")
                    cont = cont + 1
        case 3:
            if allow1 == False:
                print("Aún no hay datos que ingresar")
            else:
                cont = 1
                result = Q_S(messengers)
            for code,value in result.items():
                print(f"Repartidor {cont}:")
                print(f"Nombre del repartidor: {code},Cantidad de entregas: {value['Entregas']},Zona: {value['Zona']}")
                print(" ")
                cont = cont + 1
        case 4:
            look = input("Ingrese el nombre del repartidor que busca: ")
            find = Bus_Sec(messengers,look)
            if find == -1:
                print(f"El repartidor {look} no existe")
            else:
                print(f"Repartidor {find} existe")
                print(f"Nombre: {messengers[find]['Nombre']},Entregas: {messengers[find]['Entregas']},Zona: {messengers[find]['Zona']}")
        case 5:
            print(f"Total de paquetes entregados:")
        case 6:
            print("Gracias por utilizar el programa")
            break
        case _:
            print("La opción seleccionada no es valida")