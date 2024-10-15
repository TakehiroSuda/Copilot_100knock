def extract_characters(sentence, indices):
	# 文章を単語に分割
	words = sentence.split()
	
	# 結果を格納する辞書
	result = {}
	
	# 各単語を処理
	for i, word in enumerate(words):
		if i in indices:
			# インデックスが含まれる場合、先頭の1文字を抽出
			result[i] = word[:1]
		else:
			# インデックスが含まれない場合、先頭の2文字を抽出
			result[i] = word[:2]
	
	return result

def main():
	sentence = "This is a sample sentence."
	indices = [1, 3, 5]
	result = extract_characters(sentence, indices)
	print(result)

if __name__ == "__main__":
	main()