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

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('the total reviews incluing "good" are: ', len(good))
print(good[0])

bad = []
for d in data:
	if 'bad' in d:
		bad.append(d)
print('the reviews including bad are: ', len(bad))



wc = {}  # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # new key in dict

print(len(wc))

for word in wc:
	if wc[word] >= 10000:
		print(word, wc[word])

while True:
	word = input("enter the word you want to search: ")
	if word == 'q':
		break
	elif word in wc:
		print(word, wc[word])
	elif word not in wc:
		print("this", word, "is not in the list")
print("thank you for using this search funtion.")









