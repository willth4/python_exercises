import sqlite3

# Tutorial: https://python-programmieren.com/sqlite-datenbank/

def createdb():
    # Erstellen und öffnen von neuer Datenbank
    db = sqlite3.connect("NeueDatanbank.db")
    db.close()
    # Öffnen von existierender Datenbank
    db = sqlite3.connect("file:NeueDatanbank.db?mode=rwc", uri=True)
    db.close()

def createtable():
    # Öffnen von Datenbank
    db = sqlite3.connect("NeueDatanbank.db")
    cursor = db.cursor()
    # Kommando
    sql_command = """
    CREATE TABLE employee ( 
    id INTEGER PRIMARY KEY, 
    fname VARCHAR(20), 
    lname VARCHAR(30));"""
    # Ausführen
    cursor.execute(sql_command)
    # Speichern
    db.commit()
    # Schließen
    db.close()

def droptable():
    # Öffnen von existierender Datenbank
    db = sqlite3.connect("NeueDatanbank.db")
    cursor = db.cursor()
    # Kommando
    sql_command = """DROP TABLE employee;"""
    # Ausführen
    cursor.execute(sql_command)
    # Speichern
    db.commit()
    # Schließen
    db.close()

def writetable():
    # Datenbank öffnen
    db = sqlite3.connect("NeueDatanbank.db")
    cursor = db.cursor()
    employees = [("Tom", "Peter"),
                 ("Aldi", "Süd"),
                 ("Aldi", "Nord")]
    for e in employees:
        format_str = """INSERT INTO employee (id, fname, lname)
        VALUES (NULL, "{first}", "{last}");"""
        sql_command = format_str.format(first=e[0], last=e[1])
        cursor.execute(sql_command)
    # Speichern
    db.commit()
    # Schließen
    db.close()

def selectall():
    # Öffnen von existierender Datenbank
    db = sqlite3.connect("NeueDatanbank.db")
    cursor = db.cursor()
    # Sqlite Kommando
    sql_command = """SELECT * FROM employee"""

    # Ausführen
    cursor.execute(sql_command)
    result = cursor.fetchall()
    for r in result:
        print(r)
    # Speichern
    db.commit()
    # Schließen
    db.close()


if __name__ == '__main__':
    # createdb()
    # createtable()
    # droptable()
    # writetable()
    selectall()
