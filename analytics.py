import sys
import pandas as pd
import subprocess

def main():
    print("📊 Generating insights...")

    df = pd.read_csv(sys.argv[1])

    # ناخد الأعمدة الرقمية بس
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

    # أول عمودين numeric
    col1 = numeric_cols[0]
    col2 = numeric_cols[1]

    # Insights
    insight1 = f"Average {col1}: {df[col1].mean()}"
    insight2 = f"Average {col2}: {df[col2].mean()}"
    insight3 = f"Total rows: {df.shape[0]}, Total columns: {df.shape[1]}"

    # Save
    open("insight1.txt", "w").write(insight1)
    open("insight2.txt", "w").write(insight2)
    open("insight3.txt", "w").write(insight3)

    print("✅ Insights generated!")

    # next step
    subprocess.run(["python", "visualize.py", sys.argv[1]])

if __name__ == "__main__":
    main()