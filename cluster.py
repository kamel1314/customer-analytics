import sys
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv(sys.argv[1])

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(df)

counts = df['cluster'].value_counts()

with open("clusters.txt", "w") as f:
    f.write(str(counts))

print("Clustering done!")