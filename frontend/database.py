import sqlite3
import random

def create_tables(conn: sqlite3.Connection):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Shelter (
            CenterNo INT NOT NULL PRIMARY KEY,
            Address VARCHAR(255)
        );'''
    )

    # TODO Username -> Email
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Employee (
            EmployeeID INT PRIMARY KEY,
            CenterNo INT,
            FirstName VARCHAR(50),
            LastName VARCHAR(50),
            Email VARCHAR(255) UNIQUE, 
            Password VARCHAR(255),
            FOREIGN KEY (CenterNo) REFERENCES Shelters(CenterNo)
        );'''
    )

    conn.execute('''
        CREATE TABLE IF NOT EXISTS Adopter (
            AdopterID INT PRIMARY KEY,
            FirstName VARCHAR(50),
            LastName VARCHAR(50),
            Address VARCHAR(255),
            PhoneNo VARCHAR(20),
            Preference VARCHAR(100),
            Email VARCHAR(255) UNIQUE, 
            Password VARCHAR(255)
        );'''
    )

    conn.execute('''
        CREATE TABLE IF NOT EXISTS Pet (
            PetID INT PRIMARY KEY,
            Name VARCHAR(50),
            Sex CHAR(1),
            CenterNo INT,
            FOREIGN KEY (CenterNo) REFERENCES Shelters(CenterNo)
        );'''
    )

    conn.execute('''
        CREATE TABLE IF NOT EXISTS Animal_Detail (
            PetID INT PRIMARY KEY,
            Species VARCHAR(50),
            Breed VARCHAR(50),
            FOREIGN KEY (PetID) REFERENCES Pets(PetID)
        );'''
    )

    conn.execute('''
        CREATE TABLE IF NOT EXISTS Medical_History (
            PetID INT PRIMARY KEY,
            Status VARCHAR(50),
            Age INT,
            VaccinationHistory TEXT,
            ChipStatus VARCHAR(50),
            FOREIGN KEY (PetID) REFERENCES Pets(PetID)
        );'''
    )

    conn.execute('''
        CREATE TABLE IF NOT EXISTS Adoption_Details (
            AdoptionID INTEGER PRIMARY KEY AUTOINCREMENT,
            PetID INT,
            AdopterID INT,
            WhenAdopted DATE,
            CenterNo INT,
            FOREIGN KEY (PetID) REFERENCES Pets(PetID),
            FOREIGN KEY (AdopterID) REFERENCES Adopters(AdopterID),
            FOREIGN KEY (CenterNo) REFERENCES Shelters(CenterNo)
        );'''
    )

    conn.execute('''
        CREATE TABLE IF NOT EXISTS Long_Term_Daycare (
            PetID INT,
            AdopterID INT,
            FromDate DATE,
            ToDate DATE,
            CenterNo INT,
            PRIMARY KEY (PetID, AdopterID),
            FOREIGN KEY (PetID) REFERENCES Pets(PetID),
            FOREIGN KEY (AdopterID) REFERENCES Adopters(AdopterID),
            FOREIGN KEY (CenterNo) REFERENCES Shelters(CenterNo)
        );'''
    )

    conn.commit()

