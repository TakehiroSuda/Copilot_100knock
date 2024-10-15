from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# 特徴量とラベルの読み込み
X_train = joblib.load('features/train_features.joblib')
train_labels = joblib.load('features/train_labels.joblib')

# ロジスティック回帰モデルの定義と学習
model = LogisticRegression(max_iter=1000)
model.fit(X_train, train_labels)

# 検証データの読み込み
X_valid = joblib.load('features/valid_features.joblib')
valid_labels = joblib.load('features/valid_labels.joblib')

# 検証データでの予測
valid_predictions = model.predict(X_valid)

# 精度の評価
accuracy = accuracy_score(valid_labels, valid_predictions)
print(f"Validation Accuracy: {accuracy}")

# モデルの保存
joblib.dump(model, 'models/logistic_regression_model.joblib')