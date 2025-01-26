import numpy as np
import pandas as pd
import scipy.stats as stats
import xgboost as xgb
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('dataFile.csv', sep=',', header=0, index_col="lineNum", dtype = int, low_memory = False)

le = LabelEncoder()

nthread = -1
early_stopping_rounds = 3
objective = 'binary:logistic'
booster = 'gbtree'

param_dist = {
    "objective": ["binary:logistic", "multi:softmax"],
    "max_depth": stats.randint(1, 20),
    "n_estimators": stats.randint(10, 700),
    "max_bin": stats.randint(1, 4),
    "grow_policy": ["depthwise", "lossguide"],
    "max_leaves": stats.randint(1, 20),
    "learning_rate": stats.uniform(0.01, 0.5),
    "min_child_weight": stats.uniform(0.1, 10),
    "tree_method": ["exact", "approx", "hist"],
}

y = df["goldThisYear"].astype(int)
X = df[[col for col in df.columns if col not in ["lineNum", "goldThisYear", "silverThisYear", "bronzeThisYear"]]].astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

y_train, y_test = le.fit_transform(y_train), le.fit_transform(y_test);

xgb_model = xgb.XGBClassifier(
    nthread=nthread,
    early_stopping_rounds=early_stopping_rounds,
    objective=objective,
    booster=booster,
    device="cuda",
    
)

random_search = RandomizedSearchCV(
    xgb_model,
    param_distributions=param_dist,
    n_iter=10,
    cv=5,
    scoring="accuracy",
    n_jobs=5,
)

random_search.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=True)

print("Best parameters found: ", random_search.best_params_)
print("Best score: ", random_search.best_score_)

print("Model Parameters:")
print(xgb_model.get_params())

y_pred = random_search.predict(X_test)
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
conf_matrix = confusion_matrix(y_test, y_pred, average="weighted")  
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print("Confusion Matrix:")
print(conf_matrix)