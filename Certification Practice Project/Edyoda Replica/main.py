from admin_panel import *
import sys
admin=Admin_Panel()
while True:
    print("Press 1 For Admin Login")
    print("Press 2 For Student Login")
    print("Press 3 For Traine's Login")
    print("Press 4 For Exit")
    print("*"*100)
    choice = int(input("Enter Your Choice :" ))
    print("*"*100)
    if choice==1:
        print("************************Admin Login*******************************")
        username=input("Enter Admin UserName :")
        password=input("Enter Admin Password :")
        temp = admin.admin_login(username,password)
        if temp:
            print("Logged in Successfully ")
            print("Press 1 For Add Module :")
            print("Press 2 For Add Trainer :")
            print("Press 3 For Add Student :")
            print("Press 4 For Add Batch :")
            print("Press 5 To Get Modules Details : ")
            print("Press 6 To Get Batch Details : ")
            print("Press 7 To Get Trainer's Details : ")
            print("Press 8 To Get Student's List ")
            print("Press 9 For Remove Module : ")
            print("Press 10 For Edit Trainer's Detail : ")
            print("*"*100)
            option = int(input("Enter Your Choice :"))
            print("*"*100)
            if option==1:
                module_name=input("Please Enter Module Name :")
                module_duration=input("Please Enter Module Duration :")
                print(admin.add_module(module_name,module_duration))
                print("Module Added Successfully")
                print("*"*100)
            elif option==2:
                print(admin.add_trainer())
                print("Trainer Added Sucessfully")
                print("*"*100)
            elif option==3:
                print(admin.add_student())
                print("Student Added Sucessfully")
                print("*"*100)
            elif option==4:
                module=input("Enter Module Name :")
                trainer=input("Enter Trainer Name :")
                student=input("Enter Student Name :")
                print(admin.add_batch(module,trainer,student))
                print("Batch Added Sucessfully")
                print("*"*100)
            elif option==5:
                print(admin.get_module())
                print("*"*100)
            elif option==6:
                print(admin.get_batch())
                print("*"*100)
            elif option==7:
                print(admin.get_trainer())
                print("*"*100)
            elif option==8:
                print(admin.get_student_list())
                print("*"*100)
            elif option==9:
                admin.remove_module()
                print("Module Removed Sucessfully")
                print("*"*100)
            elif option==10:
                print(admin.edit_trainer())
                print("Data Updated Successfully")
                print("*"*100)
        else:
            print("Enter Valid UserName and Password ")
    elif choice==2:
        print("Sucessfully log in as a Student")
    elif choice==3:
        print("Sucessfully log in as a Trainer")
    elif choice==4:
        print("Thank You for Using Our Application.....")
        sys.exit()


        




