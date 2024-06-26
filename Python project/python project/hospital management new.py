import os
import mysql.connector
import datetime
now = datetime.datetime.now()


def patient_mgmt( ):
           while True :
                      print("\t\t\t\t\t\t\t\t 1. ADD PATIENT RECORD")
                      print("\t\t\t\t\t\t\t\t 2. LIST PATIENT RECORD")
                      print("\t\t\t\t\t\t\t\t 3. UPDATE PATIENT RECORD")
                      print("\t\t\t\t\t\t\t\t 4. DELETE PATIENT RECORD")
                      print("\t\t\t\t\t\t\t\t 5. EXIT(Main Menu)")
                      p=int (input("\t\t______ENTER YOUR REQUIRED CHOICE_______:"))
                      if p==1:
                                 Add_Record()
                      if p==2:
                                 List_Record()
                      if p==3:
                                 Update_Record()
                      if p==4:
                                 Delete_Record()
                      if p== 5 :
                                 break

def doctor_mgmt():
            while True :
                      print("\t\t\t\t\t\t\t\t 1. ADD DOCTOR RECORD")
                      print("\t\t\t\t\t\t\t\t 2. LIST DOCTOR RECORD")
                      print("\t\t\t\t\t\t\t\t 3. UPDATE DOCTOR RECORD")
                      print("\t\t\t\t\t\t\t\t 4. DELETE DOCTOR RECORD")
                      print("\t\t\t\t\t\t\t\t 5. EXIT(main menu")
                      d=int (input("\t\t________ENTER YOUR REQUIRED CHOICE______ :"))
                      if d==1 :
                                 add_dr_record()
                      if d==2 :
                                 list_dr_record()
                      if d==3 :
                                 update_dr_record()
                      if d==4 :
                                 delete_dr_record()
                                 break

def ward_mgmt( ):
           while True :
                      print("\t\t\t\t\t\t\t\t 1. ADD WARD RECORD")
                      print("\t\t\t\t\t\t\t\t 2. LIST WARD RECORD")
                      print("\t\t\t\t\t\t\t\t 3. DELETE WARD RECORD")
                      print("\t\t\t\t\t\t\t\t 4. INFORMATION")
                      print("\t\t\t\t\t\t\t\t 5. EXIT(main menu)")
                      b=int (input("\t\t\t\t\t\t\t\t_______  ENTER YOUR REQUIRED CHOICE_______ :"))
                      if b==1:
                                 add_ward_record()
                      if b==2:
                                 list_ward_record()
                      if b==3:
                                 delete_ward_record()
                      if b==4:
                                 information_ward_record()
                      
                                 break
def bill_mgmt( ):
            while True:
                     print("\t\t\t\t\t\t\t\t\t\t\t 1. ADD BILL RECORD")
                     print("\t\t\t\t\t\t\t\t\t\t\t 2. LIST BILL RECORD")
                     print("\t\t\t\t\t\t\t\t\t\t\t 3. DELETE RECORD")
                     print("\t\t\t\t\t\t\t\t\t\t\t 4.EXIT(main menu)")
                     w=int (input("\t\t\t\t\t\t\t____ENTER YOUR REQUIRED CHOICE_____ :"))
                     if w==1 :
                             add_bill_record()
                     if w==2 :
                             list_bill_record()
                     if w==3 :
                             delete_bill_record()
                             break


                 
