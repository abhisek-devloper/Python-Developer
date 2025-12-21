from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle

# Sample training data
data = pd.DataFrame({
    'age': [25, 30, 45, 22, 40],
    'experience': [1, 5, 10, 0, 8],
    'income_above_50k': [0, 0, 1, 0, 1]
})

X = data[['age', 'experience']]
y = data['income_above_50k']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))
