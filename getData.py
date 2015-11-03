import datetime, zipfile, os
from urllib.request import urlopen
fileString = "./votefiles/STATEWIDE "+ str(datetime.date.today())
print("Note: These are large files coming from a slow server, the download may take a while")


print("Downloading File 1")
download = "ftp://sosftp.sos.state.oh.us/free/Voter/SWVF_1_44.zip"
request = urlopen(download)
output = open("file1.zip","wb")
output.write(request.read())
output.close()

print("Downloading File 2")
download = "ftp://sosftp.sos.state.oh.us/free/Voter/SWVF_45_88.zip"
request = urlopen(download)
output = open("file1.zip","wb")
output.write(request.read())
output.close()

print("Extracting Files")
myzip = zipfile.ZipFile("file1.zip")
myzip.extractall()
myzip = zipfile.ZipFile("file2.zip")
myzip.extractall()


print("Merging files")
filenames = ['SWVF_1_44.TXT', 'SWVF_45_88.TXT']
with open(fileString, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

print("Deleting temporary files")
os.remove("file1.zip")
os.remove("file2.zip")
os.remove("SWVF_1_44.TXT")
os.remove("SWVF_45_88.TXT")


print("All done, finished file is at "+fileString)
