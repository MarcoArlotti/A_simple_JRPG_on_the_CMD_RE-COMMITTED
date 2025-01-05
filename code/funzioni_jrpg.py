import os
from random import choice,randint
from sys import platform

if platform == "linux":
    clear = "clear"   
elif platform == "win32":
    clear = "cls"

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
    

    def __str__(self):
        return f"\n{self.NOME},\n{self.COLORE},\n{self._vita_massima},\n{self._vita},\n{self.AGILITA},\n{self.POSSIBILITA_CRIT},\n{self._potenza_magie},\n{self.DIFESA},\n{self._lista_set},\n{self._set_in_uso}"
    

    def cambia_set(self,posizione_set):
        self._set_in_uso = self._lista_set[posizione_set]
        
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
        self.livello = int(1)
        self._exp_per_livellare = float(10)#
    
    def fai_magia(self,nemico,magia_scelta):
        debole = False
        annulla = False
        for debolezza in nemico._set_in_uso.DEBOLEZZE:
            if magia_scelta.TIPO == debolezza:
                debole = True

        for annulla in nemico._set_in_uso.COSA_ANNULLA:
            if magia_scelta.TIPO == annulla:
                annulla = True

        if annulla == True:
            danno = 0
        else:
            livello = magia_scelta._livello #di quanto aumentare il danno
            if debole == True:
                danno = 30 * livello
            else:
                danno = 20 * livello

                annulla = True
                
        nemico._vita = nemico._vita - int(danno)
        return danno
    
    def scegli_chi_attacare(self,lista_nemici):
        rifai = True
        while rifai:
            rifai = False
            i = 1
            os.system(clear)

            for nemico in lista_nemici:
                print(f"{i}|\t{nemico.NOME}: {nemico._vita_massima}/{nemico._vita}HP")
                i += 1
            n_scelto = int(input("scegliere il numero:\n"))
            if n_scelto > len(lista_nemici) or n_scelto <= 0:
                rifai = True

        nemico = lista_nemici[n_scelto - 1]
        return nemico
    
    def aumenta_statistiche_se_livellato(self):
        rifai_while = True #in caso si ha abbastanza exp per livellare più di una volta di fila
        ha_livellato = 0 #quanti livelli ha livellato il giocatore
        
        while rifai_while:
            rifai_while = False
            if self._exp >= self._exp_per_livellare: #controllo se si ha abbastanza exp per livellare
                print(f"{self.NOME}: E' SALITO DI LIVELLO!;\n|{self._exp}xp/{self._exp_per_livellare}xp| --> prossima xp nessaria per livellare")
                self.livello += 1 #aumenta livello
                ha_livellato += 1
                self._exp = self._exp - self.exp_per_livellare #riduci l'exp dopo aver livellato

                self._exp_per_livellare = self._exp_per_livellare * 1.6 #aumenta quanto necessita livellare

                vita_massima_prima = self._vita_massima
                sp_massimi_prima = self._sp_massimi
                potenza_magie_prima = self._potenza_magie
                #aumento statistiche
                self._vita_massima = self._vita_massima * 1.1
                self._sp_massimi = self._sp_massimi * 1.3
                self._potenza_magie = self._potenza_magie * 1.2
                print(f"STATISTICA AUMENTATA: +{int(self._vita_massima - vita_massima_prima)}|max hp")
                print(f"STATISTICA AUMENTATA: +{int(self._sp_massimi - sp_massimi_prima)}|max sp")
                print(f"STATISTICA AUMENTATA: +{int(self._potenza_magie - potenza_magie_prima)}|potenza delle magie")

        return ha_livellato
    
    def scegli_magia(self):
        scelta_non_valida = True

        while scelta_non_valida:
            os.system(clear)
            scelta_non_valida = False
            n = 0
            for magia in self._set_in_uso._lista_magie:
                n += 1
                if magia.CONSUMA_SP == True:
                    if magia._ad_area == True:
                        print(f"\n{n}|\t{magia.NOME}, LV{magia._livello}, magia che colpisce tutti i nemici, costo:{magia._quanta_sp_o_hp_richiede}SP")
                    else:
                        print(f"\n{n}|\t{magia.NOME}, LV{magia._livello}, magia che colpisce solo un nemico, costo:{magia._quanta_sp_o_hp_richiede}SP")
                else:
                    if magia._ad_area == True:
                        print(f"\n{n}|\t{magia.NOME}, LV{magia._livello}, magia che colpisce tutti i nemici, costo:{magia._quanta_sp_o_hp_richiede}HP")
                    else:
                        print(f"\n{n}|\t{magia.NOME}, LV{magia._livello}, magia che colpisce solo un nemico, costo:{magia._quanta_sp_o_hp_richiede}HP")

            magia_scelta = (int(input("inserire il numero\n")) - 1) #TODO TRY EXEPT
            os.system(clear)
            if magia_scelta >= len(self._set_in_uso._lista_magie) or magia_scelta < 0:
                scelta_non_valida = True

        magia_scelta = self._set_in_uso._lista_magie[magia_scelta]
        return magia_scelta
    
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
        self._sp = 9999
    
    @property
    def sp(self):
        return self._sp
    @sp.setter
    def sp(self,sp_da_assegnare:int):
        if type(sp_da_assegnare) == int:
            self._sp = sp_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNAZIONE DELL'SP")

    def cosa_fa_nemico(self):
        magia_scelta = choice(self._set_in_uso._lista_magie)
        return magia_scelta

    def fai_magia(self,alleato_scelto,magia_scelta):
        debole = False
        annulla = False
        for debolezza in alleato_scelto._set_in_uso.DEBOLEZZE:
            if magia_scelta.TIPO == debolezza:
                debole = True

        for annulla in alleato_scelto._set_in_uso.COSA_ANNULLA:
            if magia_scelta.TIPO == annulla:
                annulla = True

        if annulla == True:
            danno = 0
        else:
            livello = self._set_in_uso._livello #di quanto aumentare il danno

            if debole == True:
                danno = 30 * livello
            else:
                danno = 20 * livello
        alleato_scelto._vita = alleato_scelto._vita - int(danno)
        return danno

    def nemico_Attacca(self,lista_alleati_vivi):
        alleato_scelto = choice(lista_alleati_vivi)
        magia_scelta = cosa_fa_nemico()
        danno = fai_magia(alleato_scelto,magia_scelta)
        print(danno)
        
