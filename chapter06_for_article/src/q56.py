from sklearn.metrics import precision_score, recall_score, f1_score, classification_report
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

# 評価データの読み込み
eval_features, eval_labels = load_data('datafolder/test.txt')
X_eval = vectorizer.transform(eval_features)

# 評価データでの予測
eval_predictions = model.predict(X_eval)

# 適合率、再現率、F1スコアの計測
precision = precision_score(eval_labels, eval_predictions, average=None, labels=model.classes_)
recall = recall_score(eval_labels, eval_predictions, average=None, labels=model.classes_)
f1 = f1_score(eval_labels, eval_predictions, average=None, labels=model.classes_)

# カテゴリごとの性能を表示
for i, category in enumerate(model.classes_):
    print(f"Category: {category}")
    print(f"  Precision: {precision[i]}")
    print(f"  Recall: {recall[i]}")
    print(f"  F1 Score: {f1[i]}")

# マイクロ平均とマクロ平均の計測
micro_precision = precision_score(eval_labels, eval_predictions, average='micro')
micro_recall = recall_score(eval_labels, eval_predictions, average='micro')
micro_f1 = f1_score(eval_labels, eval_predictions, average='micro')

macro_precision = precision_score(eval_labels, eval_predictions, average='macro')
macro_recall = recall_score(eval_labels, eval_predictions, average='macro')
macro_f1 = f1_score(eval_labels, eval_predictions, average='macro')

print("\nMicro-Average Metrics")
print(f"  Precision: {micro_precision}")
print(f"  Recall: {micro_recall}")
print(f"  F1 Score: {micro_f1}")

print("\nMacro-Average Metrics")
print(f"  Precision: {macro_precision}")
print(f"  Recall: {macro_recall}")
print(f"  F1 Score: {macro_f1}")

# 詳細な分類レポートの表示
print("\nClassification Report")
print(classification_report(eval_labels, eval_predictions, target_names=model.classes_))