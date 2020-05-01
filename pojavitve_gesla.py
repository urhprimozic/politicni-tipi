def pojavitve_besede(besedilo, geslo: str) -> int:
    '''Poda število pojavitev gesla v danem besedilu, vključno s sklanjatvami.'''
    besede = besedilo.split()
    stevec = 0
    if geslo[-1].lower() in 'aeiou': #pri sklanjanju se končni samoglasnik pogosto izgubi
        geslo = geslo[:-1]
    for beseda in besede:
        if geslo in beseda:
            stevec += 1
    return stevec
