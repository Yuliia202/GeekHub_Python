# Write a script which accepts a <number> from user and print out a sum of
# the first <number> positive integers.

number = int(input('Please write positive integers:'))
print(sum(range(number+1)))
