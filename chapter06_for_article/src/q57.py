import joblib
import numpy as np

# 学習済みのロジスティック回帰モデルとTF-IDFベクタライザをロード
model = joblib.load('models/logistic_regression_model.joblib')
vectorizer = joblib.load('features/tfidf_vectorizer.joblib')

# 特徴量の名前を取得
feature_names = vectorizer.get_feature_names_out()

# 各クラスに対する重みを取得
for i, class_label in enumerate(model.classes_):
    print(f"Class: {class_label}")
    
    # 重みの高い特徴量トップ10
    top10_indices = np.argsort(model.coef_[i])[-10:]
    top10_features = feature_names[top10_indices]
    top10_weights = model.coef_[i][top10_indices]
    print("Top 10 positive features:")
    for feature, weight in zip(top10_features, top10_weights):
        print(f"  {feature}: {weight}")
    
    # 重みの低い特徴量トップ10
    bottom10_indices = np.argsort(model.coef_[i])[:10]
    bottom10_features = feature_names[bottom10_indices]
    bottom10_weights = model.coef_[i][bottom10_indices]
    print("Top 10 negative features:")
    for feature, weight in zip(bottom10_features, bottom10_weights):
        print(f"  {feature}: {weight}")
    
    print("\n")