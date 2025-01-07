# *JRPG Holiday project*
this project is a remake of my first project.

the objective is to make it easier to read and improve some game mecanic,
and maybe i will add some grafic improvment
using the "py_cui" library.

### ONLY FOR NOW:
you don't need to install any library.

The **requirements.txt** file, will only be used for the final version of the game 

# HOW TO RUN THE PROJECT:
for now you don't have to use a **venv**, you only need to run the **main.py** file,

that is located in the ***code*** directory (it will change file path in future).
## Here is the game logic UML

```mermaid
classDiagram
Alleato --|> Entita
Nemico --|> Entita
Entita "1"--> "1..n" Set_magia :possiede
Set_magia "1" --> "1..n" Magia :contiene

class Entita {
    NOME :str
    COLORE :str
    vita_massima :int
    AGILITA :int
    POSSIBILITA_CRIT :int
    potenza_magie :int
    DIFESA :int
    lista_set :list
    -cambia_set(set_da_verificare)
}

class Alleato {
    sp_massimi :int
    sp :int
    esperienza :float
    -aumenta_statistiche_se_livellato()
}

class Nemico{
    DROP :list
    EXP :float
    -cosa_fa_nemico()
    -fai_magia(alleato_scelto,magia_scelta)
    -nemico_Attacca(lista_alleati_vivi)
}

class Set_magia {
    NOME:str,
    lista_magie :list
    DEBOLEZZE :list
    COSA_ANNULLA :list
    -aggiungi_magia(magia)
    -rimuovi_magia(magia)
}

class Magia {
    NOME : str
    livello : int
    TIPO : str
    ad_area : bool
    CONSUMA_SP :bool
    quanta_sp_o_hp_richiede :int
    
}
```
# THE MEANING OF THE NAMES IN THE UML;
#TODO