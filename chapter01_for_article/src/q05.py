def generate_n_grams(sequence, n):
    # シーケンスの長さを取得
    length = len(sequence)
    
    # n-gramを格納するリストを初期化
    n_grams = []
    
    # シーケンスをスライドしながらn-gramを生成
    for i in range(length - n + 1):
        n_gram = sequence[i:i + n]
        n_grams.append(n_gram)
    
    return n_grams