from flask import current_app           # Points to the current flask object handling the request
import mysql.connector                  # MySQL database to store script contents/json
from mysql.connector import errorcode   # Error codes for MySQL

def check_database():
    """
    Creates the necessary database if it does not already exist
    :return:
    """

    # Connects to the mysql database using the supplied credentials
    try:
        connector = mysql.connector.connect(user=current_app.config['DATABASE_USERNAME'],
                                            password=current_app.config['DATABASE_PASSWORD'],
                                            host=current_app.config['DATABASE_HOST'])
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            print("Username={}".format(current_app.config['DATABASE_USERNAME']))
            print("password={}".format(current_app.config['DATABASE_PASSWORD']))
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    cursor = connector.cursor(prepared=True)  # Enables the execution of a prepared statement


    statement = ("CREATE DATABASE IF NOT EXISTS %s")

    # Creates the database if it doesn't already exist
    cursor.execute(statement, (current_app.config['DATABASE_NAME'],))



def open_database():
    """
    Returns a tuple of a connection and cursor to the database
    :return:
    """

    # Connects to the mysql database using the supplied credentials
    try:
        connector = mysql.connector.connect(user=current_app.config['DATABASE_USERNAME'],
                                                 password=current_app.config['DATABASE_PASSWORD'],
                                                 host=current_app.config['DATABASE_HOST'],
                                                 database=current_app.config['DATABASE_NAME'])
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            print("Username={}".format(current_app.config['DATABASE_USERNAME']))
            print("password={}".format(current_app.config['DATABASE_PASSWORD']))
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    cursor = connector.cursor(prepared=True)  # Enables the execution of a prepared statement

    return connector, cursor


def close_database(connector, cursor):
    """
    Closes the connection from the cursor and the database if they exist
    :param connector:
    :param cursor:
    :return:
    """
    if cursor:
        cursor.close()
    if connector:
        connector.close()

def check_tables():
    db_conn, db_cursor = open_database()

    statement = ("CREATE TABLE IF NOT EXISTS bugs ("
                 "int id UNSIGNED AUTO INCREMENT"
                 "VARCHAR(100) name NOT NULL"
                 "VARCHAR(500) description"
                 "SMALLINT priority NOT NULL)")

    close_database()

def createBug(name, description, priority):
    """"""
    db_conn, db_cursor = open_database()

    statement = ("INSERT INTO bugs "
                 "(address, city, state, zip) "
                 "VALUES (%s, %s, %s, %s)")
    db_cursor.execute(statement, (address, city, state, zip))
    db_conn.commit()

    propertyId = db_cursor.lastrowid

    close_database(db_conn, db_cursor)
    return propertyId