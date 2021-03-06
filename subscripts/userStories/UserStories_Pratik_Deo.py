from datetime import date
from subscripts.outputDisplay import calculateage
import prettytable
from subscripts.userStories.UserStories_MP import getIndiByID, getFamByID

today = date.today()
dateList = []


# User story 1 - all dates should be before current date
def us01(indi, fam, f):
    print("US 01 - all dates should be before current date, Running")
    lag = True
    for i in indi:
        # Checking death dates are before current dates and NA
        if str(i["DEAT"]) == "NA":
            pass
        elif i["DEAT"].date() > today:
            print("US 01 Error indi id ->" + str(i["INDI"]) + str(i["DEAT"]))
            f.write(f"Error: INDIVIDUAL: US01: Date before Current Date" + str(i["INDI"]) + " " + str(i["DEAT"]) + "\n")
            lag = False

        # Checking for Birth dates are before current Date
        if str(i["BIRT"]) == "NA":
            pass
        elif i["BIRT"].date() > today:
            print("These dates are after the current date: " + str(i["NAME"]) + str(i["BIRT"].date()))
            f.write(f"Error: INDIVIDUAL: US01: Birth date after current date" + str(i["INDI"]) + " " + str(
                i["NAME"]) + " " + str(i["BIRT"].date()) + "\n")
            lag = False

    for j in fam:

        if j["MARR"].date() > today:
            print(
                "Error: INDIVIDUAL: US01: Marriage date after current date " + str(j["MARR"].date()) + " " + str(today))
            lag = False
            f.write(f"Error: INDIVIDUAL: US01: Marriage date after current date " + str(j["MARR"].date()) + " " + str(
                today) + "\n")

        if str(j["DIV"]) == "NA":
            pass
        elif j["DIV"].date() > today:
            print("Error: INDIVIDUAL: US01: Divorce date after current date " + str(j["DIV"].date()) + " " + str(today))
            lag = False
            f.write(f"Error: INDIVIDUAL: US01: Divorce date after current date " + str(j["DIV"].date()) + " " + str(
                today) + "\n")

    if (lag):
        print("US 01 completed")
        return True
    else:
        return False


# User story 10 - Marriage should be after 14 years of age
def us10(indi, fam, f):
    print("US 10 - Marriage should be after 14 years of age, Runnning")
    flag = True
    for j in fam:
        for i in indi:
            if i["INDI"] == j["WIFE"]:
                days = 365.2425
                age = int(((j["MARR"].date()) - (i["BIRT"].date())).days / days)
                if age > 14:
                    pass
                else:
                    print("US 10 Error indi id ->" + str(i["INDI"]) + str(j["MARR"]))
                    f.write("Error: INDIVIDUAL: US10: Too young for marriage " + str(i["INDI"]) + " " + str(
                        j["MARR"]) + "\n")
                    # return False list2.append("false")
                    flag = False

            if i["INDI"] == j["HUSB"]:
                days = 365.2425
                age = int(((j["MARR"].date()) - (i["BIRT"].date())).days / days)
                if age > 14:
                    pass
                else:
                    print("US 10 Error indi id ->" + str(i["INDI"]) + str(j["MARR"]))
                    f.write("Error: INDIVIDUAL: US10: Too young for marriage " + str(i["INDI"]) + " " + str(
                        j["MARR"]) + "\n")
                    # return False

                    flag = False

        print("US 10 completed \n \n")
        print("---------------- SPRINT 1 COMPLETED -------------------\n \n")
        return flag


# User story 15 - Fewer than 15 siblings
def us15(indi, fam, f):
    print("US 15 - Fewer than 15 sublings - Running")
    flag = True
    list_of_siblings = []
    for i in fam:
        if (len(i["CHIL"]) >= 15):
            list_of_siblings.append(i["FAM"])

    if (len(list_of_siblings) == 0):
        pass
    else:
        print("Error: FAM: US15: More than 15 siblings in a family" + str(i["FAM"]))
        f.write("Error: FAM: US15: More than 15 siblings in a family" + str(i["FAM"]) + "\n")
        flag = False
    if (flag):
        print("US 15 completed")
        return True
    else:
        return False


# User Story 16


def us16(indi, fam, f):
    print("US 16 - All last names of men in family should be same - Running")
    flag = True
    for j in fam:
        names = []
        names.append(getLastNamebyId(indi, j["HUSB"]))
        if (j["CHIL"] != []):
            for h in j["CHIL"]:
                if (getSexByid(indi, h) == 'M'):
                    names.append(getLastNamebyId(indi, h))

        if (len(set(names)) != 1):
            print("Error: FAM: US 16: Single family has two or more last name" + str(j["FAM"]))
            f.write("Error: FAM: US 16: Single family has two or more last name " + str(j["FAM"]) + "\n")
            flag = False
        elif (len(set(names)) == 1):
            pass

    if (flag):
        return True
        print("US 16 completed")
    else:
        return False


