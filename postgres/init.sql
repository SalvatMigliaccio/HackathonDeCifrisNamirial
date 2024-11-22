-- Creazione della tabella User
CREATE TABLE IF NOT EXISTS "User" (
    UID SERIAL PRIMARY KEY, -- Identificativo univoco per l'utente
    Username VARCHAR(255) NOT NULL UNIQUE, -- Nome utente, unico
    PasswordHash TEXT NOT NULL -- Password hashata
);

-- Creazione della tabella Operatori
CREATE TABLE IF NOT EXISTS "Operatori" (
    UID SERIAL PRIMARY KEY, -- Identificativo univoco per l'operatore
    Username VARCHAR(255) NOT NULL UNIQUE, -- Nome utente, unico
    PasswordHash TEXT NOT NULL -- Password hashata
);

-- Creazione della tabella Gruppi
CREATE TABLE IF NOT EXISTS "Gruppi" (
    UID SERIAL PRIMARY KEY, -- Identificativo univoco per il gruppo
    GroupName VARCHAR(255) NOT NULL, -- Nome del gruppo
    ParentGroupID INT, -- ID del gruppo genitore (nullable)
    CONSTRAINT fk_parent_group FOREIGN KEY (ParentGroupID) REFERENCES "Gruppi"(UID) ON DELETE SET NULL
);

-- Creazione della tabella Pratica
CREATE TABLE IF NOT EXISTS "Pratica" (
    PracticeID SERIAL PRIMARY KEY, -- Identificativo univoco per la pratica
    WalletAddress VARCHAR(255) NOT NULL, -- Indirizzo del wallet
    UserID INT NOT NULL, -- ID dell'utente associato
    CONSTRAINT fk_user_pratica FOREIGN KEY (UserID) REFERENCES "User"(UID) ON DELETE CASCADE
);

-- Creazione della tabella Documento
CREATE TABLE IF NOT EXISTS "Documento" (
    DocID SERIAL PRIMARY KEY, -- Identificativo univoco per il documento
    Hash TEXT NOT NULL, -- Hash del documento
    UserID INT NOT NULL, -- ID dell'utente associato
    RedirectURI TEXT, -- URI di redirect
    CONSTRAINT fk_user_document FOREIGN KEY (UserID) REFERENCES "User"(UID) ON DELETE CASCADE
);

-- NOTA: La "Associazione Operatore" non è una tabella ma un'associazione logica.
-- Creiamo quindi una tabella ponte per gestire questa associazione.
CREATE TABLE IF NOT EXISTS "OperatoreGruppo" (
    OperatorID INT NOT NULL, -- ID del medico/operatore
    GroupID INT NOT NULL, -- ID del gruppo
    CONSTRAINT fk_operator_group_operator FOREIGN KEY (OperatorID) REFERENCES "Operatori"(UID) ON DELETE CASCADE,
    CONSTRAINT fk_operator_group_group FOREIGN KEY (GroupID) REFERENCES "Gruppi"(UID) ON DELETE CASCADE,
    PRIMARY KEY (OperatorID, GroupID) -- Chiave primaria composta
);
