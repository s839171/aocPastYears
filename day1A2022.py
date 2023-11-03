# load in data from file
myFile = open("advent1.txt")

myData = myFile.read().splitlines()

#loop through and add calories for each elf
most = 0
currentTotal = 0
for i in range(len(myData)):
# as long as not blank, adds to currentTotal
  if myData[i]!="":
    currentTotal += int(myData[i])
  else:
    #checks if highest and resets currentTotal
    if currentTotal > most:
      most = currentTotal
    currentTotal = 0

print(most)