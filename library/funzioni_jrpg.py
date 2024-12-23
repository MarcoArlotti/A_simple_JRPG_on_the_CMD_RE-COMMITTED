import os

class Entita:
    def __init__(
                self,
                NOME:str,
                COLORE:str,
                vita_massima:int,
                AGILITA:int,
                POSSIBILITA_CRIT:int,
                potenza_magie:int,
                DIFESA:int,
                lista_set:list
    ):
        self.NOME = NOME
        self.COLORE = COLORE
        self._vita_massima = vita_massima#
        self._vita = vita_massima#
        self.AGILITA = AGILITA
        self.POSSIBILITA_CRIT = POSSIBILITA_CRIT
        self._potenza_magie = potenza_magie
        self.DIFESA = DIFESA
        self._lista_set = lista_set#
        
        self.atterato = False
        self.one_more = False
        self._statistiche_momentanee = (0,0,0)# (ATK,DEF,AGI)
        self._set_in_uso = self._lista_set[0] #assegna di base il primo set nella lista, preso dalla lista dei set
    
    def cambia_set(self,set_da_verificare):
        """
        questa funzione si occupa di verificare se
        il set dato in input
        sia presente nella lista dei set,
        se è presente lo imposta come set in uso
        """
        set_valido = False 
        for set in self._lista_set:
            
            if set._lista_magie == set_da_verificare._lista_magie and set._debolezze == set_da_verificare._debolezze and set._cosa_annulla == set_da_verificare._cosa_annulla:
                #allora il set è presente
                set_valido = True #ho trovato il set
                self._set_in_uso = set_da_verificare
                break
        if set_valido == False: #controllo se ha trovato il set
            raise ValueError("ERRORE SET MAGIE NON TROVATO")
        
    @property
    def vita_massima(self):
        return self._vita_massima
    @vita_massima.setter
    def vita_massima(self,vita_massima_da_assegnare:int):
        if type(vita_massima_da_assegnare) == int:
            self._vita_massima = vita_massima_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNAZIONE DELLA VITA MASSIMA")

    @property
    def vita(self):
        return self._vita
    @vita.setter
    def vita(self,vita_da_assegnare:int):
        if type(vita_da_assegnare) == int and vita_da_assegnare <= self._vita_massima:
            self._vita = vita_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNAZIONE DELLA VITA")

    @property
    def statistiche_momentanee(self):
        return self._statistiche_momentanee
    @statistiche_momentanee.setter
    def statistiche_momentanee(self,statistiche_momentanee_da_assegnare):
        if type(statistiche_momentanee_da_assegnare) == tuple and len(statistiche_momentanee_da_assegnare) == 3:
            self._statistiche_momentanee = statistiche_momentanee_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNAZIONE DELLE STAT. MOMENT.")

    @property
    def lista_set(self):
        return self._lista_set
    @lista_set.setter
    def lista_set(self,lista_set_da_assegnare):
        if type(lista_set_da_assegnare) == list and len(lista_set_da_assegnare) > 0:
            self._lista_set = lista_set_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNAZIONE DELLA LISTA_SET")
    
    @property
    def potenza_magie(self):
        return self._potenza_magie
    @potenza_magie.setter
    def potenza_magie(self,potenza_magie_da_assegnare):
        if type(potenza_magie_da_assegnare) == float: #se float converti a int
            potenza_magie_da_assegnare = int(potenza_magie_da_assegnare)

        if type(potenza_magie_da_assegnare) == int:
            self._potenza_magie = potenza_magie_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNARE LA POTENZA MAGIE")
        
