import TrabajoFinalDB
from sqlalchemy import Column, String, Integer, ForeignKey

class Estado(TrabajoFinalDB.Base):
    __tablename__ = "estados"

    id = Column(Integer, primary_key=True)
    NombreEstado = Column(String(60))
    Descripcion = Column(String(255))
    
    def __init__(self, NombreEstado, Descripcion):
        self.NombreEstado = NombreEstado
        self.Descripcion = Descripcion

    def __repr__(self):
        return f'{self.id}, {self.NombreEstado}, {self.Descripcion}'

TrabajoFinalDB.Base.metadata.create_all(TrabajoFinalDB.engine)

class Usuario(TrabajoFinalDB.Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    Nombre = Column(String(60))
    Apellidos = Column(String(60))
    Correo = Column(String(60))
    
    def __init__(self, Nombre, Apellidos, Correo):
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Correo = Correo

    def __repr__(self):
        return f'{self.id}, {self.Nombre}, {self.Apellidos}, {self.Correo}'

TrabajoFinalDB.Base.metadata.create_all(TrabajoFinalDB.engine)

class Tarea(TrabajoFinalDB.Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True)
    Titulo = Column(String(60))
    Descripcion = Column(String(255))
    Estado = Column(String(60), ForeignKey("estados.NombreEstado"))
    Responsable = Column(String(60), ForeignKey("usuarios.Nombre"))
    FechaCreacion = Column(String(60))

    def __init__(self, Titulo, Descripcion, Estado, Responsable, FechaCreacion):
        self.Titulo = Titulo
        self.Descripcion = Descripcion
        self.Estado = Estado
        self.Responsable = Responsable
        self.FechaCreacion = FechaCreacion

    def __repr__(self):
        return f'{self.id}, {self.Titulo}, {self.Descripcion}, {self.Estado}, {self.Responsable}, {self.FechaCreacion}'

TrabajoFinalDB.Base.metadata.create_all(TrabajoFinalDB.engine)
