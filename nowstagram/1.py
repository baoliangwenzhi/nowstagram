import MySQLdb
con=MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='bbs')
cursor = con.cursor()
sql = 'select * from article '
cursor.execute(sql)
row = cursor.fetchall()
for oo in row:
    print oo
cursor.close()
con.close()