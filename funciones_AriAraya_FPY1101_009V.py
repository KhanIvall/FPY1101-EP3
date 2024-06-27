import os

libros=[]

libros_prestados=[]

def registro():
    titulo=input("\nIngrese el titulo del libro: ")
    autor=input("\nIngrese el autor del libro: ")
    anio=input("\nIngrese el año de publicación del libro: ")
    sku=input("\nIngrese el SKU del libro: ").upper()
    print("")

    if titulo=="" or autor=="" or anio=="" or sku=="":
        print("\nHay datos faltantes\n")
    else:
        dict_libro={
            "titulo":titulo,
            "autor":autor,
            "año":anio,
            "sku":sku
            }
        libros.append(dict_libro)

def prestamo():
    prestamo_valido=True
    usuario_prestamo=input("\nRegistre usuario para prestamo: ")
    sku_prestamo=input("\nIngrese el SKU del libro a prestar: ").upper()

    for libro in libros:
        if sku_prestamo in libro["sku"]:
            for prestamo in libros_prestados:
                if sku_prestamo in prestamo["sku"]:
                    titulo_libro=prestamo["titulo"]
                    fecha_prestamo="fecha hoy"#Desconozco algún código para generar la fecha del día.
                    dict_prestamo={
                        "usuario":usuario_prestamo,
                        "titulo":titulo_libro,
                        "sku":sku_prestamo,
                        "fecha":fecha_prestamo
                    }
                    libros_prestados.append(dict_prestamo)
                else:
                    prestamo_valido=False
        else:
            prestamo_valido=False
    if prestamo_valido==False:
        print("\nEl libro no existe o ya fue prestado\n")

def listar():
    print("\nTitulo\t\tAutor\t\tAño de publicación\t\tSKU\n")
    for libro in libros:
        print(f"\n{libro["titulo"]}\t\t{libro["autor"]}\t\t{libro["año"]}\t\t{libro["sku"]}\n")

def imprimir():
    with open("librosPrestados.txt","w") as archivo:
        archivo.write("USUARIO\t\tTÍTULO\t\tFECHA DEL PRESTAMO\n")
        for prestamo in libros_prestados:
            archivo.write(f"{prestamo["usuario"]}\t\t{prestamo["titulo"]}t\t{prestamo["fecha"]}\n")
    
    print("El archivo fue guardado correctamente en:", os.getcwd())
    print()

def menu():
    while True:
        try:
            print("* * * * M E N U * * * *")
            print("1. Registrar libro\n2. Prestar libro\n3. Listar todos los libros\n4. Imprimir reporte de prestamos\n5. Salir del programa\n")
            op=int(input("Ingrese una opción: "))
            if op==1:
                registro()
            elif op==2:
                prestamo()
            elif op==3:
                listar()
            elif op==4:
                imprimir()
            elif op==5:
                print("\nPrograma finalizado...\nDesarrollado por Ari Araya\nRUT: 19.408.808-6")
                break
            else:
                print("Debe ingresar un valor dentro del rango indicado (1-5)\n")
        except ValueError:
            print("Valor debe ser un número\n")