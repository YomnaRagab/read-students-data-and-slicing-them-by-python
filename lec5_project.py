def EnterStudent(lis_std):
    while True:
        student=input("Enter the first name, Last name, semester, GPA and ID or DONE for break ")
        if(student.lower()=="done"): #if the option is done then terminate the loop
            break
        lis_std.append(student) #if not , then append the list with new info
    return(lis_std) #return the list after modification
def Printing(lis_std):
    for i in lis_std: #loop for each student in the list
        fnLoc=i.find(" ") #search for the first space
        FirstName=i[0:fnLoc] #then from the start till the first space ,save them in the first name
        lsLoc=i.find(" ",fnLoc+1) #search for the second space , starting from the first place of it+1 to not find the first one again 
        LastName=i[fnLoc+1:lsLoc] #save the chracters from the first space+1 till the second spaace
        semLoc=i.find(" ",lsLoc+1) #same as before
        Semester=int(i[lsLoc+1:semLoc]) #same as before but convert it into integer
        GPAloc=i.find(" ",semLoc+1)
        GPA=int(i[semLoc+1:GPAloc]) 
        IDloc=i.find(" ",GPAloc+1)
        ID=int(i[GPAloc+1:IDloc])
        print("First name is",FirstName,"Last name is",LastName,
              "Semester is",Semester,"GPA is",GPA,"ID:",ID)
    
lis_std=list()
while True:
    option=int(input("choose your option\n1)New students\n2)print all students\n0)Exit\nYour choice:"))
    if option==0:
        print("Bye")
        break
    elif option==1:
        students=EnterStudent(lis_std)
        print(students)
    elif option==2:
        students=Printing(lis_std)
        
        
