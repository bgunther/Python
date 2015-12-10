#FizzBuzz Test
#Brian Gunther
#December 10 2015

#Instructions: An example of a Fizz-Buzz question is the following:
#Write a program that prints the numbers from 1 to 100. But for multiples
#of three print "Fizz" instead of the number and for the multiples of
#five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".

count = 0

while count <= 100:
    
    if count % 3 == 0 and count % 5 == 0:
        print("FizzBuzz")
    elif count % 5 == 0:
        print("Buzz")
    elif count % 3 == 0:
        print("Fizz")
    else: print(count)
    count = count + 1