# Helper functions
def getLastNamebyId(indi, Id):
    for i in indi:
        list1 = []
        if (i["INDI"] == Id):
            s = i["NAME"]
            # print(s)
            list1 = s.split()
            return list1[1]


def getSexByid(indi, Id):
    sex = ""
    for i in indi:
        if (i["INDI"] == Id):
            sex = i["SEX"]

    return sex


def getAgeById(indi, Id):
    age = 0
    for i in indi:
        if (i["INDI"] == Id):
            age = calculateage(i["BIRT"], i["DEAT"])

    return age


def getAliveById(indi, Id):
    alive = True
    for i in indi:
        if (i["DEAT"] == "NA"):
            alive = True
        else:
            alive = False

    return alive


def getNamebyId(indi, Id):
    name = " "
    for i in indi:
        if (i["INDI"] == Id):
            name = i["NAME"]

    return name


# sprint 3

def us21(indi,fam, f):
    print("US 21 - Correct gender for roles ")
    flag = True
    genderRole = []
    for j in fam:
        male = getSexByid(indi, j["HUSB"])
        female = getSexByid(indi, j["WIFE"])
        if(female != 'F'):
            genderRole.append(j["WIFE"])
            flag = False
            print("Incorrect gender role for a female in the family" + str(j["FAM"]))
            f.write("Error: INDI: US 21: Not correct gender for the role wife: " + str(j["WIFE"]) + "in family "+ str(j["FAM"]) +"\n")

        if(male != 'M'):
            genderRole.append(j["HUSB"])
            flag = False
            print("Incorrect gender role for a male in the family" + str(j["FAM"]))
            f.write("Error: INDI: US 21: Not correct gender for the role husband: " + str(j["HUSB"])+ "in family "+str(j["FAM"]) +"\n")

    if (flag):
        print("US 21: Completed")
        return True
    else:
        return False


def us22(indi, fam, f):
    print("US 22: Unique IDs Running")

    flag = True
    ids_indi = []
    ids_fam = []
    for i in indi:
        ids_indi.append(i["INDI"])

    for j in fam:
        ids_fam.append(j["FAM"])

    l = set([x for x in ids_indi if ids_indi.count(x)>1])
    fa = set([x for x in ids_indi if ids_fam.count(x)>1])
    if ((len(ids_indi) == len(set(ids_indi))) and (len(ids_fam) == len(set(ids_fam)))):
        print("US 22: completed")
        return flag
    else:
        flag = False
        if(len(l) > 0):
            print("There is a repeating id in individual" + str(l))
            f.write("Error: INDI: US 22: Duplicate ids " + str(l)+  "\n")
            return flag
        elif (len(fa)> 0 ):
            print("There is a repeating id in Fam" + str(fa))
            f.write("Error: FAM: US 22: Duplicate ids " + str(fa) + "\n")
            return flag


# US 29
def us29(indi, fam, f):
    print("US 29 - deceased List")
    flag = False
    deceasedList = []
    for i in indi:
        if (i["DEAT"] != 'NA'):
            deceasedList.append(i["INDI"])


    f.write("US 29: deceased list: "+ "\n")
    ftable = prettytable.PrettyTable()
    ftable.field_names = ["INDI ID", "Deceased Individual"]
    for i in range(len(deceasedList)):
        individual = getIndiByID(indi, deceasedList[i])
        ftable.add_row([deceasedList[i], individual["NAME"]])
    f.write(f"{str(ftable)} \n")
    print(f"{str(ftable)} \n")
    print("US 29 - completed")
    return deceasedList

# living list of singles - 31

def us31(indi, fam, f):
    single = []
    print("US 31 - Living list of singles ")
    for i in indi:
        age = calculateage(i["BIRT"], i["DEAT"])
        if (i["DEAT"] == 'NA' and i["FAMS"] == 'NA'):
            if (str(age) > '30'):
                single.append(str(i["INDI"]))


    f.write("US 31: single's list: "+"\n")
    ftable = prettytable.PrettyTable()
    ftable.field_names = ["INDI ID", "Deceased Individual"]
    for i in range(len(single)):
        individual = getIndiByID(indi, single[i])
        ftable.add_row([single[i], individual["NAME"]])
    f.write(f"{str(ftable)} \n")
    print(f"{str(ftable)} \n")
    print("US 31 completed")
    return single