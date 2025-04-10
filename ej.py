import time
import random

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []
        self.buffer = [] 
    
    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)
    
    def eliminar_conexion(self, tiempo):
        eliminar = random.randrange(0, 2)
        if tiempo > 4 and eliminar < len(self.conexiones):
            nodo_eliminado = self.conexiones.pop(eliminar)
            print(f"{self.nombre} eliminó la conexión con {nodo_eliminado.nombre}")
    
    def enviar_mensaje(self, mensaje, tiempo):
        print(f"{self.nombre} enviando mensaje: '{mensaje}'")
        for nodo in self.conexiones:
            time.sleep(tiempo)
            nodo.recibir_mensaje(mensaje, self.nombre)
    
    def recibir_mensaje(self, mensaje, remitente):
        if len(self.buffer) >= 5:
            print(f"{self.nombre} tiene el buffer lleno. Posible congestión. Mensaje de {remitente} descartado.")
            return
        print(f"{self.nombre} recibió mensaje de {remitente}, almacenado en buffer.")
        self.buffer.append((mensaje, remitente))
    
    def procesar_buffer(self):
        print(f"\n{self.nombre} procesando mensajes en el buffer...")
        while self.buffer:
            indice = 0 
            mensaje, remitente = self.buffer.pop(indice)
            
            if random.random() < 0.3:
                print(f"✖ {self.nombre} perdió el mensaje de {remitente}: '{mensaje}' (simulación de pérdida)")
            else:
                print(f"✔ {self.nombre} procesó correctamente el mensaje de {remitente}: '{mensaje}'")
        print(f"{self.nombre} ha terminado de procesar el buffer.\n")

servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")
tiempo = random.randrange(0, 6)
servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)
print("hola de nuevo a todos\n")
servidor.enviar_mensaje("Mensaje importante", tiempo)
for i in range(7):
    cliente1.recibir_mensaje(f"Mensaje #{i+1}", "Servidor")

cliente1.procesar_buffer()
