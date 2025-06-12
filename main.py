def chlen(n:int):
  lst =[['']*4 for i in range(n+1)]
  for i in range(len(lst)):
    lst[i][1] = "| "
    lst[i][2] = "| "
  lst[-1] = ["(",")","(",")",]
  for x in lst:
    print(x)

def main():
  chlen(5)
  
if __name__ == "__main__":
  main()