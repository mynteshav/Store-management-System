
import mysql.connector as sqltor
import  pandas as pd
import matplotlib.pyplot as plt
import datetime


mycon=sqltor.connect(host='localhost',user='root',passwd='teshav',database='shoedb')
if mycon.is_connected():
    print()
    print('CONNECTED SUCESSFULLY')
    print()
    print(100*'*')
cursor=mycon.cursor()
cursor.execute('create database if not exists shoedb;')
cursor.execute('use shoedb;')
cursor.execute('create table if not exists Shoe(Shoe_Id char(10) primary key , Sname char(30), Brand varchar(10),Product_for varchar(20),Rate int(5),SSize int(6),SQty int(5));')
cursor.execute('create table if not exists SSales(S_Id char(15) primary key , I_Id char(30) references Shoe(ShoeId), C_Name char(40),C_Number bigint, Brand char(20),Quantity int(8),Rate int(8),S_Date  date);')

print(100*'_')
print()
print('                            WELCOME TO SHOE SHOP MANAGEMENT SYSTEM')


def menu():
     while True:
        print()
        print('**************************************************')
        print('|  SELECT OPERATION WHICH YOU WANT!              |')
        print('|     (1.) SHOE STOCK DETAIL                     |')
        print('|     (2.) SALE SHOE                             |')
        print('|     (3.) REPORT OF STORE                       |')
        print('|     (4.) BILL PRINTING                         |')
        print('|     (5.) EXIT                                  |')
        print('**************************************************')
        print()
        Choice=int(input('ENTER YOUR CHOICE:'))
        print()
        if Choice==1:
            while True:
                print('--------------------------------------')
                print('| MENU FOR SHOES STOCK DETAILS:      |')
                print('|   1. VIEW SHOES                    |')
                print('|   2. ADD SHOES                     |')
                print('|   3. UPDATE SHOES                  |')
                print('|   4. DELETE SHOES                  |')
                print('|   5. BACK                          |')
                print('--------------------------------------')
                Ch=int(input('ENTER YOUR CHOICE:'))
                if Ch==1:
                    displayshoe()
                elif Ch==2:
                    addshoe()
                elif Ch==3:
                    updateshoe()
                elif Ch==4:
                    delshoe()
                elif Ch==5:
                    break
                else:
                    print('ENTER VALID CHOICE!')
        elif Choice==2:
            while True:
                print('--------------------------------------')
                print('| MENU FOR SHOES SALES DETAILS:      |')
                print('|   1. VIEW SOLD SHOES               |')
                print('|   2. SALES                         |')
                print('|   3. BACK                          |')
                print('--------------------------------------')
                Ch=int(input('ENTER YOUR CHOICE:'))
                if Ch==1:
                    displaysales()
                elif Ch==2:
                    getmaxid()
                elif Ch==3:
                    break
                else:
                    print('ENTER VALID CHOICE!')   
                    
        elif Choice==3:
            yearwisereport()
        elif Choice==4:
            bill()
        elif Choice==5:
            Alert=input('DO YOU WANT TO EXIT(YES/NO):')
            if Alert=='YES' or Alert=='y' or Alert=='Y' or Alert=='yes':
                break
            else:
                continue
        else:
            print('ENTER VALID CHOICE')
            



def displayshoe():
    Query='Select * from shoe'
    cursor.execute(Query)
    D=cursor.fetchall()
    Df=pd.DataFrame(D,columns=['ShoeId','Sname','Brand','Product_for','Rate','SSize','SQty'])
    print()
    print(60*'*')
    print(Df.to_string(index=False))
    print()
    print(60*'*')
    print()
    
    
    
def getmax():
        cursor.execute('Select max(Shoe_Id) as m from shoe')
        maxid=cursor.fetchone()[0]
        try:
            int_value=int(maxid[1:])
            int_value+=1
            maxid="S"+str(int_value)
        except:
            maxid="S100"
            print(maxid)
        return maxid
        

    
    