def create_database():
           mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",password="shruti123",database="hospital")
           mycursor=mydb.cursor()
           print(" Creating patient1 table")
           sql = "CREATE TABLE if not exists patient(\
                  patient_id char(20) ,\
                  patient_name char(30) NOT NULL,\
                  contact_no int(10) ,\
                  Age int(12) ,\
                  gender char(6),\
                  disease char(30),\
                  ward_no int,\
                  assistdr char(30),\
                  doctorid int,);"
           mycursor.execute(sql)
           print(" Creating doctor table")
           sql = "CREATE TABLE if not exists doctor(\
                  doctor_id char(5) ,\
                  doctor_name char(30),\
                  specialization  char(30),\
                  visiting_hr time,\
                  fees int,\
                  contact_no int);"
           mycursor.execute(sql)
           print(" Creating ward table")
           sql = "CREATE TABLE if not exists ward (\
                  patient_id int ,\
                  patient_name char(30) , \
                  type_of_ward char(30),\
                  ward_no char(10),\
                  admit_date date,\
                  disharge_date date);"
           print("creating ward_details table")
           sql="create table if not exists ward_details(\
               ward_type varchar(10),\
               amount int);"
           mycursor.execute(sql)
           print("ward_details table created")
           sql="create table bill1(patient_id int,\
           patient_name varchar(30),\
           medicine_amt int,\
           ward_amt int,\
           doctor_fee int,\
           no_of_days_admit int):"
           print("bill table created")
def list_database():
        mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",password="shruti123",database="hospital")   
        mycursor=mydb.cursor()
        sql="show tables;"
        mycursor.execute(sql)
        for i in mycursor:
                   print(i)

def Add_Record():
           mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",password="shruti123",database="hospital")
           mycursor=mydb.cursor()
           now = datetime.datetime.now()
           sql="INSERT INTO patient1(patient_id ,patient_name,contact_no , age,gender,disease ,ward_no,assistdr,doctorid) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           print("USE ONLY CAPITAL LETTERS")
           patient_id=str(input("Enter patientid  :"))
           patient_name=input("Enter patient name:")
           contact_no=int(input("Enter Phone number : "))
           Age=int(input("Enter Age: "))
           gender=input("Enter gender: ")
           disease=input("Enter disease: ")
           ward_no=input("Enter ward no: ")
           assistdr=input("Enter assist doctor name: ")
           doctorid=int(input("enter doctorid: "))
           val=(patient_id ,patient_name ,contact_no, Age,gender,disease ,ward_no,assistdr,doctorid)
           mycursor.execute(sql,val)
           mydb.commit()



def List_Record():
           mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",password="shruti123",database="hospital")
           mycursor=mydb.cursor()
           sql="SELECT * from patient1"
           mycursor.execute(sql)
           clrscr()
           print("\t\t\t\t\t\t\t ***** PATIENT DETAILS *****")
           print("-"*150)
           print("patient_id    patient_name       contact_no       age       gender       disease           ward_no          assistdr        doctorid      ")
           print("-"*150)
           for i in mycursor:
           print(" ",i[0],"\t\t",i[1],"\t  ",i[2],"\t ",i[3],"\t   ",i[4], "\t\t",i[5],"\t\t",i[6],"\t\t\t",i[7],"\t\t",i[8])
           print("-"*150)


def Update_Record():
            mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",passwd="shruti123",database="hospital")
            mycursor=mydb.cursor()
            patient_id=input("Enter patientid:")
            disease=input("Enter disease: ")
            sql="UPDATE patient1 SET disease=%s WHERE patient_id=%s;"
            val=(patient_id,disease)
            mycursor.execute(sql,val)
            mydb.commit()
            print("\t\t Record being updated")
            sql="select * from patient1"


def Delete_Record():
            mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",passwd="shruti123",database="hospital")
            mycursor=mydb.cursor()
            patient_id=int(input("Enter the patientid:"))
            sql="DELETE from patient1 WHERE patient_id=%s;"
            val=(patient_id,)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount,"record(s)deleted")
 
def add_dr_record():
           mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",password="shruti123",database="hospital")
           mycursor=mydb.cursor()
           now = datetime.datetime.now()
           sql="INSERT INTO doctor(doctor_id ,doctor_name,mobile_no ,specialization,qualification,visiting_hrs,fees) values (%s,%s,%s,%s,%s,%s,%s)"
           doctor_id=str(input("Enter doctor_id  :"))
           doctor_name=input("Enter doctor name:")
           mobile_no=int(input("Enter mobile number : "))
           specialization=input("Enter specialization: ")
           qualification=input("Enter qualification: ")
           visiting_hrs=input("Enter visiting_hrs: ")
           fees=int(input("Enter fees: "))
           val=(doctor_id ,doctor_name ,mobile_no,specialization,qualification,visiting_hrs,fees)
           mycursor.execute(sql,val)
           mydb.commit()

