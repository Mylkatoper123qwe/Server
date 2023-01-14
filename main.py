while True:
    import sqlite3

    enter = int(input("Ведіть суму: "))

    connection = sqlite3.connect('datavase.sl3', 5)
    cur = connection.cursor()

    # cur.execute('CREATE TABLE workers (name TEXT, surname TEXT,age INT,salary INT);')
    # connection.commit()

    # cur.execute(f"INSERT INTO workers (name, surname,age , salary) VALUES ('Oleg','Barbanov',32,500)")
    # connection.commit()

    # cur.execute(f"INSERT INTO workers (name, surname,age , salary) VALUES ('Dmitro','Borbdob',22,650)")
    # connection.commit()

    # cur.execute(f"INSERT INTO workers (name, surname,age , salary) VALUES ('Nazer','Gordon',26,400)")
    # connection.commit()

    # cur.execute(f"INSERT INTO workers (name, surname,age , salary) VALUES ('Taras','Chapik',29,700)")
    # connection.commit()

    # cur.execute(f"INSERT INTO workers (name, surname,age , salary) VALUES ('Marik','Perkanov',37,800)")
    # connection.commit()

    # cur.execute("SELECT rowid, name, surname, age, salary FROM workers")
    # connection.commit()
    # res = cur.fetchall()
    # print(res)

    connection.close()