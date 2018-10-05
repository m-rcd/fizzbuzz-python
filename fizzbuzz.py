def IsDivisibleByNumber(number, divisor):
    return number % divisor == 0

def FizzbuzzSays(number):
  if IsDivisibleByNumber(number, 15):
    return 'fizzbuzz'
  elif IsDivisibleByNumber(number, 3):
    return 'fizz'
  elif IsDivisibleByNumber(number, 5):
    return 'buzz'
  return number

for x in range(101):
    print(FizzbuzzSays(x))
