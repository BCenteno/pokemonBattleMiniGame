from logging import exception
from pytest_bdd import given,when,then,parsers
from clases import *
from lista_pokemon import *

# Given i select the pokemon chikorita
# And rival select the pokemon pineco
# When my pokemon has 100 salud
# And rival pokemon has 100 salud
# And my pokemon executes atacar
# Then rival pokemon has less than 100 salud

@given(parsers.parse('i select the pokemon {pokemon1}'))
def selectPokemon(pokemon1):
    global p1
    match pokemon1:
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
            raise Exception(f'no existe el pokemon {pokemon1}')

@when(parsers.parse('rival select the {pokemon2}'))
def selectPokemon(pokemon2):
    global p2
    match pokemon2:
        case 'bulbasaur':
            p2=bulbasaur
        case 'squirtle':
            p2=squirtle
        case 'charmander':
            p2=charmander
        case 'chikorita':
            p2=chikorita
        case 'totodile':
            p2=totodile
        case 'cyndaquil':
            p2=cyndaquil
        case 'pikachu':
            p2=pikachu
        case 'elekid':
            p2=elekid
        case 'pineco':
            p2=pineco
        case 'wurmple':
            p2=wurmple
        case 'sudowoodo':
            p2=sudowoodo
        case 'geodude':
            p2=geodude
        case _:
            raise Exception(f'no existe el pokemon {pokemon2}')

@when(parsers.parse('my pokemon has {salud} salud'))
def setSalud(salud):
    global p1
    p1.salud=int(salud)

@when(parsers.parse('rival pokemon has {salud} salud'))
def setSalud(salud):
    global p2
    p2.salud=int(salud)

@when('my pokemon executes atacar {tipoataque}')
def attackPokemon(tipoataque):
    global p1
    global p2
    p1.atacar(p2,tipoataque)

@then(parsers.parse('rival pokemon has less than {salud} salud'))
def finalSalud(salud):
    global p2
    assert p2.salud < int(salud), 'error al atacar'
