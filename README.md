## Social Media Analytics for Disaster Response: Classification and Geospatial Visualization Framework

#### [[Paper]](https://www.mdpi.com/) | [[Video]](https://)

Chao He and Da Hu

Kennesaw State University

This is the official demo code for [[Paper]](https://www.mdpi.com/)

<p align="center">
  <img src="1.png" width="80%" title="workflow">
</p>

Model training and deployment pipelines

<p align="center">
  <img src="2.png" width="80%" title="workflow">
</p>

Markers with corresponding classifications

<p align="center">
  <img src="3.png" width="80%" title="workflow">
</p>

The architecture and implementation of the proposed website server.


<p align="center">
  <img src="4.png" width="80%" title="workflow">
</p>

Social media information visualization of Hurricane Harvey on map (usernames are ex-cluded from the pop-up windows for privacy consideration).


## 1. Download dataset
**Dataset** : 
[github](https://crisisnlp.qcri.org/humaid_dataset)

## 2. Model Training

Create Python environment and install the required packages using Conda:
```bash
conda create --name ModernBert python==3.8
conda activate ModernBert

pip install -r requirements.txt

```

Our trained Model
**Our trained Model is uploaded to Huggingface** : 
[github](https://huggingface.co/)

## 3. Model Training

Run the training script:
```bash
python train.py



```

## 4. Model Deployment and Web

The project is Disaster Response System. 



You can deploy it using Nginx [Nginx](https://nginx.org/)
```bash
# Deploy a cloud server and get a public IP address:
#run nginx
# run the script for reasoning
python3 pridict.py

Open browser and visit https://your-public-ip-address
```

You can test it using python http server
```bash
# run http server
python3 -m http.server 8000

# run the script for reasoning
python3 pridict.py

Open browser and visit https://localhost:8000
```


## Acknowledgement
Great thanks to the [dataset](https://crisisnlp.qcri.org/humaid_dataset), as the dataset is used in our research.

## Cite
If this project is useful in your research, please cite:
> Chao He and Da Hu. "Social Media Analytics for Disaster Response: Classification and Geospatial Visualization Framework", in MPDI.
