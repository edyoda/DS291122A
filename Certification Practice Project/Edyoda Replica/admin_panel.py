import json
import random
class Admin_Panel:
    student_list=  []
    def __init__(self):
        self.module_details={}
        self.trainer_details={}
        self.student_details={}
        self.batch_details={}

    def admin_login(self,username,password):
        if username =="admin" and password == "admin":
            return True
        return False
    
    def add_module(self,module_name,duration):
        key=random.randint(1,100)
        topics_list=[]
        topics_size = int(input("Enter the number of topics you want to to add : "))
        for i in range(topics_size):
            topics = input("Enter Topic Name :")
            topics_list.append(topics)
        module={
            "module_name":module_name,
            "duration":duration,
            "topics":topics_list
        }
        self.module_details[key]=module
        with open("add_modules.json","w") as f:
            json.dump(self.module_details,f)
        return self.module_details
    
    def add_trainer(self):
        trainer_ID=random.randint(1,100)
        name=input("Enter Trainer name :")
        gender=input("Enter Trainers Gender :")
        qualification=input("Enter Trainers Qualification :")
        experience=input("Enter Trainer's Experience :")
        mobile=int(input("Enter Trainer's Mobile No :"))
        email=input("Enter Trainer's Mail Id :")
        password = input("Enter Password : ")
        age=int(input("Enter Trainer's Age :"))
        self.trainer_data = {
            "name":name,
            "gender":gender,
            "qualification":qualification,
            "age":age,
            "experience":experience,
            "mobile_no":mobile,
            "email_id":email,
            "password":password

        }
        self.trainer_details[trainer_ID]=self.trainer_data
        with open("trainer_details.json","w") as f:
            json.dump(self.trainer_details,f,indent=4)
        return self.trainer_details
        
    
    def add_student(self):
        key=random.randint(1,100)
        student_size=int(input("Enter the Number of student that you want to add :"))
        for i in range(1,student_size+1):
            print(f"Enter the Details of the student {i} :")
            name=input("Enter student Name :")
            gender=input("Enter  Student Gender :")
            age=int(input("Enter Student Age :"))
            qualification = input("Enter    Student Qualification :")
            experience=input("Enter Student Experience :")
            mobile=int(input("Enter Student's Mobile No :"))
            email=input("Enter Student's Mail Id :")
            password = input("Enter Password : ")
            self.student_data = {
            "name":name,
            "gender":gender,
            "qualification":qualification,
            "age":age,
            "experience":experience,
            "mobile_no":mobile,
            "email_id":email,
            "password":password
        
        
        }
            Admin_Panel.student_list.append(self.student_data)
            
        self.student_details[key] = Admin_Panel.student_list
        with open("student_details.json","w") as f:
            json.dump(self.student_details,f,indent=4)
        return self.student_details
    
    def add_batch(self,module_key,trainer_key,student_key):
        key=random.randint(1,100)
        batch_data={
            "module_key":module_key,
            "trainer_key":trainer_key,
            "student_key":student_key
        }
        self.batch_details[key]=batch_data
        return self.batch_details
    
    def get_module(self):
        return self.module_details
    
    def get_trainer(self):
        return self.trainer_details
     
    def get_student_list(self):
        return self.student_details
    def get_batch(self):
        return self.batch_details
    
    def remove_module(self):
        for k,v in self.module_details.items():
            print(f"Id : {k}  Data : {v}")
        module_key = int(input("Enter the Module Key that you want to remove "))
        if self.module_details[module_key]:
            self.module_details.pop(module_key)
        elif module_key not in self.module_details.keys():
            print("Please give valid Module Key")
        print("Module Successfully Deleted ")
        for k,v in self.module_details.items():
            print(f"Id : {k}  Data : {v}")
        with open("add_modules.json","w") as f:
            json.dump(self.module_details,f,indent=4)
    
    def edit_trainer(self):
        for k,v in self.trainer_details.items():
            print(f"Id : {k}  Data : {v}")
        trainer_code = int(input("Enter Trainer's code which you want to edit :"))
        trainer_edit = input("Enter which field you want to edit")
        trainer_updated_value = input("Enter Updated value :")
        self.trainer_details[trainer_code][trainer_edit] = trainer_updated_value
        
        return self.trainer_details       