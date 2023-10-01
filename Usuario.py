class Usuario:

    def __init__ (self, carnet, nombre, apellido, mail, cel, carrera, semestre, birth, password):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido 
        self.mail = mail 
        self.cel = cel 
        self.carrera = carrera
        self.semestre = semestre 
        self.birth = birth
        self.password = password

    def getNombre (self):
        return self.nombre

    def getApellido (self):
        return self.apellido

    def getMail (self):
        return self.mail
    
    def getCel (self):
        return self.cel
    
    def getCarrera (self):
        return self.cel

    def getSemestre (self):
        return self.semestre

    def getBirth (self):
        return self.birth