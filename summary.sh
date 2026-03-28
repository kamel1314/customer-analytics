#!/bin/bash
# summary.sh
# هدفه: نسخ النتائج من container → results/ على host + حذف container

# مجلد النتائج على host
RESULTS_DIR="results"
mkdir -p $RESULTS_DIR

# اسم container اللي انت هتشغله
CONTAINER_NAME="mycontainer"

echo "🧠 Copying results from container to $RESULTS_DIR..."

# انسخ ملفات CSV
docker cp $CONTAINER_NAME:/app/pipeline/data_preprocessed.csv $RESULTS_DIR/
# انسخ كل insights
docker cp $CONTAINER_NAME:/app/pipeline/insight1.txt $RESULTS_DIR/
docker cp $CONTAINER_NAME:/app/pipeline/insight2.txt $RESULTS_DIR/
docker cp $CONTAINER_NAME:/app/pipeline/insight3.txt $RESULTS_DIR/
# انسخ cluster info
docker cp $CONTAINER_NAME:/app/pipeline/clusters.txt $RESULTS_DIR/
# انسخ الصور
docker cp $CONTAINER_NAME:/app/pipeline/summary_plot.png $RESULTS_DIR/
docker cp $CONTAINER_NAME:/app/pipeline/pairplot.png $RESULTS_DIR/
docker cp $CONTAINER_NAME:/app/pipeline/heatmap.png $RESULTS_DIR/
docker cp $CONTAINER_NAME:/app/pipeline/hist_*.png $RESULTS_DIR/

echo "✅ All files copied to $RESULTS_DIR"

# وقف وحذف container
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
echo "🛑 Container $CONTAINER_NAME stopped and removed"