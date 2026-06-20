import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

# Read dataset
data = pd.read_csv("car.csv")

# Convert text data into numbers
fuel = LabelEncoder()
door = LabelEncoder()
body = LabelEncoder()

data["fueltype"] = fuel.fit_transform(data["fueltype"])
data["doornumber"] = door.fit_transform(data["doornumber"])
data["carbody"] = body.fit_transform(data["carbody"])

# Select input and output
x = data[["fueltype", "doornumber", "carbody", "wheelbase", "horsepower"]]
y = data["price_inr"]

# Create model
model = RandomForestRegressor()

# Train model
model.fit(x, y)

# Save model and encoders
joblib.dump(model, "model.pkl")
joblib.dump(fuel, "fuel.pkl")
joblib.dump(door, "door.pkl")
joblib.dump(body, "body.pkl")

print("Model trained successfully")