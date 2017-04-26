def fib(n, cache):
  if not cache:
    cache = [0, 1, 1]
    
  if n < len(cache):
    return cache[n]
  else:
    cache.append(fib(n-1, cache) + fib(n-2, cache))
    return cache[n]
    
def fib_trailing_zeros(n):
  fib_num = fib(n, [])
  return len(str(fib_num)) - len(str(fib_num).strip('0'))
  
print(fib_trailing_zeros(15))
