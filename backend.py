import sqlite3

def create_tables(conn: sqlite3.Connection):
    conn.execute('''
    CREATE TABLE IF NOT EXISTS Shelters (
        CenterNo INT NOT NULL PRIMARY KEY,
        Address VARCHAR(255)
    );''')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS Employee (
        EmployeeID INT PRIMARY KEY,
        CenterNo INT,
        Username VARCHAR(50) UNIQUE,
        Password VARCHAR(255),
        FOREIGN KEY (CenterNo) REFERENCES Shelters(CenterNo)
    );''')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS Adopters (
        AdopterID INT PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        Address VARCHAR(255),
        PhoneNo VARCHAR(20),
        Preference VARCHAR(100)
    );''')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS Pets (
        PetID INT PRIMARY KEY,
        Name VARCHAR(50),
        Sex CHAR(1),
        CenterNo INT,
        FOREIGN KEY (CenterNo) REFERENCES Shelters(CenterNo)
    );''')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS Animal_Details (
        PetID INT PRIMARY KEY,
        Species VARCHAR(50),
        Breed VARCHAR(50),
        FOREIGN KEY (PetID) REFERENCES Pets(PetID)
    );''')

    conn.execute('''
    CREATE TABLE IF NOT EXISTS Medical_History (
        PetID INT PRIMARY KEY,
        Status VARCHAR(50),
        Age INT,
        VaccinationHistory TEXT,
        ChipStatus VARCHAR(50),
        FOREIGN KEY (PetID) REFERENCES Pets(PetID)
    );''')

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
    );''')

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
    );''')

    conn.commit()

def database_info(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables:", [table[0] for table in tables if table[0] != 'sqlite_sequence'])
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

def main():
    conn = sqlite3.connect('pet_adoption')
    create_tables(conn)

    tables = database_info(conn)
    for table in tables:
        print(table_info(conn, table))
    # cursor = conn.cursor()
    # s = cursor.execute("SELECT * FROM sqlite_master;")
    # for i in s:
        # print(i)

if __name__ == "__main__":
    main()
