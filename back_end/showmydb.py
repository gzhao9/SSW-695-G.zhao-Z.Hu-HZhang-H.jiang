import connect_mydb
mydb = connect_mydb.mydb
my_cursor = mydb.cursor()

my_cursor.execute("use mealplan")
my_cursor.execute("select * from foodInfo")

for db in my_cursor:
    print(db)
