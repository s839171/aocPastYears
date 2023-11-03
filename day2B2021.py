# Read in the data

myFile = open("advent2.txt")

myData = myFile.read().splitlines()

# loop through and use find command to see direction. Split string and add value to the given direction's variable or aim

h = 0
v = 0
aim = 0

for i in range(len(myData)):
  if myData[i].find("forward")!=-1:
    current = myData[i].strip("ABCDEFGHIJKLMNOPGRSTUVWXYZabcdefghijklmnopqrstuvwyz ")
    h += int(current)
    v+=int(current)*aim
  elif myData[i].find("down")!=-1:
    current = myData[i].strip("ABCDEFGHIJKLMNOPGRSTUVWXYZabcdefghijklmnopqrstuvwyz ")
    aim+= int(current)
  elif myData[i].find("up")!=-1:
    current = myData[i].strip("ABCDEFGHIJKLMNOPGRSTUVWXYZabcdefghijklmnopqrstuvwyz ")
    aim -= int(current)

print (h*v)