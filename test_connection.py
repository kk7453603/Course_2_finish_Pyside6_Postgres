import psycopg2
host = "127.0.0.1"
user="postgres"
password = "Maxim2007"
db_name = "test"

try:
    conn=psycopg2.connect(host=host,user=user,password=password,database=db_name)
    with conn.cursor() as curs:
        curs.execute('''SELECT * FROM full_purchase;

''')

        res = curs.fetchall()
        print(res, end=' ')
        #ms = [i[0] for i in res]
except Exception as ex:
    print(ex)
finally:
    print()
    if conn:
        conn.close()
