from funciones import *

#--------------------TESTS VENTAJA--------------------

def test_fuegoVSplanta():
    p1=cyndaquil
    p2=bulbasaur
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud>p2.salud, 'error, p1 debería tener ventaja'

def test_fuegoVSbicho():
    p1=charmander
    p2=pineco
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud>p2.salud, 'error, p1 debería tener ventaja'
    
def test_plantaVSagua():
    p1=chikorita
    p2=totodile
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud>p2.salud, 'error, p1 debería tener ventaja'

def test_plantaVSroca():
    p1=bulbasaur
    p2=geodude
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud>p2.salud, 'error, p1 debería tener ventaja'

def test_aguaVSfuego():
    p1=squirtle
    p2=cyndaquil
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud>p2.salud, 'error, p1 debería tener ventaja'

def test_aguaVSroca():
    p1=totodile
    p2=sudowoodo
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud>p2.salud, 'error, p1 debería tener ventaja'

def test_electricoVSagua():
    p1=pikachu
    p2=squirtle
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud>p2.salud, 'error, p1 debería tener ventaja'

def test_bichoVSplanta():
    p1=wurmple
    p2=chikorita
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud>p2.salud, 'error, p1 debería tener ventaja'

def test_rocaVSfuego():
    p1=geodude
    p2=charmander
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud>p2.salud, 'error, p1 debería tener ventaja'

def test_rocaVSbicho():
    p1=sudowoodo
    p2=pineco
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud>p2.salud, 'error, p1 debería tener ventaja'

#--------------------TESTS DESVENTAJA--------------------

def test_fuegoVSagua():
    p1=charmander
    p2=squirtle
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud<p2.salud, 'error, p1 debería tener desventaja'

def test_fuegoVSroca():
    p1=cyndaquil
    p2=sudowoodo
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud<p2.salud, 'error, p1 debería tener desventaja'

def test_plantaVSfuego():
    p1=chikorita
    p2=charmander
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud<p2.salud, 'error, p1 debería tener desventaja'

def test_plantaVSbicho():
    p1=bulbasaur
    p2=pineco
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud<p2.salud, 'error, p1 debería tener desventaja'

def test_aguaVSplanta():
    p1=totodile
    p2=chikorita
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud<p2.salud, 'error, p1 debería tener desventaja'

def test_bichoVSfuego():
    p1=wurmple
    p2=charmander
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud<p2.salud, 'error, p1 debería tener desventaja'

def test_electricoVSplanta():
    p1=pikachu
    p2=bulbasaur
    p1.salud=100
    p2.salud=100
    batalla(p1,p2,auto=True)
    assert p1.salud<p2.salud, 'error, p1 debería tener desventaja'
