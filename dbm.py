import psycopg2 
from os import getenv

def command(filename):
    with open("sql/"+filename,"r") as f:
        query = f.read()
        return query

class Dbm:
    def execute(self, sql_command, params=None):
        try:
            db_name = getenv('PGDATABASE')
            user = getenv('PGUSER')
            password = getenv('PGPASSWORD')
            host = getenv('PGHOST')
            port = getenv('PGPORT')

            conn = psycopg2.connect(
                database=db_name,
                user=user,
                password=password,
                host=host,
                port=port
            )

            cursor = conn.cursor()

            if params:
                cursor.execute(sql_command, params)
            else:
                cursor.execute(sql_command)

            if sql_command.lower().strip().startswith('select'):
                data = cursor.fetchall()
            else:
                data = None

            conn.commit()
            conn.close()
            return data

        except Exception as e:
            print(f"Error: {e}")


    def init(self):
        self.execute(sql_command=command("create_table_links.sql"))
        self.execute(sql_command=command("create_table_data.sql"))
        return True
    def generate_link(self,data):
        self.execute(command("create_link.sql"),data)
    def fetch_link(self,identifier):
        result = self.execute(command("fetch_link.sql"),{"identifier":identifier})
        return result
    def insert_into_data(self,data):
        result = self.execute(command("insert_data.sql"),data)
        return result
    def get_stats(self,identifier):
        result = self.execute(command("get_stats.sql"),{"identifier":identifier})
        return result
