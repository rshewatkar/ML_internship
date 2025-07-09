import pandas as pd
import numpy as np  

file_path = r"D:\ML\Projects-20240722T093004Z-001\Projects\vehicle_price_prediction\Vehicle Price Prediction\dataset.csv"
vehical_data = pd.read_csv(file_path)   
vehical_data.head()  # Display the first few rows of the dataset

df = pd.DataFrame(vehical_data)

