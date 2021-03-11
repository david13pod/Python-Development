class Dairy ():
    '''
    Work in progress!!! 
    First phase completed. 
    2nd phase involves saving the schedules in file with appropriate format and being able to reteive it
    Last phase should involve searching the retreived schedules for saved appointments
    '''
    
    def initial (self):
        self.calendar=['jan','feb','mar','apr','may','jun','july','aug','sept','oct','nov','dec']
        self.edate=input ('Enter the date in this format dd/mm/yy ')
        self.date=self.edate.strip()
        self.mnth=int(self.date[3:5])
        self.month={'jan':[1,31],'feb':[1,28],'mar':[1,31],'apr':[1,30],'may':[1,31],'jun':[1,30],'july':[1,31],'aug':[1,31],'sept':[1,30],'oct':[1,31],'nov':[1,30],'dec':[1,31]}
        
       
    
    def checkmonth(self):
        for a in range(1,13):
            if a == self.mnth:
                self.chckdmnth=self.calendar[(a-1)]
                break
            elif a> 12:
                print('Wrong date format')
                Dairy.initial(self)
                break
            else:
                continue
                
    def checkdate(self):
        Dairy.checkmonth(self)
        dated=int(self.date[0:2])
        if dated< min(self.month[self.chckdmnth]) or dated> max(self.month[self.chckdmnth]):
            print('something is wrong with the date inputed, try again ')
            Dairy.initial(self)
        else:
            pass

        
    
class Doctors (Dairy):
    
    def __init__ (self):
        self.name=input ('Enter Doctors name ')
        self.schedule={}
        Dairy.initial(self)
        
    def chkappoinment(self):
        self.eappointments= input('Enter customers name ')
        self.eappointment= self.eappointments.strip()
        for nam in self.schedule.keys():
            if nam == self.eappointment:
                print (self.schedule[self.eappointment])
            else:
                print('No appointment in the database ')
                boka=input('do you want to book one? Y or N ')
                self.boka=boka.upper()
                if boka =='Y':
                    Doctors.boook(self)
                else:
                    print('Thanks!')
    
    def book(self):
        self.ecustname=input('Enter customers name ')
        self.custname=self.ecustname.strip()
        self.etime=input('Enter the appointment time in format HH:MM: from 08:00 to 17:00 ')
        self.time=self.etime.strip()
        Dairy.checkmonth(self)
        Dairy.checkdate(self)
        self.schedule={self.custname : [self.name,self.date,self.time]}


# Uncomment to book and check appointment
hos=Doctors()
#hoschck=hos.chkappoinment()
#hosbook=hos.book()
