# load in data from file
myFile = open("advent1.txt")

myData = myFile.read().splitlines()

#loop through and add calories for each elf
first = 0
second = 0
third = 0
currentTotal = 0
for i in range(len(myData)):
# as long as not blank, adds to currentTotal
  if myData[i]!="":
    currentTotal += int(myData[i])
  else:
    #checks if highest and resets currentTotal
    if currentTotal > first:
      first = currentTotal
    elif currentTotal> second:
      second = currentTotal
    elif currentTotal > third:
      third = currentTotal
    currentTotal = 0

print(first + second + third)