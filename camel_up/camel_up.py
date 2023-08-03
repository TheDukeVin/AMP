from itertools import permutations, product, chain
import copy

NUM_TILES = 16
ALL_COLORS = {'r', 'g', 'b', 'y', 'p'}


def visualize_board(board_state):
    print(board_state)
    visualized = ""
    for row in range(4, -1, -1):
        row_str = ""
        for i in range(len(board_state)):
            for camel_place, camel in enumerate(board_state[i]):
                if camel_place == row:
                    row_str += camel
            row_str += " "
        visualized += row_str + "\n"
    print(visualized)

def flatten(lst):
    for item in lst:
        if isinstance(item, (list, tuple)):
            for sub_item in flatten(item):
                yield sub_item
        else:
            yield item


def get_all_dice_roll_sequences(num_dice_left):  # Seq of length num_dice_left.
    all_seq = [[]]
    for _ in range(num_dice_left): 
        results = list(product(all_seq, range(1, 4))) # Each dice roll could be one of three.
        all_seq += results
    
    options = set()
    for item in all_seq:
        # Flatten tuple and then convert to list.
        potential_options = tuple(flatten(item))
        if len(potential_options) == num_dice_left:
            options.add(potential_options)
       
    assert(3 ** num_dice_left == len(options))
    return options

def get_best_move(board_state, dice_left, probabilities, bets_remaining):
    pass

def print_probabilities(first_place_wins):
    total_outcomes = sum(first_place_wins.values())
    for color in sorted(first_place_wins.keys()):
        print(f"{color}: {first_place_wins[color] / total_outcomes * 100:.0f}")
    print(f"{total_outcomes} total possibilities")

def get_next_state(board_state, dice_color, dice_number, verbose=False):  # Returns next state given move.
    if verbose: print("Current board state:", board_state)
    # Find the tile that this color camel is on.
    for i, tile in enumerate(board_state):
        if dice_color in tile:
            current_index = i
    # Figure out who is moving with the camel.
    index_of_camel_in_stack = board_state[current_index].index(dice_color)
    # Carry everyone on top of the current camel.
    camels_on_top = board_state[current_index][index_of_camel_in_stack + 1:] 
    # Move the camel forward, along with the other camels on top.
    next_index = (current_index + dice_number) % len(board_state)
    board_state[next_index] += [dice_color] + camels_on_top

    # Remove the camel and its camels-on-top from their old positions.
    board_state[current_index].remove(dice_color)
    for camel in camels_on_top:
        board_state[current_index].remove(camel)
    if verbose: print("Updated board state:", board_state)
    return board_state

def get_winner(board_state):  # Returns the string representing the camel in first place.
    for i in range(len(board_state) - 1, -1, -1):
        if board_state[i]:  # Not empty tile.
            return board_state[i][-1]  # Furthest ahead camel on this tile.
    return None

def compute_probabilities_for_leg(board_state, dice_left, verbose=False):  # Of each camel winning.
    if verbose: 
        print(f"{board_state=}")
        print(f"{dice_left=}")
    dice_left = list(dice_left)
    total_outcomes = 0
    first_place_wins = {color: 0 for color in ALL_COLORS}
    # Enumerate every possible leg.
    for possible_sequence in permutations(dice_left):  # Every possible permutations of the 5 dice.
        # Construct possibilities for the rolls.
        # TODO: Check this.
        possible_rolls = get_all_dice_roll_sequences(len(dice_left))
        for roll_sequence in possible_rolls:
            # Create new potential state (deep copy!)
            # "Roll out" (npi) this roll sequence, e.g. [1, 1, 2, 3, 3]
            potential_state = copy.deepcopy(board_state)
            for i, dice_roll in enumerate(roll_sequence):
                potential_state = get_next_state(potential_state, possible_sequence[i], dice_roll)
            if verbose: print("Final state", potential_state)
            total_outcomes += 1

            first_place_wins[get_winner(potential_state)] += 1        
    return first_place_wins

# board_state = get_next_state(board_state, 'r', 1, True)
# print(board_state)
# print(get_winner(board_state))


def tests():
    board_state = [[] for i in range(NUM_TILES)]
    board_state[0] = ['r', 'p', 'g']
    board_state[1] = ['b']
    board_state[2] = ['y']
    dice_left = {"r"}

    visualize_board(board_state)

    # print("TEST 1")
    # print(board_state)
    # result = compute_probabilities_for_leg(board_state, dice_left, verbose=False)
    # print_probabilities(result)

    # board_state = [[] for i in range(NUM_TILES)]
    # board_state[0] = ['r', 'p', 'g']
    # board_state[1] = ['b']
    # board_state[2] = ['y']
    # dice_left = {"r", 'y', 'b', 'g', 'p'}
    # print("TEST 2")
    # print(board_state)
    # result = compute_probabilities_for_leg(board_state, dice_left, verbose=False)
    # print_probabilities(result)

    # board_state = [[] for i in range(NUM_TILES)]
    # board_state[0] = ['r', 'p', 'g']
    # board_state[1] = ['b']
    # board_state[2] = ['y']
    # dice_left = {"r", 'y'}
    # print()
    # print("TEST 3")
    # print(board_state)
    # result = compute_probabilities_for_leg(board_state, dice_left, verbose=False)
    # print_probabilities(result)

tests()