def climb_stairs_rec(self, n):
    if n<=2: return n
    return climb_stairs_rec(n-1) + climb_stairs_rec(n-2)

def climb_stairs_mem(self, n):
    memory ={
      1:1,
      2:2
    }
    def climb(n):
        if n in memory: return memory[n]
        else:
            memory[n] =  climb(n-1) + climb(n-2)
            return memory[n]

    return climb(n)

def climb_stairs_dp(n):
    if n<=2: return n;
    paths=[]
    paths[0], paths[1], paths[2] =0, 1, 2;

    for i in range(3, n+1):
      paths[i] = paths[i-1] + paths[i-2]

    return paths[n]

def climb_stairs_fib(self, n):
    prev, prev2 = 1, 0

    for i in range(1, n+1):
       curr = prev + prev2
       prev2 = prev
       prev = curr

    return prev