class Alleato(Entita):
    def __init__(
                self,
                NOME:str,
                COLORE:str,
                vita_massima:int,
                AGILITA:int,
                POSSIBILITA_CRIT:int,
                potenza_magie:int,
                DIFESA:int,
                lista_set:list,
                sp_massimi:int,
    ):
        super().__init__(NOME, 
                        COLORE,
                        vita_massima,
                        AGILITA,
                        POSSIBILITA_CRIT,
                        potenza_magie,
                        DIFESA,
                        lista_set)

        self._sp_massimi = sp_massimi#
        self._sp = sp_massimi#
        self._exp = float(0)#
        self.livello = int(0)
        self._exp_per_livellare = float(10)#
    
    def aumenta_statistiche_se_livellato(self):
        rifai_while = True #in caso si ha abbastanza exp per livellare più di una volta di fila
        ha_livellato = 0 #quanti livelli ha livellato il giocatore
        
        while rifai_while:
            rifai_while = False
            if self._exp >= self._exp_per_livellare: #controllo se si ha abbastanza exp per livellare
                self.livello += 1 #aumenta livello
                ha_livellato += 1
                self._exp = self._exp - self.exp_per_livellare #riduci l'exp dopo aver livellato

                self._exp_per_livellare = self._exp_per_livellare * 1.6 #aumenta quanto necessita livellare

                #aumento statistiche
                self._vita_massima = self._vita_massima * 1.1
                self._sp_massimi = self._sp_massimi * 1.3
                self._vita_massima = self._vita_massima * 1.1
                self._vita_massima = self._sp_massimi * 1.3 
                self._potenza_magie = self._potenza_magie * 1.2
        return ha_livellato

            
    @property
    def sp_massimi(self):
        return self._sp_massimi
    @sp_massimi.setter
    def sp_massimi(self,sp_massimi_da_assegnare:int):
        if type(sp_massimi_da_assegnare) == int:
            self._sp_massimi = sp_massimi_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNAZIONE DELL'sp_massimi")

    @property
    def sp(self):
        return self._sp
    @sp.setter
    def sp(self,sp_da_assegnare:int):
        if type(sp_da_assegnare) == int and sp_da_assegnare <= self._sp_massimi:
            self._sp = sp_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNAZIONE DELL'SP")

    @property
    def exp(self):
        return self._exp
    @exp.setter
    def exp(self,exp_da_assegnare):
        if type(exp_da_assegnare) == float:
            self._exp = exp_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNARE L'EXP")
    
    @property
    def exp_per_livellare(self):
        return self._exp_per_livellare
    @exp_per_livellare.setter
    def exp_per_livellare(self,exp_per_livellare_da_assegnare):
        if type(exp_per_livellare_da_assegnare) == float:
            self._exp_per_livellare = exp_per_livellare_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNARE GLI EXP PER LIVELLARE")

    
class Nemico(Entita): 
    def __init__(self, NOME, COLORE, vita_massima, AGILITA, POSSIBILITA_CRIT, potenza_magie, DIFESA, lista_set,DROP,EXP):
        super().__init__(NOME, COLORE, vita_massima, AGILITA, POSSIBILITA_CRIT, potenza_magie, DIFESA, lista_set)

        self.DROP = DROP #lista dei possibili drop di un nemico
        self.EXP = EXP #exp che guadagnerà il giocatore
    

class lista_set: #TODO
    pass

class Set_magia: #TODO
    pass


class Magia: #TODO
    def __init__(self,
                NOME:str,
                livello:int,#
                TIPO:str,
                ad_area:bool,#
                CONSUMA_SP:bool,
                quanta_sp_o_hp_richiede:int#
    ):
        self.NOME = NOME
        self._livello = livello
        self.TIPO = TIPO
        self._ad_area = ad_area
        self.CONSUMA_SP = CONSUMA_SP
        self._quanta_sp_o_hp_richiede = quanta_sp_o_hp_richiede

    @property
    def livello(self):
        return self._livello
    @livello.setter
    def livello(self,livello_da_assegnare):
        if type(livello_da_assegnare) == int and livello_da_assegnare > self._livello:
            self._livello = livello_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNARE IL LIVELLO")


    @property
    def ad_area(self):
        return self._ad_area
    @ad_area.setter
    def ad_area(self,ad_area_da_assegnare):
        if type(ad_area_da_assegnare) == bool:
            self._ad_area = ad_area_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNARE ad_area")


    @property
    def quanta_sp_o_hp_richiede(self):
        return self._quanta_sp_o_hp_richiede
    @quanta_sp_o_hp_richiede.setter
    def quanta_sp_o_hp_richiede(self,quanta_sp_o_hp_richiede_da_assegnare):
        if type(quanta_sp_o_hp_richiede_da_assegnare) == int:
            self._quanta_sp_o_hp_richiede = quanta_sp_o_hp_richiede_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNARE quanta_sp_o_hp_richiede")

def calcola_exp(alleato,nemico):
    alleato._exp = alleato._exp + nemico.EXP
    ha_livellato = alleato.aumenta_statistiche_se_livellato()

def assegna_drop(alleato,nemico): #TODO
    pass