def database_info(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [table[0] for table in tables if table[0] != 'sqlite_sequence']

def table_info(conn: sqlite3.Connection, table_name: str):
    cursor = conn.execute(f"PRAGMA table_info({table_name})")
    s = f"{table_name}\n"
    for row in cursor:
        s += ' '.join([str(i) for i in row]) + '\n'
    return s

def view_data(conn: sqlite3.Connection, table_name: str):
    cursor = conn.execute(f"SELECT * FROM {table_name}")
    s = f"{table_name}"
    for row in cursor:
        s += ' '.join([str(i) for i in row]) + '\n'
    return s

def insert_record(conn: sqlite3.Connection, table_name: str, a, b, c, d):
    conn.execute(f"""INSERT INTO {table_name} (NAME, BREED, CENTER_NO, PET_TYPE)
                    VALUES (?,?,?,?)""", (a, b, c, d))
    conn.commit()

def get_pet_ids(conn: sqlite3.Connection):
    cursor: sqlite3.Cursor = conn.execute(f"SELECT PetID FROM Pet")
    return [id[0] for id in cursor.fetchall()]

def get_pet_details(conn: sqlite3.Connection, petid: str):
    cursor: sqlite3.Cursor = conn.execute(
        f"""SELECT 
            p.Name,
            mh.Age,
            p.Sex,
            ad.Breed,
            s.Address
        FROM Pet as p 
        JOIN Shelter as s ON p.CenterNo=s.CenterNo 
        JOIN Animal_Detail as ad ON p.PetID=ad.PetID
        JOIN Medical_History as mh ON p.PetID=mh.PetID 
        WHERE p.PetID=?;""", (petid, )
    )
    return cursor.fetchone()

def get_all_pets_details():
    conn = sqlite3.connect('pet_adoption')
    petids = get_pet_ids(conn=conn)

    details = []
    for petid in petids:
        d = get_pet_details(conn, petid)
        if d is not None:
            row = (*d, f"{petid}.jpg")
            row = tuple(map(str, row))
            details.append(row)
    conn.close()
    return details

def add_adopter(fname, lname, address, phno, pref, email, password):
    conn = sqlite3.connect('pet_adoption')
    cursor = conn.execute(f"""SELECT AdopterID FROM Adopter ORDER BY rowid DESC LIMIT 1;""")
    id = int(cursor.fetchone()[0]) + 1
    conn.execute(f"""INSERT INTO Adopters (AdopterID FirstName LastName Address PhoneNo Preference, Email, Password)
        (?, ?, ?, ?, ?, ?, ?, ?)""",
        (id, fname, lname, address, phno, pref, email, password)
    )
    conn.commit()

def add_employee(centerno, fname, lname, email, password, address ): #TODO implement this 
    pass

def new_shelter(fname, lname, email, password, address):
    conn = sqlite3.connect('pet_adoption')
    cursor = conn.execute(f"""SELECT EmployeeID FROM Employee ORDER BY EmployeeID DESC LIMIT 1;""")
    id = int(cursor.fetchone()[0]) + 1
    cursor = conn.execute(f"""SELECT CenterNo FROM Shelters ORDER BY CenterNo DESC LIMIT 1;""")
    cno = int(cursor.fetchone()[0]) + 1
    conn.execute(f"""INSERT INTO Shelters (CenterNo, Address) VALUES (?, ?)""", (cno, address))
    conn.execute(f"""INSERT INTO Employee (EmployeeID, CenterNo, FirstName, LastName, Email, Password) VALUES
        (?, ?, ?, ?)""",
        (id, cno, fname, lname, email, password)
    )
    conn.commit()
    conn.close()

def login(email, password) -> tuple[str, str] | None: 
    conn = sqlite3.connect('pet_adoption')
    cursor = conn.execute(f"""SELECT EmployeeID FROM Employee WHERE Email=? AND Password=?""", (email, password))
    empid = cursor.fetchone()
    empid = str(empid[0]) if empid else None
    if empid:
        return (empid, "empl")
    
    cursor = conn.execute(f"""SELECT AdopterID FROM Adopter WHERE Email=? AND Password=?""", (email, password))
    adid = cursor.fetchone()
    adid = str(adid[0]) if adid else None
    if adid:
        return (adid, "adpt")
    cursor.close()
    conn.close
    return None

if __name__ == "__main__": #TODO Make dummy data for the new tables
    conn = sqlite3.connect('pet_adoption')
    create_tables(conn)
    db_info = database_info(conn)
    print(db_info)
    for table in db_info:
        print(table_info(conn, table))

    # cursor = conn.cursor()
    # s = cursor.execute("SELECT * FROM sqlite_master;")
    # for i in s:
        # print(i)