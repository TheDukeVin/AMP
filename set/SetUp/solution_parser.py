##https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c

import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import timedelta
import json

class Game:
    def __init__(self, puzzle, solutions):
        self.puzzle = puzzle
        self.solutions = solutions

filename = str(date.today() - timedelta(days = 1))

set_solution_url = "https://www.setgame.com/set/puzzle/yesterday"
solution_html = requests.get(set_solution_url).text

#save webpage for reference
with open(filename+".html",'w') as f:
    f.write(solution_html)

soup = BeautifulSoup(solution_html, 'html.parser')

#Find puzzle images
puzzle=[]
for i in range(1, 13):
    card = soup.find_all(attrs={"name": "card"+str(i)})
    puzzle.append(card[0]['src'].split("/")[-1])

#Find solution images
solutions=[]
tables=soup.find_all(attrs={"class": "set-yesterday-table"})
for t in range(1, 7): #first table is solution
 first= tables[t].tbody.tr.td.img['src'].split("/")[-1]
 second= tables[t].tbody.tr.td.next_sibling.next_sibling.img['src'].split("/")[-1]
 third = tables[t].tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.img['src'].split("/")[-1]
 solutions.append([[first, second, third], tables[t].next_sibling.strip()])

game = Game(puzzle, solutions)
gameStr = json.dumps(game.__dict__, indent=2)

#save webpage for reference
with open(filename+".json",'w') as f:
    f.write(gameStr)
