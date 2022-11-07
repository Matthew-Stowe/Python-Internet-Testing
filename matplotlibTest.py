from matplotlib import pyplot as plt
import csv

def FormatCSV(fileName):

    xValues = []
    yValues = []
    Data = []
    
    #opens CSV file and reads all contents into Data array
    with open(fileName) as TestData:
        csv_reader = csv.reader(TestData, delimiter=",")
        for row in csv_reader:
            Data.append(row)

    #removes header        
    Data.pop(0)

    #sets data from CSV to axis
    for i in Data:
        xValues.append(i[1])
        yValues.append(i[4])

    #formats xValues to seconds from 00:00:00
    xFormat = []
    ftr = [3600,60,1]
    for i in xValues:
        xFormat.append(sum([a*b for a,b in zip(ftr, map(int,i.split(':')))]))

    #sets xValues as seconds from 00:00:00
    xValues = xFormat

    return [xValues,yValues]


def Plot(color):
    DataSet = FormatCSV("InternetTestData.csv")

    xAxisData = DataSet[0]
    yAxisData = DataSet[1]
    
    #plotting csv file data            
    plt.plot(xAxisData,yAxisData, color="navy")
    plt.title("Ping against Time Plot")
    plt.xlabel("Time from 00:00:00 (s)")
    plt.ylabel("Ping (ms)")
    plt.show()

if __name__ == "__main__":
    Plot("navy")
