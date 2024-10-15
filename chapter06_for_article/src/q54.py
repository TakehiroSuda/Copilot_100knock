from sklearn.metrics import accuracy_score
import joblib

# 学習済みのロジスティック回帰モデルとTF-IDFベクタライザをロード
model = joblib.load('models/logistic_regression_model.joblib')
vectorizer = joblib.load('features/tfidf_vectorizer.joblib')

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

# 学習データの読み込み
train_features, train_labels = load_data('datafolder/train.txt')
X_train = vectorizer.transform(train_features)

# 学習データでの予測
train_predictions = model.predict(X_train)

# 学習データでの正解率
train_accuracy = accuracy_score(train_labels, train_predictions)
print(f"Train Accuracy: {train_accuracy}")

# 評価データの読み込み
eval_features, eval_labels = load_data('datafolder/test.txt')
X_eval = vectorizer.transform(eval_features)

# 評価データでの予測
eval_predictions = model.predict(X_eval)

# 評価データでの正解率
eval_accuracy = accuracy_score(eval_labels, eval_predictions)
print(f"Evaluation Accuracy: {eval_accuracy}")