class Set_magia:
    def __init__(self,
                NOME:str,
                lista_magie:list,
                DEBOLEZZE:list,
                COSA_ANNULLA:list,
        ):
        self.NOME = NOME
        self._lista_magie = lista_magie
        self.DEBOLEZZE = DEBOLEZZE
        self.COSA_ANNULLA = COSA_ANNULLA
    
    #@property #FORSE SERVE
    #def lista_magie(self):
    #    return self._lista_magie
    #@lista_magie.setter
    #def lista_magie(self,lista_magie_da_assegnare):
    #    if type(lista_magie_da_assegnare) == list and lista_magie_da_assegnare != []:
    #        self._lista_magie = lista_magie_da_assegnare
    #    else:
    #        raise ValueError("ERRORE NELL'ASSEGNAZIONE DELLA lista_magie")
    

    def aggiungi_magia(self,magia):
        self._lista_magie.append(magia)
    
    def rimuovi_magia(self,magia_da_verificare):
        magia_valida = False 
        for magia in self._lista_magie:
            
            if magia.NOME == magia_da_verificare.NOME and magia._livello == magia_da_verificare._livello and magia.TIPO == magia_da_verificare.TIPO and magia._ad_area == magia_da_verificare._ad_area and magia.CONSUMA_SP == magia_da_verificare.CONSUMA_SP and magia._quanta_sp_o_hp_richiede == magia_da_verificare._quanta_sp_o_hp_richiede:
                #allora la magia è presente
                magia_valida = True #ho trovato la magia
                self._lista_magie.remove(magia_da_verificare)
                break
        if magia_valida == False: #controllo se ha trovato la magia
            raise ValueError("ERRORE magia NON TROVATO")

class Magia:
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

def calcola_exp(alleato,exp_da_dare_a_fine_partita):
    alleato._exp = alleato._exp + exp_da_dare_a_fine_partita
    ha_livellato = alleato.aumenta_statistiche_se_livellato()

def assegna_drop(alleato,nemico): #TODO
    if not nemico.DROP == None:
        pass
    pass

