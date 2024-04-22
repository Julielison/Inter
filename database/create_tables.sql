-- Cria a tabela de usuários caso não exista
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

-- Cria a tabela de comands caso não exista
CREATE TABLE IF NOT EXISTS commands (
    id INTEGER PRIMARY KEY,
    command TEXT NOT NULL
);

-- Cria a tabela de logs caso não exista
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY,
    id_user INTEGER NOT NULL,
    id_command INTEGER NOT NULL,
    date_hour TEXT NOT NULL,
    FOREIGN KEY (id_user) REFERENCES users(id),
    FOREIGN KEY (id_command) REFERENCES commands(id)
);