import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# 学習済みのロジスティック回帰モデルとTF-IDFベクタライザをロード
model = joblib.load('models/logistic_regression_model.joblib')
vectorizer = joblib.load('features/tfidf_vectorizer.joblib')

def preprocess_text(text):
    # 必要に応じて前処理を行う（例：小文字化、特殊文字の除去など）
    return text.lower()

def predict_category(headline):
    # 記事見出しを前処理
    processed_headline = preprocess_text(headline)
    
    # 前処理された見出しをTF-IDFベクタライザで変換
    X = vectorizer.transform([processed_headline])
    
    # モデルで予測
    probabilities = model.predict_proba(X)[0]
    predicted_category = model.classes_[np.argmax(probabilities)]
    
    return predicted_category, probabilities

# 評価データの読み込み
with open('datafolder/dummy.txt', 'r') as file:
    headlines = file.readlines()

# 各記事見出しに対してカテゴリと予測確率を計算し、結果を表示
for headline in headlines:
    category, probabilities = predict_category(headline.strip())
    print(f"見出し: {headline.strip()}\nカテゴリ: {category}, 予測確率: {probabilities}\n")