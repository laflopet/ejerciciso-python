import sqlite3
from ClaseEstudiante import alumno

conn = sqlite3.connect('midocumento.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Alumnos (
    id INTEGER PRIMARY KEY NOT NULL,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL)""")

alum1 = alumno(111, 'Julian', 'Correa')
alum2 = alumno(222, 'Stefany', 'Mendoza')
alum3 = alumno(333, 'Juan', 'Madrigal')
alum4 = alumno(444, 'Andres', 'Perea')
alum5 = alumno(555, 'Fernando', 'El chando')
alum6 = alumno(666, 'Julieta', 'Caseres')
alum7 = alumno(777, 'Adriana', 'Correa')
alum8 = alumno(888, 'Marcial', 'Blanco')

manyAlumnos = [
    (alum1.id, alum1.nombre, alum1.apellido),
    (alum2.id, alum2.nombre, alum2.apellido),
    (alum3.id, alum3.nombre, alum3.apellido),
    (alum4.id, alum4.nombre, alum4.apellido),
    (alum5.id, alum5.nombre, alum5.apellido),
    (alum6.id, alum6.nombre, alum6.apellido),
    (alum7.id, alum7.nombre, alum7.apellido),
    (alum8.id, alum8.nombre, alum8.apellido)
]


c.executemany("INSERT INTO Alumnos VALUES (?, ?, ?)", manyAlumnos)
# c.execute("INSERT INTO Alumnos VALUES(111,'Roberto','Caseres')")

# def insertarEstudiantes(alumno):
#     c.execute("INSERT INTO Alumnos VALUES (?, ?, ?)",
#               (alumno.id, alumno.nombre, alumno.apellido))
#     conn.commit()
#
# insertarEstudiantes(alum1)

c.execute("SELECT * FROM Alumnos WHERE nombre=?", ('Julieta',))
alumnos = c.fetchall()
print(alumnos)

conn.close()
