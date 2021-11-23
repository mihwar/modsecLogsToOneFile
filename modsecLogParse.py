import os
from datetime import date, timedelta

date = date.today() - timedelta(days=1)
yesterday = date.strftime('%Y%m%d')
#yesterday = '20211108'
#print(yesterday)
archiveFilePath = "/var/log/modsec.archive/"
archiveFileName = "modsec-" + yesterday + ".log"
archiveFile = archiveFilePath + archiveFileName

logPath = '/var/log/modsec/'
content = os.listdir(logPath)

def makeLog(modsecFile,archiveFile):
    modsec = open(modsecFile, 'r')
    archive = open(archiveFile,'a')
    logs = modsec.read()
    archive.write(logs)
    archive.close()
    modsec.close()

for dir in content:
    if os.path.isdir(os.path.join(logPath, dir)) and dir.endswith(yesterday):
        logPath1 = os.path.join(logPath, dir)
        content1 = os.listdir(logPath1)
        for dir1 in content1:
            if os.path.isdir(os.path.join(logPath1, dir1)) and dir1.startswith(yesterday):
                logPath2 = os.path.join(logPath1, dir1)
                content2 = os.listdir(logPath2)
                for file in content2:
                    logFilePath = os.path.join(logPath2, file)
                    if os.path.isfile(logFilePath):
                        makeLog(logFilePath,archiveFile)
