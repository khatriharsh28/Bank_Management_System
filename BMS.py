#import mysql connector to access sql database.
import mysql.connector as a

#.connect method of the MySQL Connector class to connect MySQL
#It would return a MySQLConnection object if the connection established successfully
con=a.connect(host="localhost", user="root",passwd="22380@khatri",database="bank")

#Function to get new user account detail and store it in database
def openAcc():
    n=input("Enter Name: ")
    ac=int(input("Enter Account No: "))
    db=int(input("Enter D.O.B: "))
    ad=input("Enter Address: ")
    p=int(input("Enter Phone: "))
    ob=int(input("Enter Opening Balance: "))

    #create a cursor object to perform various SQL operations.
    cur=con.cursor()
    
    #execute() methods run the SQL query and return the result.
    sql='select acno from account_detail where acno=%s'
    data=(ac,)
    cur.execute(sql,data)

    #fetchone() or fetchmany() to read query result.
    detail=cur.fetchone()
    
    if detail:
        print("This Acc No is already present in our database.")
    else:
        sql1='insert into account_detail values(%s,%s,%s,%s,%s,%s)'
        sql2='insert into amount values(%s,%s,%s)'
        data1=(n,ac,db,ad,p,ob)
        data2=(n,ac,ob)
        cur.execute(sql1,data1)
        cur.execute(sql2,data2)

        #To save changes in database.
        con.commit()
        print("Data Entered Successfully")
    main()

#Function to add new data(add money) in exciting data(money).
def depoAmo():
    am=int(input("Enter Amount: "))
    ac=input("Enter Account no: ")
    if acc_present(ac):
        cur=con.cursor()
        sql1="select balance from amount where acno=%s"
        data1=(ac,);
        cur.execute(sql1,data1)
        result=cur.fetchone()
        newam=am+result[0]
        sql2="update amount set balance=%s where acno=%s"
        data2=(newam,ac)
        cur.execute(sql2,data2)
        con.commit()
    main()

def  withAm():
    withdraw_amount=int(input("Enter Amount: "))
    ac=input("Enter Account no: ")
    
    if acc_present(ac):
        cur=con.cursor()
        sql1="select balance from amount where acno=%s"
        data1=(ac,);
        cur.execute(sql1,data1)
        money=cur.fetchone()
        if(money[0] < withdraw_amount):
            print("Insufficient Balance")
        else:
            newam=money[0]-withdraw_amount
            sql2="update amount set balance=%s where acno=%s"
            data2=(newam,ac)
            cur.execute(sql2,data2)
            con.commit()
    main()

def balEnq():
    ac=input("Enter Account no: ")
    if acc_present(ac):
        cur=con.cursor()
        sql1="select balance from amount where acno=%s"
        data1=(ac,);
        cur.execute(sql1,data1)
        money=cur.fetchone()
        print("Your Current Balance is "+str(money[0]))
    main()

def disAcc():
    ac=input("Enter Account no: ")
    if acc_present(ac):
        cur=con.cursor()
        sql1="select * from account_detail where acno=%s"
        data1=(ac,);
        cur.execute(sql1,data1)
        detail=cur.fetchone()
        for i in detail:
            print(i,end="  ")
    main()

def closeAcc():
    ac=input("Enter Account no: ")
    if acc_present(ac):
        cur=con.cursor()
        sql1="delete from amount where acno=%s"
        sql2="delete from account_detail where acno=%s"
        data=(ac,);
        cur.execute(sql1,data)
        cur.execute(sql2,data)
        con.commit()
    main()

def acc_present(ac):
    cur=con.cursor()
    sql='select acno from account_detail where acno=%s'
    data=(ac,)
    cur.execute(sql,data)
    detail=cur.fetchone()
    if detail:
        return True
    print("This account no. is not present in our database")
    return False

def main():
    print("""
    1. OPEN NEW ACCOUNT.
    2. DEPOSIT AMOUNT.
    3. WITHDRAW AMOUNT.
    4. BALANCE ENQUIRY.
    5. DISPLAY CUSTOMER DETAILS.
    6. CLOSE AN ACCOUNT.
    """)
    choice=input("Enter your Choice: ")
    if(choice=='1'):
        openAcc()
    elif(choice=='2'):
        depoAmo()
    elif(choice=='3'):
        withAm()
    elif(choice=='4'):
        balEnq()
    elif(choice=='5'):
        disAcc()
    elif(choice=='6'):
        closeAcc()
    else:
        print("Wrong Choice...")
        main()

main()
