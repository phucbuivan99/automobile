import mysql.connector
import pandas as pd
from pandas import ExcelWriter

mydb= mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tool_forward",
)
mycursor= mydb.cursor(dictionary=True, buffered=True)

if mycursor:
    print("connected")
else:
    print("failed connected")

def getExcel():
    file_import= "C:/MQM/tool_forward/tool_forward/grouplink.xlsx"
    data = pd.read_excel(file_import)
    val= data.values.tolist()
    return val

# insert excel data to db
def insertLink():
    sql = "INSERT INTO join_group (group_type, group_link) VALUES (%s, %s)"
    data= getExcel()
    mycursor.executemany(sql,data)
    mydb.commit()

insertLink()
#delete duplicate link_group
def delDupLink():
    sql = "delete from join_group where id in(select max(id) from join_group group by group_type, group_link having count(*) > 1)"
    mycursor.execute(sql)
    mydb.commit()

delDupLink()

#insert data to join_group table
def insertJoinedgroup(group_id, group_tittle):
    sql = "INSERT INTO groupchat (group_id, group_tittle) VALUES (%s, %s)"
    val= (group_id, group_tittle)
    mycursor.execute(sql,val)
    mydb.commit()

#delete duplicated data
def delDupData():
    sql = "delete from groupchat where id in(select max(id) from groupchat group by group_id, group_tittle having count(*) > 1)"
    mycursor.execute(sql)
    mydb.commit()

# delDupData()
#get data from groupchat table
def selectGroup():
    # sql= "SELECT * FROM groupchat"
    sql= "SELECT * from groupchat"
    mycursor.execute(sql)
    res= mycursor.fetchall()
    return res

# listGroup= selectGroup()
# print(listGroup)
# print("===========")
# for i in listGroup:
#     print(i['group_id'],i['group_tittle'])

# group_id=int(selectGroup()['group_id'])
# print(res)

#get data from join_group table
def selectLink():
    sql= "SELECT * FROM join_group"
    mycursor.execute(sql)
    res= mycursor.fetchall()
    return res
# print(selectLink())