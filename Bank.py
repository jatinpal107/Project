
base = []
def registraion():    
    
    Data_base = {}
    Data_base["Customer Name"] = input("Enter Name: ")
    Data_base["Age"] = int(input("Enter age: "))
    while True:
        m = int(input("Enter mobile number: "))
        n = str(m)
        if(n[0]!=0 and len(n)==10):
            Data_base["Mobile number"] = m
            break
        else:
            pass
    Data_base["Customer ID"] = len(base)
    Data_base["Password"] = input("Enter Password: ")
    print("Your password is ", Data_base["Password"])
    Data_base["Balance"] = int(input("Enter amount: "))
    base.append(Data_base)
  #  f = open("Untitled-2.py","a")
   # f.write(Data_base)
    return

print(base)
registraion()

server = []
def serv():
    i = 0
    while i<len(base):
        ci = int(input("Enter Customer ID: "))

        td = base[i]
        choice = 0
        i+=1
        if(ci==td["Customer ID"]):
            P = input("Enter Password: ")
            m = base[ci]
            pa = 0
            if(P==m["Password"] and pa<4):
                while True:
                    print("Press: \n 1 -> View Details\n 2 -> Edit Details\n 3 -> Exit ")
                    choice = int(input("Enter choice: "))
                    if(choice==1):
                        for key,value in m.items():
                            print(key,":",value)
                        break
                    elif(choice==2):
                        print("1. Name\n2.Age\n3. Mobile number\n4. Password\n5. Exit")
                        c = int(input("Choice: "))
                        if(c==1):
                            m["Name"] = input("Enter New name: ")
                            print(m["Name"])
                        elif(c==2):
                            m["Age"] = int(input("Enter age: "))
                            print(m["Age"])
                        elif(c==3):
                            while True:
                                correct =  int(input("Enter mobile number: "))
                                n = str(correct)
                                if(n[0]!=0 and len(n)==10):
                                    m["Mobile Number"] = n
                                    break
                                else:
                                    print("Try again invalid mobile number")                   
                        elif(c==4):
                            n = input("Enter Old password: ")
                            if(n==m["Password"]):
                                m["Password"] =  input("Enter New Password: ")
                                print(m["Password"])
                            else:
                                print("Try again invalid password")
                        elif(c==5):
                            break
                    elif(choice==3):
                    
                        break
                    else:
                        print("You choose wrong")

        elif(pa==3):
            print("Invalid password")
            print("1-> Back to login \n 2-> Exit")
            option = int(input("1-> Back to login \n Press any number expect of 1 -> Exit"))
            if(option== 1):
                serv()
            else:
                break
        else:
            print("Invalid password")
            pa += 1
        
    return

serv()
            
                    
                    



