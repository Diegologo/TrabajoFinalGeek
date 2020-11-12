import TrabajoFinalDB
from TrabajoFinalOO import Tarea, Usuario, Estado

contador = 0
salir = True
Buscar = True
'''
def EstadosPredeterminados():
    NombreEstado = "Sólido"
    Descripcion = "La parte contratante de la primera parte será en este contrato la parte contratante de la primera parte"
    Estado = "Líquido"
    Descripcion = "La parte contratante de la segunda parte será en este contrato la parte contratante de la segunda parte"
    Estado = "Gaseoso"
    Descripcion = "La parte contratante de la tercera parte será en este contrato la parte contratante de la tercera parte"

    estado = Estado(NombreEstado, Descripcion)
    TrabajoFinalDB.session.add(estado)
    TrabajoFinalDB.session.commit()

EstadosPredeterminados()'''
    #aquí lo que quiero que haga es que cree automáticamente los 3 estados posibles

def VerTarea():
    print('\nEstas són tus tareas\n')
    tareas = TrabajoFinalDB.session.query(Tarea).all()
    print(tareas)
    #como hacer que las tareas salgan una debajo de otra y no al lado? Había un comentario de algo parecido en slack pero no me sale.

def BuscarTarea():
    global Buscar

    print('\nBuscando tarea')
    while Buscar:
        Filtro = input("Filtrar por: Título, Responsable o Estado?: ")
        if(Filtro == 'Título'):
            Titulo = input("Filtrar por titulos: ")
            tarea = TrabajoFinalDB.session.query(Tarea).filter_by(Titulo=Titulo).first()
            #cuando pongo el lower peta al buscar tareas
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
            Buscar=False
            print('\nFiltro no reconocido, asegurese que está bien escrito y vuelva a intentarlo')

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
    print('\nEliminando tarea\n')
    TituloReferencia = input("Que tarea quieres eliminar? ")
    confirmacion = input ('Seguro que quiere borrarlo? y/n: ')
    if confirmacion == 'y':
        tarea = TrabajoFinalDB.session.query(Tarea).filter_by(Titulo=TituloReferencia).first()
        TrabajoFinalDB.session.delete(tarea)
        TrabajoFinalDB.session.commit()
        print('\nTarea eliminada\n')
    else:
        print('\nNo se ha borrado')

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

    if(int(opciones) == 1):
        VerTarea()
    elif(int(opciones) == 2):
        CrearTarea()
    elif(int(opciones) == 3):
        CambiarEstadoTarea()
    elif(int(opciones) == 4):
        EditarTarea()
    elif(int(opciones) == 5):
        BorrarTarea()
    elif(int(opciones) == 6):
        BuscarTarea()
    elif(int(opciones) == 7):
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
