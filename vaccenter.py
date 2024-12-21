print("---ABDULRAHMAN ALI OMAR ABDULLAH---")
print("---TP063120--- ")
import datetime

#search function is to check the patient record and vaccinatio status
def search():
    fl = open("patientinfo.txt", "r")
    pationid = str(input("please enter the patient id to search his record")).strip()
    for i in fl:
        # to show the pation record from patientinfo.txt
        if pationid in i: #to check if the ID exist
            print(i)
            break
        else:
            continue
    if pationid not in i:
        print("invalid id entered")

    # to show the vaccination status
    ff = open("vaccination", "r")
    cnt = 0
    cnt1 = 0
    cnt2 = 0
    for n in ff:
        if pationid in n:
            if "NEW" not in n:
                if "EC" in n:
                    cnt = cnt + 1
                    break
                elif "booth" in n:
                    cnt1 = cnt1 + 1
                elif "D1" in n:
                    cnt2 = cnt2 + 1

    if cnt == 0 and cnt1 == 1 and cnt2 == 1:
        print("vaccination status: vaccinated with booth doses (COMPLETED)")
    elif cnt == 1:
        print("vaccination status: vaccinated with EC (COMPLETED)")
    elif cnt2 == 1 and cnt1 == 0:
        print("vaccination status: vaccinated with  the firt dose (wating for the second dose)")
    elif cnt1==0 and cnt1==0 and cnt2==0:
        print("vaccination status: NEW")
def idline():
    file=open("abdulrahman.txt","r")
    for i in file:
        lastl=i
        conv1=int(lastl)+1 #converting from str to int
        conv2=len(str(conv1))
        if conv2==1:
            id='00000'+str(conv1)
        elif conv2==2:
            id = '0000' + str(conv1)
        elif conv2==3:
            id = '000' + str(conv1)
        elif conv2==4:
            id = '00' + str(conv1)
        elif conv2==5:
            id = '0' + str(conv1)
        else:
            id=str(conv1) #converting from int to str
    file = open("abdulrahman.txt", "w")
    file.write(id)
    return id
def reg():
    #to calculate the date
    days = datetime.timedelta(days=5)
    d = datetime.datetime.now()
    datenow = datetime.datetime.date(d)
    datafter = days + datenow
    vc=input("which vaccinatin center you prefer(vc1/vc2)").strip().upper()
    name = input("enter name")
    i = len(name)
    for char in range(i):#name validation
        if name[char].isalpha() or name[char].isspace():
            cnt = 1
        else:
            cnt = 2
            break
    try:
        age = int(input("enter age"))
        cnt1 = 1
    except:
        cnt1 = 2
    email = input("enetr email")
    cnt2 = 0
    if "@" in email and "." in email:#email validation
        try:
            if email.index(".") > email.index("@"):
                cnt2 = 1
        except:
            print(" ")
    else:
        cnt2 = 0

    if cnt==1:
        print("valid name enterd")
    else:
        print("invalid name enterd")
    if cnt1==1:
        print("valid age enterd")
        if age > 45:
            print("AF: this vacc required 2 doses and 2 weeks between the doses")
            print("DM: this vacc required 2 doses and 4 weeks between the doses")
            print("BV: this vacc required 2 doses and 3 weeks between the doses")
            print("EC: this vacc required 1 doses only")
            vaccine = input("please chose the vaccine you want from the vaccines list displayed").strip().upper()
            if vaccine == "AF":
                print("ok")
            elif vaccine == "DM":
                print("ok")
            elif vaccine == "BV":
                print("ok")
            elif vaccine == "EC":
                print("ok")
            else:
                print("sorry this vaccine is not avilable")

        elif age >= 12 and age >= 18 and age <= 45:
            print("CZ: this vacc required 2 doses and 3 weeks between the doses")
            print("AF: this vacc required 2 doses and 2 weeks between the doses")
            print("DM: this vacc required 2 doses and 4 weeks between the doses")
            print("BV: this vacc required 2 doses and 3 weeks between the doses")
            print("EC: this vacc required 1 doses only ")
            vaccine = input("please chose the vaccine you want from the vaccines list displayed").strip().upper()
            if vaccine == "CZ":
                print("ok")
            elif vaccine == "AF":
                print("ok")
            elif vaccine == "DM":
                print("ok")
            elif vaccine == "EC":
                print("ok")
            elif vaccine == "BV":
                print("ok")
            else:
                print("sorry this vaccine is not avilable")
        elif age >= 12 and age < 18:
            print("DM: this vacc required 2 doses and 4 weeks between the doses")
            print("CZ: this vacc required 2 doses and 3 weeks between the doses")
            print("AF: this vacc required 2 doses and 2 weeks between the doses")
            vaccine = input("please chose the vaccine you want from the vaccines list displayed").strip().upper()
            if vaccine == "CZ":
                print("ok")
            elif vaccine == "AF":
                print("ok")
            elif vaccine == "DM":
                print("ok")
            else:
                print("sorry this vaccine is not avilable")
        else:
            print("vaccination is not available for you ")
    else:
        print("invalid age enterd")
    try:
        if vaccine == "AF" or vaccine == "DM" or vaccine == "CZ" or vaccine == "BV" or vaccine == "EC":
            print("valid vaccine enterd")
            cnt4 = 1
        else:
            print("invalid vaccine enterd")
            cnt4 = 2
    except:
        print(" ")
    if vc=="VC1"or vc=="VC2":
        print("valid vaccination center enterd")
        cnt3=1
    else:
        print("ivalid vaccination center enterd")
        cnt3=2
    if cnt2==1:
        print("valid email enterd")
    else:
        print("invalid email enterd")
    if cnt==1 and cnt1==1 and cnt2==1 and cnt4==1 and cnt3==1:
        idline()
        f = open("abdulrahman.txt", "r")
        for id in f:
            break
        filee=open("patientinfo.txt","a")
        filee.write(f"{id}:{name}:{age} yeras old:{email} :{vc} :{vaccine}:registration date{datenow}:first dose data{datafter}\n")
        print("YOU HAVE BEEN REGISTERD")
        fil=open("vaccination","a")
        fil.write(f"{id} : NEW : {vc}\n")
    else:print("please enter correct information")
