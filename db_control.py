import os
import psycopg2


class DB:
    def __init__(self, database, host, user, password):
        conn = psycopg2.connect(database=database, host=host, user=user, password=password)
        self.conn = conn

    def get_connection(self):
        return self.conn

    def __del__(self):
        self.conn.close()


class UsersModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS karma
                                (id int,
                                username text,
                                karma int
                                )
                                 ''')
        cursor.close()
        self.connection.commit()

    def new_user(self, id, username):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO karma
                SELECT %d, '%s', 0
                WHERE NOT EXISTS (SELECT * FROM karma WHERE id = %d)''' % (id, username, id))
        self.connection.commit()

    def id_of_user(self, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id FROM karma WHERE username='%s'" % username)
        id = cursor.fetchone()
        if id is None:
            return 0
        else:
            return id[0]


class KarmaModel:
    def __init__(self, connection):
        self.connection = connection

    def current_karma(self, id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT karma FROM karma WHERE id = %d" % id)
        karma = cursor.fetchone()[0]
        return karma

    def karma_plus(self, id, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM karma WHERE id = %d" % id)
        user = cursor.fetchone()
        if user is None:
            cursor.execute("INSERT INTO karma VALUES (%d, '%s', 1)" % (id, username))
        else:
            karma = int(user[2]) + 1
            cursor.execute("UPDATE karma SET karma=%d WHERE id=%d" % (karma, id))
        self.connection.commit()

    def karma_minus(self, id, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM karma WHERE username = '%s'" % username)
        user = cursor.fetchone()
        karma = -1
        if user is None:
            cursor.execute("INSERT INTO karma VALUES (%d, '%s', -1)" % (id, username))
        else:
            karma = int(user[2]) - 1
            cursor.execute("UPDATE karma SET karma=%d WHERE id=%d" % (karma, id))
        self.connection.commit()
        if karma < -99:
            return 2
        else:
            return (1)

    def top20(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM karma")
        count = int(cursor.fetchone()[0])
        if count == 0:
            return "Нет пользователя в бд"
        else:
            if count > 20:
                count = 20
            top_list = "Лучшие с позитивным репом: "
            cursor.execute("SELECT * FROM karma ORDER BY karma DESC LIMIT 20")
            top20 = cursor.fetchall()
            for i in range(count):
                top_list += "\n" + str(int(i + 1)) + ". @" + "[" + str(top20[i][1]) + "]" + " с репом " + str(
                    top20[i][2]) + "."
            return top_list

    def untop20(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM karma")
        count = int(cursor.fetchone()[0])
        if count == 0:
            return "Нет в бд"
        else:
            if count > 20:
                count = 20
            top_list = "Отсосники: "
            cursor.execute("SELECT * FROM karma ORDER BY karma LIMIT 20")
            top20 = cursor.fetchall()
            for i in range(count):
                top_list += "\n" + str(int(i + 1)) + ". @" + "[" + str(top20[i][1]) + "]" + " с репом " + str(
                    top20[i][2]) + "."
            return top_list
