# code to check if the number is prime or not

num = 26



# define a flag 
flag = False

# prime numbers are always greater than 1
if num > 1:
    # check for the factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")