#function to manage the Vaccine Administration
def vacadm():
    pationid = str(input("please enter the patient id ")).strip() #pationid= the patient ID
    fll = open("patientinfo.txt", "r")
    fil = open("vaccination", "r")
    for m in fll:
        if pationid in m:
            print(f"first dose date:{m[-11:-1]}")
    fll.close()
    strdate = m[-11:-1]
    conv = datetime.datetime.strptime(strdate, '%Y-%m-%d').date()
    print("enter the current date")
    year = int(input('Enter a year'))
    month = int(input('Enter a month'))
    day = int(input('Enter a day'))
    date1 = datetime.date(year, month, day) #date1= the curent date
    if date1 >= conv:
        datee = 1
    else:
        datee = 2
    fl = open("patientinfo.txt", "r")
    r=0
    s=0
    for i in fl:            #to check the vaccine type and the center
        if pationid in i:
            r=r+1
            if pationid in i and "EC" not in i and "VC1" in i:

                for g in fil:
                    if pationid in g:
                        vaccine="-"
                        center="VC1"

                        s=s+1


                    elif pationid not in g:
                        center="VC1"
            elif pationid in i and "EC" not in i and "VC2" in i:
                for g in fil:
                    if pationid in g:
                        center = "VC2"
                        vaccine="-"

                        s=s+1

                    elif pationid not in g:
                        center = "VC2"


            elif pationid in i and "EC" in i and "VC2" not in i:

                for g in fil:

                    if pationid in g:
                        vaccine = "EC"

                        center = "VC1"

                        s = s + 1

            elif pationid in i and "EC" in i and "VC1" not in i:

                for g in fil:

                    if pationid in g:
                        vaccine = "EC"

                        center = "VC2"

                        s = s + 1
        elif pationid not in i:
            r=r+0

    try:
        if r==1:
            if vaccine=="EC":
                if center=="VC2" and datee==1 and s==1:
                    filee = open("vaccination", "a")
                    filee.write(f"{pationid}:")
                    filee.write("completed EC: VC2\n")
                    print("vaccination completed")
                elif center=="VC1" and datee==1 and s==1:
                    filee = open("vaccination", "a")
                    filee.write(f"{pationid}:")
                    filee.write("completed EC: VC1\n")
                    print("vaccination completed")
            elif vaccine!="EC":
                if s==2 and center=="VC1" and datee==1 :
                    fil = open("vaccination", 'r')
                    for i in fil:
                        if pationid in i:
                            if "next" in i:
                                strdate1 = i[-11:-1]
                                conv = datetime.datetime.strptime(strdate1, '%Y-%m-%d').date()
                                if date1 >= conv:
                                    filee = open("vaccination", "a")
                                    filee.write(f"{pationid}:")
                                    filee.write("completed booth: VC1\n")
                                    print("vaccination completed")
                                else:
                                    print(f"wait until your second dose date\nyor second dose date is:{conv}")
                elif s==2 and center=="VC2" and datee==1 :
                    fil = open("vaccination", 'r')
                    for i in fil:
                        if pationid in i:
                            if "next" in i:
                                strdate1 = i[-11:-1]
                                conv = datetime.datetime.strptime(strdate1, '%Y-%m-%d').date()
                                if date1 >= conv:
                                    filee = open("vaccination", "a")
                                    filee.write(f"{pationid}:")
                                    filee.write("completed booth: VC2\n")
                                    print("vaccination completed")
                                else:
                                    print(f"wait until your second dose date\nyor second dose date is:{conv}")
                elif s==1 and center=="VC1" and datee==1:
                    filee = open("vaccination", "a")
                    filee.write(f"{pationid}:")
                    filee.write("completed D1: VC1")
                elif s==1 and center=="VC2" and datee==1 :
                    filee = open("vaccination", "a")
                    filee.write(f"{pationid}:")
                    filee.write("completed D1: VC2")
                if datee!=1:
                    print("wait until your vccination date")

        else:

           print("invalid ID enterd")
    except: # to check the number of doses and assign the date for doses
        print(' ')
    if s==1:
        fill = open("patientinfo.txt", 'r')
        fil = open('vaccination', 'r')
        cnt = 0
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        for i in fill:
            if pationid in i:
                if "BV" in i:
                    vaccinee = "BV"
                    for i in fil:
                        if pationid in i:
                            cnt = cnt + 1
                elif "CZ" in i:
                    vaccinee = "CZ"
                    for i in fil:
                        if pationid in i:
                            cnt1 = cnt1 + 1
                elif "AF" in i:
                    vaccinee = "AF"
                    for i in fil:
                        if pationid in i:
                            cnt2 = cnt2 + 1
                elif "DM" in i:
                    vaccinee = "DM"
                    for i in fil:
                        if pationid in i:
                            cnt3 = cnt3 + 1

        try:
            if vaccinee == "BV":
                if cnt == 1:
                    days = datetime.timedelta(days=21)
                    d2date = days + date1
                else:
                    print("thanks")
            elif vaccinee == "CZ":
                if cnt1 == 1:
                    days = datetime.timedelta(days=21)
                    d2date = days + date1
                else:
                    print("thanks")
            elif vaccinee == "AF":
                if cnt2 == 1:
                    days = datetime.timedelta(days=14)
                    d2date = days + date1
                else:
                    print("thanks")
            elif vaccinee == "DM":
                if cnt3 == 1:
                    days = datetime.timedelta(days=28)
                    d2date = days + date1
                else:
                    print("thanks")
            if date1 >= conv:
                file=open("vaccination",'a')
                file.write(f":next dose date {d2date}\n")
                print("first dose completed")
        except:
            print(" ")