def addshoe():
    while True:
        displayshoe()
        print('ENTER SHOE DETAILS:')
        SId=getmax()
        Rt=int(input('Enter Rate:'))
        Sz=int(input('Enter Size:'))
        Sqty=int(input('Enter Quantity:'))
        print('-----------------------------------------')
        print('|  TYPE OF SHOES:                       |')
        print('|   1. SNEAKER                          |')
        print('|   2. BOOTS                            |')
        print('|   3. SANDALS                          |')
        print('|   4. HIGH TOP SHOE                    |')
        print('-----------------------------------------')
        Stype=int(input('Enter Your Choice:'))
        print('-----------------------------------------')
        print('|  BRANDS OF SHOES:                     |')
        print('|   1. Adidas                           |')
        print('|   2. Nike                             |')
        print('|   3. Puma                             |')
        print('|   4. Rebook                           |')
        print('-----------------------------------------')
        Br=int(input('Enter Your Choice:'))
        print('-----------------------------------------')
        print('|  FOR WHOM YOU WANTS SHOES:            |')
        print('|   1. MALES                            |')
        print('|   2. FEMALE                           |')
        print('|   3. BOYS                             |')
        print('|   4. GIRLS                            |')
        print('|   5. KIDS                             |')
        print('-----------------------------------------')
        P_for=int(input('Enter Your Choice:'))
        
        
        if Stype==1 and Br==1 and P_for==1:
            cursor.execute('insert into Shoe values("{}","Sneaker","Adidas","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==2 and P_for==1:
            cursor.execute('insert into Shoe values("{}","Sneaker","Nike","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==3 and P_for==1:
            cursor.execute('insert into Shoe values("{}","Sneaker","Puma","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==4 and P_for==1:
            cursor.execute('insert into Shoe values("{}","Sneaker","Rebook","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==1 and P_for==2:
            cursor.execute('insert into Shoe values("{}","Sneaker","Adidas","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==2 and P_for==2:
            cursor.execute('insert into Shoe values("{}","Sneaker","Nike","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==3 and P_for==2:
            cursor.execute('insert into Shoe values("{}","Sneaker","Puma","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==4 and P_for==2:
            cursor.execute('insert into Shoe values("{}","Sneaker","Rebook","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        
        
        
        elif Stype==1 and Br==1 and P_for==3:
            cursor.execute('insert into Shoe values("{}","Sneaker","Adidas","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==2 and P_for==3:
            cursor.execute('insert into Shoe values("{}","Sneaker","Nike","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==3 and P_for==3:
            cursor.execute('insert into Shoe values("{}","Sneaker","Puma","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==4 and P_for==3:
            cursor.execute('insert into Shoe values("{}","Sneaker","Rebook","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==1 and P_for==4:
            cursor.execute('insert into Shoe values("{}","Sneaker","Adidas","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==2 and P_for==4:
            cursor.execute('insert into Shoe values("{}","Sneaker","Nike","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==3 and P_for==4:
            cursor.execute('insert into Shoe values("{}","Sneaker","Puma","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==4 and P_for==4:
            cursor.execute('insert into Shoe values("{}","Sneaker","Rebook","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        
        
        elif Stype==1 and Br==1 and P_for==5:
            cursor.execute('insert into Shoe values("{}","Sneaker","Adidas","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==2 and P_for==5:
            cursor.execute('insert into Shoe values("{}","Sneaker","Nike","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==3 and P_for==5:
            cursor.execute('insert into Shoe values("{}","Sneaker","Puma","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==1 and Br==4 and P_for==5:
            cursor.execute('insert into Shoe values("{}","Sneaker","Rebook","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break   
        elif Stype==2 and Br==1 and P_for==1:
            cursor.execute('insert into Shoe values("{}","Boots","Adidas","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==2 and P_for==1:
            cursor.execute('insert into Shoe values("{}","Boots","Nike","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==3 and P_for==1:
            cursor.execute('insert into Shoe values("{}","Boots","Puma","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==4 and P_for==1:
            cursor.execute('insert into Shoe values("{}","Boots","Rebook","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        
        
        
        elif Stype==2 and Br==1 and P_for==2:
            cursor.execute('insert into Shoe values("{}","Boots","Adidas","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==2 and P_for==2:
            cursor.execute('insert into Shoe values("{}","Boots","Nike","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==3 and P_for==2:
            cursor.execute('insert into Shoe values("{}","Boots","Puma","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==4 and P_for==2:
            cursor.execute('insert into Shoe values("{}","Boots","Rebook","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==1 and P_for==3:
            cursor.execute('insert into Shoe values("{}","Boots","Adidas","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==2 and P_for==3:
            cursor.execute('insert into Shoe values("{}","Boots","Nike","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==3 and P_for==3:
            cursor.execute('insert into Shoe values("{}","Boots","Puma","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==4 and P_for==3:
            cursor.execute('insert into Shoe values("{}","Boots","Rebook","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        
        
        
        elif Stype==2 and Br==1 and P_for==4:
            cursor.execute('insert into Shoe values("{}","Boots","Adidas","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==2 and P_for==4:
            cursor.execute('insert into Shoe values("{}","Boots","Nike","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==3 and P_for==4:
            cursor.execute('insert into Shoe values("{}","Boots","Puma","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==4 and P_for==4:
            cursor.execute('insert into Shoe values("{}","Boots","Rebook","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==1 and P_for==5:
            cursor.execute('insert into Shoe values("{}","Boots","Adidas","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==2 and P_for==5:
            cursor.execute('insert into Shoe values("{}","Boots","Nike","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==3 and P_for==5:
            cursor.execute('insert into Shoe values("{}","Boots","Puma","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==2 and Br==4 and P_for==5:
            cursor.execute('insert into Shoe values("{}","Boots","Rebook","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()    
            break
        
        
        
        elif Stype==3 and Br==1 and P_for==1:
            cursor.execute('insert into Shoe values("{}","Sandals","Adidas","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==2 and P_for==1:
            cursor.execute('insert into Shoe values("{}","Sandals","Nike","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==3 and P_for==1:
            cursor.execute('insert into Shoe values("{}","Sandals","Puma","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==4 and P_for==1:
            cursor.execute('insert into Shoe values("{}","Sandals","Rebook","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==1 and P_for==2:
            cursor.execute('insert into Shoe values("{}","Sandals","Adidas","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==2 and P_for==2:
            cursor.execute('insert into Shoe values("{}","Sandals","Nike","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==3 and P_for==2:
            cursor.execute('insert into Shoe values("{}","Sandals","Puma","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==4 and P_for==2:
            cursor.execute('insert into Shoe values("{}","Sandals","Rebook","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        
        
        elif Stype==3 and Br==1 and P_for==3:
            cursor.execute('insert into Shoe values("{}","Sandals","Adidas","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==2 and P_for==3:
            cursor.execute('insert into Shoe values("{}","Sandals","Nike","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==3 and P_for==3:
            cursor.execute('insert into Shoe values("{}","Sandals","Puma","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==4 and P_for==3:
            cursor.execute('insert into Shoe values("{}","Sandals","Rebook","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==1 and P_for==4:
            cursor.execute('insert into Shoe values("{}","Sandals","Adidas","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==2 and P_for==4:
            cursor.execute('insert into Shoe values("{}","Sandals","Nike","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==3 and P_for==4:
            cursor.execute('insert into Shoe values("{}","Sandals","Puma","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==4 and P_for==4:
            cursor.execute('insert into Shoe values("{}","Sandals","Rebook","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        
        
        
        elif Stype==3 and Br==1 and P_for==5:
            cursor.execute('insert into Shoe values("{}","Sandals","Adidas","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==2 and P_for==5:
            cursor.execute('insert into Shoe values("{}","Sandals","Nike","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==3 and P_for==5:
            cursor.execute('insert into Shoe values("{}","Sandals","Puma","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==3 and Br==4 and P_for==5:
            cursor.execute('insert into Shoe values("{}","Sandals","Rebook","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()     
            break
        elif Stype==4 and Br==1 and P_for==1:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Adidas","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==2 and P_for==1:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Nike","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==3 and P_for==1:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Puma","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==4 and P_for==1:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Rebook","Male",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        
        
        elif Stype==4 and Br==1 and P_for==2:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Adidas","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==2 and P_for==2:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Nike","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==3 and P_for==2:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Puma","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==4 and P_for==2:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Rebook","Female",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==1 and P_for==3:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Adidas","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==2 and P_for==3:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Nike","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==3 and P_for==3:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Puma","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==4 and P_for==3:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Rebook","Boys",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        
        
        elif Stype==4 and Br==1 and P_for==4:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Adidas","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==2 and P_for==4:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Nike","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==3 and P_for==4:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Puma","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==4 and P_for==4:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Rebook","Girls",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==1 and P_for==5:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Adidas","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==2 and P_for==5:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Nike","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==3 and P_for==5:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Puma","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        elif Stype==4 and Br==4 and P_for==5:
            cursor.execute('insert into Shoe values("{}","High Top Shoe","Rebook","Kids",{},{},{})'\
                           .format(SId,Rt,Sz,Sqty))
            print('SHOE SUCESSFULLY ADDED!')
            mycon.commit()
            break
        else:
            print('Enter Valid Choice!')
            print()
            break
    displayshoe()
    print(70*'*')    
     
        
     
        
def updateshoe():
    while True:
        displayshoe()
        print('--------------------------------------')
        print('| MENU FOR UPDATES OF SHOES DETAILS: |')
        print('|   1. SHOES TYPE                    |')
        print('|   2. SHOES BRAND                   |')
        print('|   3. PRODUCT_FOR                   |')
        print('|   4. RATE                          |')
        print('|   5. SIZE                          |')
        print('|   6. SHOE QUANTITY                 |')
        print('|   7. BACK                          |')
        print('--------------------------------------')
        Ch=int(input('Enter Your Choice:'))
        if Ch==1:
            SID=input('Enter shoe ID:')
            NStype=input('Enter new shoe type:')
            cursor.execute('update shoe set Sname="{}" where Shoe_Id="{}"'.format(NStype,SID))
            mycon.commit()
            cnt=cursor.rowcount
            if cnt>0:
                print('SHOE Type UPDATED!')
            else:
                print('RECORD NOT UPDATED...  PLEASE ENTER VALID DETAILS')
        elif Ch==2:
            SID=input('Enter shoe ID:')
            NSBr=input('Enter new shoe brand:')
            cursor.execute('update shoe set Brand="{}" where Shoe_Id="{}"'.format(NSBr,SID))
            mycon.commit()
            cnt=cursor.rowcount
            if cnt>0:
                print('SHOE BRAND UPDATED!')
            else:
                print('RECORD NOT UPDATED...  PLEASE ENTER VALID DETAILS')
        elif Ch==3:
            SID=input('Enter shoe ID:')
            NSP_f=input('Enter new shoe product_for:')
            cursor.execute('update shoe set Product_for="{}" where Shoe_Id="{}"'.format(NSP_f,SID))
            mycon.commit()
            cnt=cursor.rowcount
            if cnt>0:
                print('SHOE TYPE UPDATED!')
            else:
                print('RECORD NOT UPDATED...  PLEASE ENTER VALID DETAILS')
                
                
                
        elif Ch==4:
            SID=input('Enter shoe ID:')
            NSR=int(input('Enter new shoe rate:'))
            cursor.execute('update shoe set Rate={} where Shoe_Id="{}"'.format(NSR,SID))
            mycon.commit()
            cnt=cursor.rowcount
            if cnt>0:
                print('SHOE RATE UPDATED!')
            else:
                print('RECORD NOT UPDATED...  PLEASE ENTER VALID DETAILS')
        elif Ch==5:
            SID=input('Enter shoe ID:')
            NSD=int(input('Enter new shoe Size:'))
            cursor.execute('update shoe set SSize={} where Shoe_Id="{}"'.format(NSD,SID))
            mycon.commit()
            cnt=cursor.rowcount
            if cnt>0:
                print('SHOE SIZE UPDATED!')
            else:
                print('RECORD NOT UPDATED...  PLEASE ENTER VALID DETAILS')
        elif Ch==6:
            SID=input('Enter shoe ID:')
            NSQ=int(input('Enter new shoe Qty:'))
            cursor.execute('update shoe set SQty={} where Shoe_Id="{}"'.format(NSQ,SID))
            print('SHOE QUANTITY UPDATED!')
            mycon.commit()
            cnt=cursor.rowcount
            if cnt>0:
                print('SHOE QUANTITY UPDATED!')
            else:
                print('RECORD NOT UPDATED...  PLEASE ENTER VALID DETAILS')
        elif Ch==7:
            break
        else:
            print('ENTER VALID CHOICE')   
            


    
def delshoe():
    displayshoe()
    D=input('Enter Shoe ID which you wants to delete:')
    Q='delete from shoe where Shoe_ID="{}"'.format(D)
    cursor.execute(Q)
    RC=cursor.rowcount
    if RC>0:
        print('RECORD SUCESSFULLY DELETED!')
        mycon.commit()
        displayshoe()
    else:
        print('ID NOT AVAILABLE!')




def displaysales():
    cursor.execute('Select * from ssales')
    D=cursor.fetchall()
    Df=pd.DataFrame(D,columns=['S_id','I_id','C_Name','C_Number','Brand','Quantity','Rate','S_Date'])
    print()
    print(70*'*')
    print('SALE:')
    print(Df.to_string(index=False))
    print()
    print(70*'*')

     
 
       
def getmaxid():
    cursor.execute('Select max(S_Id) as m from ssales')
    r=cursor.fetchone()[0]
    maxid=0
    if r==None:
        maxid=1001
    else:
        maxid=int(r)
        maxid+=1
    addsales(maxid)
    
    
    

def addsales(getid):
    displayshoe()
    while True:
        cname=input('Enter Customer Name:')
        cmobile=int(input('Enter Customer Mobile Num:'))
        print('ENTER SHOE DETAILS:')
        shoeid=input('Enter Shoe Id:')
        query="Select shoe_id,sname,brand,product_for,rate,sqty from shoe where\
            shoe_id='{}'".format(shoeid)
        cursor.execute(query)
        data=cursor.fetchall()
        df=pd.DataFrame(data,columns=['ShoeID','SName','Brand','Category','Rate','Qty'])
        print(df)
        sname=str(df.SName[0])
        Brand=str(df.Brand[0])
        price=int(df.Rate[0])
        oldqty=int(df.Qty[0])            
        newqty=int(input('Enter Quantity:'))    
        if oldqty<newqty:
            print('CANNOT SALE QUANTITY MORE THAN EXISTING QUANTITY!')
            break
        else:
            I='Insert into ssales values({},"{}","{}",{},"{}",{},{},curdate())'\
                .format(getid,shoeid,cname,cmobile,Brand,newqty,price)
            cursor.execute(I)
            mycon.commit()  
            U='Update shoe set SQty=SQty-{} where Shoe_iD="{}"'.format(newqty,shoeid)
            cursor.execute(U)
            print('SHOE SUCESSFULLY SOLD!')
            displayshoe()
            displaysales()
            mycon.commit()   
            Msg=input('Do you want to purchase more?')
            if Msg=='YES' or Msg=='yes':
                continue
            else:
                break
    
    
    
def yearwisereport():
    while True:
        print('-----------------------------------------')
        print('|  ENTER YOUR CHOICE FOR GRAPH:         |')
        print('|   1. GRAPH OF PURCHASE                |')
        print('|   2. GRAPH OF SALE                    |')
        print('|   3. BACK                             |')
        print('-----------------------------------------')
        CH=int(input('ENTER YOUR CHOICE:'))
        if CH==1:
            print('-------------------------------------------')
            print('|  ENTER YOUR CHOICE:                     |')
            print('|   1. GRAPH FOR NUMBER OF SHOE PURCHASED |')
            print('|   2. GRAPH FOR MOSTLY PURCHASED BRAND   |')
            print('|   3. GRAPH FOR FINAL CONSUMER OF SHOE   |')
            print('|   4. BACK                               |')        
            print('-------------------------------------------')
            P=int(input('ENTER YOUR CHOICE:'))
            if P==1:
                Q='Select SQty,Sname from shoe group by Sname'
                cursor.execute(Q)
                F=cursor.fetchall()
                Df=pd.DataFrame(F,columns=['SQty','Sname'])
                print()
                print(Df.to_string(index=False))
                print()
                plt.plot(Df['Sname'],Df['SQty'],color='g',marker='o',linestyle='dashed',markerfacecolor='b')
                plt.ylim(0,1000)
                plt.title('TOTAL QUANTITY OF SHOE PURCHASED',fontsize=13.0)
                plt.xlabel('SHOE TYPE',fontsize=12.0)
                plt.ylabel('QUANTITY OF PURCHASES',fontsize=12.0)
                plt.show()
                print(60*'*')
            elif P==2:
                Q='Select Brand,Rate,SQty from shoe'
                cursor.execute(Q)
                F=cursor.fetchall()
                Df=pd.DataFrame(F,columns=['Brand','Rate','Quantity'])
                print()
                print(Df)
                print()
                Df['Total Amount']=Df['Rate']*Df['Quantity']
                print()
                print(Df)
                print()
                plt.bar(Df['Brand'],Df['Total Amount'],color=['b','g','r','k','c'])
                plt.title('MOSTLY PURCHASED BRAND',fontsize=13.0)
                plt.xlabel('TOTAL AMOUNT',fontsize=12.0)
                plt.ylabel('BRAND',fontsize=12.0)
                plt.show() 
                print(60*'*')
                
                
            elif P==3:
                Q='Select Product_for,SQty from shoe group by Product_for '
                cursor.execute(Q)
                F=cursor.fetchall()
                Df=pd.DataFrame(F,columns=['Product_for','SQty'])
                print(Df.to_string(index=False))
                plt.pie(Df['SQty'],labels=Df['Product_for'],colors=['r','b','g','c','k'],
                        autopct='%1.f%%',shadow=True,startangle=140)
                plt.axis('equal')
                plt.title('FINAL CONSUMER OF SHOES',fontsize=13.0)
                print()
                plt.legend(Df['Product_for'],loc='best')
                plt.show()
            elif P==4:
                break
            else:
                print('Enter Valid Choice!')                
        elif CH==2:
            print('-------------------------------------------')
            print('|  ENTER YOUR CHOICE:                     |')
            print('|   1. GRAPH FOR NUMBER OF SHOE SALES     |')
            print('|   2. GRAPH FOR MOSTLY SOLD BRAND        |')
            print('|   3. BACK                               |')        
            print('-------------------------------------------')
            S=int(input('ENTER YOUR CHOICE:'))
            if S==1:
                Q='Select Quantity,C_Name from ssales group by S_id'
                cursor.execute(Q)
                F=cursor.fetchall()
                Df=pd.DataFrame(F,columns=['Quantity','C_Name'])
                print()
                print(Df.to_string(index=False))
                print()
                plt.scatter(Df['C_Name'],Df['Quantity'],color='k')
                plt.ylim(0,500)
                plt.title('TOTAL QUANTITY OF SHOE SOLD',fontsize=13.0)
                plt.xlabel('CUSTOMER',fontsize=12.0)
                plt.ylabel('QUANTITY OF SALES',fontsize=12.0)
                plt.show()  
                
                
            elif S==2:
                Q='Select Brand,Rate,Quantity from ssales'
                cursor.execute(Q)
                F=cursor.fetchall()
                Df=pd.DataFrame(F,columns=['Brand','Rate','Quantity'])
                print(Df)
                print('*'*60)
                Df['Total Amount']=Df['Rate']*Df['Quantity']
                print(Df)
                print('*'*60)
                plt.barh(Df['Brand'],Df['Total Amount'],color=['b','k','r','y','c'])
                plt.title('MOSTLY SOLD BRAND',fontsize=13.0)
                plt.xlabel('TOTAL AMOUNT',fontsize=12.0)
                plt.ylabel('BRAND',fontsize=12.0)
                plt.show()  
            elif S==3:
                break
            else:
                print('ENTER VALID CHOICE')
        elif CH==3:
            break
        else:
            print('Enter Valid Choice!')
        
        
        
        
def bill():
    while True:
        print('---------------------------------------------')
        print('|  ENTER YOUR CHOICE!                       |')
        print('|   (1.) PURCHASE BILL                      |')
        print('|   (2.) SALES BILL                         |')
        print('|   (3.) BACK                               |')
        print('---------------------------------------------')
        y=int(input("ENTER YOUR COHICE:"))
        
        
        if y==1:
            displayshoe()
            SID=input('Enter SHOE ID:')
            query="Select Shoe_id,Sname,brand,Product_for,Rate,SQty\
                from shoe where shoe_id='{}'".format(SID)
            cursor.execute(query)
            data=cursor.fetchall()
            df=pd.DataFrame(data,columns=['ShoeID','Sname','Brand','Consumber','Rate','Qty'])
            print(df)
            sname=str(df.Sname[0])
            Brand=str(df.Brand[0])
            consumber=str(df.Consumber[0])
            price=int(df.Rate[0])
            qty=int(df.Qty[0])           
            now=datetime.datetime.now( )
            dtm=str(now)
            gstRate=9
            val=price* qty
            cgst=val*((gstRate/2)/100)
            sgst=cgst
            x=int(input("enter dicount(%):"))
            Discount=val*x/100
            print(Discount)
            print()
            net=val+cgst+sgst-Discount
            print('-' * 70)
            print('|TYPE OF SHOE:{0:>24s}                               |'.format(sname))
            print('-' * 70)
            print('|\t\t\t        PURCHASE INVOICE                     |')
            print('-' * 70)
            print('|Date : {0:>55s}      |'.format(dtm))
            print('-' * 70)
            print('|Brand :{0:>57}    |'.format(Brand))
            print('-' * 70)
            print('|Consumer:{0:>55}    |'.format(consumber))
            print('-' * 70)
            print('|ltem:-\t\t Unit Price|\tQuantity|\t value\t\t     |')
            print('-' * 70)
            print('|{0:<25s}'.format(SID),end=' ')
            print('{0:>7.2f}'.format(price),end=' ')
            print('|{0:>10d} '.format(qty),end=' ')
            print('|{0:>14.2f}      |'.format(val))
            print('-' * 70)
            print('|CGST :{0:>57.2f}     |'.format(cgst))
            print('-' * 70)
            print('|SGST :{0:>57.2f}     |'.format(sgst))
            print('-' * 70)
            print('|Discount :{0:>52.2f}      |'.format(Discount))
            print('-' *70)
            print('|Amount Payable:{0:>49.2f}    |'.format(net))
            print('-'* 70)
            print('|\t\t\t\tTHANK YOU                            |')
            print('-' * 70)
            
            
        elif y==2:
            displaysales()
            billno=input('Enter Bill No:')
            query="Select s_id,c_name,c_Number,brand,Rate,Quantity\
                from ssales where s_id='{}'".format(billno)
            cursor.execute(query)
            data=cursor.fetchall()
            df=pd.DataFrame(data,columns=['SId','CName','Mobile','Brand','Rate','Qty'])
            print(df)
            cname=str(df.CName[0])
            mobile=int(df.Mobile[0])
            Brand=str(df.Brand[0])
            price=int(df.Rate[0])
            qty=int(df.Qty[0])           
            now=datetime.datetime.now( )
            dtm=str(now)
            gstRate=9
            val=price* qty
            cgst=val*((gstRate/2)/100)
            sgst=cgst
            x=int(input("enter dicount(%):"))
            print()
            Discount=val*x/100
            net=val+cgst+sgst-Discount
            print('-' * 70)
            print('|customer name:{0:>24s}                               |'.format(cname))
            print('-' * 70)
            print('|\t\t\t\tSALES INVOICE                         |')
            print('-' * 70)
            print('|Date : {0:>55s}       |'.format(dtm))
            print('-' * 70)
            print('|Mobile :{0:>57}    |'.format(mobile))
            print('-' * 70)
            print('|Brand :{0:>57}     |'.format(Brand))
            print('-' * 70)   
            print('|ltem:-\t\t\tUnit Price  | Quantity  |\tvalue  \t     |')
            print('-' * 70)
            print('|{0:<25s}'.format(billno),end=' ')
            print('{0:>7.2f}'.format(price),end=' ')
            print('|{0:>10d} '.format(qty),end=' ')
            print('|{0:>14.2f}       |'.format(val))
            print('-' * 70)
            print('|CGST :{0:>57.2f}      |'.format(cgst))
            print('-' * 70)
            print('|SGST :{0:>57.2f}      |'.format(sgst))
            print('-' * 70)
            print('|Discount :{0:>52.2f}       |'.format(Discount))
            print('-' *70)
            print('|Amount Payable:{0:>49.2f}     |'.format(net))
            print('-'* 70)
            print('|\t\t\t\tTHANK YOU                             |')
            print('-' * 70)
        elif y==3:
            break
        else:
            print('Enter Valid Choice')
            
            
menu()
 
