from funciones import *

def test_sonido_entrenador():
    p1= geodude
    at=2
    res=sonido_entrenador(p1,at)
    assert res, 'no se reprodujo sonido entrenador'

def test_sonido_rival():
    p2=charmander
    at=1
    res=sonido_rival(p2,at)
    assert res, 'no se reprodujo sonidorival'

def test_playsoundfile():
    #path='C:\\code\\pokemongame\\sounds\\placaje.mp3'
    path='C:\code\pokemongame\sounds\placaje.mp3'
    playsound(path)