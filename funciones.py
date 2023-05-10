from lista_pokemon import*
from playsound import playsound

def turno(entrenador,rival,auto=False):

    if auto: 
        eleccion_movimiento = 2
        rival_eleccion_movimiento = 2
    else:
        print(f"\nELEGÍ TU MOVIMIENTO\n1- {entrenador.ataque1}\n2- {entrenador.ataque2}\n3- CURARSE")
        eleccion_movimiento = int(input("\nElegí tu movimiento: "))
        rival_eleccion_movimiento = random.randint(1, 2 if rival.salud == 100 else 3)
    

    if eleccion_movimiento == 1:
        print(f"Elegiste {entrenador.ataque1}. Tu {entrenador.nombre} causa un daño de {entrenador.atacar(rival, eleccion_movimiento)} puntos.")
        sonido_entrenador(entrenador,eleccion_movimiento,auto)
    if eleccion_movimiento == 2:
        print(f"Elegiste {entrenador.ataque2}. Tu {entrenador.nombre} causa un daño de {entrenador.atacar(rival, eleccion_movimiento, auto)} puntos.")
        print(entrenador.efectividad)
        sonido_entrenador(entrenador,eleccion_movimiento,auto)

    if rival_eleccion_movimiento == 1:
        print(f"{rival.nombre} eligió {rival.ataque1}. {rival.nombre} te causa un daño de {rival.atacar(entrenador, rival_eleccion_movimiento)} puntos.")
        sonido_rival(rival,rival_eleccion_movimiento,auto)
    if rival_eleccion_movimiento == 2:
        print(f"{rival.nombre} eligió {rival.ataque2}. {rival.nombre} te causa un daño de {rival.atacar(entrenador, rival_eleccion_movimiento, auto)} puntos.")
        print(rival.efectividad)
        sonido_rival(rival,rival_eleccion_movimiento,auto)

    if eleccion_movimiento == 3:
        print(f"Tu {entrenador.nombre} eligió CURARSE y restauró {entrenador.curar()} puntos de salud.")
        sonido_entrenador(entrenador,eleccion_movimiento,auto)
    if rival_eleccion_movimiento == 3:
        print(f"Tu {rival.nombre} eligió CURARSE y restauró {rival.curar()} puntos de salud.")
        sonido_rival(rival,rival_eleccion_movimiento,auto)
    resultado_turno(entrenador, rival)

    return entrenador, rival

def resultado_turno(entrenador,rival):
    print(f"La salud de tu {entrenador.nombre} es de {entrenador.salud} puntos")
    print(f"La salud de {rival.nombre} es de {rival.salud} puntos")

def batalla(entrenador,rival,auto=False):

    print(f'{entrenador.nombre} VS {rival.nombre}')
    asignar_ventajas(entrenador,rival)
    while entrenador.salud > 0 and rival.salud > 0:
        turno(entrenador,rival,auto)
    entrenador.dar_neutro()
    rival.dar_neutro()
    return entrenador, rival

def asignar_ventajas(entrenador,rival):
    match entrenador.tipo:
        case 'fuego':
            if rival.tipo in ['planta','bicho']:
                entrenador.dar_ventaja()
                rival.dar_desventaja()
            if rival.tipo in ['agua','roca']:
                rival.dar_ventaja()
                entrenador.dar_desventaja()

        case 'planta':
            if rival.tipo in ['agua','roca']:
                entrenador.dar_ventaja()
            if rival.tipo == 'agua':
                rival.dar_desventaja()
            if rival.tipo in ['fuego','bicho']:
                rival.dar_ventaja()
                entrenador.dar_desventaja()

        case 'agua':
            if rival.tipo in ['fuego','roca']:
                entrenador.dar_ventaja()
            if rival.tipo == 'fuego':
                rival.dar_desventaja()
            if rival.tipo in ['planta','electrico']:
                rival.dar_ventaja()
                entrenador.dar_desventaja()

        case 'electrico':
            if rival.tipo in ['agua']:
                entrenador.dar_ventaja()
            if rival.tipo == 'planta':
                entrenador.dar_desventaja()

        case 'bicho':
            if rival.tipo in ['planta']:
                entrenador.dar_ventaja()
                rival.dar_desventaja()
            if rival.tipo in ['fuego','roca']:
                rival.dar_ventaja()
            if rival.tipo == 'fuego':
                entrenador.dar_desventaja()

        case 'roca':
            if rival.tipo in ['fuego','bicho']:
                entrenador.dar_ventaja()
            if rival.tipo is 'fuego':
                rival.dar_desventaja()
            if rival.tipo in ['planta','agua']:
                rival.dar_ventaja()

