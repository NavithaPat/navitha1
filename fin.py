class Mtca:
    principal = 'Mr.Prabhakar Naidu'
    college = 'MTCA'
    Location = 'palamaner'
     
    def __init__(self,name,mob,email,sem):
        self.name=name
        self.mobile=mob
        self.email=email
        self.sem=sem
    def update_mob(self,new):
        self.mobile=new
        print('mobile number updated')
        