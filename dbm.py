import sqlite3

def command(filename):
    with open("sql/"+filename,"r") as f:
        query = f.read()
        return query

class Dbm:

    def execute(self, sql_command, params_dict=None): #using type hints for the first time! 
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            if params_dict:
                result = cursor.execute(sql_command, params_dict)
            else:
                result = cursor.execute(sql_command)
            data = result.fetchall()
            conn.commit()
            conn.close()
            return data
        except sqlite3.Error as e:
            print("SQLite error:", e)
            return None

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
