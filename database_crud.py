import sqlite3

class Database:
    def __init__(self) -> None:
        self.conection = sqlite3.connect('./database/data.db')
        self.cursor = self.conection.cursor()
        self.create_tables()
        self.create_view_log()
        self.insert()

    def create_tables(self):
        # Abrir o arquivo SQL e ler o conteúdo
        with open('./database/create_tables.sql', 'r') as arquivo_sql:
            script_sql = arquivo_sql.read()

        # Executar o script SQL
        self.cursor.executescript(script_sql)

    def create_view_log(self):
        # Abrir o arquivo SQL e ler o conteúdo
        with open('./database/create_temporary_views.sql', 'r') as arquivo_sql:
            script_sql = arquivo_sql.read()

        # Executar o script SQL
        self.cursor.executescript(script_sql)

    def insert(self):
        # Abrir o arquivo SQL e ler o conteúdo
        with open('./database/insert_test.sql', 'r') as arquivo_sql:
            script_sql = arquivo_sql.read()

        # Executar o script SQL
        self.cursor.executescript(script_sql)

    def check_username(self):
        