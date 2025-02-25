from funzioni_jrpg import calcola_danno_fatto

def salta_turno(nemico):
    """
    l'effetto di questa magia
    fa saltare un turno a un o più avversari
    """
    nemico.salta_il_tuo_prossimo_turno = True

def attacco_2_turni(magia_scelta,giocatore,nemico):
    """
    questa magia fa un danno maggiore
    ma a discapito di saltare il prossimo turno,
    questo attacco è di tipo "speciale"
    """
    giocatore.salta_il_tuo_prossimo_turno = True
    danno = calcola_danno_fatto(magia_scelta,nemico)
    danno = int(danno * 2.2) #aumento manuale del danno, TODO verificare che sia bilanciato il moltiplicatore messo
    return danno

def rage_drive(giocatore,nemico): #TODO SE LA MAGIA è UTILIZZABILE, RENDERE VISIBILE CON DEI COLORI NELLA CUI
    """
    questa magia può essere usata una sola volta per battaglia,
    in più aumenta l'attacco
    """
    giocatore.aumenta_ATK()
    #TODO

def rage_art(giocatore,nemico): #TODO SE LA MAGIA è UTILIZZABILE, RENDERE VISIBILE CON DEI COLORI NELLA CUI
    """
    identica al rage drive,
    ma la si sblocca solo dopo che il giocatore rimane con il 15% di vita,
    se il suddetto giocatore si cura la magia svanirà,
    ma non verrà consumata nel processo,

    la magia fà più danno del rage drive,
    ma non da effetti al giocatore

    (valore che cambia in base alla vita max)  
    """
    giocatore.aumenta_ATK()
    #TODO