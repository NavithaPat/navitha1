class A:
    a=90
    b=70
    def __init__(self,c,d):
      self.c=c
      self.d=d
class B(A):
   a=30
   def __init__(self,c,d,e,f):
      super().__init__(c,d)
      self.e=e
      self.f=f
class c(B):
     b=40

     def __init__ (self,c,d,e,f,g,h):
        super().__init__(c,d,e,f)
        self.g=g
        self.h=h

obj=c(4,5,6,7,8,9)
       
