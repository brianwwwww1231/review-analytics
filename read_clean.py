import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1 # count = count + 1
		bar.update(count)
	bar.finish()
		# # if count % 1000 == 0: 
		# # 	print('目前母體留言數：', len(data))
# sum_len = 0 

# for d in data:
# 	sum_len = sum_len + len(d)
# 	print('目前留言累積字數：', sum_len)
# 	print('目前每筆留言平均字數：', sum_len / len(data))

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
		good.append(d)
print('留言有提到東西好的(good)的比數有：', len(good), '筆。') # 這邊我容易把len(good)寫成len(d)
print(good[0])

# 文字計數
bar_1 = progressbar.ProgressBar(max_value=1000000)
count_1 = 0
start_time = time.time()
wc = {} # word_count
for d in data: # d 是字串，data是裝了很多字串的「清單(list)」
	count_1 += 1 # count = count + 1
	bar_1.update(count_1)
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
bar_1.finish() 
end_time = time.time()
print('dict建立花了', int(end_time - start_time), '秒')
print(count_1)

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])


# for word in wc:
# 	search = input('請輸入查找字元： ')
# 	if search in wc:
# 		print(wc[search])
# 	else:
# 		print('沒有這個字喔')

while True:
	word = input('請輸入你想查的字： ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數是：', wc[word])
	else:
		print('這個字沒有出現過喔')
print('感謝使用本查詢功能')