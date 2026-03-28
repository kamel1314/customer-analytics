import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def main():
    print("🔥 Start preprocessing")

    file_path = sys.argv[1]
    df = pd.read_csv(file_path)

    # =========================
    # 1. Data Cleaning
    # =========================
    print("Cleaning data...")
    df = df.drop_duplicates()

    # fill numeric missing values
    df = df.fillna(df.mean(numeric_only=True))

    # =========================
    # 2. Encoding
    # =========================
    print("Encoding categorical features...")
    df = pd.get_dummies(df, drop_first=True)

    # =========================
    # 3. Scaling
    # =========================
    print("Scaling data...")
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    # =========================
    # 4. Feature Reduction
    # =========================
    print("Reducing features...")
    df_scaled = df_scaled.iloc[:, :10]  # أول 10 أعمدة

    # =========================
    # 5. Discretization
    # =========================
    print("Discretizing...")
    df_scaled['binned'] = pd.qcut(df_scaled.iloc[:, 0], 4, labels=False)

    # save output
    df_scaled.to_csv("data_preprocessed.csv", index=False)

    print("✅ Preprocessing done")

    # call next step
    os.system("python analytics.py data_preprocessed.csv")

if __name__ == "__main__":
    main()