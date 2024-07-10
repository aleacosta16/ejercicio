



registro_estudiantes = []

def AgregarEstudiante(registro,id,nombre,edad):
    #verificar si alumno existe
    for alumno in registro:
        if alumno[id] == id:
            print("El alumno ya existe")
            return
        
        RegAlum = {
            'id' : id,
            'nombre' : nombre,
            'edad' : edad
        }
        registro.append(RegAlum)

def MostrarEstudiantes(registro):
    for alumno in registro:
        print(alumno)

def BuscarEstudiante(registro,alumno):
    encontrado = False
    for alumno in registro:
        if alumno['nombre'].lower() == nombre.lower():
            print(f"id: {alumno['id']}, edad: {alumno['edad']}")
            encontrado = True
    if  not encontrado:
        print("No se encontro el alumno", nombre)

def ExportarArchivo(registro, nombre_archivo):
    with open(nombre_archivo,'w') as archivo:
        for alumno in registro:
            archivo.write(f"id: {alumno['id']}, nombre: {alumno['nombre']} ,edad: {alumno['edad']}\n")


while True:
    print("Menu")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante (por nombre)")
    print("4. Exportar registro a archivo de texto")
    print("5. Salir")

    opcion = int(input("Ingrese la opcion que desee (1-5): "))

    if opcion == 1:
        id_estudiante = input("Ingrese el ID del estudiante: ")
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        edad_estudiante = int(input("Ingrese la edad del estudiante: "))
        AgregarEstudiante(registro_estudiantes,id_estudiante,nombre_estudiante,edad_estudiante)
        print("Estudiante agregado correctamente")
    
    elif opcion == 2:
        MostrarEstudiantes(registro_estudiantes)
    
    elif opcion == 3:
        nombre = input("Ingrese el nombre del estudiante a buscar: ")
        BuscarEstudiante(registro_estudiantes,nombre)
    
    elif opcion == 4:
        nombre_archivo = "registro_estudiante.txt"
        ExportarArchivo(registro_estudiantes, nombre_archivo)
    
    elif opcion == 5:
        break
    else:
        print("Opcion no valida")
