data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1 # count = count + 1
		if count % 1000 == 0: 
		# %是「取餘數」的意思，ex.1002 / 1000 餘數是2
		# 所以當餘數是0，代表你是這個分母的倍數
			print(len(data))
print(len(data))

print(data[0])
print('---------我是分隔線---------')
print(data[1])