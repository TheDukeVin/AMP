"""The following puzzle is derived from Programming for the Puzzled by Srini Devadas"""

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
  if not caps: return shouts

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
        if t[0] == t[1]:
            shouts.append((f"Person in position {str(t[0])} flip your cap!"))
        else:
            shouts.append((f"People in positions {str(t[0])} through {str(t[1])} flip your caps!"))

  return shouts

def please_flip_streamlined(caps: list[str])-> list[str]: 
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
    if not caps: return shouts
    
    my_caps = caps + ["END"]
    #Step 1: Determine intervals where hats face the same direction
    for i in range(0, len(my_caps)):
        if i == len(my_caps) - 1 or my_caps[interval_start] != caps[i]:
            intervals.append((interval_start, i-1, my_caps[interval_start])) #(start, end, direction)
            
            if my_caps[interval_start] == 'F':
                forward_count += 1
            else:
                backward_count += 1

            interval_start = i   #new hat direction->new interval start 
    
    #Step 2: Decide which way to flip based on hat direction with least number of intervals
    if forward_count < backward_count:
        flip_direction = 'F'
    else:
        flip_direction = 'B'
    
    #Step 3: Flip all of the intervals that match with the flip direction
    for t in intervals:
        if t[2] == flip_direction:
            if t[0] == t[1]:
                shouts.append((f"Person in position {str(t[0])} flip your cap!"))
            else:
                shouts.append((f"People in positions {str(t[0])} through {str(t[1])} flip your caps!"))

    return shouts

def please_flip_bare(caps: list[str])-> list[str]:  
    """
    Generates a minimal list of shouts needed to have all fan caps face the same direction, skipping
    fans with no cap.

      Args:
      caps: list of strings which are either 'F' (Forward) or 'B' (Backward) or 'H' (Bareheaded)

      Return:
      a list of shouts, which could be empty if the list of caps is either empty or all the same direction
    """
    intervals = []       
    interval_start = 0 
    forward_count = backward_count = 0 
    shouts = []
    if not caps: return shouts

    my_caps = caps + ["END"]
    for i in range(1, len(my_caps)):
        if i == len(my_caps) - 1 or my_caps[interval_start] != my_caps[i]:
            
            intervals.append((interval_start, i-1, my_caps[interval_start]))

            if my_caps[interval_start] == 'F':
                forward_count += 1
            elif my_caps[interval_start] == 'B':
                backward_count += 1
           
            interval_start = i    
    
    if forward_count < backward_count:
        flip_direction = 'F'
    else:
        flip_direction = 'B'
    
    for t in intervals:
        if t[2] == flip_direction:
            if t[0] == t[1]:
                shouts.append((f"Person in position {str(t[0])} flip your cap!"))
            else:
                shouts.append((f"People in positions {str(t[0])} through {str(t[1])} flip your caps!"))

    return shouts

def please_flip_one_pass(caps: list[str])-> list[str]:  
    """
    Generates a minimal list of shouts needed to have all fan caps face the same direction using exactly 1 for loop

      Args:
      caps: list of strings which are either 'F' (Forward) or 'B' (Backward)

      Return:
      a list of shouts, which could be empty if the list of caps is either empty or all the same direction
    """
    shouts = []

    if not caps: return []

    my_caps = caps + [caps[0]]
    start = 0
    for i in range(1, len(my_caps)):
        if my_caps[i] != my_caps[i - 1]:
            if my_caps[i] != my_caps[0]:
                start = i
            else:
                if start == i - 1:
                    shouts.append(f"Person in position {i - 1} flip your cap!")
                else:
                    shouts.append(f"People in positions {start} through {i - 1} flip your caps!")
    return shouts

def run_length_encode(message:str) -> str:
    ''' Optional Challenge: Run-length Encoding
       
        Args:
        message: a single string comprised of exactly two characters:  'F'  or 'B'

        Return:
        an encoded string which uses integers to indicate sucessive repetitions of 'F' and 'B'

        Example
        ------
        >>>run_length_encode('BFFFFFBFFFF')
        '1B5F1B4F'
    '''
    encoding = ""
    if not message:
        return encoding

    message += "X"  # Sentinel value to mark last "chunk". 
    # Note this assumes there are no Xs in the original message!
    current = message[0]
    count = 1
    for i in range(1, len(message)):
        if message[i] == current:
            count += 1
        else:
            # Add chunk.
            encoding += str(count) + current
            current = message[i]
            count = 1
    return encoding

def run_length_decode(encoded_message:str)-> str:
    ''' Optional Challenge: Run-length Decoding
        
        Args:
        encoded_message: an encoded string which uses integers to indicate sucessive repetitions of 'F' and 'B'

        Return:
        a decoded string comprised of exactly two characters: 'F'  or 'B'

        Example
        ------
        >>>run_length_decode('1B5F1B4F')
        'BFFFFFBFFFF'
    '''
    decoded = ""
    if not encoded_message:
        return decoded

    for i in range(0, len(encoded_message), 2): 
        # Every other character is the actual character to add.
        count, char = encoded_message[i], encoded_message[i + 1]
        decoded += char * int(count)

    return decoded

if __name__ == "__main__":
    # Some exercise 1, 2, & 4 test cases:
    caps_1 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
    caps_2 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]
    caps_3 = ["B", "B", "F", "F", "B", "F", "F", "F", "B", "B"]
    caps_4 = ["B", "B", "B", "B", "B"]

    # Some exercise 3 test cases:
    caps_5 = ["F", "F", "B", "H", "B", "F", "B", "B", "B", "F", "H", "F", "F"]
    caps_6 = ["B", "B", "F", "H", "F", "B", "F", "F", "F", "B", "H", "B", "H"]

    #print(please_flip_original(["F", "B", "F", "B", "F", "B"]))           #Ex 1
    #print(please_flip_streamlined(["F", "B", "F", "B", "F", "B"]))       #Ex 2

    print(please_flip_bare(["F", "F", "B", "H", "B", "F", "B", "B", "B", "F", "H", "F", "F"]))             #Ex 3

    #print(please_flip_one_pass(caps_1))          #Ex 4
    

