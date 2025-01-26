import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import (classification_report, confusion_matrix, precision_score, recall_score)
from sklearn.model_selection import train_test_split


# Load data
df = pd.read_csv('dataFile.csv', sep=',', header=0, index_col="lineNum",dtype=int,low_memory=False)

y = df["goldThisYear"].astype(int)
X = df[[col for col in df.columns if col not in ["lineNum", "goldThisYear", "silverThisYear", "bronzeThisYear"]]].astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

print(f"Size of train dataset: {X_train.shape[0]} rows")
print(f"Size of test dataset: {X_test.shape[0]} rows")

classifier = xgb.sklearn.XGBClassifier(
    objective="reg:squarederror",
    booster="gbtree",
    early_stopping_rounds=3,
    grow_policy="depthwise",
    
)