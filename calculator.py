logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""

print(logo)

def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b

operations= {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

def calculator():
  num1=float(input("What's the first number?: "))
  print("Choose any one of the following operations")
  for i in operations:
    print(i)
  cont=True

  while cont==True:
    op=input("Operation chosen is: ")
    num2=float(input("What's the next number?: "))

    calculation_function=operations[op]
    ans=calculation_function(num1,num2)
    print(f"{num1}{op}{num2}={ans}")

    x=input(f"Type y to continue calculating with {ans}, type n to start over again or type anything else to stop: ")
    if x=="y":
      num1=ans
    elif x=="n":
      cont=False
      calculator()
    else:
      break

calculator()
