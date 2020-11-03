import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn
            
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def createDB():
    database = r"fly.db"

    tabla_piloto = """ CREATE TABLE IF NOT EXISTS PILOTO (
                                        idPiloto integer,
                                        nombre text NOT NULL,
                                        horasVuelo integer NOT NULL
                                    ); """

    tabla_pasajero = """CREATE TABLE IF NOT EXISTS PASAJERO (
                                    cedulaPasajero integer,
                                    nombre text NOT NULL,
                                    edad integer NOT NULL,
                                    genero integer NOT NULL,
                                    nroVuelo integer NOT NULL,
                                    PRIMARY KEY (cedulaPasajero,nroVuelo)
                                );"""
    tabla_vuelo = """CREATE TABLE IF NOT EXISTS VUELO (
                                numeroVuelo integer,
                                ciudadSalida text NOT NULL,
                                ciudadLlegada text NOT NULL,
                                numeroPuestos integer NOT NULL,
                                idPiloto integer NOT NULL,
                                idPasajero integer NOT NULL,
                                PRIMARY KEY (numeroVuelo,idPasajero),
                                FOREIGN KEY (idPiloto) REFERENCES PILOTO (idPiloto),
                                FOREIGN KEY (idPasajero) REFERENCES PASAJERO (cedulaPasajero)

                            );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # crear tabla piloto
        create_table(conn, tabla_piloto)

        # crear tabla pasajero
        create_table(conn, tabla_pasajero)

        # crear tabla vuelo
        create_table(conn, tabla_vuelo)
    else:
        print("Error! cannot create the database connection.")

def crearPasajero(pasajero):
    database = r"fly.db"
    conn = create_connection(database)
    sql = ''' INSERT INTO PASAJERO (cedulaPasajero,nombre,edad,genero,nroVuelo)
              VALUES(?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, pasajero)
    conn.commit()

    return cur.lastrowid

def crearPiloto(piloto):
    database = r"fly.db"
    conn = create_connection(database)
    sql = ''' INSERT INTO PILOTO (idPiloto,nombre,horasVuelo)
              VALUES(?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, piloto)
    conn.commit()

    return cur.lastrowid

def insertarVuelo(vuelo):
    database = r"fly.db"
    conn = create_connection(database)
    sql = ''' INSERT INTO VUELO (numeroVuelo,ciudadSalida,ciudadLlegada,numeroPuestos,idPiloto,idPasajero)
              VALUES(?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, vuelo)
    conn.commit()

    return cur.lastrowid
#createDB()

#crearPasajero((123,"Juan",20,0,1234456))
#crearPasajero((123,"Juan",20,0,4444))

def query(sql):
    database = r"fly.db"
    conn = create_connection(database)
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()

    for row in rows:
        print(row)