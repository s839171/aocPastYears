myFile = open("advent2.txt", "r")

myData = myFile.read().splitlines()
#from last challenge - MODIFY!!!!!!!!!!!!


#determines score for each round
def eachTurn(y, r):
  score = 0
  #score based on result
  if r == "X":
    score += 0
  elif r == "Y":
    score += 3
  elif r =="Z":
    score +=6
# score based on choice
  if r=="Y" and y == "A":
    score +=1
  elif r == "Y" and y == "B":
    score += 2
  elif r=="Y" and y == "C":
    score += 3
  elif r== "X" and y == "B":
    score +=1
  elif r == "Z" and y == "B":
    score += 3
  elif r == "Z" and y == "A":
    score += 2
  elif r =="X" and y == "A":
    score +=3
  elif r == "Z" and y == "C":
    score +=1
  elif r == "X" and y == "C":
    score += 2
    

  return score
s = 0
i=0

#loops through data and puts opponent and result into variables
while i< len(myData):
  you = myData[i][0]
  result = myData[i][2]
  s += eachTurn(you, result)
  i+=1
print(s)