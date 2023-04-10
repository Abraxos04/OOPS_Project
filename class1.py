class Car:
    ID=0
    model=""
    make=""
    year=0
    price=0
    avail=True
    def __init__(self,id,mod,maker,yr,cost,avail):
        self.ID=id
        self.model=mod
        self.make=maker
        self.year=yr
        self.price=cost
    def disp(self):
        print(f'Car ID: {self.ID}, Car Make: {self.make}, Car Model: {self.model}, Car Year: {self.year}, Car Rental Price per Day: ${self.price}')

c1=Car(1,"Supra","Toyota",2018,50,True)
c2=Car(2,"Civic","Honda",2019,40,True)
c3=Car(3,"Mustang","Ford",2017,60,True)
c4=Car(4,"Alto 800","Maruti",2018,35,True)
list_cars= [c1,c2,c3,c4]


class customer:
    customer_ID=0
    Name=""
    cars=[]
    def __init__ (self,ID,custname,ca):
        self.customer_ID=ID
        self.Name=custname
        self.cars=ca
    def rent(self,choice,days):
        cost=0
        if(list_cars[choice-1].avail):
            self.cars.append(list_cars[choice-1])
            cost=days*list_cars[choice-1].price
            print(f'Car rented successfully.')
            list_cars[choice-1].disp()
            print(f'Rental Days: {days}')
            print(f'Rental Price: {cost}')
            list_cars[choice-1].avail=False
        else:
            print('Car not available for Rent')
        return cost

    def ret(self,id):
        check=0
        for i in self.cars:
            if(i.ID==id):
                check=1
                list_cars[id-1].avail=True
                self.cars.remove(i)
                print('Car returned successfully')
        if(check==0):            
            print('You have not rented this car')

    def disp(self):
        if(len(self.cars)==0):
            print("You have not rented any cars")
        else:    
            for i in self.cars:
                i.disp

cust=[]
class CarRental:
    TotRev=0
    def __init__(self):
        Totrev=0

    def dispav(self):
        for i in list_cars:
            if(i.avail):
                i.disp()
    
    def disprent(self):
        for i in list_cars:
            if(i.avail==False):
                i.disp()

    def Rent(self):
        print('Enter your name: ')
        x=input()
        print('Enter Car ID: ')
        id=(int)(input())
        print('Enter Rental Days: ')
        day=(int)(input())
        check=0
        for i in cust:
            if(i==x):
                check=1
                self.TotRev+=i.rent(id,day)
        if(check==0):
            c=customer(len(cust)+1,x,[])
            self.TotRev+=c.rent(id,day)
            cust.append(c)

    def Return(self):
        print('Enter your name: ')
        x=input()
        print('Enter Car ID: ')
        id=(int)(input())
        
        check=0
        for i in cust:
            if(i==x):
                check=1
                self.Totrev+=i.ret(id)
        if(check==0):
            c=customer(len(cust)+1,x,[])
            i.ret(id)

    def dispRev(self):
        print(f"Total Revenue: {self.TotRev}")

print('''
        Welcome to Car Rental System!
        1. Display available cars for rent
        2. Rent a car
        3. Return a car
        4. Display the list of rented cars
        5. Display the total revenue
        6. Exit
    ''')

print('Enter your choice: ')
ch=(int)(input())
System=CarRental()
while ch!=6:
    if(ch==1):
        System.dispav()
    elif(ch==2):
        System.Rent()
    elif(ch==3):
        System.Return()
    elif(ch==4):
        System.disprent()
    elif(ch==5):
        System.dispRev()
    elif(ch==6):
        break
    else:
        print("Invalid Input, Try Again!")
    print('Enter your choice: ')
    ch=(int)(input())

print('Thank You')


        



        

        


        

