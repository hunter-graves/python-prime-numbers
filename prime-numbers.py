posIntHowManyToDisplay = None
listOfPrimes = []
listOfPrimes.append(2)
while True:
  howManyToDisplay = input("How many consecutive prime numbers (starting with 2) should be displayed?: ")
  try:
    parseDataType = int(howManyToDisplay)
    if parseDataType >0 :
      break
    print("Please enter a positive integer.")

  except ValueError:
    print("Please enter a positive integer.")

posIntHowManyToDisplay = int(howManyToDisplay)

#what are our constraints??
#constraints mean boundaries
#prime numbers are divisible only by 1 and themselves
#1)Validate the user input

#2)We get a number that tells us how many prime numbers to generate
#3)We generate that many prime numbers
#4)We add each prime number that we generate to a list

#5)We print out that list to the user
#Let's say we give this function the number "8"
#starts at 2
#if 8 / 2 has no remainder, return False
#otherwise, add 8 to the list of primes
#and return True
#let's try 7
#we start at 7/2
# 7/2 has a remainder
#we return false
#we increment X
#we have 7/3
#7/3 has a remainder
#we return false
#we increment X
#we have 7/4
#7/4 has a remainder
#we return false
#we increment X
#we have 7 / 5
#....
  #make sure that you understand modulo
  #If 
  #10 % 2 = 0
  #then that means that
  #2 * x = 10
  #so
  #x = 10 / 2
  #x = 5
  #so 5 is a factor of 10
  #and 2 is a factor of 10
  #so 10 is not a prime number
#......

def displayPrimes(num):
  for x in range(2,num):
    if num % x == 0:
      return False
  else:
    listOfPrimes.append(num)
    return True

if posIntHowManyToDisplay == 1:
  print(listOfPrimes)
else:
  counter = 1
  num = 3
  while True:
    if counter == posIntHowManyToDisplay:
      break
    else:
      if not displayPrimes(num):
        num+=1
      else:
        num+=1
        counter+=1

  print(listOfPrimes)
