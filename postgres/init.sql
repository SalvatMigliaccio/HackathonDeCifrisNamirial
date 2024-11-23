-- Creazione della tabella users
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY, -- Identificativo univoco per l'utente
    username VARCHAR(255) NOT NULL UNIQUE, -- Nome utente, unico
    password_hash TEXT NOT NULL, -- Password hashata
    email VARCHAR(255) NOT NULL UNIQUE -- Aggiunta del campo email
);

-- Creazione della tabella operatori
CREATE TABLE IF NOT EXISTS operatori (
    id SERIAL PRIMARY KEY, -- Identificativo univoco per l'operatore
    username VARCHAR(255) NOT NULL UNIQUE, -- Nome utente, unico
    password_hash TEXT NOT NULL, -- Password hashata
    email VARCHAR(255) NOT NULL UNIQUE -- Aggiunta del campo email
);

-- Creazione della tabella gruppi
CREATE TABLE IF NOT EXISTS gruppi (
    id SERIAL PRIMARY KEY, -- Identificativo univoco per il gruppo
    group_name VARCHAR(255) NOT NULL, -- Nome del gruppo
    parent_group_id INT, -- ID del gruppo genitore (nullable)
    CONSTRAINT fk_parent_group FOREIGN KEY (parent_group_id) REFERENCES gruppi(id) ON DELETE SET NULL -- Corretto riferimento alla colonna 'id'
);

-- Creazione della tabella pratica
CREATE TABLE IF NOT EXISTS pratica (
    practice_id SERIAL PRIMARY KEY, -- Identificativo univoco per la pratica
    wallet_address VARCHAR(255) NOT NULL, -- Indirizzo del wallet
    user_id INT NOT NULL, -- ID dell'utente associato
    CONSTRAINT fk_user_pratica FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE -- Corretto riferimento alla colonna 'id'
);

-- Creazione della tabella documento
CREATE TABLE IF NOT EXISTS documento (
    doc_id SERIAL PRIMARY KEY, -- Identificativo univoco per il documento
    dochash TEXT NOT NULL, -- Hash del documento
    user_id INT NOT NULL, -- ID dell'utente associato
    redirect_uri TEXT, -- URI di redirect
    CONSTRAINT fk_user_document FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE -- Corretto riferimento alla colonna 'id'
);

-- Creazione della tabella operatore_gruppo per gestire l'associazione
CREATE TABLE IF NOT EXISTS operatore_gruppo (
    operator_id INT NOT NULL, -- ID dell'operatore
    group_id INT NOT NULL, -- ID del gruppo
    CONSTRAINT fk_operator_group_operator FOREIGN KEY (operator_id) REFERENCES operatori(id) ON DELETE CASCADE, -- Corretto riferimento alla colonna 'id'
    CONSTRAINT fk_operator_group_group FOREIGN KEY (group_id) REFERENCES gruppi(id) ON DELETE CASCADE, -- Corretto riferimento alla colonna 'id'
    PRIMARY KEY (operator_id, group_id) -- Chiave primaria composta
);

-- Aggiunta della colonna email nella tabella users (se non è già presente)
ALTER TABLE users ADD COLUMN IF NOT EXISTS email VARCHAR(255) UNIQUE NOT NULL;
