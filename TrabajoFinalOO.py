import TrabajoFinalDB
from sqlalchemy import Column, String, Integer

class Tarea(TrabajoFinalDB.Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True)
    Titulo = Column(String(60))
    Descripcion = Column(String(255))
    Estado = Column(String(60))
    Responsable = Column(String(60))
    FechaCreacion = Column(String(60))

    def __init__(self, Titulo, Descripcion, Estado, Responsable, FechaCreacion):
        self.Titulo = Titulo.lower
        self.Descripcion = Descripcion
        self.Estado = Estado
        self.Responsable = Responsable
        self.FechaCreacion = FechaCreacion

    def __repr__(self):
        return f'{self.id}, {self.Titulo}, {self.Descripcion}, {self.Estado}, {self.Responsable}, {self.FechaCreacion}'

TrabajoFinalDB.Base.metadata.create_all(TrabajoFinalDB.engine)

class Usuario(TrabajoFinalDB.Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    Nombre = Column(String(60))
    Apellidos = Column(String(60))
    Correo = Column(String(60))
    
    def __init__(self, Titulo, Descripcion, Estado, Responsable, FechaCreacion):
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Correo = Correo

    def __repr__(self):
        return f'{self.id}, {self.nombre}, {self.Apellidos}, {self.Correo}'

TrabajoFinalDB.Base.metadata.create_all(TrabajoFinalDB.engine)

class Estado(TrabajoFinalDB.Base):
    __tablename__ = "estados"

    id = Column(Integer, primary_key=True)
    Estado = Column(String(60))
    Descripcion = Column(String(255))
    
    def __init__(self, Estado, Descripcion):
        self.Titulo = Estado
        self.Descripcion = Descripcion

    def __repr__(self):
        return f'{self.id}, {self.Estado}, {self.Descripcion}'

TrabajoFinalDB.Base.metadata.create_all(TrabajoFinalDB.engine)
