import sqlite3

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

