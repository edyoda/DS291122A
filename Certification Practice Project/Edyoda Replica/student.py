class Student:
    def __init__(self,ID,name,gender,qualification,age,experience,mobile_no,email_ID,password):
        self.__name=name
        self.__ID=ID
        self.__gender=gender
        self.__qualification=qualification
        self.__experience=experience
        self.__mobile_no=mobile_no
        self.__email_ID=email_ID
        self.__password=password
        self.__age=age

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name=name

    def get_ID(self):
        return self.__ID
    
    def set_ID(self,ID):
        self.__ID=ID

    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender
    
    def get_qualification(self):
        return self.__qualification
    
    def set_qualification(self,qualification):
        self.__qualification=qualification
    
    def get_experience(self):
        return self.__experience

    def set_experience(self,experience):
        self.__experience=experience

    def get_mobile(self):
        return self.__mobile_no
    
    def set_mobile(self,mobile_no):
        self.__mobile_no=mobile_no
    
    def get_email(self):
        return self.__email_ID

    def set_email(self,email):
        self.__email_ID=email
    
    def get_password(self):
        return self.__password
    def set_password(self,password):
        self.__password=password

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age=age
    
    def __str__(self):
        return ("Name : "+self.__name+"\nGender:"+self.__gender+"\nQualification :"+self.__qualification+"\nExperience :"+self.__experience+"\nMobile Number "+str(self.__mobile_no)+"\nEmail Id :"+self.__email_ID+"\nAge :"+str(self.__age))
    
#self,ID,name,gender,qualification,age,experience,mobile_no,email_ID,password)
c=Student(10,"Pratyush","Male","M.Tech","21","5 years",9876543210,"pratyushsrivastava@gmail.com","Qui")
print(c)
