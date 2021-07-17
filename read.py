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

# 建立篩選清單機制
# 想要知道留言字數小於100字的留言有幾筆

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('留言小於100字的留言共有：', len(new), '筆。')
print(new[0])

good = [] #這個good清單準備裝著所有有'good'的留言

for d in data:
	if 'good' in d:
	# if d == 'good': -> 為什麼吧能這樣寫？
	# 因為這樣做的話只有當d裡面的所有字串內容就完完全全是'good'才會被列出來
	# 但如果是問個是非題「good 有沒有含在這些d裡面」
	# 這樣所有d中，有包含good的都會跑出來！
		good.append(d)
print('留言有提到東西好的(good)的比數有：', len(good), '筆。') # 這邊我容易把len(good)寫成len(d)
print(good[0])

# list comprehension
# 上面good 的例子如果看寫成一行表示，你會怎麼做？
good = [d for d in data if 'good' in d]
print(good)

# 如果是bad in d呢？
# 並且我也沒有要加任何篩選條件(if)
bad = ['bad' in d for d in data]
# 那上面這段擴寫是怎麼表達得？
# bad = []
# for d in date:
#	bad.append('bad' in d)
print(bad)

# 所以由此可知這個list comprehension的架構如下
# output = [ (nuber-1) for number in reference if number %2 == 0]
#               運算         變數        清單         篩選條件