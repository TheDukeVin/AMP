import json
import os

uniqueGames={}
currentDir= os.getcwd()

for filename in os.listdir(currentDir):
  if filename.split(".")[1] != "py":
      f = open(os.path.join(currentDir, filename), 'r')
      game_object = json.loads(f.read())
      puzzle = game_object["puzzle"]
      puzzle.sort()
      tuplePuzzle = tuple(puzzle)
      if(tuplePuzzle not in uniqueGames):
        uniqueGames[tuplePuzzle]=game_object["solutions"]

print(len(uniqueGames))
