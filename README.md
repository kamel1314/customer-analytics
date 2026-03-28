# Customer Analytics Pipeline

## How to run

### Build Docker
docker build -t analytics .

### Run Container
docker run -it --name mycontainer analytics

### Inside container
python ingest.py dataset.csv

## Flow
ingest → preprocess → analytics → visualize → cluster

## Outputs
- CSV files
- Insights (txt)
- Plots (png)

## Team
- Your Name