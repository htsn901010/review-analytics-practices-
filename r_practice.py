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

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('the average length of the review is: ', sum_len/len(data))

 







print('0' in data)

print(data[0])
print("---------------------")
print(data[1])

new = []

for d in data:
    if len(d) < 50:
    	new.append(d)
print('the length less than 50 words of the total reviews are: ', len(new))
