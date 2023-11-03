myFile = open("advent2a.txt", "r")

myData = myFile.read().splitlines()
#determines score for each round
def eachTurn(y, m):
  score = 0
  #determines win, lose, or tie
  if m == "X" and y == "A":
    score +=3
  elif m == "Y" and y == "B":
    score += 3
  elif m == "Z" and y == "C":
    score += 3
  elif m == "X" and y == "B":
    score +=0
  elif m == "Z" and y == "B":
    score += 6
  elif m == "Y" and y == "A":
    score += 6
  elif m == "Z" and y == "A":
    score +=0
  elif m == "X" and y == "C":
    score +=6
  elif m == "Y" and y == "C":
    score += 0
    
  #determines points based on what you chose
  if m == "X":
    score += 1
  elif m == "Y":
    score += 2
  elif m == "Z":
    score +=3
  return score
s = 0
i=0
#loops through data and puts opponent and your play into variables
while i< len(myData):
  you = myData[i][0]
  me = myData[i][2]
  s += eachTurn(you, me)
  i+=1
print(s)