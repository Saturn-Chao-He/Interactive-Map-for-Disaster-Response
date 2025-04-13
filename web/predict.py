import json
import pandas as pd
import torch
import os
import time
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np

# Folder containing CSV files
folder_path = "streams"
output_json_path = "markers.json"

# Load the trained model and tokenizer
model_path = "./best_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Check if CUDA is available and move the model to GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Define label mapping (update according to your training labels)
id2label = {0: "caution_and_advice", 1: "displaced_people_and_evacuations", 2: "infrastructure_and_utility_damage",
            3: "injured_or_dead_people", 4: "missing_or_found_people", 5: "not_humanitarian", 6: "other_relevant_information",
            7: "requests_or_urgent_needs", 8: "rescue_volunteering_or_donation_effort", 9: "sympathy_and_support"}

# Function to perform inference
def classify_text(text):
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=-1).item()
    return id2label[predicted_class]

# Load existing markers.json if it exists
if os.path.exists(output_json_path):
    with open(output_json_path, "r") as json_file:
        output_data = json.load(json_file)
else:
    output_data = []

# Process CSV files every 15 seconds
csv_files = sorted(os.listdir(folder_path))  # Ensure files are processed in order
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    df = pd.read_csv(file_path)
    
    # Process each row and classify
    df["class"] = df["text"].apply(classify_text)
    
    for _, row in df.iterrows():
        output_data.append({
            "lat": row["lat"],
            "lng": row["lng"],
            "message": row["text"],
            "class": row["class"]
        })
    
    # Save updated JSON
    with open(output_json_path, "w") as json_file:
        json.dump(output_data, json_file, indent=4)
    
    print(f"Processed {csv_file} and updated {output_json_path}")
    time.sleep(15)