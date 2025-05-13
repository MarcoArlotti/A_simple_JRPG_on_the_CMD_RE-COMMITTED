from funzioni_jrpg import Magia, Magia_speciale, Set_magia, Alleato

vita_massima = 200
# creazione delle varie magie di galo (un personaggio)
magia4 = Magia(
    "PUGNO",
    1,
    "bho",
    False,
    True,
    6,
)

magia7 = Magia(
    "ACCOLTELLATA",
    4,
    "bho",
    ad_area=False,
    CONSUMA_SP=True,
    quanta_sp_o_hp_richiede=5,
)
magia8 = Magia(
    "PREPARAZIONE DI UN UML",
    4,
    "bho",
    ad_area=False,
    CONSUMA_SP=True,
    quanta_sp_o_hp_richiede=4,
)  # TODO AUMENTA IL DANNO DEL GALO
magia9 = Magia(
    "COLPO MULTIPLO CON BORRACCIA",
    3,
    "bho",
    ad_area=True,
    CONSUMA_SP=True,
    quanta_sp_o_hp_richiede=13,
)
magia10 = Magia(
    "CALCIO IN RINCORSA",
    5,
    "bho",
    ad_area=False,
    CONSUMA_SP=False,
    quanta_sp_o_hp_richiede=18,
)

# creazione delle varie liste di magie da mettere nei set
magia_s_3 = Magia_speciale(
    "ACQUA DELLA BORRACCIA",
    2,
    "SPECIALE",
    ad_area=False,
    CONSUMA_SP=True,
    quanta_sp_o_hp_richiede=10,
    POSIZIONE_ASSOCIATA=5,
)

galo_lista_magie1 = [
    magia7,
    magia8,
]
galo_lista_magie2 = [
    magia9,
    magia_s_3,
]
galo_lista_magie3 = [
    magia10,
    magia4,
]

galo_set1 = Set_magia(
    NOME="MONDAINO FIGHTING STANCE",
    lista_magie=galo_lista_magie1,
    DEBOLEZZE=[],
    COSA_ANNULLA=[],
)
galo_set2 = Set_magia(
    "TECNICHE DELLA BORRACCIA INARRESTABILE",
    galo_lista_magie2,
    [],
    [],
)  # TODO
galo_set3 = Set_magia(
    "INFO45 FIGHTING STANCE",
    galo_lista_magie3,
    [],
    [],
)  # TODO

lista_set_galo = [
    galo_set1,
    galo_set2,
    galo_set3,
]

galo = Alleato(
    NOME="GALO",
    COLORE="BLU",  # TODO
    vita_massima=136,
    AGILITA=25,
    POSSIBILITA_CRIT=25,
    potenza_magie=17,
    DIFESA=15,
    lista_set=lista_set_galo,
    sp_massimi=50,
)

# assegnazione dei set creati a galo
galo._lista_set = lista_set_galo
