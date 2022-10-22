# Junwei Shen, 1005244326
# INF1340H F
# Maher Elshakankiri
# Master of Information
# Department of Information
# University of Toronto

# Midterm Project
# Data Analysis on the World CO2 emission over the past few decades
# Created Oct 19, 2022
# Last modified Oct 19, 2022

import csv  # import the csv data file
file = open('C:/Users/Owner/Desktop/co2_emission.csv')
csvreader = csv.reader(file)
datarow = []  # list of data in list of rows
for row in csvreader:
    datarow.append(row)
del datarow[0]  # delete the first row of column names (i.e. attribute names)


# get all data from country entered
def getdata(country):
    datalst = []
    for i in datarow:
        if i[0] == country:
            datalst.append(i)
    return datalst


# get country code from country entered
def getcode(country):
    for i in datarow:
        if i[0] == country:
            return i[1]


# get the start and end year of data collection of country entered
def getstartend(country):
    lst = getdata(country)
    start = lst[0][2]  # 1st item in lst for start year
    end = lst[-1][2]  # last item in lst for end year
    return start, end


# get co2 emission information of country entered
def getemission(country):
    emlst = []
    for i in datarow:
        if i[0] == country:
            emlst.append(i[3])  # append all emission information
    return emlst


# get co2 emission average of all the possible data from country entered
def getavg(country):
    avglst = []
    for i in datarow:
        if i[0] == country:
            avglst.append(float(i[3]))  # append all emission information
    avg = sum(avglst)/len(avglst)  # calculating the mean of CO2 emission
    return avg


# get maximum co2 emission of all the possible data from country entered
def getmax(country):
    maxlst = []
    maxyearlst = []
    for i in datarow:
        if i[0] == country:
            maxlst.append(float(i[3]))  # append all emission information
            maxyearlst.append(i[2])  # append all year information
    maxi = max(maxlst)  # calculating maximum among all emission information
    maxdict = dict(zip(maxlst, maxyearlst))  # dictionary to match emission with year
    maxyear = ""
    for key in maxdict:
        if key == maxi:
            maxyear = maxdict[key]  # map the maximum to the year with maximum value
    return maxi, maxyear  # return a tuple of float maximum and string maxyear


# get minimum co2 emission of all the possible data from country entered
def getmin(country):
    minlst = []
    minyearlst = []
    for i in datarow:
        if i[0] == country:
            minlst.append(float(i[3]))  # append all emission information
            minyearlst.append(i[2])  # append all year information
    mini = min(minlst)  # calculating minimum among all emission information
    mindict = dict(zip(minlst, minyearlst))  # dictionary to match emission with year
    minyear = ""
    for key in mindict:
        if key == mini:
            minyear = mindict[key]  # map the minimum to the year with minimum value
    return mini, minyear  # return a tuple of float minimum and string minyear


# get standard deviation of co2 emission of all the possible data from country entered
def getstd(country):
    val = 0
    for i in datarow:
        if i[0] == country:
            val += (abs(float(i[3]) - getavg(country))) ** 2  # absolute value of emission minus average emission
    var = val / len(getdata(country))  # variance calculation using formula
    std = var ** (1 / 2)  # sqrt of variance for std
    return std


# get all country names
def getcountry():
    output = []
    for i in datarow:
        if i[0] not in output and i[0] != "World":  # do not want to include world as country names
            output.append(i[0])
    return output


# get every countries' average of CO2 emission
def getallavg():
    cavg = []
    for i in getcountry():
        cavg.append(getavg(i))
    return cavg


# get a dictionary with keys as countries and values as every countries' CO2 emission
def getworlddict():
    dc = dict(zip(getcountry(), getallavg()))  # creating dictionary using two lists
    return dc


# get a report of summary of basic statistics of country entered
def report(country):
    outfile = open("C:/Users/Owner/Desktop/CO2_emission_of_"+country+".txt", "w")
    outfile.write("The average CO2 emission of " + country+" is " + str(getavg(country)) + " between " +
                  getstartend(country)[0] + " and " + getstartend(country)[1] + "." +
                  "\n" + country + " has a max value of " + str(getmax(country)[0]) + " tonnes in year " +
                  getmax(country)[1] + ", " + "it has a min value of " + str(getmin(country)[0]) +
                  " tonnes in year " + getmin(country)[1] + ". \nThe standard deviation for the CO2 emission of " +
                  country + " is " + str(getstd(country)) + ". \nAll data are collected from " +
                  getstartend(country)[0] + " to " + getstartend(country)[1]+".")


# get a full report of summary of basic statistics of every country
# may take a bit longer to run since the output file includes all countries' information and basic statistics
def reportall():
    outfile = open("C:/Users/Owner/Desktop/World_CO2_emission.txt", "w")
    for i in getcountry():
        if i != "World":
            outfile.write("The average CO2 emission of " + i + " is " + str(getavg(i)) + " between " +
                          getstartend(i)[0] + " and " + getstartend(i)[1] + "." + "\n" + i + " has a "
                          "max value of " + str(getmax(i)[0]) + " tonnes in year " + getmax(i)[1] + ", " +
                          "it has a min value of " + str(getmin(i)[0]) + " tonnes in year " + getmin(i)[1] +
                          ". \nThe standard deviation for the CO2 emission of " + i + " is " + str(getstd(i))
                          + ". \nAll data are collected from " + getstartend(i)[0] + " to " + getstartend(i)[1]
                          + ".")
    outfile.close()


