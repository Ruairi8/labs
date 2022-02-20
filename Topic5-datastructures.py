# A program that puts 10 random numbers into a queue (list), the program shud output all the values in 
# the queue, then take the numbers from the queue one at a time, print it & the current numbers in the queue.
# queue is [17, 72, 31, 89, 42, 19, 83, 49, 62]
# current Number is 17 and the queue now is [72, 31, 89, 42, 19, 83, 49, 62]
# current Number is 72 and the queue now is [31, 89, 42, 19, 83, 49, 62]
# current Number is 62 and the queue is []
# the queue is now empty.

from ast import If
import random
x = []
while len(x) < 10:
    x.append(random.randint(1, 100))
print("queue is ", x)
y = x.pop(0)
while len(x) != 0:
    y = x.pop(0)
    print("current number is ", y , " and the queue now is ", x)

print("the queue is now empty")

# A program that reads in a students name, modules and grades until the user enters a blank name.
student = {"name": "Mary", "modules": [{"coursename"}]}
x = input(student["modules"]["coursename"])

    