def elegir_pokemon(auto=False):
    if auto:
        nu=random.randint(1, 6)
    else:
        print(f'\nELEGÍ UN POKEMON\n1- {entrenador_pkm[0].nombre}({entrenador_pkm[0].salud})\n2- {entrenador_pkm[1].nombre}({entrenador_pkm[1].salud})\n3- {entrenador_pkm[2].nombre}({entrenador_pkm[2].salud})\n4- {entrenador_pkm[3].nombre}({entrenador_pkm[3].salud})\n5- {entrenador_pkm[4].nombre}({entrenador_pkm[4].salud})\n6- {entrenador_pkm[5].nombre}({entrenador_pkm[5].salud})')
        nu = int(input("\nELEGÍ UN POKEMON: "))
    return entrenador_pkm[nu-1]

def elegir_pokemon_rival():
    lmay15=[pkm for pkm in rival_pkm if pkm.salud>15]
    c=len(lmay15)
    if c > 0:
        nr = random.randint(1, c)
        return lmay15[nr-1]
    else:
        nr = random.randint(1, 6)
        return rival_pkm[nr-1]

def ronda():
    entrenador= elegir_pokemon()
    print(f'Elegiste a {entrenador.nombre}')
    playsound(entrenador.sonido)
    rival = elegir_pokemon_rival()
    print(f'Tu rival eligió a {rival.nombre}')
    playsound(rival.sonido)
    batalla(entrenador,rival)
    print('\n')
    print(f"Tu salud final es {entrenador.salud}")
    print(f"La salud final de {rival.nombre} es {rival.salud}")

    if entrenador.salud < rival.salud:
        print("\n¡Perdiste!") 
    if entrenador.salud == rival.salud:
        print("\n¡Empate!")
    if entrenador.salud > rival.salud:
        print(f"\n¡Le ganaste a {rival.nombre}!")

    return entrenador, rival

def contador(p_entrenador,p_rival,entrenador,rival):
    if entrenador.salud == rival.salud:
        pass
    else:
        if entrenador.salud > rival.salud:
            p_entrenador += 1
        else:
            p_rival += 1
    return p_entrenador,p_rival

def torneo():
    p_entrenador=0
    p_rival=0

    print('-----------INICIA LA PRIMER BATALLA-----------')
    entrenador,rival=ronda()
    p_entrenador,p_rival=contador(p_entrenador,p_rival,entrenador,rival)
    print('----------FINALIZA LA PRIMER BATALLA----------')

    print('-----------INICIA LA SEGUNDA BATALLA----------')
    entrenador,rival=ronda()
    p_entrenador,p_rival=contador(p_entrenador,p_rival,entrenador,rival)
    print('----------FINALIZA LA SEGUNDA BATALLA---------')

    print('-----------INICIA LA TERCER BATALLA-----------')
    entrenador,rival=ronda()
    p_entrenador,p_rival=contador(p_entrenador,p_rival,entrenador,rival)
    print('\n\n')

    if p_entrenador == p_rival:
        print('¡Es un EMPATE!')
    if p_entrenador > p_rival:
        playsound('C:\\code\\pokemongame\\sounds\\win.mp3')
        print('¡GANASTE el torneo!')
    if p_entrenador < p_rival:
        playsound('C:\\code\\pokemongame\\sounds\\lose.wav')
        print('¡PERDISTE el torneo!')

def jugar_denuevo():
    jd = input('¿QUERÉS VOLVER A JUGAR? (Y/N)')
    if jd.upper() == 'Y':
        for lista in [entrenador_pkm,rival_pkm]:
            for poke in lista:
                poke.salud=100
        torneo()
    if jd.upper() == 'N':
        print('¡Hasta luego!')

