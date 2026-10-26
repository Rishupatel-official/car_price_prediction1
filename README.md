# Car Price Prediction

A Streamlit app that predicts a car’s price in Indian rupees (₹). It uses a Random Forest regression model trained on the included `car.csv` dataset.

## Features

Enter a car’s fuel type, number of doors, body style, wheelbase, and horsepower to get a predicted price.

## Project files

- `app.py` — Streamlit prediction app
- `carpricepridictionmodel.py` — trains the model and saves it with its encoders
- `car.csv` — training data
- `model.pkl` — trained model
- `fuel.pkl`, `door.pkl`, `body.pkl` — encoders used by the app
- `requirements.txt` — Python dependencies

## Setup

Use Python 3, then install the dependencies from the project folder:

```bash
pip install -r requirements.txt streamlit
```

## Run the app

```bash
streamlit run app.py
```

Open the local URL shown in the terminal, enter the car details, and select **Predict Price**.

## Retrain the model

To train the model again using `car.csv`:

```bash
python carpricepridictionmodel.py
```

This updates `model.pkl` and the three encoder files in the current folder.

## Model details

The model uses these inputs:
- Fuel type
- Number of doors
- Car body style
- Wheelbase
- Horsepower

Text fields are converted to numeric values with scikit-learn `LabelEncoder`. The target is the `price_inr` column in `car.csv`.

## Limitations

The training script fits the model on the full dataset and does not report evaluation metrics. The prediction is an estimate based on the supplied data; it may not reflect a car’s condition, location, or current market price.
