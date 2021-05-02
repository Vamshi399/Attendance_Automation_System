import mysql.connector
class DBConnection:
    @staticmethod
    def getConnection():
        database = mysql.connector.connect(host="localhost", user="root", passwd="2277", db='automaticattendance')
        return database
if __name__=="__main__":
    print(DBConnection.getConnection())