def sonido_entrenador(entrenador,eleccion_movimiento,auto=False):
    if not auto:
        if eleccion_movimiento == 1:
            match entrenador.ataque1:
                    case 'PLACAJE':
                        path='C:\\code\\pokemongame\\sounds\\placaje.mp3'
                    case 'ARAÑAZO':
                        path='C:\\code\\pokemongame\\sounds\\aranazo.mp3'
                    case 'LÁTIGO':
                        path='C:\\code\\pokemongame\\sounds\\latigo.mp3'
                    case 'ATAQUE RÁPIDO':
                        path='C:\\code\\pokemongame\\sounds\\ataquerapido.mp3'
                    case 'ATIZAR':
                        path='C:\\code\\pokemongame\\sounds\\atizar.mp3'
        if eleccion_movimiento ==2:    
            match entrenador.ataque2:
                case 'LÁTIGO CEPA':
                    path='C:\\code\\pokemongame\\sounds\\latigocepa.mp3'
                case 'PISTOLA AGUA':
                    path='C:\\code\\pokemongame\\sounds\\pistoladeagua.mp3'
                case 'ASCUAS':
                    path='C:\\code\\pokemongame\\sounds\\ascuas.mp3'
                case 'HOJA AFILADA':
                    path='C:\\code\\pokemongame\\sounds\\hojaafilada.mp3'
                case 'IMPACTRUENO':
                    path='C:\\code\\pokemongame\\sounds\\impactrueno.mp3'
                case 'PICADURA':
                    path='C:\\code\\pokemongame\\sounds\\picadura.mp3'
                case 'LANZARROCAS':
                    path='C:\\code\\pokemongame\\sounds\\lanzarocas.mp3'
                case 'DESENROLLAR':
                    path='C:\\code\\pokemongame\\sounds\\desenrollar.mp3'
        if eleccion_movimiento ==3:
                path='C:\\code\\pokemongame\\sounds\\curar.wav'

        playsound(path)
        return playsound

def sonido_rival(rival,rival_eleccion_movimiento,auto=False):
    if not auto:
        if rival_eleccion_movimiento==1:
            match rival.ataque1:
                case 'PLACAJE':
                    path='C:\\code\\pokemongame\\sounds\\placaje.mp3'
                case 'ARAÑAZO':
                    path='C:\\code\\pokemongame\\sounds\\aranazo.mp3'
                case 'LÁTIGO':
                    path='C:\\code\\pokemongame\\sounds\\latigo.mp3'
                case 'ATAQUE RÁPIDO':
                    path='C:\\code\\pokemongame\\sounds\\ataquerapido.mp3'
                case 'ATIZAR':
                    path='C:\\code\\pokemongame\\sounds\\atizar.mp3'

        if rival_eleccion_movimiento==2:
                match rival.ataque2:
                    case 'LÁTIGO CEPA':
                        path='C:\\code\\pokemongame\\sounds\\latigocepa.mp3'
                    case 'PISTOLA AGUA':
                        path='C:\\code\\pokemongame\\sounds\\pistoladeagua.mp3'
                    case 'ASCUAS':
                        path='C:\\code\\pokemongame\\sounds\\ascuas.mp3'
                    case 'HOJA AFILADA':
                        path='C:\\code\\pokemongame\\sounds\\hojaafilada.mp3'
                    case 'IMPACTRUENO':
                        path='C:\\code\\pokemongame\\sounds\\impactrueno.mp3'
                    case 'PICADURA':
                        path='C:\\code\\pokemongame\\sounds\\picadura.mp3'
                    case 'LANZARROCAS':
                        path='C:\\code\\pokemongame\\sounds\\lanzarocas.mp3'
                    case 'DESENROLLAR':
                        path='C:\\code\\pokemongame\\sounds\\desenrollar.mp3'

        if rival_eleccion_movimiento==3:
                path='C:\\code\\pokemongame\\sounds\\curar.wav'

        playsound(path)
        return playsound
        
def game():
    torneo()
    jugar_denuevo()

