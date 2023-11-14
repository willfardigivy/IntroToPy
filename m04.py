import sqlite3

# required stuff
connection = sqlite3.connect("StudentDB.db")
cursor = connection.cursor()

# makes the tables
cursor.execute("""CREATE TABLE IF NOT EXISTS studentInfo_table(             
               studentId REAL, 
               firstName TEXT,
               lastName TEXT,
               email TEXT,
               programId REAL
                )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS program_table(             
               programId REAL, 
               programName TEXT,
               departmentId REAL
                )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS department_table(             
               departmentId REAL, 
               departmentName TEXT
                )""")

# statements for students
cursor.execute("""INSERT INTO studentInfo_table(studentId,firstname,lastname,email,programId)
               VALUES(123456,'John','Doe','jdoe@ivytech.edu',101)""")
cursor.execute("""INSERT INTO studentInfo_table(studentId,firstname,lastname,email,programId)
               VALUES(468424,'Jane','Doe','jdoe2@ivytech.edu',101)""")
cursor.execute("""INSERT INTO studentInfo_table(studentId,firstname,lastname,email,programId)
               VALUES(408843,'Brian','Guy','bguy@ivytech.edu',102)""")
cursor.execute("""INSERT INTO studentInfo_table(studentId,firstname,lastname,email,programId)
               VALUES(976424,'Lucas','White','lwhite@ivytech.edu',201)""")
cursor.execute("""INSERT INTO studentInfo_table(studentId,firstname,lastname,email,programId)
               VALUES(399912,'Penelope','Adams','padams@ivytech.edu',102)""")

#statements for programs
cursor.execute("""INSERT INTO program_table(programId,programName,departmentId)
               VALUES(101,"Intro to Something or Other",090)""")
cursor.execute("""INSERT INTO program_table(programId,programName,departmentId)
               VALUES(102,"Intro to Whatchamacallit",090)""")
cursor.execute("""INSERT INTO program_table(programId,programName,departmentId)
               VALUES(201,"Advanced Something or Other",090)""")

#statement for department
cursor.execute("""INSERT INTO department_table(departmentId,departmentName)
               VALUES(090,"Whozeewhatzit")""")

# get it to print everything
cursor.execute("SELECT * from studentInfo_table")
print(cursor.fetchall())
cursor.execute("SELECT * from program_table")
print(cursor.fetchall())
cursor.execute("SELECT * from department_table")
print(cursor.fetchall())

# wrapping everything up
connection.commit()
connection.close()