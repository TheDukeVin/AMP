#Inspiration from https://www.sonofacorner.com/an-introduction-to-monte-carlo/

def throw_and_sum_n_dice(n):
    '''
    This function throws n dice and sums the results
    '''
    total = 0
    for i in range(0,n):
        throw = randint(1,6)
        total += throw
    return total

def compute_profit_path(k, n):
    '''
    This function returns the porfit (or loss) path at the end of
    k iterations of the game, and where we throw n dice.
    '''
    total_profit = 0
    for i in range(k):
        total = throw_and_sum_n_dice(n)
        if total >= 40 and total <= 50:
            total_profit += 10
        else:
            total_profit += -2
    return total_profit

def generate_profit _histogram():
        iterations = 100000
        total_profits = []
        for i in range(iterations):
            total_profits.append(compute_profit_path(50,10))

        #insert matplotlib code for histograms

if __name__ == "__main__":
    iterations = 1000000
    winning_occurances = 0
    for i in range(iterations):
        total = throw_and_sum_n_dice(10)
        if total >= 40 and total <= 50:
            winning_occurances += 1
    print(f"We would've won money {winning_occurances:,.0f} times -- a.k.a. {winning_occurances/iterations:.3%} of the time.")
    #print expected value
    #EV = 10*.2 - 2*.8 = 0.39   20%chance of winning $10, 80% of losing $2
    #EV is slightly in our favor
