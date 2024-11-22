-- Creazione della tabella users
CREATE TABLE IF NOT EXISTS users (
    uid SERIAL PRIMARY KEY, -- Identificativo univoco per l'utente
    username VARCHAR(255) NOT NULL UNIQUE, -- Nome utente, unico
    password_hash TEXT NOT NULL -- Password hashata
);

-- Creazione della tabella operatori
CREATE TABLE IF NOT EXISTS operatori (
    uid SERIAL PRIMARY KEY, -- Identificativo univoco per l'operatore
    username VARCHAR(255) NOT NULL UNIQUE, -- Nome utente, unico
    password_hash TEXT NOT NULL -- Password hashata
);

-- Creazione della tabella gruppi
CREATE TABLE IF NOT EXISTS gruppi (
    uid SERIAL PRIMARY KEY, -- Identificativo univoco per il gruppo
    group_name VARCHAR(255) NOT NULL, -- Nome del gruppo
    parent_group_id INT, -- ID del gruppo genitore (nullable)
    CONSTRAINT fk_parent_group FOREIGN KEY (parent_group_id) REFERENCES gruppi(uid) ON DELETE SET NULL
);

-- Creazione della tabella pratica
CREATE TABLE IF NOT EXISTS pratica (
    practice_id SERIAL PRIMARY KEY, -- Identificativo univoco per la pratica
    wallet_address VARCHAR(255) NOT NULL, -- Indirizzo del wallet
    user_id INT NOT NULL, -- ID dell'utente associato
    CONSTRAINT fk_user_pratica FOREIGN KEY (user_id) REFERENCES users(uid) ON DELETE CASCADE
);

-- Creazione della tabella documento
CREATE TABLE IF NOT EXISTS documento (
    doc_id SERIAL PRIMARY KEY, -- Identificativo univoco per il documento
    hash TEXT NOT NULL, -- Hash del documento
    user_id INT NOT NULL, -- ID dell'utente associato
    redirect_uri TEXT, -- URI di redirect
    CONSTRAINT fk_user_document FOREIGN KEY (user_id) REFERENCES users(uid) ON DELETE CASCADE
);

-- Creazione della tabella operatore_gruppo per gestire l'associazione
CREATE TABLE IF NOT EXISTS operatoregruppo (
    operator_id INT NOT NULL, -- ID dell'operatore
    group_id INT NOT NULL, -- ID del gruppo
    CONSTRAINT fk_operator_group_operator FOREIGN KEY (operator_id) REFERENCES operatori(uid) ON DELETE CASCADE,
    CONSTRAINT fk_operator_group_group FOREIGN KEY (group_id) REFERENCES gruppi(uid) ON DELETE CASCADE,
    PRIMARY KEY (operator_id, group_id) -- Chiave primaria composta
);
