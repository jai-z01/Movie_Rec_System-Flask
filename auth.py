import mysql.connector as msc
conn = msc.connect(host = "localhost",port = 3306,user = "root",password = "jais@22",db = "model")
cursor = conn.cursor()

def loginverify(uname,pwd):
    cursor.execute(f"SELECT password FROM accs WHERE uname='{uname}'")
    p = cursor.fetchone()
    if(p and pwd==p[0]):
        return True
    return False

def newuser(email,uname,pwd):
    cursor.execute(f"SELECT * FROM accs WHERE uname='{uname}' or email='{email}'")
    if cursor.fetchall():
        return False
    cursor.execute("INSERT INTO accs (email,uname,password) VALUES (%s,%s,%s)",(email,uname,pwd))
    conn.commit()
    return True