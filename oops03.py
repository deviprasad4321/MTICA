class Student:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displayStudent(self):
        print(self.name,'is a student of',self.college,'Pursueing',self.course,'with a roll number of',self.rollno)
if __name__=="__main__":
    s1=Student("Devi Prasad",'1234')
    s2=Student("Revanth",'1235')
    s1.displayStudent()
    s2.displayStudent()

   
    
    
