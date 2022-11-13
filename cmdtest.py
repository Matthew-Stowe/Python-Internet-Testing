import os
import time
import re
from datetime import datetime

#successfull ping:
#   Pinging google.com [142.250.187.238] with 32 bytes of data:
#   Reply from 142.250.187.238: bytes=32 time=20ms TTL=117
#   Reply from 142.250.187.238: bytes=32 time=17ms TTL=117
#   Reply from 142.250.187.238: bytes=32 time=19ms TTL=117
#   Reply from 142.250.187.238: bytes=32 time=19ms TTL=117
#
#   Ping statistics for 142.250.187.238:
#       Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
#   Approximate round trip times in milli-seconds:
#       Minimum = 17ms, Maximum = 20ms, Average = 18ms


#failed ping:
#   Ping request could not find host google.com. Please check the name and try again.

def FormatFileText(Data):
    CurrentD = datetime.now().strftime('%Y-%m-%d')
    CurrentT = datetime.now().strftime('%H:%M:%S')
    CurrentDT = CurrentD + " " + CurrentT

    #Text File Format
    TextString = f"{CurrentDT}: min = {str(Data[0])} , max = {str(Data[1])} , avr = {str(Data[2])} \n"

    #CSV File Format
    CSVString = f"{CurrentD},{CurrentT},{str(Data[0])},{str(Data[1])},{str(Data[2])},\n"

    #appends to Text File
    with open("InternetTests.txt" , "a") as TestHistory:
        TestHistory.write(TextString)

    #appends to CSV File
    with open("InternetTestData.csv" , "a") as DataFile:
        DataFile.write(CSVString)


#time: delay per check/ping
def runConnectionTest(delay):

    while True:
        #cmd /k keeps window open (remain)
        #cmd /c closees window after exec (terminate)
        
        #runs command "ping google.com" and stores output in file "tmp"
        os.system('cmd /c "ping google.com"  > tmp.txt')

        #reads tmp file contents
        #splits lines into arrays
        Output = open("tmp.txt", "r").read().splitlines()

        #last line contain ping speed timing
        LastLine = Output[-1]

        if LastLine != "Ping request could not find host google.com. Please check the name and try again.":
            #gets data into array using regular expression
            DataSet = re.findall(r'\d+', LastLine)

            FormatFileText(DataSet)

            #deletes tmp file
            os.remove("tmp.txt")

            #repeates every n seconds
            time.sleep(delay)
        else:
            FormatFileText["0","0","0"]




if __name__ == "__main__":
    runConnectionTest(5)
