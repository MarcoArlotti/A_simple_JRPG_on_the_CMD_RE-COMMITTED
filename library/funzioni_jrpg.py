class Entita:
    def __init__(
                self,
                nome:str,
                colore:str,
                vita_massima:int,
                vita:int,
                AGILITA:int,
                POSSIBILITA_CRIT:int,
                POTENZA_MAGIE:int,
                DIFESA:int,
                set_magie:list
    ):
        self._nome = nome
        self._colore = colore
        self._vita_massima = vita_massima
        self._vita = vita
        self.AGILITA = AGILITA
        self.POSSIBILITA_CRIT = POSSIBILITA_CRIT
        self.POTENZA_MAGIE = POTENZA_MAGIE
        self.DIFESA = DIFESA
        self._set_magie = set_magie
        
        self.atterato = False
        self.one_more = False
        self._statistiche_momentanee = (0,0,0)#(ATK,DEF,AGI)
        self._set_in_uso = self._lista_set_magie[0] #assegna di base come set in uso il prima nella lista
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome_da_assegnare:str):
        if type(nome_da_assegnare) == str and len(nome_da_assegnare) <= 9: 
            self._nome = nome_da_assegnare

    @property
    def colore(self):
        return self._colore
    @colore.setter
    def colore(self,colore_da_assegnare:str):
        if type(colore_da_assegnare) == str:
            self._colore = colore_da_assegnare
    
    @property
    def vita_massima(self):
        return self._vita_massima
    @vita_massima.setter
    def vita_massima(self,vita_massima_da_assegnare:int):
        if type(vita_massima_da_assegnare) == int:
            self._vita_massima = vita_massima_da_assegnare

    @property
    def vita(self):
        return self._vita
    @vita.setter
    def vita(self,vita_da_assegnare:int):
        if type(vita_da_assegnare) == int and vita_da_assegnare <= self._vita_massima:
            self._vita = vita_da_assegnare
    
    @property
    def set_magie(self):
        return self._set_magie
    @set_magie.setter
    def set_magie(self,set_magie_da_assegnare:list):
        if type(set_magie_da_assegnare) == list and len(set_magie_da_assegnare) > 0:


class Alleato(Entita):
    pass


class Nemico(Entita):
    pass


class Set_magie:
    pass


class Magia:
    pass


