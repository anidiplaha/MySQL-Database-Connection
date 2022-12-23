import mysql.connector
import os
from beautifultable import BeautifulTable
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="student")
global listS
global a
a=""
listS=[""]      
def insert():
       try:
              a='Y'
              while(a=='Y'):
                     clsscr()
                     cursor=mydb.cursor()
                     sql=("""select stuID from newstu""")
                     cursor.execute(sql)
                     cursor.fetchall()
                     stuID=cursor.rowcount+1
                     print("""******Student Info Insert******""")
                     print("\nStudent ID : ",stuID)
                     stuName=input("Enter Student Name :")
                     stuRoll=input("Enter Student Roll :")
                     stuFName=input("Enter Student F Name :")
                     sql=("""INSERT INTO newstu(stuID,stuName,stuRoll,stuFName) VALUES(%s,%s,%s,%s)""")
                     data=(stuID,stuName,stuRoll,stuFName)
                     cursor.execute(sql,data)
                     mydb.commit()
                     print("Record inserted successfully")
                     a=(input("\nDo you went to Contuine ? (Y/N):[ ]\b\b")).upper()
       except mysql.connector.Error as error:
              print("Failed to insert record {}".format(error))
       finally:
              print("")
              clsscr()
              manage()
       #print("Calling Insert def")
def update():
       try:
              a='Y'
              while(a=='Y'):
                     clsscr()
                     cursor=mydb.cursor()
                     print("""******Student Info Update******""")
                     stuID=input("\nEnter Which Student ID You Went To Update :")
                     sql=("""select * from newstu where stuID = %s""")
                     dat=(stuID,)
                     cursor.execute(sql,dat)
                     x=cursor.fetchall()
                     if cursor.rowcount > 0:
                            table=BeautifulTable()
                            table.column_headers=["ID","NAME","ROLL","F_NAME"]                            
                            for row in x:
                                   #print("ID : ",row[0], )
                                   #print("Name : ",row[1], )
                                   #print("Roll : ",row[2], )
                                   #print("F_Name: ",row[3],"\n")                                   
                                   table.append_row([row[0],row[1],row[2],row[3]])
                                   print(table)
                                   stuID1=input("\nEnter Updated Student ID :")
                                   stuName=input("Enter Updated Student Name :")
                                   stuRoll=input("Enter Updated Student Roll :")
                                   stuFName=input("Enter Updated Student F Name :")
                                   sql=("""UPDATE newstu SET stuID=%s,stuName=%s,stuRoll=%s,stuFName=%s WHERE stuID=%s""")
                                   data=(stuID1,stuName,stuRoll,stuFName,stuID)
                                   cursor.execute(sql,data)
                                   mydb.commit()
                                   print("Record Updated successfully")
                     else:
                            print("Record not fount")
                     a=(input("\nDo you went to Contuine ? (Y/N):[ ]\b\b")).upper()                     
       except mysql.connector.Error as error:
              print("Failed to Update record into Laptop table {}".format(error))
       finally:
              print("")
              clsscr()
              manage()             
                     
       #print("Calling Update def")
def search():
       try:
              a='Y'
              while(a=='Y'):
                     clsscr()
                     cursor=mydb.cursor()
                     print("""******Student Info Search******""")
                     stuID=input("\nEnter Student ID :")
                     sql=("""select * from newstu where stuID = %s""")
                     dat=(stuID,)
                     cursor.execute(sql,dat)
                     x=cursor.fetchall()
                     if cursor.rowcount >0:
                            #print('==============================================================')
                            #print('ID\t | NAME\t\t\t | ROLL\t\t | F_NAME')
                            #print('==============================================================')
                            table=BeautifulTable()
                            table.column_headers=["ID","NAME","ROLL","F_NAME"]
                            for row in x:
                                   table.append_row([row[0],row[1],row[2],row[3]])
                                   #print("ID : ",row[0], )
                                   #print("Name : ",row[1], )
                                   #print("Roll : ",row[2], )
                                   #print("F_Name: ",row[3],"\n")
                                   #print(row[0],'\t |',row[1])
                                   #print('-------------------------------------------------------')
                            print(table)
                     else:
                            print("Record Not Found")
                     a=(input("\nDo you went to Contuine ? (Y/N):[ ]\b\b")).upper() 
       except mysql.connector.Error as error:
              
              print("Failed to Search record  {}".format(error))
       finally:
              clsscr()
              manage()
       #print("Calling search def")
