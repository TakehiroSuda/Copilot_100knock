import csv
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

# データの読み込み
def load_data(file_path):
    features = []
    labels = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if row[0] not in ['b', 't', 'e', 'm']:
                continue
            labels.append(row[0])
            features.append(row[1])
    return features, labels

# 学習データの読み込み
train_features, train_labels = load_data('datafolder/train.txt')

# TF-IDFベクタライザの学習
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_features)

# 特徴量とラベルの保存
joblib.dump(X_train, 'features/train_features.joblib')
joblib.dump(train_labels, 'features/train_labels.joblib')
joblib.dump(vectorizer, 'features/tfidf_vectorizer.joblib')

# 学習データの読み込み
valid_features, valid_labels = load_data('datafolder/valid.txt')

# TF-IDFベクタライザの学習
X_valid = vectorizer.transform(valid_features)

# 特徴量とラベルの保存
joblib.dump(X_valid, 'features/valid_features.joblib')
joblib.dump(valid_labels, 'features/valid_labels.joblib')