FileName = input("Enter the file name to oepn: ");
try:
    FileHandler = open(FileName);
except:
    print("File cannot be opened (perhaps file does not exist?) ",FileName);
    quit();
INTcount = 0;
for EachLine in FileHandler:
    if EachLine.startswith("Lorem "):
        INTcount = INTcount + 1;
print("There were ", INTcount, " subject lines in",FileName);

