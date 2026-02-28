server = []
base = []
comfirmation = 0
customer_id = 0
verify = 0
def registration():    
    
    Data_base = {}
    Data_base["Customer Name"] = input("Enter Name: ")
    Data_base["Age"] = int(input("Enter age: "))
    while True:
        m = int(input("Enter mobile number: "))
        n = str(m)
        if(n[0]!=0 and len(n)==10):
            Data_base["Mobile Number"] = m
            break
        else:
            print("Enter correct mobile number shouldn't start with 0 \n Total digits remains 10")
    Data_base["Customer ID"] = len(base)*100000+951357-159735
    Data_base["Password"] = input("Enter Password: ")
    print("Your password is ", Data_base["Password"])
    Data_base["Debit Card ID"] = len(base)*10000+8520-2587
    Data_base["DC PIN"] = int(input("Create Debit Card Pin: "))
    Data_base["Balance"] = int(input("Enter amount: "))
    base.append(Data_base)
    server.append(len(base)-1)
    return


def find_user():
    x = int(input("Enter User no.: "))
    i = 0
    while i < len(server):
        if(server[i]==x):
            print("This user exist in database")
            global comfirmation
            comfirmation = 1+x
        else:
            pass
        i += 1
    if(comfirmation==0):
        print("User not found please check user no.")
        exit()
    else:
        pass
    return

def authenticate():
    pa = 0
    global customer_id 
    customer_id = int(input("Enter Customer ID : "))
    td = base[comfirmation-1]
    ca = 0
    while True:
        if(customer_id == td["Customer ID"]):
            p = input("Enter password: ")
            if(p==td["Password"]):
                global verify
                verify += 1
                break
            elif(pa<4):
                print("Your all attempts sre are used so sorry please check paasword")
                global comfirmation, customer_id
                customer_id = 0
                comfirmation = 0
                exit()
            else:
                pa = pa+1
                print(pa,"out of attempt used")
        elif(ca<4):
            global customer_id, comfirmation
            comfirmation = 0
            customer_id = 0
            break
        else:
            ca += 1
            print("Invalid Customer ID\n",ca,"out of 4 attmept used")
    return
            
def deposit():
    if(verify==1):
        import random
        OTP = random.randint(111111,999999)
        print(OTP)
        oe = int(input("Enter OTP: "))
        if(oe==OTP):
            tb = base[comfirmation-1]
            print("Current balance: ",tb["Balance"])
            amount = int(input("Enter amount to deposit: "))
            tb["Balance"] = tb["Balance"] + amount
            print("Updated balance: ",tb["Balance"])
        else:
            print("Incorrect OTP")
    else:
        print("Please first verify password")
    return

def withdrawal():
    di = int(input("Enter Debit Card ID: "))
    tb = base[comfirmation-1]
    da = 0
    pa = 0
    while True:
        if(di==tb["Debit Card ID"]):
            pin = int(input("Enter Pin: "))
            if(pin==tb["DC PIN"]):
                amount = int(input("Enter amount to withdrawal: "))
                if(tb["Balance"] >= amount):
                    tb["Balance"] = tb["Balance"] - amount
                    print("Withdrawal succesfully\n Updated balance: ",tb["Balance"])
                    break
                else:
                    print("Insufficient balnce")
            elif(pa>=3):
                global comfirmation, customer_id, verify
                verify = 0
                comfirmation = 0
                customer_id = 0
                break
            else:
                pa += 1
                print(pa,"out of 3 attempt used")
        elif(da>=3):
            global comfirmation, customer_id, verify
            verify = 0
            comfirmation = 0
            customer_id = 0
            break
        else:
            da += 1
    return

def check_balance():
    if(comfirmation >= 1 and verify == 1):
        tb = base[comfirmation-1]
        print(tb["Balance"])
    else:
        print("Please verify user number and password")
    return
def details():
    tb = base[comfirmation-1]
    for key,value in tb.items():
        print(key,":",value)
    return
def edit_details():
    tb = base[comfirmation-1]
    while True:
        print("1. Name\n2.Age\n3. Mobile number\n4. Password\n5. Exit")
        c = int(input("Choice: "))
        if(c==1):
            tb["Name"] = input("Enter New name: ")
            print(tb["Name"])
        elif(c==2):
            tb["Age"] = int(input("Enter age: "))
            print(tb["Age"])
        elif(c==3):
            while True:
                correct =  int(input("Enter mobile number: "))
                n = str(correct)
                if(n[0]!=0 and len(n)==10):
                    tb["Mobile Number"] = n
                    break
                else:
                    print("Try again invalid mobile number")     
        elif(c==4):
                n = input("Enter Old password: ")
                if(n==tb["Password"]):
                    tb["Password"] =  input("Enter New Password: ")
                    print(tb["Password"])
                else:
                    print("Try again invalid password")
        elif(c==5):
            break
    return

find_user()
authenticate()
while True:
    choice  = int(input("1-> Check Details\n2-> Edit detail\n3-> Check balance\n4-> Deposit\n5-> Withdrawal\n6-> Exit"))
    if(choice==1):
        details()
        choose = int(input("Press\n 1-> Back to menu\n 2-> exit"))
        if(choose==1):
            pass
        else:
            break
    elif(choice==2):
        edit_details()
        choose = int(input("Press\n 1-> Back to menu\n 2-> exit"))
        if(choose):
            pass
        else:
            break
    elif(choice==3):
        check_balance()
        choose = int(input("Press\n 1-> Back to menu\n 2-> exit"))
        if(choose==1):
            pass
        else:
            break
    elif(choice==4):
        deposit()
        choose = int(input("Press\n 1-> Back to menu\n 2-> exit"))
        if(choose==1):
            pass
        else:
            break
    elif(choice==5):
        withdrawal()
        choose = int(input("Press\n 1-> Back to menu\n 2-> exit"))
        if(choose==1):
            pass
        else:
            break
    elif(choice==6):
        break
    else:
        print("Invalid choice")
    
    

        
                

