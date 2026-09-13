class SolicitudMatricula:
  def __init__(self,documento,nombre,programa,valor):
      self.documento = documento
      self.nombre = nombre
      self.programa = programa
      self.valor = valor

class ColaProcesamientoMatricula:
  def __init__(self,capacidad):
    self.capacidad = capacidad
    self.datos = [None] * capacidad
    self.frente = 0
    self.tamano = 0

  def esta_vacia(self):
    if self.tamano ==0:
        return True
    else:
        return False

  def esta_llena(self):
    if self.tamano == self.capacidad:
        return True
    else:
        return False

  def encolar (self,solicitud):
      if self.esta_llena() ==True:
        print("SERVIDOR OCUPADO: No se pudo procesar a" + solicitud.nombre)
        return False

      posicion = (self.frente + self.tamano) % self.capacidad
      self.datos[posicion] = solicitud
      self.tamano = self.tamano + 1
      print("INGRESO EXITOSO: " + solicitud.nombre + " entro a la cola ")
      return True

  def desencolar(self):
      if self.esta_vacia() == True:
        print ("ADVERTENCIA: no hay solicitudes pendientes.")
        return None

      solicitud_procesada = self.datos [self.frente]
      self.datos[self.frente] = None
      self.frente = (self.frente + 1) % self.capacidad
      self.tamano = self.tamano - 1

      print("LIQUIDACION GENERADA: Estudiante " + solicitud_procesada.nombre +" - Documento: " + solicitud_procesada.documento)
      return solicitud_procesada

if __name__ == "__main__":
      print("SERVIDOR DE MATRICULAS")

      servidor_matriculas = ColaProcesamientoMatricula(3)

      print("\nPRUEBA COLA VACIA")
      servidor_matriculas.desencolar()

      print("\nINGRESO DE ESTUDIANTES")
      est1 = SolicitudMatricula ("1090436483", "Dhayanna Ortega", "Ingenieria de sistemas", 2500000)
      est2 = SolicitudMatricula ("1090569854", "Carolina Ortiz", "Administracion de empresas", 2100000)
      est3 = SolicitudMatricula ("1005112233", "Pedro Perez", "Fisioterapia", 2800000)

      servidor_matriculas.encolar (est1)
      servidor_matriculas.encolar (est2)
      servidor_matriculas.encolar (est3)

      print("\nPRUEBA SERVIDOR LLENO")
      est4 = SolicitudMatricula ("1090654385", " Martha Camacho", "Contaduria publica", 1800000)
      servidor_matriculas.encolar (est4)

      print("\nPROCESAR Y GENERAR LIQUIDACION")
      servidor_matriculas.desencolar ()

      print("\nREUTILIZAR ESPACIO EN COLA")
      servidor_matriculas.encolar (est4)

      print("\nVACIAR LA COLA")
      while servidor_matriculas.esta_vacia () == False:
          servidor_matriculas.desencolar()
      
    
        
