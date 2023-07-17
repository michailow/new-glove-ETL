DROP TABLE IF EXISTS student;
CREATE TABLE student(
    PupilID    INTEGER PRIMARY KEY,
    FirstName  TEXT,
    MiddleName TEXT,
    LastName   TEXT
);


DROP TABLE IF EXISTS attendance;
CREATE TABLE attendance(
    Date       INTEGER,
    PupilID    TEXT,
    Attendance TEXT,
    FOREIGN KEY(PupilID) REFERENCES student(PupilID)
);


DROP TABLE IF EXISTS grade;
CREATE TABLE grade(
    Date       INTEGER,
    PupilID    TEXT,
    GradeId    INTEGER,
    FOREIGN KEY(PupilID) REFERENCES student(PupilID)
);

DROP TABLE IF EXISTS stream;
CREATE TABLE stream(
    Date       INTEGER,
    PupilID    TEXT,
    Stream     TEXT,
    FOREIGN KEY(PupilID) REFERENCES student(PupilID)
);

DROP TABLE IF EXISTS status;
CREATE TABLE status(
    Date       INTEGER,
    PupilID    TEXT,
    Status     TEXT,
    FOREIGN KEY(PupilID) REFERENCES student(PupilID)
);
