class date:
    def __init__(self,a,b,c):
        self.d=a
        self.m=b
        self.y=c
    def day(self):
        print("Day: ",self.d)
    def month(self):
        print("month: ",self.m)
    def year(self):
        print("Year: ",self.y)
    def monthname(self):
        month=["Unknown","January","February","March","April","May","June","July","August","September","October","November","December"]
    def isleapyear(self):
        if(self.y%400==0)and(self.y%100==0):
            print("It is a leap yeay")
        elif(self.y%4==0)and(self.y%100!=0):
            print("It is  a leap year")
        else:
            print("It's not a leap year")
d1=date(14,3,2000)
d1.day()
d1.month()
d1.year()
d1.monthname()
d1.isleapyear()
        # it works