#To count the number of people been vaccinetd in each center
def statisinfo():
    vcenter=int(input("enter the vaccine center you want to read it's Statistical Information 1/2"))
    file=open("vaccination","r")
    cnt1=0
    cnt2=0
    cnt3=0
    cnt4=0
    cnt5=0
    cnt6=0
    if vcenter == 1:
        for i in file:
            if "VC1" in i and "D1" in i:
                cnt1=cnt1+1
            elif "VC1" in i and "booth" in i :
                cnt2=cnt2+1
            elif "VC1" in i and "EC"  in i:
                cnt3=cnt3+1
        print(f"number of people vaccinated in VC1 :{cnt3+cnt1}")
        print(f"number of people waiting next dose is:{cnt1-cnt2}")
        print(f"number of people completed vaccination in VC1 :{cnt3+cnt2}")
    elif vcenter == 2:
        for i in file:
            if "VC2" in i and "D1" in i:
                cnt4=cnt4+1
            elif "VC2" in i and "booth"  in i :
                cnt5=cnt5+1
            elif "VC2" in i and "EC"  in i:
                cnt6=cnt6+1
        print(f"number of people vaccinated in VC2 :{cnt6+cnt4}")
        print(f"number of people waiting for next dose in VC2 :{cnt4-cnt5}")
        print(f"number of people completed vaccination in VC2 :{cnt6+cnt5}")

user1=["staff1","1010101"]
user2=["staff2","2020202"]
username=input("enter the user name")
password=input("enter the password")
if   username==user1[0] and password==user1[1] or username==user2[0] and password==user2[1]:
    print('WELCOME')
    while True:
        print("1- Register new patient\n")
        print("2- Vaccine Administration\n")
        print("3- Search patient record and Vaccination status \n")
        print("4-Statistical Information")
        print("5- Exit")
        choice = input("Enter your Choice :")
        if choice == "1":
            reg()
        elif choice == "2":
            vacadm()
        elif choice == "3":
            search()
        elif choice == "4":
            statisinfo()
        elif choice == "5":
            break
else:
    print("wrong password or username enterd")
