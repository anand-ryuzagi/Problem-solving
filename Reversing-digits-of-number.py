#Reversing the digitd of number

num = int(input("Enter number to reverse: "))
rev = 0

while num > 0:
    reminder = num % 10
    rev = rev*10 + reminder
    num = num//10

print(rev)
