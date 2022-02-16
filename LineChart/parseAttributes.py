import numpy as np 
import pandas as pd
from datetime import datetime

def convertCSV(CSVpre, CSVpost):
    
    data = []
    json = []
    for line in open(CSVpre):
        temp = line.strip().split("|")
        json.append(temp[-1])
        data.append(temp[:-1])

    data_npy = np.array(data)
    for i in range(len(data_npy)):
        data_npy[i,3] = datetime.utcfromtimestamp(int(data_npy[i,3])).strftime('%Y-%m-%d')


    DF = pd.DataFrame(data_npy[:,[3, 8]])
    DF.columns = ['date', 'price']
    DF['price'] = DF['price'].astype(float)
    DF = DF.groupby('date').mean()
    DF.to_csv(CSVpost)

convertCSV("CoolCats.csv", "CoolCats2.csv")
convertCSV("BoredApes.csv", "BoredApes2.csv")
