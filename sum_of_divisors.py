def sum_divisors(n):
  sum = 0
  divs = 1
  while divs <= (n//2):
    if n % divs == 0:
      sum = sum + divs
    divs = divs + 1
  return sum
  # Return the sum of all divisors of n, not including n
  
  

  

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
