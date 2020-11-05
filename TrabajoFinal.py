import TrabajoFinalDB
from TrabajoFinalOO import Tarea

contador = 0
salir = True
Buscar = True

def BuscarTarea():
    global Buscar

    print('\nBuscando tarea')
    while Buscar:
        Filtro = input("Filtro de búsqueda: ")
        if(Filtro == 'Titulo'):
            Titulo = input("Filtrar por titulos: ")
            tarea = TrabajoFinalDB.session.query(Tarea).filter_by(Titulo=Titulo.lower).first()
            print(tarea)
            Buscar=False
        elif(Filtro == 'Responsable'):
            Responsable = input("Filtrar por responsables: ")
            tarea = TrabajoFinalDB.session.query(Tarea).filter_by(Responsable=Responsable).first()
            print(tarea)
            Buscar=False
        elif(Filtro == 'Estado'):
            Responsable = input("Filtrar por estados: ")
            tarea = TrabajoFinalDB.session.query(Tarea).filter_by(Estado=Estado).first()
            print(tarea)
            Buscar=False
        else:
            print('Filtro no reconocido, asegurese que está bien escrito y vuelva a intentarlo')
            Buscar=False

    print(tarea)
    #como hacer que vuelva al bucle anterior?
    #Hacer un submenú que te deje seleccionar por qué campo quieres buscar.

def CrearTarea():
    print('\nCreando Tarea:\n')
    Titulo = input('Titulo de la tarea: ')
    Descripcion = input('Escribe una breve descripción de la tarea: ')
    Estado = input('En que estado se encuentra la tarea? ')
    #hacer menú para seleccionar entre los diferentes estados
    Responsable = input('Quién es el responsable: ')
    FechaCreacion = input('Fecha en la que se originó esta tarea: ')

    tarea = Tarea(Titulo, Descripcion, Estado, Responsable, FechaCreacion)
    TrabajoFinalDB.session.add(tarea)
    TrabajoFinalDB.session.commit()
    print('\nTarea Creada\n')

def CambiarEstadoTarea():
    print('\nActualizando estado de la tarea\n')
    #menú para seleccionar entre los diferentes estados
    print('\nEstado de la tarea actualizado')

def EditarTarea():
    print('\nModificando tarea\n')
    TituloReferencia = input("Que tarea quieres modificar? ")
    Titulo = input('Nuevo título de la tarea: ')
    Descripcion = input('Nueva descripción de la tarea: ')
    Responsable = input('Nuevo Responsable: ')
    tarea = TrabajoFinalDB.session.query(Tarea).filter_by(Titulo=TituloReferencia).first()
    tarea.Titulo = Titulo
    tarea.Descripcion = Descripcion
    tarea.Responsable = Responsable
    TrabajoFinalDB.session.commit()

    print('\nTarea modificada\n')

def BorrarTarea():
    #Como poner una confirmación antes de eliminar?
    print('\nEliminando tarea\n')
    TituloReferencia = input("Que tarea quieres eliminar? ")
    confirmacion = input ('Seguro que quiere borrarlo y/n')
        if confirmacion.lower == 'y':
        tarea = TrabajoFinalDB.session.query(Tarea).filter_by(Titulo=TituloReferencia).first()
        else confirmacion.ower == 'n':
            print ('No se ha borrado')

    TrabajoFinalDB.session.delete(tarea)
    TrabajoFinalDB.session.commit()
    print('\nTarea eliminada\n')

while salir:

    print("\nLISTADO DE TAREAS\n\n")

    print("[1]Ver tareas\n")
    print("[2]Crear nueva tarea\n")
    print("[3]Cambiar estado de una tarea nueva\n")
    print("[4]Editar una tarea\n")
    print("[5]Borrar una tarea\n")
    print("[6]Búsqueda por usuario o coincidencia de Nombre\n")
    print("[7]Salir\n\n")

    opciones = input("Selecciona una opción: ")

    if(opciones == '1'):
        print('\nEstas són tus tareas')
    elif(opciones == '2'):
        CrearTarea()
    elif(int(opciones) == 3):
        CambiarEstadoTarea()
    elif(opciones == '4'):
        EditarTarea()
    elif(opciones == '5'):
        BorrarTarea()
    elif(opciones == '6'):
        BuscarTarea()
    elif(opciones == '7'):
        salir=False
        print('\nNo hagas hoy lo que puedas dejar para mañana\n')
    else:
        if (contador == 0):
            print('\nLos núemros que están entre corchetes són las opciones, solo puedes seleccionar esas')
        elif (contador == 1):
            print('\nEs solo darle a uno de los números que tienes arriba, no es tan difícil, de verdad')
        elif (contador == 2):
            print('\nA ver, a ti que te pasa, es 1, 2, 3, 4, 5, 6 o 7, no hay más, así que no insistas')
        else:
            print('\nParece que han vuelto a dejar la jaula del mono abierta y se ha puesto a jugar con el móvil, otra vez, cerrando la aplicación y llamando a la protectora.')
            salir=False
        contador += 1
