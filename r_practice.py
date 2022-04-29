# exercise 

data = []
count = 0
with open('reviews.txt', 'r', encoding = 'utf8') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('the file has been read, the overall data has', len(data), 'reviews.')

print('0' in data)

print(data[0])
print("---------------------")
print(data[1])