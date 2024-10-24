# add your code here
# Prompt the user for the starting number, ending number, and increment
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
increment = int(input("Enter the increment: "))

# Output the numbers in the specified range using the given increment
for number in range(start, end, increment):
    print(number)

