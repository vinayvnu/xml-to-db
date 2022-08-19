import mysql.connector
from mysql.connector import Error

class DBHandler:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost',
                                                  database='arbor',
                                                  user='root',
                                                  password='password'
                                                  )

        self.__curosr = self.connection.cursor(dictionary=True)
        #print("COnnection established")

    def __close(self):
        try:
            c = self.__curosr
            c.close()
        except Error as e:
            print("Error while connecting to MySQL", e)

    def close(self):
        self.__close()

    def executeQuery(self, query, args=None, size=None):
        c = self.__curosr
        try:
            c.execute(query, args)
            self.connection.commit()
        except Error as e:
            print("Error while connecting to MySQL", e)
        #return(c.fetchall())
