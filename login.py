import pymysql as pms
conn = pms.connect(host="localhost", 
                   port=3306,
                   user="root",
                   password="Roops@2003",
                   db="passwords")
print(conn)
cursor=conn.cursor()

def getcredentials():
    username =[]
    pwd=[]
    cursor.execute("SELECT * FROM Login ")
    result =cursor.fetchall()
    print(result)
    for i in result:
        username.append(i[0])
        pwd.append(i[1])

    return username , pwd