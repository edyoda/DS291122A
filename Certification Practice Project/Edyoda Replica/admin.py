class Admin:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def get_username(self):
        return self.username
    def set_username(self,username):
        self.username=username
    def get_password(self):
        return self.password
    def set_password(self,password):
        self.password=password
    