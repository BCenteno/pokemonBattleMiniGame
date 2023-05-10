import random

class Pokemon:
    salud_ = 100
    salud = salud_
    def __init__(self,nombre,tipo,ataque1,ataque2,efectividad,sonido):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque1 = ataque1
        self.ataque2 = ataque2
        self.rango_ataque1 = (18,25)
        self.rango_ataque2 = (10,35)
        self.efectividad = efectividad
        self.sonido = sonido

    def dar_ventaja(self):
        self.rango_ataque2 = (20,40)
        self.efectividad = '¡El ataque es muy efectivo!\n'

    def dar_desventaja(self):
        self.rango_ataque2 = (5,25)
        self.efectividad = 'No es muy efectivo...\n'

    def dar_neutro(self):
        self.rango_ataque2 = (10,35)
        self.efectividad = ''

    def atacar(self, other, eleccion, auto=False):
        
        if eleccion == 1:
            a1,a2=self.rango_ataque1
            puntos_de_ataque = random.randint(a1, a2)
        elif eleccion == 2:
            a1,a2=self.rango_ataque2
            puntos_de_ataque = a1 if auto else random.randint(a1, a2)
        else:
            print("Movimiento inválido, perdés el turno")
            puntos_de_ataque = 0
        other.salud = max(0,other.salud - puntos_de_ataque)
        return puntos_de_ataque

#DEFINO CURAR
    def curar(self):
        puntos_de_curacion = random.randint(18, 35)
        self.salud = min(self.salud_, self.salud + puntos_de_curacion)
        return puntos_de_curacion