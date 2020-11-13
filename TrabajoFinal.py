import TrabajoFinalDB
from TrabajoFinalOO import Tarea, Usuario, Estado

contador = 0
salir = True
Buscar = True

def EstadosPredeterminados():
    NombreEstado = 'En proceso'
    Descripcion = 'La parte contratante de la primera parte será en este contrato la parte contratante de la primera parte'
    estado = Estado(NombreEstado, Descripcion)
    TrabajoFinalDB.session.add(estado)
    TrabajoFinalDB.session.commit()

    NombreEstado = 'En revisión'
    Descripcion = 'La parte contratante de la segunda parte será en este contrato la parte contratante de la segunda parte'
    estado = Estado(NombreEstado, Descripcion)
    TrabajoFinalDB.session.add(estado)
    TrabajoFinalDB.session.commit()

    NombreEstado = 'Completada'
    Descripcion = 'La parte contratante de la tercera parte será en este contrato la parte contratante de la tercera parte'
    estado = Estado(NombreEstado, Descripcion)
    TrabajoFinalDB.session.add(estado)
    TrabajoFinalDB.session.commit()

EstadosPredeterminados()

def ListaTareas():
    print('\nEstas són tus tareas\n')
    tareas = TrabajoFinalDB.session.query(Tarea).all()
    for tarea in tareas:
        print(tarea.Titulo, tarea.Descripcion, tarea.Estado, tarea.Responsable, tarea.FechaCreacion)

def CrearTarea():
    print('\nCreando Tarea:\n')
    Titulo = input('Titulo de la tarea: ')
    Descripcion = input('Escribe una breve descripción de la tarea: ')
    Estado = 'En proceso'
    Responsable = input('Quién es el responsable: ')
    FechaCreacion = input('Fecha en la que se originó esta tarea: ')

    tarea = Tarea(Titulo, Descripcion, Estado, Responsable, FechaCreacion)
    TrabajoFinalDB.session.add(tarea)
    TrabajoFinalDB.session.commit()
    print('\nTarea Creada\n')

def CambiarEstadoTarea():
    #menú para seleccionar entre los diferentes estados
    print('\nActualizando estado de la tarea\n')
    EstadoReferencia = input("Que tarea quieres modificar? ")
    NombreEstado = input('Nuevo estado de la tarea: ')
    Descripcion = input('Nueva descripción de la tarea: '):
        if:
        
        estado.NombreEstado = Responsable
        estado.Descripcion = Descripcion
        TrabajoFinalDB.session.commit()

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
        print('\nNo se ha borrado\n')

def BuscarTarea():
    global Buscar

    print('\nBuscando tarea')
    while Buscar:
        Filtro = input("Filtrar por: título, responsable o estado?: ")
        if(Filtro.lower() == 'título'):
            Titulo = input("Filtrar por titulos: ")
            tarea = TrabajoFinalDB.session.query(Tarea).filter_by(Titulo=Titulo).first()
            print(tarea)
            Buscar=False
        elif(Filtro.lower() == 'responsable'):
            Responsable = input("Filtrar por responsables: ")
            tarea = TrabajoFinalDB.session.query(Tarea).filter_by(Responsable=Responsable).first()
            print(tarea)
            Buscar=False
        elif(Filtro.lower() == 'estado'):
            Responsable = input("Filtrar por estados: ")
            tarea = TrabajoFinalDB.session.query(Tarea).filter_by(Estado=Estado).first()
            print(tarea)
            Buscar=False
        else:
            Buscar=False
            print('\nFiltro no reconocido, asegurese que está bien escrito y vuelva a intentarlo')

def ListaUsuario():
    print('\nEstos són los responsables\n')
    usuarios = TrabajoFinalDB.session.query(Usuario).all()
    for usuario in usuarios:
        print(usuario.Nombre, usuario.Apellidos, usuario.Correo)

def CrearUsuario():
    print('\nCreando responsable:\n')
    Nombre = input('Nombre del responsable: ')
    Apellidos = input('Apellidos del responsable: ')
    Correo = input('Correo del responsable: ')
    #igual se podría poner algo para verificar que es una cuenta de correo

    usuario = Usuario(Nombre, Apellidos, Correo)
    TrabajoFinalDB.session.add(usuario)
    TrabajoFinalDB.session.commit()
    print('\nResponsable Creado\n')

def BorrarUsuario():
    print('\nEliminando responsable\n')
    NombreReferencia = input("Que responsable quieres eliminar? ")
    confirmacion = input ('Seguro que quiere borrarlo? y/n: ')
    if confirmacion == 'y':
        usuario = TrabajoFinalDB.session.query(Usuario).filter_by(Nombre=NombreReferencia).first()
        TrabajoFinalDB.session.delete(usuario)
        TrabajoFinalDB.session.commit()
        print('\nUsuario eliminado\n')
    else:
        print('\nNo se ha eliminado\n')

while salir:

    print("\nLISTADO DE TAREAS\n")

    print("[0]Lista de tareas")
    print("[1]Crear nueva tarea")
    print("[2]Cambiar estado de una tarea nueva")
    print("[3]Editar una tarea")
    print("[4]Borrar una tarea")
    print("[5]Búsqueda por usuario o coincidencia de Nombre")
    print("[6]Lista de responsables")
    print("[7]Crear nuevo responsable")
    print("[8]Eliminar responsable")
    print("[9]Salir\n\n")

    opciones = input("Selecciona una opción: ")

    if(int(opciones) == 0):
        ListaTareas()
    elif(int(opciones) == 1):
        CrearTarea()
    elif(int(opciones) == 2):
        CambiarEstadoTarea()
    elif(int(opciones) == 3):
        EditarTarea()
    elif(int(opciones) == 4):
        BorrarTarea()
    elif(int(opciones) == 5):
        BuscarTarea()
    elif(int(opciones) == 6):
        ListaUsuario()
    elif(int(opciones) == 7):
        CrearUsuario()
    elif(int(opciones) == 8):
        BorrarUsuario()
    elif(int(opciones) == 9):
        salir=False
        print('\nNo hagas hoy lo que puedas dejar para mañana\n')
    else:
        if (contador == 0):
            print('\nLos números que están entre corchetes són las opciones, solo puedes seleccionar esas')
        elif (contador == 1):
            print('\nEs solo darle a uno de los números que tienes arriba, no es tan difícil, de verdad')
        elif (contador == 2):
            print('\nA ver, a ti que te pasa, es 0, 1, 2, 3, 4, 5, 6, 7, 8 o 9 no hay más, así que no insistas')
        else:
            print('\nParece que han vuelto a dejar la jaula del mono abierta y se ha puesto a jugar con el móvil, otra vez, cerrando la aplicación y llamando a la protectora.')
            salir=False
        contador += 1
