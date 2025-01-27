import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import (classification_report, confusion_matrix, precision_score, recall_score)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('2028FullData.csv', sep=',', header=0, index_col="lineNum",dtype=int,low_memory=False);

X = df[[col for col in df.columns if col not in ["lineNum"]]].astype(int);

goldModel = xgb.XGBClassifier();
silverModel = xgb.XGBClassifier();
bronzeModel = xgb.XGBClassifier();
goldModel.load_model('XGB_Gold.json');
silverModel.load_model('XGB_Silver.json');
bronzeModel.load_model('XGB_Bronze.json');

goldPredictions = goldModel.predict(X);
silverPredictions = silverModel.predict(X);
bronzePredictions = bronzeModel.predict(X);

lineNum = 0;
with open('2028FullData.csv', 'r') as f:
    with open('2028Predictions.csv', 'w') as g:
        header = f.readline();  # Skip header line
        header = header.strip();
        header += ",goldThisYear,silverThisYear,bronzeThisYear";
        print(header, file=g);
        for line in f:
            line = line.strip();
            line += f",{goldPredictions[lineNum]},{silverPredictions[lineNum]},{bronzePredictions[lineNum]}";
            lineNum += 1;
            print(line, file=g);