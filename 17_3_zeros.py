def fib(n, cache):
  if not cache:
    cache = [0, 0, 1, 1]
    
  if n < len(cache):
    return cache[n]
  else:
    cache.append(fib(n-1, cache) + fib(n-2, cache))
    return cache[n]
  
print(fib(10, []))
