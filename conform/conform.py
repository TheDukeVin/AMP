
def please_flip_original(caps):   
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
        if t[0] == t[1]:
            shouts.append(f"Person in position {str(t[0])} flip your cap!")
        else:   
            shouts.append(f"People in positions {str(t[0])} through {str(t[1])} flip your caps!")
  return shouts

def please_flip_streamlined(caps:list)->list:
    """
    Generates a minimal list of shouts even if bareheaded individuals are in the group
    Return a list of commands
    """
    shouts = [] #list to hold the string commands that will be returned by the function
    start = 0
    forward = 0
    backward = 0
    intervals = [] #list to hold the intervals for each hat direction

    caps = caps + ["END"]

    # Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))
            start = i

    for t in intervals:
        if t[2] != caps[0]:
            if t[0] == t[1]:
                shouts.append(f"Person in position {str(t[0])} flip your cap!")
            else:
                shouts.append(f"People in positions {str(t[0])} through {str(t[1])} flip your caps!")

    return shouts

def please_flip_bare(caps:list)->list:
    shouts=[]
    Fcount = 0
    Bcount = 0
    lastCap = 'H'
    for cap in caps:
      if cap == lastCap:
        continue
      if cap == 'F':
        Fcount += 1
      if cap == 'B':
        Bcount += 1
      lastCap = cap
    caps.append('H')
    lastCap = 'H'
    if Fcount <= Bcount:
       flipType = 'F'
    else:
       flipType = 'B'
    for i, cap in enumerate(caps):
      if cap == lastCap:
          continue
      if cap == flipType:
          start = i
      if lastCap == flipType:
          if i == start+1:
              shouts.append(f"Person in position {str(start)} flip your cap!")
          else:
              shouts.append(f"People in positions {str(start)} through {str(i-1)} flip your caps!")
      lastCap = cap
    return shouts

def please_flip_one_pass(caps:list)->list:
    """
    Generates a minimal list of shouts by using exactly 1 for loop
    Return a list of strings (ie. shouts)
    """

    shouts = []
    if len(caps) == 0:
        return shouts
    lastCap = caps[0]
    for i, cap in enumerate(caps + [caps[0]]):
      if cap == lastCap:
        continue
      if cap != caps[0]:
        start = i
      else:
        end = i-1
        if start == end:
            shouts.append(f"Person in position {str(start)} flip your cap!")
        else:
            shouts.append(f"People in positions {str(start)} through {str(end)} flip your caps!")
      lastCap = cap

    return shouts

def run_length_encode(message:str) -> str:
    ''' Optional Challenge
    
        Example
        ------
        >>>run_length_encode('BFFFFFBFFFF')
        '1B5F1B4F'
    '''
    currLen = 0
    code = ""
    for i in range(len(message)):
       currLen += 1
       if i == len(message)-1 or message[i] != message[i+1]:
          code += str(currLen) + message[i]
          currLen = 0
    return code

def run_length_decode(encoded_message:str)-> str:
    ''' Optional Challenge

        Example
        ------
        >>>run_length_decode('1B5F1B4F')
        'BFFFFFBFFFF'
    '''
    currIndex = 0
    message = ""
    while currIndex < len(encoded_message):
        firstF = encoded_message.find('F', currIndex)
        if firstF == -1:
            firstF = len(encoded_message)
        firstB = encoded_message.find('B', currIndex)
        if firstB == -1:
           firstB = len(encoded_message)
        endIndex = min(firstF, firstB)
        rep = int(encoded_message[currIndex:endIndex])
        message += encoded_message[endIndex] * rep
        currIndex = endIndex + 1
    return message

def test_caps(caps):
  ans1 = please_flip_original(caps) 
  ans2 = please_flip_streamlined(caps)
  ans3 = please_flip_one_pass(caps)
  assert ans1 == ans2 and ans2 == ans3

def test_code(message):
   assert run_length_decode(run_length_encode(message)) == message

if __name__ == "__main__":
    # Some exercise 1, 2, & 4 test cases:
    caps_1 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
    caps_2 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]
    caps_3 = ["B", "B", "F", "F", "B", "F", "F", "F", "B", "B"]
    caps_4 = ["B", "B", "B", "B", "B"]

    # Some exercise 3 test cases:
    caps_5 = ["F", "F", "B", "H", "B", "F", "B", "B", "B", "F", "H", "F", "F"]
    caps_6= ["B", "B", "F", "H", "F", "B", "F", "F", "F", "B", "H", "B", "H"]

    # print(please_flip_original(caps_1))           #Ex 1
    # print(please_flip_streamlined(caps_1))       #Ex 2

    # # print(please_flip_bare(caps_5))             #Ex 3

    # print(please_flip_one_pass(caps_1))          #Ex 4

    test_caps(caps_1)
    test_caps(caps_2)
    test_caps(caps_3)
    test_caps(caps_4)

    print(run_length_encode('BFFFFFBFFFF'))
    print(run_length_decode('1B5F1B4F'))

    test_code('BFFFFFBFFFF')
    test_code('BBBBB')
    test_code('BFFBBFBBBBFFFFF')

    if True:
        caps = ["F", "B", "F", "B", "F", "B"]
        print(please_flip_one_pass(caps))