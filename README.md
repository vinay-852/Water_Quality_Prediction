# Water_Quality_Prediction

## Project Structure

This project is modularized into the following components:

- **data**: Contains scripts for data loading and cleaning.
  - `data_loader.py`: Functions to load and clean the dataset.

- **features**: Contains scripts for feature engineering.
  - `features.py`: Functions to select and encode features.

- **model**: Contains the model definition and utilities.
  - `model.py`: Class for training, saving, loading, and predicting with the model.

- **predict**: Contains scripts for making predictions.
  - `predict.py`: Functions to prepare input and predict pollutant levels.

- **train**: Contains the training pipeline.
  - `train.py`: Script to train the model and evaluate its performance.

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Train the model:
   ```bash
   python train/train.py
   ```

3. Make predictions:
   Use the `predict/predict.py` script to predict pollutant levels for a given station and year.