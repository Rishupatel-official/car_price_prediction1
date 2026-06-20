from tkinter import *
from tkinter import ttk
import joblib

# Load model
model = joblib.load("model.pkl")

fuel_encoder = joblib.load("fuel.pkl")
door_encoder = joblib.load("door.pkl")
body_encoder = joblib.load("body.pkl")


def predict():

    fuel = fuel_encoder.transform([fuel_box.get()])[0]
    door = door_encoder.transform([door_box.get()])[0]
    body = body_encoder.transform([body_box.get()])[0]

    wheelbase = float(wheelbase_entry.get())
    horsepower = float(horsepower_entry.get())

    value = [[fuel, door, body, wheelbase, horsepower]]

    price = model.predict(value)

    result.config(text="Price = ₹ {:.0f}".format(price[0]))


root = Tk()

root.title("Car Price Predictor")
root.geometry("400x400")

Label(root, text="Car Price Prediction",
      font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Fuel Type").pack()

fuel_box = ttk.Combobox(root,
                        values=["gas", "diesel"])
fuel_box.pack()
fuel_box.current(0)

Label(root, text="Door Number").pack()

door_box = ttk.Combobox(root,
                        values=["two", "four"])
door_box.pack()
door_box.current(0)

Label(root, text="Car Body").pack()

body_box = ttk.Combobox(root,
                        values=["sedan",
                                "hatchback",
                                "wagon",
                                "convertible",
                                "hardtop"])
body_box.pack()
body_box.current(0)

Label(root, text="Wheelbase").pack()

wheelbase_entry = Entry(root)
wheelbase_entry.pack()

Label(root, text="Horsepower").pack()

horsepower_entry = Entry(root)
horsepower_entry.pack()

Button(root,
       text="Predict Price",
       command=predict).pack(pady=15)

result = Label(root,
               text="",
               font=("Arial", 14))
result.pack()

root.mainloop()