myfile = open("advent1a.txt", "r")

myData = myfile.read().splitlines()


myfile.close()
count = 0
#loop through and count values greater than the one before them
for i in  range(1,len(myData)):
  #checks if value is larger
  if int(myData[i])>int(myData[i-1]):
    count+=1
print(count)
