## Social Media Analytics for Disaster Response: Classification and Geospatial Visualization Framework

#### [[Paper]](https://www.mdpi.com/2076-3417/15/8/4330) | [[Video]](https://youtu.be/gU3no4x2rHs)

[[Chao He]](https://scholar.google.com/citations?user=g4Yv3BkAAAAJ&hl=en) and [[Da Hu]](https://scholar.google.com/citations?user=Y7_j-GMAAAAJ&hl=en&oi=ao) 

Kennesaw State University

This is the official demo code for [[Paper]](https://www.mdpi.com/2076-3417/15/8/4330). 

We develop a disaster response system that can read social media data and do post classification, then visualize the info on map.

<div align="center">
  <img src="1.png" width="100%" title="workflow"><br>
  <strong>Figure 1.</strong> Model training and deployment pipelines.
</div>
<br><br>


<div align="center">
  <img src="2.png" width="100%" title="workflow"><br>
  <strong>Figure 2.</strong> Markers with corresponding classifications.
</div>
<br><br>


<div align="center">
  <img src="3.png" width="100%" title="workflow"><br>
  <strong>Figure 3.</strong> The architecture and implementation of the proposed website server.
</div>
<br><br>

<div align="center">
  <img src="4.png" width="100%" title="workflow"><br>
  <strong>Figure 4.</strong> Social media information visualization of Hurricane Harvey on map (usernames are excluded from the pop-up windows for privacy considerations).
</div>
<br><br>


## 1. Download Dataset
**Dataset** : 
[[HumAID]](https://crisisnlp.qcri.org/humaid_dataset)

Alam, F.; Qazi, U.; Imran, M. HumAID: Human-Annotated Disaster Incidents Data from Twitter with Deep Learning Benchmarks. ICWSM 2021, 15, 933–942, doi:10.1609/icwsm.v15i1.18116.

## 2. Model Training

Create Python environment and install the required packages:
```bash
conda create --name ModernBert python==3.9
conda activate ModernBert

#python == 3.9
pip install "torch==2.4.1" tensorboard
pip install flash-attn "setuptools<71.0.0" scikit-learn 
pip install  --upgrade \
   "datasets==3.1.0" \
   "accelerate==1.2.1" \
   "hf-transfer==0.1.8"
pip install "git+https://github.com/huggingface/transformers.git@6e0515e99c39444caae39472ee1b2fd76ece32f1" --upgrade
pip install nltk
pip install ipywidgets --upgrade
pip install --upgrade transformers

```

Our Trained Model
**Our trained Model is uploaded to Huggingface** : 
[[Huggingface]](https://huggingface.co/)

Run the training script in the folder train:
```bash
# download the dataset to data/
# save the best model to best_model/ 
run *.ipynb

```

## 3. Model Deployment and Visualization on Map


You can deploy it using [[Nginx]](https://nginx.org/)
```bash
# Deploy a cloud server and get a public IP address
# then install nginx
sudo apt update
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx

# Allow Nginx through firewall (if ufw is enabled)
sudo ufw allow 'Nginx Full'

# run the script for reasoning
python pridict.py

Open browser and visit https://your-public-ip-address
```

You can test it using python http server
```bash
# run http server
python -m http.server 8000

# run the script for reasoning
python pridict.py

Open browser and visit https://localhost:8000
```


## Acknowledgement
Great thanks to the [[HumAID]](https://crisisnlp.qcri.org/humaid_dataset), as the dataset is used in our research.

## Cite
If this project is useful in your research, please cite [[Paper]](https://www.mdpi.com/2076-3417/15/8/4330):
> He, C., & Hu, D. (2025). Social Media Analytics for Disaster Response: Classification and Geospatial Visualization Framework. Applied Sciences, 15(8), 4330. https://doi.org/10.3390/app15084330
