class students:
    def __init__(self,m1,m2) -> None:
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m=self.m1+other.m1
        n=self.m2+other.m2
        return students(m,n)
    
s1=students(20,20)
s2=students(30,30)
s3=s1 + s2

print(type(s3),s3.m1,s3.m2)