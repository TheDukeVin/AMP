from TimingProfiler import TimingProfiler

def fib_iterative(n):
  #Generates the nth term of the fibonacci sequence using an iterative approach
  a, b, c = 0, 1, 0

  if n<=1: return a
  if n==2: return b

  for i in range(3, n+1):
   c = a + b
   a, b  = b, c

  return c

def fib_recursive(n):
   #Generates the nth term of the fibonacci sequence using a recursive approach
   if n <= 1: return 0
   if n==2: return 1
   return fib_recursive(n-1) + fib_recursive(n-2)

def fib_memoized(n):
   #Generates the nth term of the fibonacci sequence using a memoized recursive approach
   fib_lookup = {}

   def fib_helper(n):
    if (n in fib_lookup):
            return fib_lookup[n]
    if n <= 1:
            result = 0
    elif n==2:
            result = 1
    else:
            result = fib_helper(n-1) + fib_helper(n-2)

    fib_lookup[n] = result

    return result
   
   return fib_helper(n)

if __name__ == "__main__":

    algorithms =[fib_iterative, fib_memoized, fib_recursive]
    inputs=[5, 10, 15, 20, 25, 30, 35]
    trials = 10

    experiment = TimingProfiler(algorithms, inputs, trials)
    experiment.run_experiments()
    print(experiment.results)
    experiment.graph(title="fib Timings", scale="log")