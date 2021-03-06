# A script with functions to create and edit the FAM, INDI dictionaries
from collections import OrderedDict
import datetime


# obj variable will refer to the object being parsed at a given moment
# v variable will be a list with { level, tag, args } format


def inddetails(obj, v):
    us42 = list()
    if obj is None:
        # create a new INDI Dict, v[1] will be "INDI" in this line, v[2] will be the id
        obj = OrderedDict({
            "INDI": v[2],
            "NAME": "NA",
            "SEX": "NA",
            "BIRT": "NA",  # datetime
            "DEAT": "NA",  # datetime
            "FAMC": "NA",  # array to check possible errors
            "FAMS": "NA"  # array
        })
        return obj, us42
    # end of if
    if v[1] in ("FAMC", "FAMS"):
        if obj[v[1]] == "NA":
            obj[v[1]] = list()
        obj[v[1]].append(v[2])

    elif v[1] in ("BIRT", "DEAT"):
        if obj[v[1]] == "NA":
            obj[v[1]] = None
        else:
            print(f" {v[1]} second birth")
            obj["us32"] = True
            obj[v[1]] = None

    elif v[1] == "DATE":
        try:
            if obj["DEAT"] is None:
                # convert string to datetime
                obj["DEAT"] = datetime.datetime.strptime(v[2], "%d %b %Y")
            elif obj["BIRT"] is None:
                obj["BIRT"] = datetime.datetime.strptime(v[2], "%d %b %Y")
            else:
                print("A Date exists without proper gedcom grammar")
        except:
            date_details = v[2].split()
            new_date = f"1 {date_details[1]} {date_details[2]}"
            if obj["BIRT"] is None:
                obj["BIRT"] = datetime.datetime.strptime(new_date, "%d %b %Y")
            elif obj["DEAT"] is None:
                obj["DEAT"] = datetime.datetime.strptime(new_date, "%d %b %Y")
            us42.append(obj["INDI"])
    # other tags : INDI, NAME, SEX
    else:
        obj[v[1]] = v[2]
    # end of if

    return obj, us42


def famdetails(obj, v):
    us42 = list()
    if obj is None:
        # create a new FAM Dict, v[1] will be "FAM" in this line
        obj = OrderedDict({
            "FAM": v[2],
            "HUSB": "NA",
            "WIFE": "NA",
            "CHIL": "NA",
            "MARR": "NA",
            "DIV": "NA",
        })
        return obj, us42
    # end of if
    if v[1] == "CHIL":
        if obj["CHIL"] == "NA":
            obj["CHIL"] = list()
        obj["CHIL"].append(v[2])
    elif v[1] in ("DIV", "MARR"):
        if obj[v[1]] == "NA":
            obj[v[1]] = None
        else:
            print(f"Error: {v} second marriage in same family")
            obj[v[1]] = None
    elif v[1] == "DATE":
        try:
            if obj["DIV"] is None:
                # convert string to datetime
                obj["DIV"] = datetime.datetime.strptime(v[2], "%d %b %Y")
            elif obj["MARR"] is None:
                # convert string to datetime
                obj["MARR"] = datetime.datetime.strptime(v[2], "%d %b %Y")
            else:
                print(f"Error with date {v}")
        except:
            date_details = v[2].split()
            new_date = f"1 {date_details[1]} {date_details[2]}"
            if obj["MARR"] is None:
                obj["MARR"] = datetime.datetime.strptime(new_date, "%d %b %Y")
            elif obj["DIV"] is None:
                obj["DIV"] = datetime.datetime.strptime(new_date, "%d %b %Y")
            us42.append(obj["FAM"])
    else:
        obj[v[1]] = v[2]

    return obj, us42
