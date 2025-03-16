import os
from random import choice,randint
from sys import platform
from magie_con_effetti import *
#questo serve per svuotare il terminale, sia da linux che da windows
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
        
        self.salta_il_tuo_prossimo_turno = False

        self.atterato = False
        self.one_more = False
        self._statistiche_momentanee = (0,0,0) #(ATK,DEF,AGI)
        self.durata_stat_momentanee = (0,0,0) #quanti turni ancora dura una determinata stat
        self._set_in_uso = self._lista_set[0] #assegna di base il primo set nella lista, preso dalla lista dei set 

    #"statistiche_momentanee" --> (0,0,0) -corrisponde a -> "(ATK,DEF,AGI)"
    def controllo_che_le_statistiche_non_superino_1(self,stat_dopo):
        if stat_dopo[0] > 1:
            stat_dopo = (1,self._statistiche_momentanee[1],self._statistiche_momentanee[2])
        
        elif stat_dopo[1] > 1:
            stat_dopo = (self._statistiche_momentanee[0],1,self._statistiche_momentanee[2])
        
        elif stat_dopo[2] > 1:
            stat_dopo = (self._statistiche_momentanee[0],self._statistiche_momentanee[1],1)
        return stat_dopo

    def aumenta_ATK(self):
        stat_dopo = (self._statistiche_momentanee[0] + 1,self._statistiche_momentanee[1],self._statistiche_momentanee[2])
        stat_dopo = self.controllo_che_le_statistiche_non_superino_1(stat_dopo)
        self._statistiche_momentanee = stat_dopo
        self.durata_stat_momentanee = (3,self.durata_stat_momentanee[1],self.durata_stat_momentanee[2])

    def aumenta_DEF(self):
        stat_dopo = (self._statistiche_momentanee[0],self._statistiche_momentanee[1] + 1,self._statistiche_momentanee[2])
        stat_dopo = self.controllo_che_le_statistiche_non_superino_1(stat_dopo)
        self._statistiche_momentanee = stat_dopo
        self.durata_stat_momentanee = (self.durata_stat_momentanee[0],3,self.durata_stat_momentanee[2])

    def aumenta_AGI(self):
        stat_dopo = (self._statistiche_momentanee[0],self._statistiche_momentanee[1],self._statistiche_momentanee[2] + 1)
        stat_dopo = self.controllo_che_le_statistiche_non_superino_1(stat_dopo)
        self._statistiche_momentanee = stat_dopo
        self.durata_stat_momentanee = (self.durata_stat_momentanee[0],self.durata_stat_momentanee[1],3)


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
        if type(magia_scelta) == Magia:
            danno = calcola_danno_fatto(magia_scelta,nemico)
        else:
            danno = fai_magia_speciale(magia_scelta,self,nemico)

        if not danno == None:
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
                os.system(clear)
                print(f"{self.NOME}: E' SALITO DI LIVELLO!;\n|{self._exp}xp/{self._exp_per_livellare}xp| --> prossima xp nessaria per livellare")
                x = input("")
                self.livello += 1 #aumenta livello
                ha_livellato += 1
                self._exp = self._exp - self.exp_per_livellare #riduci l'exp dopo aver livellato

                self._exp_per_livellare = int(self._exp_per_livellare * 1.7) #aumenta quanto necessita livellare

                vita_massima_prima = self._vita_massima
                sp_massimi_prima = self._sp_massimi
                potenza_magie_prima = self._potenza_magie

                #aumento statistiche
                self._vita_massima = int(self._vita_massima * 1.1)
                self._sp_massimi = int(self._sp_massimi * 1.3)
                self._potenza_magie = int(self._potenza_magie * 1.2)

                vita_max_guadagnata = int(self._vita_massima - vita_massima_prima)
                sp_massimi_guadagnati = int(self._sp_massimi - sp_massimi_prima)
                potenza_magie_guadagnata = int(self._potenza_magie - potenza_magie_prima)

                #aumento della vita normale e dell'sp in base a quanto guadagnato
                self._vita += vita_max_guadagnata
                self._sp += sp_massimi_guadagnati

                #stampa dell'aumento delle statistiche
                print(f"STATISTICA AUMENTATA: +{vita_max_guadagnata}|max hp")
                print(f"STATISTICA AUMENTATA: +{sp_massimi_guadagnati}|max sp")
                print(f"STATISTICA AUMENTATA: +{potenza_magie_guadagnata}|potenza delle magie")
                x = input("\n")

    
    def scegli_magia(self):
        scelta_non_valida = True

        while scelta_non_valida:
            os.system(clear)
            scelta_non_valida = False
            n = 0
            print(f"LISTA DELLE MAGIE |{self._set_in_uso.NOME}|:")
            for magia in self._set_in_uso._lista_magie:
                n += 1
                if magia.CONSUMA_SP == True:
                    if magia._ad_area == True:
                        print(f"{n}|\t{magia.NOME}, LV{magia._livello}, magia che colpisce tutti i nemici, costo:{magia._quanta_sp_o_hp_richiede}SP")
                    else:
                        print(f"{n}|\t{magia.NOME}, LV{magia._livello}, magia che colpisce solo un nemico, costo:{magia._quanta_sp_o_hp_richiede}SP")
                else:
                    if magia._ad_area == True:
                        print(f"{n}|\t{magia.NOME}, LV{magia._livello}, magia che colpisce tutti i nemici, costo:{magia._quanta_sp_o_hp_richiede}HP")
                    else:
                        print(f"{n}|\t{magia.NOME}, LV{magia._livello}, magia che colpisce solo un nemico, costo:{magia._quanta_sp_o_hp_richiede}HP")

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
    def __init__(self,
                NOME,
                LIVELLO,
                COLORE,
                vita_massima,
                AGILITA,
                POSSIBILITA_CRIT,
                potenza_magie,
                DIFESA,
                lista_set,
                DROP,
                EXP
        ):
        super().__init__(NOME, COLORE, vita_massima, AGILITA, POSSIBILITA_CRIT, potenza_magie, DIFESA, lista_set)

        self.DROP = DROP #lista dei possibili drop di un nemico
        self.EXP = EXP #exp che guadagnerà il giocatore
        self._sp = 9999
        self.LIVELLO = LIVELLO
    
    def cosa_fa_nemico(self):
        magia_scelta = choice(self._set_in_uso._lista_magie)
        return magia_scelta

    def fai_magia(self,alleato_scelto,magia_scelta):
        danno = calcola_danno_fatto(magia_scelta,alleato_scelto) #alleato in questo caso è al posto di "nemico"
        return danno

    def nemico_attacca(self,lista_giocatori_vivi):
        alleato_scelto = choice(lista_giocatori_vivi)

        magia_scelta = self.cosa_fa_nemico()
        danno = self.fai_magia(alleato_scelto,magia_scelta)

        if not danno == None:
            alleato_scelto._vita = alleato_scelto._vita - int(danno)
        return danno,magia_scelta

    @property
    def sp(self):
        return self._sp
    @sp.setter
    def sp(self,sp_da_assegnare:int):
        if type(sp_da_assegnare) == int:
            self._sp = sp_da_assegnare
        else:
            raise ValueError("ERRORE NELL'ASSEGNAZIONE DELL'SP")
     
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
    
    #TODO al posto che mettere e scegliere la magia dalla classe "alleato", FORSE è meglio eseguirla qui

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

