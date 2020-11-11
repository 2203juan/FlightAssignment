import sqlite3
from sqlite3 import Error

database = r"fly.db"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = sqlite3.connect(db_file)
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


def create_data_base():

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

    tabla_admin = """CREATE TABLE IF NOT EXISTS ADMIN (
                                correo text NOT NULL,
                                clave text NOT NULL
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

        # crear tabla administradores
        create_table(conn, tabla_admin)

    else:
        print("Error! cannot create the database connection.")

def crear_pasajero(pasajero):
    conn = create_connection(database)
    sql = ''' INSERT INTO PASAJERO (cedulaPasajero,nombre,edad,genero,nroVuelo)
              VALUES(?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, pasajero)
    conn.commit()

    return cur.lastrowid

def crear_piloto(piloto):
    conn = create_connection(database)
    sql = ''' INSERT INTO PILOTO (idPiloto,nombre,horasVuelo)
              VALUES(?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, piloto)
    conn.commit()

    return cur.lastrowid

def insertar_vuelo(vuelo):
    conn = create_connection(database)
    sql = ''' INSERT INTO VUELO (numeroVuelo,ciudadSalida,ciudadLlegada,numeroPuestos,idPiloto,idPasajero)
              VALUES(?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, vuelo)
    conn.commit()

    return cur.lastrowid

def insertar_admin(admin):
    conn = create_connection(database)
    sql = ''' INSERT INTO ADMIN (correo,clave)
              VALUES(?,?) '''

    cur = conn.cursor()
    cur.execute(sql, admin)
    conn.commit()

    return cur.lastrowid


def query(sql):
    conn = create_connection(database)
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()

    return rows

create_data_base()
