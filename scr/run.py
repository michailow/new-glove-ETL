import pandas as pd
import sqlite3


def makeConnection(dbPath):
    """
    Create connection to DB
    """
    connection = sqlite3.connect(dbPath)
    cursor = connection.cursor()
    return connection, cursor


def createTables(filepath, cursor):
    """
    Opens script and creates tables
    """
    with open(filepath, 'r') as sql_file:
        sqlScript = sql_file.read()

    cursor.executescript(sqlScript)


def main():
    connection, cursor = makeConnection('db/newglobe.db')

    df = pd.read_csv("data/PupilData.csv")
    dfFactTable = df[["PupilID", "FirstName", "MiddleName", "LastName"]].drop_duplicates()
    dfAttendance = pd.read_csv("data/PupilAttendance.csv")
    dfGrade = df[['SnapshotDate', 'PupilID', 'GradeId']]
    dfStream = df[['SnapshotDate', 'PupilID', 'Stream']]
    dfStatus = df[['SnapshotDate', 'PupilID', 'Status']]

    createTables('db/tables.sql', cursor)

    dfFactTable.to_sql('student', connection, if_exists='replace', index=False)
    dfAttendance.to_sql('attendance', connection, if_exists='replace', index=False)
    dfGrade.to_sql('grade', connection, if_exists='replace', index=False)
    dfStream.to_sql('stream', connection, if_exists='replace', index=False)
    dfStatus.to_sql('status', connection, if_exists='replace', index=False)

    connection.commit()


if __name__ == '__main__':
    main()