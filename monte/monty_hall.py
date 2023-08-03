import random
import matplotlib.pyplot as pyplot

doors = ["goat", "goat", "car"]

def monte_hall(trials):

    switch_wins = 0
    original_guess_wins = 0

    for i in range(1, trials+1):
        original_choices = [0,1,2]

        random.shuffle(doors)

        door_selected = random.choice(original_choices) #0, 1, 2
        car_door = doors.index("car")

        if door_selected == car_door:
            original_guess_wins += 1
        else:
            switch_wins += 1

        switch_wins_prob.append(switch_wins/i)
        original_guess_wins_prob.append(original_guess_wins/i)

    print(switch_wins_prob)
    print(original_guess_wins_prob)

if __name__=="__main__":

    switch_wins_prob =[]
    original_guess_wins_prob =[]

    monte_hall(10000)
