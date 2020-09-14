import psycopg2 as pg
import weijieWeb.settings as settings

connection = settings.CONNECTION_PG
cursor = connection.cursor()

# Print PostgreSQL Connection properties
print ( connection.get_dsn_parameters(),"\n")

# Print PostgreSQL version
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")

cursor.execute("SELECT * FROM public.users;")
record = cursor.fetchone()
print("You are watching users - ", record,"\n")
