import pandas
import psycopg2 as psy


def connect_db(db_params):
	connection = psy.connect(**db_params)
	print(f"Connection successful {connection}")
	connection.close()

def __main__():
	db_params = {
		"dbname":"piscineds",
		"user":"marsoare",
		"password":"secret",
		"host":"localhost",
		"port":"5432"
	}
	connect_db(db_params)

__main__()
