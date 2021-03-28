from gateway import utility



def create_bug(name, description, priority):
    """"""
    db_conn, db_cursor = utility.open_database()

    statement = ("INSERT INTO bugs "
                 "(bugName, description, priority) "
                 "VALUES (%s, %s, %s)")
    db_cursor.execute(statement, (name, description, priority))
    db_conn.commit()

    bugID = db_cursor.lastrowid

    utility.close_database(db_conn, db_cursor)
    return bugID

def get_bugs():
    db_conn, db_cursor = utility.open_database()
    bugs = []

    # MySql statement to get everything from a table
    statement = ("SELECT * FROM bugs")

    # Execute statement
    db_cursor.execute(statement)

    for bug in db_cursor:
        bugs.append(bug)

    utility.close_database(db_conn, db_cursor)

    return bugs
