import mysql.connector
import json


class MySql:
      
    def getConnection(self):
        
        #Move the connection detail to config file
        return mysql.connector.connect(
            host = 'localhost',
            user =  'root',
            password = 'teamat',
            database = 'driverdb'
        )

    def dataInsert(self,data):
        conn = self.getConnection()
        data = (data)
        print("Data receives is ",data)
        cur = conn.cursor()
        s = ("INSERT INTO table1 VALUE (%s,%s,%s,%s,%s,%s)")
        #data = (1,2,3,4,5,6)
        #try:
        # Executing the SQL command
        cur.execute(s,data)

        # Commit your changes in the database
        conn.commit()
        conn.close()
        # print("Data inserted")

        # except:
        #    # Rolling back in case of error
        #    conn.rollback()
        #    print("ss")



