import pymysql as db
import os
conn=db.connect("localhost","root","","digital_diary")
cur=conn.cursor()
def insertrecord():
    name=input("Enter the name of your frined: ")
    address=input("Enter the address of your friend: ")
    contact=input("Enter the contact no. of your friend: ")
    email=input("Enter the email of your friend: ")
    birthday=input("Enter the dob of your friend: ")
    qry=f"""insert into friends(name,address,contact,email,birthday)
    values ('{name}','{address}',{contact},'{email}','{birthday}')"""
    cur.execute(qry)
    conn.commit()
    print("Record Inserted Successfully")
def updaterecord():
    s_no=int(input("Enter the s.no: "))
    name=input("Enter the name of your friend: ")
    qry="update friends set "
    for i in ["address","contact","email","birthday"]:
        ch=input(f"Do you want to update {i} y/n: ")
        if ch=='y':
            val=input(f"enter {i} ")
            qry+=f"{i}='{val}' "
    qry+=f"where s_no={s_no} and name='{name}'"
    cur.execute(qry)
    conn.commit()
    print("Record Updated Successfully")
def showfriends():
    print("All data in diary are following:   ")
    qry=f"select * from friends"
    cur.execute(qry)
    for val in cur:
        print([val])
    conn.commit()
def deletefriend():
    s_no=int(input("Enter the s.no: "))
    name=input("Enter the name of your friend: ")
    ch=input(f"Do you want to delete your friend from list y/n: ")
    if ch=='y':
        qry=f"delete from friends where s_no={s_no} and name='{name}'"
        cur.execute(qry)
        conn.commit()
    else:
        print(f"Don't do this '{name}' is your friend")
    print("Deleted Successfully")
def searchfriend():
    ch=input("""what you know about your friend name and birthday 
    1)For name: 
    2)For birthday: 
    Enter Here: """)
    if ch=='1':
        name=input("Enter the name of your friend: ")
        qry=f"select * from friends where name='{name}'"
        cur.execute(qry)
        res=cur.fetchall()
        for i in res:
            print([i])
        conn.commit()
    elif ch=='2':
        birthday=input("Enter the birthday of your friend: ")
        qry=f"select * from friends where birthday={birthday}"
        cur.execute(qry)
        res=cur.fetchall()
        for val in res:
          print([val])
        conn.commit()
    print("Your Friend Data are above")
while True:
    os.system('cls')
    choice=input("""What you want to be done in diary: 
    1)Insertion
    2)Deletion
    3)Updation
    4)Show all Diary
    5)Searching Friend
    6)Exit
    """)
    if choice=='1':
        insertrecord()
    elif choice=='2':
        deletefriend()
    elif choice=='3':
        updaterecord()
    elif choice=='4':
        showfriends()
    elif choice=='5':
        searchfriend()
    elif choice=='6':
        break
    else:
        print("Invalid Input")
    os.system('pause')
cur.close()
conn.close()
os.system('cls')