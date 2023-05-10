from logging import exception
from pytest_bdd import given,when,then,parsers 
from clases import *
from lista_pokemon import *

# Feature:curacion
# Scenario: 1.damaged pokemon gets healed
# Given i select the pokemon bulbasaur
# When my pokemon has 50 salud
# When my pokemon executes curar
# Then my pokemon has more than 50 salud

p1=bulbasaur

@given(parsers.parse('i select the pokemon {pokemon}'))
def selectPokemon(pokemon):
    global p1
    match pokemon:
        case 'bulbasaur':
            p1=bulbasaur
        case 'squirtle':
            p1=squirtle
        case 'charmander':
            p1=charmander
        case 'chikorita':
            p1=chikorita
        case 'totodile':
            p1=totodile
        case 'cyndaquil':
            p1=cyndaquil
        case 'pikachu':
            p1=pikachu
        case 'elekid':
            p1=elekid
        case 'pineco':
            p1=pineco
        case 'wurmple':
            p1=wurmple
        case 'sudowoodo':
            p1=sudowoodo
        case 'geodude':
            p1=geodude
        case _:
            raise Exception(f'no existe el pokemon {pokemon}')

@when(parsers.parse('my pokemon has {salud} salud'))
def setSalud(salud):
    global p1
    p1.salud=int(salud)

@when('my pokemon executes curar')
def healPokemon():
    global p1
    p1.curar()

@then(parsers.parse('my pokemon has more than {salud} salud'))
def finalSalud(salud):
    global p1
    assert int(salud) < p1.salud, 'error al curar'

