import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor
from src.utils.config import DATA_PROCESSED

def train_model():
    df = pd.read_csv(f"{DATA_PROCESSED}/race_results.csv")

    X = df.drop("finish", axis=1)
    y = df["finish"]

    X_encoded = pd.get_dummies(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=0.2, shuffle=False
    )

    model = XGBRegressor()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    print("MAE:", mae)

    return model


if __name__ == "__main__":
    train_model()