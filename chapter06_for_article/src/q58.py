import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# データの読み込み
def load_data(file_path):
    features = []
    labels = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            label, feature = line.strip().split('\t', 1)
            labels.append(label)
            features.append(feature)
    return features, labels

# 学習データ、検証データ、評価データの読み込み
train_features, train_labels = load_data('datafolder/train.txt')
valid_features, valid_labels = load_data('datafolder/valid.txt')
eval_features, eval_labels = load_data('datafolder/test.txt')

# TF-IDFベクタライザのロード
vectorizer = joblib.load('features/tfidf_vectorizer.joblib')

# データの変換
X_train = vectorizer.transform(train_features)
X_valid = vectorizer.transform(valid_features)
X_eval = vectorizer.transform(eval_features)

# 正則化パラメータのリスト
C_values = [0.01, 0.1, 1, 10, 100,1000,10000]

# 正解率を格納するリスト
train_accuracies = []
valid_accuracies = []
eval_accuracies = []

# 異なる正則化パラメータでモデルを学習
for C in C_values:
    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, train_labels)
    
    # 学習データでの正解率
    train_predictions = model.predict(X_train)
    train_accuracy = accuracy_score(train_labels, train_predictions)
    train_accuracies.append(train_accuracy)
    
    # 検証データでの正解率
    valid_predictions = model.predict(X_valid)
    valid_accuracy = accuracy_score(valid_labels, valid_predictions)
    valid_accuracies.append(valid_accuracy)
    
    # 評価データでの正解率
    eval_predictions = model.predict(X_eval)
    eval_accuracy = accuracy_score(eval_labels, eval_predictions)
    eval_accuracies.append(eval_accuracy)

# グラフのプロット
plt.figure(figsize=(10, 6))
plt.plot(C_values, train_accuracies, label='Train Accuracy', marker='o')
plt.plot(C_values, valid_accuracies, label='Validation Accuracy', marker='o')
plt.plot(C_values, eval_accuracies, label='Evaluation Accuracy', marker='o')
plt.xscale('log')
plt.xlabel('Regularization Parameter (C)')
plt.ylabel('Accuracy')
plt.title('Effect of Regularization Parameter on Accuracy')
plt.legend()
plt.grid(True)
plt.savefig('regularization_accuracy.png')