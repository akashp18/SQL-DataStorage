import sqlite3

DB_NAME = "User.db"
connection = any


class DBHelper:

    def dbConnect(self):
        global connection
        connection = sqlite3.connect(DB_NAME)

    def dbClose(self):
        global connection
        connection.close()

    def insertUser(self, login, password):
        self.dbConnect()
        cursor = connection.cursor()
        insertQuery = "INSERT INTO TB_USER (LOGIN, CRYPTOGRAPHIC_PASSWORD) VALUES ('{}','{}');".format(login, password)
        cursor.execute(insertQuery)
        cursor.execute("COMMIT;")
        cursor.close()
        self.dbClose()

    def updateUser(self, login):
        self.dbConnect()
        cursor = connection.cursor()
        updateQuery = "UPDATE TB_USER SET ACCESS_COUNT = ACCESS_COUNT + 1 WHERE LOGIN = '{}'".format(login)
        cursor.execute(updateQuery)
        cursor.execute("COMMIT;")
        cursor.close()
        self.dbClose()

    def selectUser(self, login):
        self.dbConnect()
        cursor = connection.cursor()
        selectQuery = "SELECT CRYPTOGRAPHIC_PASSWORD,ACCESS_COUNT FROM TB_USER WHERE LOGIN = '{}';".format(login)
        cursor.execute(selectQuery)
        results = cursor.fetchall()
        cursor.close()
        self.dbClose()
        return results

    def selectAllUsers(self):
        self.dbConnect()
        cursor = connection.cursor()
        selectQuery = "SELECT * FROM TB_USER;"
        cursor.execute(selectQuery)
        results = cursor.fetchall()
        cursor.close()
        self.dbClose()
        return results