def list_dr_record():
           mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",password="shruti123",database="hospital")
           mycursor=mydb.cursor()
           sql="SELECT * from doctor"
           mycursor.execute(sql)
           clrscr()
           print("\t\t\t DOCTOR DETAILS")
           print("-"*100)
           print("doctor_id   doctor_name    mobile_no    specialization    qualification     visiting_hrs      fees")
           print("-"*100)
           for i in mycursor:
                      print(i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t ",i[5],"\t",i[6],"\t")
           print("-"*100)

def update_dr_record():
              mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",passwd="shruti123",database="hospital")
              mycursor=mydb.cursor()
              doctor_id=input("Enter doctor_id:")
              fees=input("Enter fees: ")
              sql="UPDATE doctor SET fees=fees+%s WHERE doctor_id=%s;"
              val=(doctor_id,fees)
              mycursor.execute(sql,val)
              mydb.commit()
              print("\t\t Record being updated")


def delete_dr_record():
            mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",passwd="shruti123",database="hospital")
            mycursor=mydb.cursor()
            doctor_id=int(input("Enter the doctor_id:"))
            sql="DELETE from doctor WHERE doctor_id=%s;"
            val=(doctor_id,)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount,"record(s)deleted");



def add_ward_record():
            mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",passwd="shruti123",database="hospital")
            mycursor=mydb.cursor()
            sql="insert into ward(patient_id,patient_name,type_of_ward,ward_no,admit_date,discharge_date) values(%s,%s,%s,%s,%s,%s)"
            patient_id=int(input("ENTER PATIENT ID :"))
            patient_name=input("ENTER PATIENT NAME :")
            type_of_ward=input("ENTER WARD-(PEDIATRICS,MATERNITY,GERIATRICS,PSYCHIATRIC :")
            ward_no=int(input("ENTER WARD NO :"))
            admit_date=input("ENTER ADMIT DATE :")
            discharge_date=input("ENTER DISCHARGE DATE :")
            val=(patient_id,patient_name,type_of_ward,ward_no,admit_date,discharge_date)
            mycursor.execute(sql,val)
            mydb.commit()
            print("RECORD ADDED SUCCESSFULLY")


def list_ward_record():
            mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",passwd="shruti123",database="hospital")
            mycursor=mydb.cursor()
            sql="select * from ward"
            mycursor.execute(sql)
            clrscr()
            print("\t\t\t\t\t******WARD DETAILS******\t\t\t\t\t\t")
            print("-"*100)
            print("patient_id   patient_name      ward          ward_no     admit_date     discharge_date")
            print("-"*100)
            for i in mycursor:
                      print(i[0],"\t\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4],"\t ",i[5],"\t")
            


def delete_ward_record():
            mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",passwd="shruti123",database="hospital")
            mycursor=mydb.cursor()
            patient_id=int(input("Enter the patient_id:"))
            sql="DELETE from ward WHERE patient_id=%s;"
            val=(patient_id,)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount,"record(s)deleted sucessfully");

            
def information_ward_record():
                mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",passwd="shruti123",database="hospital")
                mycursor=mydb.cursor()
                print('*'*85)
                print('WARD TYPE                    |                   CHARGES')
                print('*'*45,end=''"*"*40)       
                print('\n   GENERAL                 |                    Rs.1500')
                print('  PRIVATE                    |                    Rs.2000')
                print('  ICU                        |                    Rs.5000')
                print('*'*45,end=''"*"*40)

