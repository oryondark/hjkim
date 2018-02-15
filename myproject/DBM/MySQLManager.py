import MySQLdb
import QueryModel

class MySQLDBM:

    def dbconnector(HOST, USER, PASSWD, DBPATH):
        db = MySQLdb.connect(host = HOST,
                             user = USER,
                             passwd = PASSWD,
                             db = DBPATH)

        return db

    def dbExecute(idx, arg1, arg2):
        

        
