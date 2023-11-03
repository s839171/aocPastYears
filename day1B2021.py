myfile = open("advent1b.txt", "r")

myData = myfile.read().splitlines()


myfile.close()
count = 0
#loop through and sum
sumList =[]
i=0
#adds the three values together and puts in list
while i+2< len(myData):
  sumList.append(int(myData[i])+int(myData[i+1])+int(myData[i+2]))
  i +=1
#checks and counts increasing
for i in  range(1,len(sumList)):
  if int(sumList[i])>int(sumList[i-1]):
    count+=1
print(count)
