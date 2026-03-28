# visualize.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# اقرأ البيانات
df = pd.read_csv("data_preprocessed.csv")

# 1. Histogram لكل عمود رقمي
for col in df.select_dtypes(include='number').columns:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(f'Histogram of {col}')
    plt.savefig(f'hist_{col}.png')
    plt.close()

# 2. Pairplot
sns_plot = sns.pairplot(df)
sns_plot.savefig("pairplot.png")
plt.close()

# 3. Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.close()

print("✅ All plots saved: hist_*.png, pairplot.png, heatmap.png")