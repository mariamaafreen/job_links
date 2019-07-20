import psycopg2

conn = psycopg2.connect(
            host = "localhost",
            database = "job",
            user = "postgres",
            password = "minu")

c = conn.cursor()



c.execute("SELECT * from jobs")

print(c.fetchall())


conn.commit()

conn.close()
