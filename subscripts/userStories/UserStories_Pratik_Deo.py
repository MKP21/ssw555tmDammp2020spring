from datetime import date
from subscripts.outputDisplay import calculateage

today = date.today()
dateList = []


# User story 1 - all dates should be before current date
def DatebeforeCurrentDate(indi, fam):
    print("user story 1 - all dates should be before current date")
    for i in indi:
        # Checking death dates are before current dates and NA
        if str(i["DEAT"]) == "NA":
            pass
        elif i["DEAT"].date() > today:
            print(" Wrong death dates ")

        # Checking for Birth dates are before current Date
        if str(i["BIRT"]) == "NA":
            pass
        elif i["BIRT"].date() > today:
            print("These dates are after the current date: " + str(i["NAME"]) + str(i["BIRT"].date()))

    for j in fam:

        if j["MARR"].date() > today:
            print("Marriage date " + str(j["MARR"].date()) + " cannot be after current date " + str(today))

        if str(j["DIV"]) == "NA":
            pass
        elif j["DIV"].date() > today:
            print("Divorce date " + str(j["DIV"].date()) +" cannot be after the current date " + str(today))
    
    print("User stroy 1 ends ")
    

# User story 10 - Marriage should be after 14 years of age
def MarriageAfter14(indi, fam):
    print("User story 10 - Marriage should be after 14 years of age")
    
    for j in fam:
        for i in indi:
            if i["INDI"] == j["WIFE"]:
                days = 365.2425
                age = int(((j["MARR"].date()) - (i["BIRT"].date())).days / days)
                if age > 14:
                    pass
                else:
                    print("Invalid marriage date ")

            if i["INDI"] == j["HUSB"]:
                days = 365.2425
                age = int(((j["MARR"].date()) - (i["BIRT"].date())).days / days)
                if age > 14:
                    pass
                else:
                    print("Invalid marriage date ")                 
    
    print("User story 10 ends ")
    

#Helper functions
def getLastNamebyId(indi, Id):
    for i in indi:
        list1= []
        if(i["INDI"] == Id):
            s = i["NAME"]
            #print(s)
            list1 = s.split()
            return list1[1]

def getSexByid(indi, Id):
    sex = ""
    for i in indi:
        if(i["INDI"] == Id):
            sex = i["SEX"]
            
    return sex

def getAgeById(indi, Id):
    age = 0
    for i in indi:
        if(i["INDI"] == Id ):
            age = calculateage(i["BIRT"], i["DEAT"])
    
    return age

def getAliveById(indi, Id):
    alive = True
    for i in indi:
        if(i["DEAT"] == "NA"):
            alive = True
        else: 
            alive = False
    
    return alive

def getNamebyId(indi, Id):
    name = " "
    for i in indi:
        if(i["INDI"] == Id):
            name = i["NAME"]

    return name