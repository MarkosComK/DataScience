import pandas
import psycopg2 as psy


def connect_db():
	connection = psy.connect(
		dbname="piscineds",
		user="marsoare",
		password="secret",
		host="localhost",
		port="5432"
	)
	print(f"Connection successful {connection}")
	connection.close()

def __main__():
	connect_db()

__main__()
