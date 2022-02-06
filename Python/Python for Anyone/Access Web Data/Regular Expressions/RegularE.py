# First Activity
import re
data = open("ActualData.txt", "r")
numbers = []
totalSum = 0
for line in data:
	listNumber = re.findall('[0-9]+',line)
	numbers += listNumber
for number in numbers:
	num = int(number)
	totalSum += num
print(totalSum)