def delete():
       try:
              a='Y'
              while(a=='Y'):
                     clsscr()
                     cursor=mydb.cursor()
                     print("""******Student Info Update******""")
                     stuID=input("\nEnter Which Student ID You Went To Update :")
                     sql=("""select * from newstu where stuID = %s""")
                     dat=(stuID,)
                     cursor.execute(sql,dat)
                     x=cursor.fetchall()
                     if cursor.rowcount > 0:
                            for row in x:
                                   print(x[0])
                                   sql=("""DELETE FROM newstu WHERE stuID = %s""")
                                   data=(stuID,)
                                   cursor.execute(sql,data)
                                   mydb.commit()
                                   print("Record Deleted successfully")
                     else:
                            print("Record Not Found")
                     a=(input("\nDo you went to Contuine ? (Y/N):[ ]\b\b")).upper()                     
       except mysql.connector.Error as error:
              print("Failed to Update record into Laptop table {}".format(error))
       finally:
              print("")
              clsscr()
              manage()
       #print("Calling Delete def")
def showall():
       try:
              a=''
              while(a==''):
                     clsscr()
                     cursor=mydb.cursor()
                     print("""******Show All Record******\n""")
                     sql=("""select * from newstu""")
                     cursor.execute(sql)
                     x=cursor.fetchall()
                     if cursor.rowcount >0:
                            table=BeautifulTable()
                            table.set_style(BeautifulTable.STYLE_GRID)                            
                            table.column_headers=["ID","NAME","ROLL","F_NAME"]
                            #print('==============================================================')
                            #print('ID\t | ROLL\t\t | NAME\t\t\t | F_NAME')
                            #print('==============================================================')
                            for row in x:
                                   #print("ID : ",row[0], )
                                   #print("Name : ",row[1], )
                                   #print("Roll : ",row[2], )
                                   #print("F_Name: ",row[3],"\n")
                                   #print(row[0],'\t |',row[2],'\t |',row[1],'\t |',row[3])
                                   #print('-----------------------------------------------------------------')                                   
                                   table.append_row([row[0], row[1], row[2], row[3]])                                   
                            print(table)
                     else:
                            print("Record Not Found")
                     a=(input("\nEnter 'X' to Back Main Menu :")).upper()
                     if a=='X':
                            clsscr()
                            manager()
                     else:
                            showall()              
       except mysql.connector.Error as error:
              print("Failed to Search record  {}".format(error))
       finally:
              clsscr()
              manage()
def manage():
       print("""

 --------------------------------------------------
 |************************************************|
 |**************Welcome to Project ***************|
 |************************************************|
 |#####################RKMSCC#####################|
 --------------------------------------------------
Enter 1 : To Add New Student
Enter 2 : To Update Student
Enter 3 : To View Student
Enter 4 : To Remove Student
Enter 5 : To Show All Record
Enter 9 : To Quit Application

                """)       
       try: #Using Exceptions For Validation
            userInput = int(input("Please Select An Above Option : ")) #Will Take Input From User
       except ValueError:
            exit("\nHy! That's Not A Number") #Error Message
       else:
            print("\n") #Print New Line
       if(userInput==1):
              #call Insert def
              insert()
       elif(userInput==2):
              #Call Update def
              update()
       elif(userInput==3):
              #Call Update def
              search()
       elif(userInput==4):
              #Call Update def
              delete()
       elif(userInput==5):
              showall()
       elif(userInput==9):
              quit()
              exit()
            
def clsscr():
       os.system('cls')
#-------------------------------------------------------------------------------------------------------
clsscr()
manage()
