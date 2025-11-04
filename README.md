# 🌸 Iris Flower Classification

## 📘 Overview
This project uses **Logistic Regression** to classify iris flowers into one of three species:
- *Iris-setosa*
- *Iris-versicolor*
- *Iris-virginica*

It’s one of the most famous beginner-friendly datasets in machine learning and demonstrates key concepts like **data preprocessing**, **feature scaling**, **train-test split**, and **model evaluation**.

---

## 📊 Dataset
**Source:** [Iris Dataset (Kaggle)](https://www.kaggle.com/datasets/uciml/iris)

| Feature | Description |
|----------|-------------|
| SepalLengthCm | Length of the sepal (cm) |
| SepalWidthCm | Width of the sepal (cm) |
| PetalLengthCm | Length of the petal (cm) |
| PetalWidthCm | Width of the petal (cm) |
| Species | Target variable (Setosa / Versicolor / Virginica) |

---

## ⚙️ Steps Involved

1. **Importing Libraries** – pandas, sklearn, etc.  
2. **Data Loading** – using `pd.read_csv()`  
3. **Feature Scaling** – standardizing numeric features using `StandardScaler`  
4. **Model Training** – `LogisticRegression()`  
5. **Prediction & Evaluation** – `accuracy_score()`  
6. **User Input Prediction** – takes new measurements and predicts the species  

---

## 🚀 Model Used
**Logistic Regression** – a simple yet powerful classification algorithm that works well for linearly separable data.

---

## 📈 Results
| Metric | Score |
|---------|-------|
| Accuracy | ~96% |
| Model | Logistic Regression |

---

## 💬 Example Prediction
Enter the length of Sepal(cm): 5.2
Enter the width of Sepal(cm): 3.5
Enter the length of Petal(cm): 4.2
Enter the width of Petal(cm): 2.4

The predicted species is: Iris-virginica

---

## 🧰 Libraries Used
- pandas  
- scikit-learn  
- numpy  

---

## 💡 Future Improvements
- Add visualization using **matplotlib / seaborn**
- Build an interactive **Streamlit app**
- Try other models: SVM, Decision Tree, KNN

---

## Author
**Sahithi Bashetty**  
bashettysahithi@gmail.com  
Built with Python and scikit-learn
