from funciones import *

def test_atacar():
    p1=bulbasaur
    p2=chikorita
    vida_previa=p2.salud
    p1.atacar(p2,1)
    vida_posterior=p2.salud
    assert vida_previa > vida_posterior, 'error al hacer daño'

def test_curar():
    p1=bulbasaur
    p1.salud=50
    vida_previa=p1.salud
    p1.curar()
    vida_posterior=p1.salud
    assert vida_previa < vida_posterior, 'error al curar'

def test_turno():
    p1=bulbasaur
    p2=chikorita
    p1.salud=100
    p2.salud=100
    vida_previa=p1.salud,p2.salud
    turno(p1,p2,auto=True)
    vida_posterior=p1.salud,p2.salud
    assert vida_previa > vida_posterior, 'errir al finalizar turno neutro'

def test_batalla():
    p1=charmander
    p2=chikorita
    p1.salud=100
    p2.salud=100
    batalla(p1,p2, auto=True)
    un_pokemon_murio=p1.salud==0 or p2.salud==0
    assert un_pokemon_murio, 'error al batalla'

def test_contador():
    p_entrenador=0
    p_rival=0
    p1=cyndaquil
    p2=bulbasaur
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    p_entrenador,p_rival=contador(p_entrenador,p_rival,p1,p2)
    print(p_entrenador,p_rival)
    assert p_entrenador > p_rival, 'error'

def test_asignar_ventajas():
    p1=bulbasaur
    p2=geodude
    asignar_ventajas(p1,p2)
    a1,a2=p1.rango_ataque2
    b1,b2=p2.rango_ataque2
    assert (a1,a2)>(b1,b2), 'error, no se asigno ventaja'

