import datetime


class Logger():

    def __init__(self, logName):
        global logFile
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
