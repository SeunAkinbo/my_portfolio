import mysql.connector


def create_table():
    try:
        conn = mysql.connector.connect(user='root',
                                       password='password',
                                       host='127.0.0.1',
                                       database='logins',
                                       auth_plugin='mysql_native_password')

        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS contact")
        conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


def update_table(data):
    conn = mysql.connector.connect(user='root',
                                   password='password',
                                   host='127.0.0.1',
                                   database='logins',
                                   auth_plugin='mysql_native_password')

    cursor = conn.cursor()
    query = "INSERT INTO logins.contact(subject, email, message) VALUES(%s, %s, %s)"

    tb_data = (data['Subject'], data['Email'], data['Message'])
    cursor.execute(query, tb_data)
    conn.commit()
    conn.close()


# data = {'Email': 'seunakinbo@gmail.com',
#         'Subject': 'Hello',
#         'Message': 'I am Here for you'
#         }
# print(data['Email'], data['Subject'], data['Message'])
# update_table(data)
# create_table()
