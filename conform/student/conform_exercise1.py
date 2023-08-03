# Starter code for You Will All Conform, Exercise 1 only.

def please_flip_original(caps: list[str])-> list[str]:   
  """
    Generates a minimal list of shouts needed to have all fan caps face the same direction.

    Args:
      caps: list of strings which are either 'F' (Forward) or 'B' (Backward)

    Return:
      a list of shouts, which could be empty if the list of caps is either empty or all the same direction
  """
  intervals = []       
  interval_start = 0 
  forward_count = backward_count = 0 
  shouts = []

  #Step 1: Determine intervals where hats face the same direction
  for i in range(1, len(caps)):
    if caps[interval_start] != caps[i]:
      intervals.append((interval_start, i - 1, caps[interval_start])) #(start, end, direction)
       	 
      if caps[interval_start] == 'F':
        forward_count += 1
      else:
        backward_count += 1
      interval_start = i   #new hat direction->new interval start 

  intervals.append((interval_start, len(caps)-1, caps[interval_start]))
  if caps[interval_start] == 'F':
    forward_count += 1
  else:
    backward_count += 1
  
  #Step 2: Decide which way to flip based on hat direction with least number of intervals
  if forward_count < backward_count:
    flip_direction = 'F'
  else:
    flip_direction = 'B'
  
  #Step 3: Flip all of the intervals that match with the flip direction
  for t in intervals:
    if t[2] == flip_direction:
        shouts.append(f"People in positions {str(t[0])} through {str(t[1])} flip your caps!")

  return shouts


if __name__ == "__main__":
    # Some exercise 1, 2, & 4 test cases:
    caps_1 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
    caps_2 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]
    caps_3 = ["B", "B", "F", "F", "B", "F", "F", "F", "B", "B"]
    caps_4 = ["B", "B", "B", "B", "B"]

    # Some exercise 3 test cases:
    caps_5 = ["F", "F", "B", "H", "B", "F", "B", "B", "B", "F", "H", "F", "F"]
    caps_6= ["B", "B", "F", "H", "F", "B", "F", "F", "F", "B", "H", "B", "H"]

    print(please_flip_original(caps_1))           #Ex 1