def add_bill_record():
            mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",passwd="shruti123",database="hospital")
            mycursor=mydb.cursor()
            sql="insert into bill1(patient_id,patient_name,medicine_amt,ward_amt,doctor_fee, no_of_days_admit) values(%s,%s,%s,%s,%s,%s)"
            patient_id=int(input("Enter patient_id:"))
            patient_name=input("Enter patient_name :")
            medicine_amt=int(input("Enter medicine amount :"))
            ward_amt=int(input("enter ward amount:"))
            doctor_fee=int(input("enter doctor fees:"))
            no_of_days_admit=int(input("Enter total no of admit days :"))
            val=(patient_id,patient_name,medicine_amt,ward_amt,doctor_fee,no_of_days_admit)
            mycursor.execute(sql,val)
            mydb.commit()



def list_bill_record():
            mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",passwd="shruti123",database="hospital")
            mycursor=mydb.cursor()
            sql="select * from bill1"
            mycursor.execute(sql)
            clrscr()
            print("\t\t\t\t\t\t\t\t\t******BILL DETAILS******\t\t\t\t\t\t")
            #print("-"*100)
            print("\t\t\t\t\t\t\t\t\t______CITY HOSPITAL______")
            print("\t\t\t\t\t\t\t\t\t\tINDORE(452013)          ")
            print("\t\t\t\t\t\t\t\t______________________________________")
            print("\t\t\t\t\t\t\t\t\t\tBILL GENERATE")
            a=input("enter payment mode:")
            for i in mycursor:
                print("\t\t\t\t\t\t\tpatient id :",i[0],"\t\t" ,"patient name :",i[1])
                print("\t\t\t\t\t\t\t\t\tmedicine_amt:",i[2])
                print("\t\t\t\t\t\t\t\t\tward_amt:",i[3])
                print("\t\t\t\t\t\t\t\t\tdoctor_fees :",i[4])
                print("\t\t\t\t\t\t\t\t\ttotal amount =",i[2]+i[3]+i[4]*i[5])
                print("\t\t\t\t\t\t\t\t\tPAYMENT DONE VIA",a)
            #print("-"*100)
def delete_bill_record():
            mydb=mysql.connector.connect(host="localhost",user="root",charset="utf8",passwd="shruti123",database="hospital")
            mycursor=mydb.cursor()
            patient_id=int(input("Enter the patient_id:"))
            sql="DELETE from bill1 WHERE patient_id=%s;"
            val=(patient_id,)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount,"record(s)delete")
          
def db_mgmt( ):
           while True :
                      print("\t\t\t 1. Database creation")
                      print("\t\t\t 2. List Database")
                      print("\t\t\t 3. Back (Main Menu)")
                      p=int (input("\t\tEnter Your Choice :"))
                      if p==1 :
                                 create_database()
                      if p==2 :
                                 list_database()
                      if p== 3 :
                                 break
def clrscr():
            print("\n"*2)


while True:
           clrscr()
           print("\t\t\t\t\t\t ********************************************************************************************\n")
           print("\t\t\t\t\t\t_______________WELCOME TO ONLINE HOSPITAL MANAGEMENT SYSTEM______________")
           print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n")
           print("\t\t\t\t\t\t ********************************************************************************************\n")
           print("\t\t\t\t\t\t\t 1. PATIENT MANAGEMENT")
           print("\t\t\t\t\t\t\t 2. DOCTOR MANAGEMENT")
           print("\t\t\t\t\t\t\t 3. WARD MANAGEMENT")
           print("\t\t\t\t\t\t\t 4. BILL MANAGEMENT")
           print("\t\t\t\t\t\t\t 5. EXIT\n")
           n=int(input("Enter your choice :"))
           if n== 1:
                      patient_mgmt()
           if n== 2:
                      os.system('cls')
                      doctor_mgmt()
           if n== 3:
                      ward_mgmt()
           if n== 4:
                      bill_mgmt()
           if n==5 :
                              
               break
                    
