class Entita:
    def __init__(
                self,
                nome:str,
                colore:str,
                vita_massima:int,
                AGILITA:int,
                POSSIBILITA_CRIT:int,
                POTENZA_MAGIE:int,
                DIFESA:int,
                lista_set:list
    ):
        self._nome = nome#
        self._colore = colore#
        self._vita_massima = vita_massima#
        self._vita = vita_massima#
        self.AGILITA = AGILITA
        self.POSSIBILITA_CRIT = POSSIBILITA_CRIT
        self.POTENZA_MAGIE = POTENZA_MAGIE
        self.DIFESA = DIFESA
        self._lista_set = lista_set#
        
        self.atterato = False
        self.one_more = False
        self._statistiche_momentanee = (0,0,0)# (ATK,DEF,AGI)
        self._set_in_uso = self._lista_set[0] #assegna di base come set in uso il prima nella lista
    
    def cambia_set(self,set_da_verificare):
        #self,nome:str, livello:int, tipo:str, ad_area:bool, consuma_sp:bool, quanto_richiede:int
        for set in self._lista_set:
            set_valido = False #debug
            if set._lista_magie == set_da_verificare._lista_magie and set._debolezze == set_da_verificare._debolezze and set._cosa_annulla == set_da_verificare._cosa_annulla:
                #allora il set è presente
                set_valido = True #debug
                self._set_in_uso = set_da_verificare
                break
            return set_valido #debug
        
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
    def statistiche_momentanee(self):
        return self._statistiche_momentanee
    @statistiche_momentanee.setter
    def statistiche_momentanee(self,statistiche_momentanee_da_assegnare):
        if type(statistiche_momentanee_da_assegnare) == tuple and len(statistiche_momentanee_da_assegnare) == 3:
            self._statistiche_momentanee = statistiche_momentanee_da_assegnare

    @property
    def lista_set(self):
        return self._lista_set
    @lista_set.setter
    def lista_set(self,lista_set_da_assegnare):
        if type(lista_set_da_assegnare) == list and len(lista_set_da_assegnare) > 0:
            self._lista_set = lista_set_da_assegnare
    

class Alleato(Entita):
    pass


class Nemico(Entita):
    pass


class lista_set:
    pass


class Magia:
    pass


