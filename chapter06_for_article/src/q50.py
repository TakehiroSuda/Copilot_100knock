import pandas as pd
from sklearn.model_selection import train_test_split


def extract_specific_publishers(file_path):
    # 読み込み
    df = pd.read_csv(file_path, sep='\t', header=None, names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])
    
    # 指定された情報源
    target_publishers = ["Reuters", "Huffington Post", "Businessweek", "Contactmusic.com", "Daily Mail"]
    
    # 抽出
    filtered_df = df[df['PUBLISHER'].isin(target_publishers)]
    
    return filtered_df

def shuffle_articles(df):
    # ランダムにシャッフル
    shuffled_df = df.sample(frac=1).reset_index(drop=True)
    return shuffled_df

def split_and_save_data(df):
    # データを分割
    train, temp = train_test_split(df, test_size=0.2, random_state=42)
    valid, test = train_test_split(temp, test_size=0.5, random_state=42)

    # カテゴリが b, t, e, m のいずれかでない行を除去
    valid_categories = ['b', 't', 'e', 'm']
    train = train[train['CATEGORY'].isin(valid_categories)]
    valid = valid[valid['CATEGORY'].isin(valid_categories)]
    test = test[test['CATEGORY'].isin(valid_categories)]

    # ファイルに保存
    train.to_csv('train.txt', columns=['CATEGORY', 'TITLE'], sep='\t', index=False, header=False)
    valid.to_csv('valid.txt', columns=['CATEGORY', 'TITLE'], sep='\t', index=False, header=False)
    test.to_csv('test.txt', columns=['CATEGORY', 'TITLE'], sep='\t', index=False, header=False)
    
    # 各データセットのカテゴリごとの事例数を出力
    print("Train data category counts:")
    print(train['CATEGORY'].value_counts())
    print("\nValidation data category counts:")
    print(valid['CATEGORY'].value_counts())
    print("\nTest data category counts:")
    print(test['CATEGORY'].value_counts())

# 使用例
file_path = 'news+aggregator/newsCorpora.csv'
filtered_articles = extract_specific_publishers(file_path)
shuffled_articles = shuffle_articles(filtered_articles)
split_and_save_data(shuffled_articles)

# データの読み込み
def load_data(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 2 and parts[0] in ['b', 't', 'e', 'm']:
                data.append(parts)
    return pd.DataFrame(data, columns=['CATEGORY', 'TITLE'])

# データの読み込みとクリーニング
train = load_data('train.txt')
valid = load_data('valid.txt')
test = load_data('test.txt')

# データの保存
train.to_csv('datafolder/train.txt', sep='\t', index=False, header=False)
valid.to_csv('datafolder/valid.txt', sep='\t', index=False, header=False)
test.to_csv('datafolder/test.txt', sep='\t', index=False, header=False)