import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import (classification_report, confusion_matrix, precision_score, recall_score)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()  # Initialize LabelEncoder object to convert categorical features to numerical values.

# Load data
df = pd.read_csv('dataFile.csv', sep=',', header=0, index_col="lineNum",dtype=int,low_memory=False)

y = df["silverThisYear"].astype(int)
X = df[[col for col in df.columns if col not in ["lineNum", "goldThisYear", "silverThisYear", "bronzeThisYear"]]].astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

y_train, y_test = le.fit_transform(y_train), le.fit_transform(y_test);

print(f"Size of train dataset: {X_train.shape[0]} rows")
print(f"Size of test dataset: {X_test.shape[0]} rows")

classifier = xgb.sklearn.XGBClassifier(
    objective="multi:softmax",
    learning_rate=.5,
    max_bin=3,
    max_depth=8,
    max_leaves=5,
    min_child_weight=2.2,
    n_estimators=455,
    tree_method="approx",
    booster="gbtree",
    early_stopping_rounds=3,
    grow_policy="lossguide",
    nthread=-1,
    device="cuda",
)

classifier.fit(X_train, y_train, eval_set=[(X_test, y_test)])
classifier.save_model("XGB_Silver.json");

y_pred = classifier.predict(X_test);

print(f"Model accuracy: {100 * classifier.score(X_test, y_test):.2f}%")
print(classification_report(y_test, y_pred))

print("Model Parameters:")
print(classifier.get_params())

y_pred = classifier.predict(X_test)
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
conf_matrix = confusion_matrix(y_test, y_pred)  
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
print("Feature Importances:")
importance = classifier.feature_importances_
for i, v in enumerate(importance):
    print(f"Feature {i+1}: {v:.4f}")