def salta_turno(nemico):
    """
    l'effetto di questa magia
    fa saltare un turno a un o più avversari
    """
    nemico.salta_il_tuo_prossimo_turno = True

def attacco_2_turni(giocatore,nemico):
    """
    questa magia fa un danno maggiore
    ma a discapito di saltare un turno successivamente
    """
    giocatore.salta_il_tuo_prossimo_turno = True

def rage_drive(): #TODO
    """
    questa magia può essere usata una sola volta per battaglia,
    in più aumenta l'attacco

    """
    pass

def rage_art(): #TODO
    """
    identica al rage drive,
    ma la si sblocca solo dopo che il giocatore rimane con il 15% di vita,
    se il suddetto giocatore si cura la magia svanirà,
    ma non verrà consumata nel processo,

    la magia fà più danno del rage drive,
    ma non da effetti al giocatore

    (valore che cambia in base alla vita max)  
    """
    pass