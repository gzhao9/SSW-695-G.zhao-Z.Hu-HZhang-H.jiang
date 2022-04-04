import mysql.connector
mydb = mysql.connector.connect(
    host = "35.245.128.110",
    user = "root",
    password = "695695",
    db = 'mealplan'
)

# my_cursor = mydb.cursor()
# my_cursor.execute("CREATE DATABASE MP")
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)