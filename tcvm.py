from model import *

class app:
    tea=2000
    coffee=2000
    sugar=8000
    water=15000
    milk=10000

    choise=0

    teacount=0
    blkteacount=0
    coffcount=0
    blkcoffcount=0

    def start(self):
        while True:
            self.printoption()
            if app.choise==1:
                self.maketea()
            elif app.choise==2:
                self.makecoffee()
            elif app.choise==3:
                self.makeblktea()
            elif app.choise==4:
                self.makeblkcof()
            elif app.choise==5:
                self.refill()
            elif app.choise==6:
                self.sale()
            elif app.choise==7:
                self.status()
            elif app.choise==8:
                self.reset()

    def printoption(self):
        print("1. Make Tea")
        print("2. Make Coffee")
        print("3. Make Black tea")
        print("4. Make Black coffee")
        print("5. Refill Container")
        print("6. Check Total Sele")
        print("7. Container Status")
        print("8. Reset Container")

        app.choise=int(input("Enter Your Choise"))

    def maketea(self):
        c=int(input(" number of Tea cup-"))
        app.teacount+=c
        tc=tea()
        app.tea-=tc.te*c
        app.water-=tc.water*c
        app.milk-=tc.milk*c
        app.sugar-=tc.sugar*c
        print("Thank You")
    
    def makecoffee(self):
        c=int(input("number of Coffee cup-"))
        app.coffcount+=c
        cf=coffee()
        app.coffee-=cf.coff*c
        app.water-=cf.water*c
        app.milk-=cf.milk*c
        app.sugar-=cf.sugar*c
        print("Thank You")

    def makeblktea(self):
        c=int(input("number of Black Tea cup"))
        app.blkteacount+=c
        bt=black_tea()
        app.tea-=bt.te*c
        app.water-=bt.water*c
        app.sugar-=bt.sugar*c
        print("Thank You")

    def makeblkcof(self):
        c=int(input("number of Black Coffee cup-"))
        app.blkcoffcount+=c
        bc=black_coffee()
        app.coffee-=bc.coff*c
        app.water-=bc.water*c
        app.sugar-=bc.sugar*c
        print("Thank You")

    def sale(self):
        sum=0
        sum=(app.teacount*10)+(app.coffcount*15)+(app.blkteacount*5)+(app.blkcoffcount*10)
        print("total sale",sum,"Rs")

    def status(self):
        print("tea status-",app.tea/1000,"Kg")
        print("coffee status-",app.coffee/1000,"Kg")
        print("sugar status-",app.sugar/1000,"Kg")
        print("water status-",app.water/1000,"L")
        print("milk status-",app.milk/1000,"L")
        
    def refill(self):
        app.tea=2000
        app.coffee=2000
        app.sugar=8000
        app.water=15000
        app.milk=10000
        print("Refilling is Done")

    def reset(self):
        app.teacount=0
        app.blkteacount=0
        app.coffcount=0
        app.blkcoffcount=0








service=app()
service.start()
