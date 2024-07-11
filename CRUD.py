# Creacion de CRUD asociado a la obtencion de la informacion.

import db
DATABASE_NAME = "tarea3emergentes"

### ------------------------------------------------------------------------------------------------------------------------------------- ###
###                                                             Location                                                                  ###
def getalldata_Location():
    db = db.get_db(DATABASE_NAME)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Location")
    rows = cursor.fetchall()
    db.close()
    return rows

def getdata_Location(id):
    db = db.get_db(DATABASE_NAME)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Location WHERE id = ?", [id])
    rows = cursor.fetchone()
    db.close()
    return rows

def setLocation(id, name, address, phone, email): # Update Location
    db = db.get_db(DATABASE_NAME)
    cursor = db.cursor()

    cursor.execute("INSERT INTO Location (id, name, address, phone, email) VALUES (?, ?, ?, ?, ?)", (id, name, address, phone, email))
    db.commit()
    return True

def deleteLocation(id): # Delete Location
    db = db.get_db(DATABASE_NAME)
    cursor = db.cursor()

    cursor.execute("DELETE FROM Location WHERE id = ?", [id])
    db.commit()
    return True

### ------------------------------------------------------------------------------------------------------------------------------------- ###
###                                                             Sensor                                                                    ###

def getalldata_Sensor():
    db = db.get_db(DATABASE_NAME)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Sensor")
    rows = cursor.fetchall()
    db.close()
    return rows

def getdata_Sensor(id):
    db = db.get_db(DATABASE_NAME)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Sensor WHERE id = ?", [id])
    rows = cursor.fetchone()
    db.close()
    return rows

def setSensor(id, name, type, location_id): # Update Sensor
    db = db.get_db(DATABASE_NAME)
    cursor = db.cursor()

    cursor.execute("INSERT INTO Sensor (id, name, type, location_id) VALUES (?, ?, ?, ?)", (id, name, type, location_id))
    db.commit()
    return True

def deleteSensor(id): # Delete Sensor
    db = db.get_db(DATABASE_NAME)
    cursor = db.cursor()

    cursor.execute("DELETE FROM Sensor WHERE id = ?", [id])
    db.commit()
    return True

### ------------------------------------------------------------------------------------------------------------------------------------- ###
###                                                      Sensor Data                                                                      ###

def getalldata_SensorData():
    db = db.get_db(DATABASE_NAME)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM SensorData")
    rows = cursor.fetchall()
    db.close()
    return rows

def getdata_SensorData(id):
    db = db.get_db(DATABASE_NAME)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM SensorData WHERE id = ?", [id])
    rows = cursor.fetchone()
    db.close()
    return rows

def setSensorData(id, sensor_id, value, date): # Update SensorData
    db = db.get_db(DATABASE_NAME)
    cursor = db.cursor()

    cursor.execute("INSERT INTO SensorData (id, sensor_id, value, date) VALUES (?, ?, ?, ?)", (id, sensor_id, value, date))
    db.commit()
    return True

def deleteSensorData(id): # Delete SensorData
    db = db.get_db(DATABASE_NAME)
    cursor = db.cursor()

    cursor.execute("DELETE FROM SensorData WHERE id = ?", [id])
    db.commit()
    return True
