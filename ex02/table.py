import pandas as pd
import psycopg2 as psy


def connect_db(db_params):
	try:
		with psy.connect(**db_params) as connection:
			print(f"Connection successful {connection}")
			if connection.closed != 0:
				connection.close()
	except psy.connect as error:
		print(f"Connection failed {error}")

def open_file(file_path: str):
	try:
		file = pd.read_csv(file_path)
		print(file.head(1)) #prints the first line of .CSV
		# generate file_name without .csv
		start = 0
		found = file_path.rfind("/") + 1
		if found != -1:
			start = found
		end = file_path.find(".csv")
		if start and end:
			table_name = file_path[start:end]
			return table_name
	except Exception as error:
		print(f"Error while opening file: {error}")

def __main__():
	db_params = {
		"dbname":"piscineds",
		"user":"marsoare",
		"password":"secret",
		"host":"localhost",
		"port":"5432"
	}
	table_name = open_file("../subject/customer/data_2022_dec.csv")
	print(f"Table name: {table_name}")
	connect_db(db_params)

__main__()

