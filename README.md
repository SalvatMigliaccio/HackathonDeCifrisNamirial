Project Ripple x Public Amministration

Autenticazione:
    - Nome Utente
    - Password

Database Postgres:
User:
    - UID
    - Nome Utente
    - Password (hash) 

Operatori:
    -UID
    - Nome utente
    - Password (hashata)

Gruppi:
    -UID
    -Name Group
    -ID Gruppo Genitore (nullable) 
    (serve per lavorare sulla firma ad anello!)


Associazione Operatore (Non è una tabella)
    - ID medico
    - ID nome gruppo

Pratica:
    - ID pratica
    - Indirizzo Wallet
    - ID utente

Documento:
    - ID
    - Hash
    - ID utente
    - Redirect URI



Punti Focali:
L'utente iniziale crea la pratica, il quale è un operazione su blockchain, perchè equivale creare il wallet. La pratica non comprare su blockchain?, comprare un indirizzo 