import random
from colorama import Fore, Back, Style, init

class CamelUpGame:
    def __init__(self):
        self.NUM_TILES = 16
        self.ALL_COLORS = {'r', 'g', 'b', 'y', 'p'}
        self.DICE_VALUES = {1,2,3}
        self.board = [[] for i in range(self.NUM_TILES)]
        self.board[0] = list(self.ALL_COLORS)
        self.colors={
        "r": Back.RED+Style.BRIGHT,
        "b": Back.BLUE+Style.BRIGHT,
        "g": Back.GREEN+Style.BRIGHT,
        "y": Back.YELLOW+Style.BRIGHT,
        "p": Back.MAGENTA
        }

        self.BETTING_TICKETS = [(2,1,-1), (3,1,-1), (5,1,-1)]
        self.betting_tickets_left = {}
        for color in self.ALL_COLORS:
            self.betting_tickets_left[color] = len(self.BETTING_TICKETS)

        self.dice_remaining = {color for color in self.ALL_COLORS}
        self.dice_rolled = []
        self.NUM_PLAYERS = 2 # TBD potentially generalize to >2 players?
        self.money = [0 for i in range(self.NUM_PLAYERS)] 
        # self.bets_placed[player_num] is a list of betting tickets
        # each betting ticket is a tuple (color, 1st place payout, 2nd place payout, other payout)
        self.bets_placed = [[] for i in range(self.NUM_PLAYERS)] 
               
    def draw_board(self):
        visualized = ""
        for row in range(4, -1, -1):
            row_str = [" "]*16
            for i in range(len(self.board)):
                for camel_place, camel in enumerate(self.board[i]):
                    if camel_place == row:
                        row_str[i]=self.colors[camel]+ camel +  Style.RESET_ALL 
            visualized += "🌴 "+str("   ".join(row_str))+" |🏁\n"
        visualized += "   "+"".join([str(i)+"   " for i in range(1, 10)])
        visualized += "".join([str(i)+"  " for i in range(10, 17)])+"\n"
        if len(self.dice_rolled) > 0:
            dice_string = "Dice Rolled: "
            for die in self.dice_rolled:
                dice_string+=self.colors[die[0]]+str(die[1])+Style.RESET_ALL+" "
            visualized += dice_string +"\n"

        for i in range(self.NUM_PLAYERS):
            visualized += f"Player {i+1} has {self.money[i]} coins."
            if len(self.bets_placed[i])>0:
                bets_string = " ".join([self.colors[bet[0]]+str(bet[1])+Style.RESET_ALL for bet in self.bets_placed[i]])
                visualized += f" Bets: {bets_string}"  
            visualized+="\n"                
        print("\n"+visualized)

    # Returns next state given move.
    # TODO check whether camel finishes a lap
    def move_camel(self, dice_color, dice_number, verbose=False):
        if verbose: print("Current board state:", self.board)
        # Find the tile that this color camel is on.
        for i, tile in enumerate(self.board):
            if dice_color in tile:
                current_index = i
        # Figure out who is moving with the camel.
        index_of_camel_in_stack = self.board[current_index].index(dice_color)
        # Carry everyone on top of the current camel.
        camels_on_top = self.board[current_index][index_of_camel_in_stack + 1:] 
        # Move the camel forward, along with the other camels on top.
        next_index = (current_index + dice_number) % len(self.board)
        self.board[next_index] += [dice_color] + camels_on_top

        # Remove the camel and its camels-on-top from their old positions.
        self.board[current_index].remove(dice_color)
        for camel in camels_on_top:
            self.board[current_index].remove(camel)
        if verbose: print("Updated board state:", self.board)
        return self.board
    
    # Roll a random die from the pyramid of reminaing dice
    # Returns color, value of dice roll
    def shake_pyramid(self)->tuple[str,int]:
        assert(len(self.dice_remaining) > 0)
        color = random.choice(tuple(self.dice_remaining))
        value = random.choice(tuple(self.DICE_VALUES))
        self.dice_remaining.remove(color)
        return color, value

    def make_move(self, player_num)->list:
        """Prompts the use to enter a valid menu choice to indicate which move they want to make.
        """
        print(f"Player {player_num+1}- (B)et: Take a betting ticket   (R)oll: Shake the pyramid to roll a die ")     
        choice = "not_an_option"
        while choice not in ["b", "r"]:
            choice = input("Which move would you like to make?\n").lower()

        match choice.lower():
            case "b":
                print("Available betting tickets:")
                for color in self.betting_tickets_left:
                    if self.betting_tickets_left[color] > 0:
                        ticket_num = self.betting_tickets_left[color]-1
                        print(f"Color: {color}. Ticket: {self.BETTING_TICKETS[ticket_num]}")
                
                ticket_color = "not_an_option"
                while ticket_color not in self.betting_tickets_left:
                    ticket_color = input("Which betting ticket would you like to take?\n").lower()

                ticket_num = self.betting_tickets_left[ticket_color]-1
                ticket = self.BETTING_TICKETS[ticket_num]
                self.bets_placed[player_num].append((ticket_color,) + ticket)

                self.betting_tickets_left[ticket_color] -= 1
                if self.betting_tickets_left[ticket_color] <= 0:
                    self.betting_tickets_left.pop(ticket_color)

            case "r":
                color, value = self.shake_pyramid()
                self.dice_rolled.append((color, value))
                self.move_camel(color, value)
                self.money[player_num] += 1

    # Returns a tuple of strings of (1st, 2nd) place camels
    def get_winner(self):
        first = False
        second = False
        for i in range(len(self.board) - 1, -1, -1):
            if self.board[i]:  # Not empty tile.
                if not first:
                    first = self.board[i][-1]  # Furthest ahead camel on this tile.
                elif not second:
                    second = self.board[i][-1]
                    return first, second
        return None

    # Main game loop
    def play(self):
        curr_player = 0
        # TODO: add code to stop game if a camel finishes a lap
        while len(self.dice_remaining) > 0:
            self.draw_board()

            self.make_move(curr_player)
            curr_player = (curr_player + 1) % self.NUM_PLAYERS
        
        # Game over, total money
        self.draw_board()
        first, second = self.get_winner()
        for player in range(self.NUM_PLAYERS):
            for bet in self.bets_placed[player]:
                if bet[0] == first:
                    self.money[player] += bet[1]
                elif bet[1] == second:
                    self.money[player] += 1
                else:
                    self.money[player] -= 1
        
        for player in range(self.NUM_PLAYERS):
            print(f"Player {player+1} ended with {self.money[player]} coins.")

if __name__ == "__main__":
    camelup = CamelUpGame()
    camelup.play()