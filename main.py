def factorial(n:int) -> int:
  x = 1
  for i in range(n):
    x*=n
    n-=1
  return x

def main():
  print("Hello, world!")
  print(factorial(5))
  
  
if __name__ == "__main__":
  main()
