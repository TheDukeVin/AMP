def exponent(n:int, power:int)->int:
    ''' 
      Returns n**power, assuming p is a positive integer
    '''
    return 0

def sum_1_to_n(n:int)->int:
    '''
     Calculates the sum of the numbers from 1 to n (inclusive)
    '''
    return 0

def reverse_word(word:str)->str:
    '''
     Reverses the order of the letters in a word
    '''
    return word

def gcd_iterative(a:int, b:int)->int:
  '''
    1. If B is 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.
    2. Write A in quotient remainder form (A = B⋅Q + R)
    3. Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)
  '''
  while b:
    a,b = b, a%b
  return a

def gcd_recursive(a:int, b:int)->int:
    '''
      1. If B is 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.
      2. Write A in quotient remainder form (A = B⋅Q + R)
      3. Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)
    '''
    return 0

if __name__ == "__main__":   
   base = 3
   power = 5
   print(f"{base} rased to the power of {power} is {exponent(base, power)}")

   word = "New York City"
   print(f"{word} reversed is {reverse_word(word)}")

   num1 = 50
   num2 = 100
   print(f"The sum of the numbers from 1 to {num1} is {sum_1_to_n(num1)}")
   print(f"GCD of {num1} and {num2} is {gcd_recursive(num1, num2)}")
   print(f"GCD of {num1} and {num2} is {gcd_iterative(num1, num2)}")