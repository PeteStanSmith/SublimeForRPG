import datetime


class Logger():

    def __init__(self, logFileName):
        global logFile
        global logName
        logName = logFileName

        logFile = open('C:\\jhc\\src\\RPG\\CR\\' + logName + '.txt', 'a')

    def log(self, text):
        global logFile
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        printString = timestamp + ': ' + text
        logFile.write(printString + "\n")
        print(printString, end="\n")
        return

    def close(self):
        logFile.write("----------------------------------"
                     + "---------------------------------"
                     + "---------------" + "\n")
        logFile.close()

    def getIrCrNumber(self, programName):
        searchText = "User entered program: " + programName
        logFile.write(searchText)
        with open('C:\\jhc\\src\\RPG\\CR\\' + logName + '.txt', 'r') as f:
            searchLines = f.readlines()
        for i, line in enumerate(searchLines):
            if searchText in line:
                for l in searchLines[i:i+3]:
                    logFile.write(l,)


