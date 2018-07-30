#Program do odczytu listy z pliku
listfile = open('list.txt','r')
try:
     list = listfile.read()
finally:
    listfile.close()

list = list.split('\n')

for indx in range(0,len(list)):
    buffer=list[indx].split()
    list[indx]=int(buffer[3])

#INPUT
