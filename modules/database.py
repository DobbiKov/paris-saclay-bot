import sqlite3

class Database:
    def __init__(self):
        self.connect()
        self.create_users_table_if_doesnt_exist()
    def connect(self):
        conn = sqlite3.connect('users.db')
        self.conn = conn

    def create_users_table_if_doesnt_exist(self):
        check_sql = self.conn.execute("PRAGMA table_info(USERS)")
        check_sql = check_sql.fetchall()
        check_table = [c for c in check_sql]

        if len(check_table) == 4:
            print("Table users was found!")
        else:
            self.conn.execute("CREATE TABLE USERS\
                    (ID INTEGER PRIMARY KEY         AUTOINCREMENT,\
                    USER_ID        INT          NOT NULL,\
                    NICKNAME       TEXT,\
                    FORMATION          TEXT);")
        
    def get_user(self, user_id):
        cursor = self.conn.execute(f"SELECT ID, USER_ID, NICKNAME, FORMATION from USERS WHERE USER_ID = ?", [user_id])
        data = {}
        for row in cursor:
            if row[0] == "" or row[0] == None:
                return None
            
            data['ID'] = row[0]
            data['USER_ID'] = row[1]
            data['NICKNAME'] = row[2]
            data['FORMATION'] = row[3]
        return data
    
    def get_users(self):
        cursor = self.conn.execute(f"SELECT ID, USER_ID, NICKNAME, FORMATION from USERS")
        data = []
        for row in cursor:
            if row[0] == "" or row[0] == None:
                return None
            
            user = {}
            user['ID'] = row[0]
            user['USER_ID'] = row[1]
            user['NICKNAME'] = row[2]
            user['FORMATION'] = row[3]
            data.append(user)
        return data
        
    
    def create_user(self, user_id, nickname, formation="L1-MI3"):
        if formation is None or formation == "":
            formation = "L1-MI3"
        self.conn.execute(f"INSERT INTO USERS (USER_ID,NICKNAME,FORMATION) VALUES (?, ?, ?)", [user_id, nickname, formation])
        self.conn.commit()

    def update_user_formation(self, user_id, formation):
        if formation is None or formation == "":
            formation = "L1-MI3"
        self.conn.execute(f"UPDATE USERS set FORMATION = ? where USER_ID = ?", [formation, user_id])
        self.conn.commit()
