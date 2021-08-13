import mysql.connector


class MySQLFcm:
    def __init__(self):
        self.host = "localhost"
        self.database = "api"
        self.user = "root"
        self.password = ""

        self.con = mysql.connector.connect(host=self.host, database=self.database, user=self.user,
                                           password=self.password)

        if self.con.is_connected():
            db_info = self.con.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            self.cursor = self.con.cursor()

    def setDevice(self, pns, device_register):
        sql = "UPDATE  user SET device_register=%s WHERE pns_id=%s "
        self.query(sql, (pns, device_register))
        print(self.cursor.rowcount, "record inserted")

    def getDevice(self, pns):
        sql = "SELECT device_register, first_name, last_name FROM user WHERE pns_id= %s"
        self.query(sql, (pns,))

    def getAllDevice(self):
        sql = "SELECT device_register, first_name, last_name ," \
              "CASE WHEN HOUR(NOW()) > 6  AND HOUR(NOW()) <= 11 THEN 1 ELSE 0 END AS `pagi`," \
              "CASE WHEN HOUR(NOW()) > 11 AND HOUR(NOW()) <= 12 THEN 1 ELSE 0 END AS `siang`," \
              "CASE WHEN HOUR(NOW()) > 12 AND HOUR(NOW()) <= 18 THEN 1 ELSE 0 END AS `sore`," \
              "CASE WHEN HOUR(NOW()) > 18 THEN 1 ELSE 0 END AS `lembur`," \
              "CASE WHEN HOUR(NOW()) <= 6  THEN 1 ELSE 0 END AS `absen`" \
              "FROM user WHERE  device_register IS NOT NULL"
        self.query(sql)

    def updateDevice(self, pns, device_register):
        sql = "UPDATE  user SET device_register=%s WHERE pns_id=%s "
        self.query(sql, (pns, device_register))
        print("record update")

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def num_rows(self):
        return self.cursor.rowcount

    def result(self):
        return self.cursor.fetchall()

    def row(self):
        return self.cursor.fetchone()

    def commit(self):
        self.con.commit()

    def close(self, commit=True):
        if commit:
            self.commit()

        if self.con.is_connected():
            self.cursor.close()
            self.con.close()
            print("MySQL connection is closed")
