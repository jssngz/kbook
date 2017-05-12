import sqlite3
conn  = sqlite3.connect('../db.sqlite3')
print("ok")
cursor = conn.execute("SELECT id, tagName from kbookspider_tag where id=?",(1,))
for row in cursor:
    print("id=",row[0])
    print("tagName=", row[1])
cursor = conn.execute("INSERT INTO  kbookspider_tag (tagName) VALUES (?)",('zhangsan',))
cursor.close()
conn.commit()
conn.close()