class Magia_speciale(Magia):
    def __init__(self, NOME, livello, TIPO, ad_area, CONSUMA_SP, quanta_sp_o_hp_richiede,POSIZIONE_ASSOCIATA):
        super().__init__(NOME, livello, TIPO, ad_area, CONSUMA_SP, quanta_sp_o_hp_richiede)
        
        self.POSIZIONE_ASSOCIATA = POSIZIONE_ASSOCIATA

def calcola_exp(alleato,exp_da_dare_a_fine_partita):
    alleato._exp = alleato._exp + exp_da_dare_a_fine_partita
    alleato.aumenta_statistiche_se_livellato()

def assegna_drop(alleato,nemico): #TODO
    if not nemico.DROP == None:
        pass
    pass

def genera_nemici(lista_nemici_tutti):
    quanti_nemici_generare = randint(1,3)

    lista_nemici = []
    for i in range(quanti_nemici_generare):
        nemico_scelto = choice(lista_nemici_tutti)
        lista_nemici.append(nemico_scelto)
    return lista_nemici

def controlla_vita_nemici(lista_nemici):
    fine_partita = False
    partita_vinta = False

    lista_nemici_nuova = []
    for nemico in lista_nemici:
        if nemico._vita <= 0:
            exp_da_dare_a_fine_partita =+ nemico.EXP
            #TODO da fare anche con i drop
        else:
            lista_nemici_nuova.append(nemico)

    if len(lista_nemici) == 0: #nemici sconfitti, fine della partita
        fine_partita = True
        partita_vinta = True
    
    lista_nemici = lista_nemici_nuova #così facendo tutti i nemici vengono rimossi in un solo turno
    return lista_nemici,fine_partita,partita_vinta

def controlla_vita_giocatori(lista_giocatori):
    fine_partita = False
    partita_vinta = False
    lista_giocatori_nuova = []
    lista_giocatori_morti = []

    for giocatore_ in lista_giocatori:
        if giocatore_._vita <= 0:   #il giocatore è morto
            lista_giocatori_morti.append(giocatore_)
        else:                       #il giocatore è vivo
            lista_giocatori_nuova.append(giocatore_)
            
    lista_giocatori_vivi = lista_giocatori_nuova

    if len(lista_giocatori_vivi) == 0: #giocatori sconfitti, fine della partita
        fine_partita = True
    
    return lista_giocatori_vivi,lista_giocatori_morti,partita_vinta,fine_partita
           
