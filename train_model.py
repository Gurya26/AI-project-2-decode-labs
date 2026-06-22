# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Load Iris Dataset
iris = load_iris()

X = iris.data
y = iris.target

# Step 2: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Step 3: Create the Machine Learning model
model = KNeighborsClassifier(n_neighbors=3)

# Step 4: Train the model
model.fit(X_train, y_train)

# Step 5: Test the model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("=" * 40)
print("AI MODEL TRAINED SUCCESSFULLY")
print("=" * 40)
print(f"Accuracy : {accuracy * 100:.2f}%")

# Step 6: Save the model
joblib.dump(model, "iris_model.pkl")

print("\nModel saved as iris_model.pkl")