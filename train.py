import pandas as pd
import pickle

from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("dataset/MBA.csv")
data.fillna(value={'race':  "Unknown"}, inplace=True)
data.loc[data["admission"] == "Waitlist", "admission"] = "Admit"
data["admission"] = (data["admission"] == "Admit").astype(int)

dv = DictVectorizer(sparse=True)

data_full_train, data_test = train_test_split(data, test_size=0.2)
y_train = data_full_train.admission.values
y_test = data_test.admission.values
del data_full_train["admission"]
del data_test["admission"]

full_train_dict = data_full_train.to_dict(orient='records')
X_full_train = dv.fit_transform(full_train_dict)

test_dict = data_test.to_dict(orient='records')
X_test = dv.fit_transform(test_dict)

model = RandomForestClassifier(max_depth=5, n_estimators=80, min_samples_leaf=15, max_features="sqrt", bootstrap=True)
model.fit(X_full_train, y_train)

model_file = "model.bin"
with open(model_file, 'wb') as f:
    pickle.dump(model, f)

dv_file = "dv.bin"
with open(dv_file, 'wb') as f:
    pickle.dump(dv, f)