def genera_nemici(): #TODO
    magia3 = Magia("testata",2,"bho",False,True,1) #TODO cambiare il tipo di magia
    magia4 = Magia("pugno",1,"bho",False,True,1)
    magia5 = Magia("colpo con spada",3,"bho",True,True,1)
    magia6 = Magia("carica",3,"bho",False,True,1)

    lista_magie_goblin = [magia3,magia4]

    set_goblin = Set_magia("",lista_magie_goblin,[],[])
    lista_set_goblin = [set_goblin]
    goblin = Nemico("Goblin","red",86,30,10,10,20,lista_set_goblin,None,10)

    lista_magie_cavaliere = [magia5]

    set_cavaliere = Set_magia("",lista_magie_cavaliere,[],[])
    lista_set_cavaliere = [set_cavaliere]
    cavaliere_nero = Nemico("Cavaliere nero","red",120,4,2,2,10,lista_set_cavaliere,None,15.5)

    lista_magie_cavaliere_normale = [magia6]

    set_cavaliere_normale = Set_magia("",lista_magie_cavaliere_normale,[],[])
    lista_set_cavaliere_normale = [set_cavaliere_normale]
    cavaliere_normale = Nemico("Cavaliere","red",80,4,2,2,10,lista_set_cavaliere_normale,None,15.5)

    lista_nemici_tutti = [goblin,cavaliere_nero,cavaliere_normale]

    quanti_nemici_generare = randint(1,3)

    lista_nemici = []
    for i in range(quanti_nemici_generare):
        nemico_scelto = choice(lista_nemici_tutti)
        lista_nemici.append(nemico_scelto)
    return lista_nemici

def turno(lista_giocatori): #TODO
    exp_da_dare_a_fine_partita = 0
    lista_nemici = genera_nemici()
    fine_partita = False
    while fine_partita == False:

        if fine_partita == False:
            for giocatore in lista_giocatori:
                os.system(clear)
                for nemico in lista_nemici:
                    if nemico._vita <= 0:
                        exp_da_dare_a_fine_partita =+ nemico.EXP
                        #TODO da fare anche con i drop
                        lista_nemici.remove(nemico)

                if len(lista_nemici) == 0: #nemici sconfitti, fine della partita
                    fine_partita = True

                for nemico in lista_nemici:
                    print(f"\n{nemico.NOME}: {nemico._vita}/{nemico._vita_massima}HP",end="\t")
                print("\n\n")
                if fine_partita == False:
                    scelta = input(f"TURNO DI: {giocatore.NOME}:\n|1|:MAGIA    |2|:CAMBIA SET\n")
                    os.system(clear)
                    if scelta == "1":
                        #scegli magia
                        magia_scelta = giocatore.scegli_magia()

                        if magia_scelta._ad_area == False:
                            nemico = giocatore.scegli_chi_attacare(lista_nemici)
                            danno = giocatore.fai_magia(nemico,magia_scelta)
                            print(f"{nemico.NOME}: ha subito - {danno}")
                            x = input("\n")
                        else:
                            for nemico in lista_nemici:
                                danno = giocatore.fai_magia(nemico,magia_scelta)
                                print(f"{nemico.NOME}: ha subito -{danno}")
                            x = input("\n")

                    elif scelta == "2":
                        input_sbagliato = True
                        while input_sbagliato:
                            input_sbagliato = False
                            os.system(clear)
                            n = 1
                            for set in giocatore._lista_set:
                                print(f"{n}|\t{set.NOME}")#TODO aggiungere più dettagli
                                n = n + 1
                            set_da_verificare = (int(input("inserire il numero del set\n")) - 1)
                            os.system(clear)
                            if set_da_verificare < 0 or set_da_verificare > len(giocatore._lista_set):
                                input_sbagliato = True

                        giocatore.cambia_set(set_da_verificare)
                        print(f"il giocatore: {giocatore.NOME}\nha equipaggiato: {giocatore._set_in_uso.NOME}")
                        x = input("\n")
                        

    print("VITTORIA PER;")
    for giocatore in lista_giocatori:
        print(f"|{giocatore.NOME}")
        x = input("\n")
        os.system(clear)
        calcola_exp(giocatore,exp_da_dare_a_fine_partita)