# get a bar plot of CO2 emission from 1950 to 2000 of country entered
def getcountrybar(country):
    year = []
    emission = []
    for i in getdata(country):
        if 1950 <= float(i[2]) <= 2000:
            year.append(i[2])  # get all years as lists
            emission.append(i[3])  # get all emission information from 1950 to 2000
    dcc = dict(zip(year, emission))  # creating dictionary using lists
    import matplotlib.pyplot as plt
    plt.bar(list(dcc.keys()), dcc.values(), color='green')  # bar plot with year as x-axis, emission amount as y-axis
    plt.xticks(rotation=90)  # rotate x-axis for better visualization
    plt.xlabel('Year')
    plt.ylabel('CO2 emission (tonnes)')
    plt.title("The CO2 emission bar plot of "+country+"\n" +
              "from 1950 to 2000")  # adding title to the plot
    plt.show()
    plt.close()


# present the comparison of CO2 emission of two countries in the same year
# fully customizable for users
def whichbetter(country1, country2, year):
    c1emm = 0
    for i in datarow:
        if i[0] == country1 and i[2] == str(year):
            c1emm = i[3]  # 1st country emission value
    c2emm = 0
    for i in datarow:
        if i[0] == country2 and i[2] == str(year):
            c2emm = i[3]  # 2nd country emission value
    if c1emm < c2emm:
        return country1 + " is doing better with less CO2 emission in " + str(year)
    elif c1emm == c2emm:
        return "They are the in terms of CO2 emission"
    else:
        return country2 + " is doing better with less CO2 emission in " + str(year)


# present the comparison of CO2 emission of two years in the same country
# fully customizable for users
def whichyearbetter(country, year1, year2):
    y1emm = 0
    for i in datarow:
        if i[0] == country and i[2] == str(year1):
            y1emm = i[3]  # 1st year emission value
    y2emm = 0
    for i in datarow:
        if i[0] == country and i[2] == str(year2):
            y2emm = i[3]  # 2nd year emission value
    if y1emm < y2emm:
        return country + " is doing better with less CO2 emission in " + str(year1)
    elif y1emm == y2emm:
        return country + "is doing the same in terms of CO2 emission in " + str(year1) +\
               "and" + str(year2)
    else:
        return country + " is doing better with less CO2 emission in " + str(year2)


# present the average of CO2 emission from entered start and end year of entered country
# fully customizable for users
def getcustavg(country, start, end):
    custavglst = []
    for i in datarow:
        if i[0] == country and start <= float(i[2]) <= end:  # limit the year within the users' input
            custavglst.append(float(i[3]))
    custavg = sum(custavglst)/len(custavglst)
    return country + " has average CO2 emission of " + str(custavg) + " tonnes from " + str(start) \
        + " to " + str(end)


# present the maximum of CO2 emission from entered start and end year of entered country
# fully customizable for users
def getcustmax(country, start, end):
    custmaxlst = []
    custmaxyearlst = []
    for i in datarow:
        if i[0] == country and start <= float(i[2]) <= end:  # limit the year within the users' input
            custmaxlst.append(float(i[3]))
            custmaxyearlst.append(i[2])
    custmaxi = max(custmaxlst)
    custmaxdict = dict(zip(custmaxlst, custmaxyearlst))  # creating dictionary with 2 lists
    custmaxyear = ""
    for key in custmaxdict:
        if key == custmaxi:
            custmaxyear = custmaxdict[key]
    return country + " has max CO2 emission of " + str(custmaxi) + " tonnes in " + custmaxyear +\
        " from " + str(start) + " to " + str(end)


# present the minimum of CO2 emission from entered start and end year of entered country
# fully customizable for users
def getcustmin(country, start, end):
    custminlst = []
    custminyearlst = []
    for i in datarow:
        if i[0] == country and start <= float(i[2]) <= end:  # limit the year within the users' input
            custminlst.append(float(i[3]))
            custminyearlst.append(i[2])
    custmini = min(custminlst)
    custmindict = dict(zip(custminlst, custminyearlst))  # creating dictionary with 2 lists
    custminyear = ""
    for key in custmindict:
        if key == custmini:
            custminyear = custmindict[key]
    return country + " has min CO2 emission of " + str(custmini) + " tonnes in " + custminyear +\
        " from " + str(start) + " to " + str(end)


# present the standard deviation of CO2 emission from entered start and end year of entered country
# fully customizable for users
def getcuststd(country, start, end):
    custavglst1 = []
    for i in datarow:
        if i[0] == country and start <= float(i[2]) <= end:  # limit the year within the users' input
            custavglst1.append(float(i[3]))
    custavg1 = sum(custavglst1)/len(custavglst1)  # get the average for later formula usage
    custval = 0
    for i in datarow:
        if i[0] == country and start <= float(i[2]) <= end:  # limit the year within the users' input
            custval += (abs(float(i[3]) - custavg1)) ** 2
    custvar = custval / (end-start+1)  # applying varaince formula
    custstd = custvar ** (1 / 2)  # applying standard deviation formula
    return custstd


# example run
print(getdata("Canada"))
print(getcode("Canada"))
print(getstartend("Canada"))
print(getemission("Canada"))
print(getavg("Canada"))
print(getmax("Canada"))
print(getmin("Canada"))
print(getstd("Canada"))
print(getcountry())
print(getallavg())
print(getworlddict())
report("Canada")
reportall()
getcountrybar("Canada")
whichbetter("Canada", "Japan", 2000)
print(whichyearbetter("Canada", 1990, 2000))
print(getcustavg("Canada", 1990, 2000))
print(getcustmax("Canada", 1990, 2000))
print(getcustmin("Canada", 1990, 2000))
print(getcuststd("Canada", 1990, 2000))
