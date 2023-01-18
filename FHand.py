File = open('test.txt');
INTcount = 0;
for EachLine in File:
    INTcount = INTcount + 1;
    print(File);
print('Line Count: ',INTcount);
print("\n\n");

File2 = open('test.txt');
for EachLine in File2:
    EachLine = EachLine.rstrip(); #remove whitespaces
    if not EachLine.startswith('yo'): #if false continue
        continue;
    elif not '@dbsfisbdikb' in EachLine:
        continue;
    print(EachLine);