def turno(lista_giocatori,lista_nemici_tutti): #
    exp_da_dare_a_fine_partita = 0

    lista_nemici = genera_nemici(lista_nemici_tutti)
    fine_partita = False

    while fine_partita == False:
        lista_giocatori_vivi,lista_giocatori_morti,partita_vinta,fine_partita = controlla_vita_giocatori(lista_giocatori)

        for giocatore in lista_giocatori_vivi: #determina di che giocatore è il turno
            lista_nemici,fine_partita,partita_vinta = controlla_vita_nemici(lista_nemici)

            if fine_partita == False and giocatore.salta_il_tuo_prossimo_turno == False:
                    #stampa della CUI in combattimento
                    print("- - -NEMICI- - -")
                    for nemico in lista_nemici:
                        print(f"{nemico.NOME}: {nemico._vita}/{nemico._vita_massima}HP")
                    print("- - -",end="\n\n")

                    print("- - - GIOCATORI - - -")
                    for giocatore in lista_giocatori_vivi:
                        print(f"{giocatore.NOME}: {giocatore._vita}/{giocatore._vita_massima}HP|{giocatore._sp}/{giocatore._sp_massimi}SP")
                    print("- - -\n")
                    if len(lista_giocatori_morti) > 0:
                        print("|-|-|-GIOCATORI MORTI-|-|-|")
                        for giocatore in lista_giocatori_morti:
                            print(f"{giocatore.NOME}:{giocatore._sp}/{giocatore._sp_massimi}SP")
                        print("-"*30)
                    scelta = input(f"///////TURNO DI: {giocatore.NOME}:///////\n|1|:MAGIA    |2|:CAMBIA SET\n")

                    os.system(clear)
                    if scelta == "1":
                        #scegli magia
                        magia_scelta = giocatore.scegli_magia()

                        if magia_scelta._ad_area == False:
                            
                            nemico = giocatore.scegli_chi_attacare(lista_nemici)
                            danno = giocatore.fai_magia(nemico,magia_scelta)
                            if not danno == None:
                                print(f"{nemico.NOME}: ha subito - {danno}")
                                x = input("\n")
                        else:
                            almeno_un_nemico_danneggiato = False

                            for nemico in lista_nemici:
                                danno = giocatore.fai_magia(nemico,magia_scelta)

                                if not danno == None:
                                    almeno_un_nemico_danneggiato = True
                                    print(f"{nemico.NOME}: ha subito -{danno}")

                                if almeno_un_nemico_danneggiato == True:
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

                            if set_da_verificare < 0 or set_da_verificare >= len(giocatore._lista_set):
                                input_sbagliato = True

                        giocatore.cambia_set(set_da_verificare)
                        print(f"il giocatore: {giocatore.NOME}\nha equipaggiato: {giocatore._set_in_uso.NOME}")
                        x = input("\n")
            
            if giocatore.salta_il_tuo_prossimo_turno == True:
                os.system(clear)
                print(f"{giocatore.NOME} ha saltato il suo turno")
                giocatore.salta_il_tuo_prossimo_turno = False
                x = input("")

        for nemico in lista_nemici: #inizia il turno dei nemici
            if fine_partita == False and nemico.salta_il_tuo_prossimo_turno == False:
                danno,magia_scelta = nemico.nemico_attacca(lista_giocatori_vivi)
                print(f"il nemico {nemico.NOME} ha attaccato usando: |{magia_scelta.NOME}| -{danno}HP | LV:{magia_scelta._livello}")
                x = input("")

            if nemico.salta_il_tuo_prossimo_turno == True:
                os.system(clear)
                print(f"{nemico.NOME} ha saltato il suo turno")
                nemico.salta_il_tuo_prossimo_turno = False
                x = input("")

    if partita_vinta == True:
        os.system(clear)
        print("VITTORIA PER;")
        for giocatore in lista_giocatori_vivi:
            print(f"|{giocatore.NOME}")
            x = input("\n")
            calcola_exp(giocatore,exp_da_dare_a_fine_partita)
    return partita_vinta

def fai_magia_speciale(magia,giocatore,nemico):
    case = str(magia.POSIZIONE_ASSOCIATA)
    match case:
        case "1": #"salta_turno"
            # salta_turno(nemico) TODO non ha senso come utilità
            danno = None

        case "2": #"danno_2_turni"
            salta_turno(giocatore)
            danno = calcola_danno_fatto(magia,nemico)
            danno = int(danno * 2.2)

        case "3": #"rage_drive"
            danno = calcola_danno_fatto(magia,nemico)
            danno = int(danno * 2.3)
            giocatore.aumenta_ATK()


        case "4": #"rage_art"
            pass #TODO fare in modo che la maagia possa fallire se la vita è sopra il 15%
        
    return danno

def calcola_danno_fatto(magia_scelta,nemico):
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
        livello = magia_scelta._livello #il livello influenza quanto danno si fà
        if debole == True:
            danno = 30 * livello
        else:
            danno = 20 * livello
            annulla = True
    return danno