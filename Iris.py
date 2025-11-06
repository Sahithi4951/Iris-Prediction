import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
data = pd.read_csv(r"C:\Users\bashe\Downloads\archive (2)\Iris.csv")
X = data[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
y = data["Species"]
scaler = StandardScaler()
X[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]] = scaler.fit_transform(X[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]])
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.2,random_state = 12)
model = LogisticRegression()
model.fit(X_train,y_train)
pred = model.predict(X_test)
slen = float(input("Enter the length of Sepal(cm):"))
swidth = float(input("Enter the width of Sepal(cm):"))
plen = float(input("Enter the length of Petal(cm):"))
pwidth = float(input("Enter the width of Petal(cm):"))
X_copy = [[slen,swidth,plen,pwidth]]
X_scaled = scaler.transform(X_copy)
predicted_species = model.predict(X_scaled)
print("The predicted species is ",predicted_species)
print("Accuracy:",accuracy_score(pred,y_test))