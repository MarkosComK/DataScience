import pandas as pd
import psycopg2 as psy
from psycopg2 import extras

def connect_db(db_params, table_query, table_name, file):
	try:
		with psy.connect(**db_params) as connection:
			print(f"Connection successful {connection}")
			print("Creating table query")
			with connection.cursor() as cursor:
				# Create the table if it doesn't exist
				cursor.execute(table_query)

				# Prepare the insert query
				insert_query = f"INSERT INTO {table_name} ({', '.join(file.columns)}) VALUES %s"

				# Batch insert the data using psycopg2.extras.execute_values
				rows = [tuple(row) for index, row in file.iterrows()]
				extras.execute_values(cursor, insert_query, rows)

				print(f"Data from CSV inserted into the table '{table_name}' successfully.")

			if connection.closed != 0:
				connection.close()

	except psy.DatabaseError as error: # Catching the correct exception
		print(f"Connection failed: {error}")

def open_file(file_path: str):
	try:
		file = pd.read_csv(file_path)
		return file
	except Exception as error:
		print(f"Error while opening file: {error}")
		return None

def get_table_name(file, file_path):
		# generate file_name without .csv
		start = 0
		found = file_path.rfind("/") + 1
		if found != -1:
			start = found
		end = file_path.find(".csv")
		if start and end:
			table_name = file_path[start:end]
			create_table(table_name, file)
			return table_name

def create_table(table_name, file):
	#define column_types
	column_types = {
		'event_time': 'TIMESTAMP',
		'event_type': 'TEXT',
		'product_id': 'INTEGER',
		'price': 'DECIMAL',
		'user_id': 'INTEGER',
		'user_session': 'TEXT'
	}
	
	# Create table SQL query
	create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
	create_table_query += "event_time TIMESTAMP NOT NULL, "  # Add event_time as the first column
	create_table_query += ", ".join([f"{col} {column_types.get(col, 'TEXT')}" for col in file.columns if col != "event_time"])
	create_table_query += ");"

	return create_table_query

def __main__():
	db_params = {
		"dbname":"piscineds",
		"user":"marsoare",
		"password":"secret",
		"host":"localhost",
		"port":"5432"
	}
	file_path = "../subject/customer/data_2022_dec.csv"
	file = open_file(file_path)
	if file is not None:
		print(file.head(1)) #prints the first line of .CSV
		table_name = get_table_name(file, file_path)
		table_query = create_table(table_name, file)
		connect_db(db_params, table_query, table_name, file)
	else:
		print("An error ocurred with the file.")

__main__()

