data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1 # count = count + 1
		if count % 1000 == 0: 
		# %是「取餘數」的意思，ex.1002 / 1000 餘數是2
		# 所以當餘數是0，代表你是這個分母的倍數
			print('目前母體留言數：', len(data))

sum_len = 0 # 宣告一個變數為「長度加總」

for d in data:
	# 我把data這個[list]中的所有東西，透過for loop一個一個
	# 把他「複製」進 d 這個變數
	sum_len = sum_len + len(d)
	# 所以當我從data這個[list]裡面複製一個 d出來後
	# 我把它丟到len()這個函數裡去計算他的長度
	# 再把他丟入sum_len這個公式去加總計算
	print('目前留言累積字數：', sum_len)
	print('目前每筆留言平均字數：', sum_len / len(data))