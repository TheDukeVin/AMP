from TimingProfiler import TimingProfiler

def fib_iterative(n):
  #Generates the nth term of the fibonacci sequence using an iterative approach
  #Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21... 
  a, b, c = 0, 1, 0

  if n<=1: return a
  if n==2: return b

  for i in range(3, n+1):
   c = a + b
   a, b  = b, c

  return c

def fib_recursive(n):
   #Generates the nth term of the fibonacci sequence using a recursive approach
   #Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21... 
   if n <= 1: return 0
   if n==2: return 1
   return fib_recursive(n-1) + fib_recursive(n-2)

if __name__ == "__main__":
    algorithms =[fib_iterative, fib_recursive]
    inputs=[5, 10, 15, 20, 25, 30, 35]
    trials = 10
    experiment = TimingProfiler(algorithms, inputs, trials)
    experiment.run_experiments()
    print(experiment.results)
    experiment.graph(title="fib Timings", scale="linear")