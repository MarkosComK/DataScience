import pandas
import psycopg2 as psy


def connect_db(db_params):
	try:
		with psy.connect(**db_params) as connection:
			print(f"Connection successful {connection}")
			if connection.closed != 0:
				connection.close()
	except psy.connect as error:
		print(f"Connection failed {error}")

def open_file(file_path):
	with open(file_path, "r") as file:
		line = file.readline()
		print(line)

def __main__():
	db_params = {
		"dbname":"piscineds",
		"user":"marsoare",
		"password":"secret",
		"host":"localhost",
		"port":"5432"
	}
	open_file("../subject/customer/data_2022_dec.csv")
	connect_db(db_params)

__main__()

