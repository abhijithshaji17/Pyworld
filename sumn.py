# Sum of whole numbers upto N
def sum_upto_n(n):
  if n == 0:
    return 0    
  else: 
    return n + sum_upto_n(n - 1)
  