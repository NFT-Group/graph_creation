import numpy as np 
import pandas as pd
import json
from datetime import datetime


def startDate(CSV):
    i = 0
    for line in open(CSV):
        temp = line.strip().split("|")
        i+=1
        if (i == 2):
            break
    temp = line.strip().split(",")
    return temp[0]

def endDate(CSV):
    for line in open(CSV):
        temp = line.strip().split("|")
    temp = line.strip().split(",")
    return temp[0]

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

def findFirstLastDates(CSV1, CSV2):
    startDate1 = startDate(CSV1).strip().split("-")
    startDate2 = startDate(CSV2).strip().split("-")
    endDate1 = endDate(CSV1).strip().split("-")
    endDate2 = endDate(CSV2).strip().split("-")
    
    startDate1 = [int(i) for i in startDate1]
    startDate2 = [int(i) for i in startDate2]
    endDate1 = [int(i) for i in endDate1]
    endDate2 = [int(i) for i in endDate2]
    
    if startDate1 > startDate2:
        startDateFirst = startDate2
    else:
        startDateFirst = startDate1

    if endDate1 < endDate2:
        endDateFinal = endDate2
    else:
        endDateFinal = endDate1

    return startDateFirst, endDateFinal

def mergeCSV(CSV1, CSV2, MergedCSV):
    data1 = pd.read_csv(CSV1)
    data2 = pd.read_csv(CSV2)
    output1 = pd.merge(data1, data2, on='date', how='inner')
    output1.to_csv(MergedCSV, index = False)

def addDollarPrice(CSV, DollarCSV):
    mergeCSV(CSV, DollarCSV, 'temp.csv')
    temp = pd.read_csv('temp.csv')
    output1 = pd.read_csv(CSV)
    output1['dollar_price'] = temp['Close']
    output1.to_csv(CSV, index = False)

def attachDollarPrice(MergedCSV):
    output1 = pd.read_csv(MergedCSV)
    output1.columns = ['date', 'bored_apes_1', 'cool_cats_1', 'dollar_price']
    output1['bored_apes_2'] = output1['dollar_price'] * output1['bored_apes_1']
    output1['cool_cats_2'] = output1['dollar_price'] * output1['cool_cats_1']
    output1.to_csv(MergedCSV, index = False)

def csvToJSON(CSV):
    df = pd.read_csv(CSV)
    result = df.to_json(orient='records')
    json.dump(result, 'Merged.json')


convertCSV("CoolCats.csv", "CoolCats2.csv")
convertCSV("BoredApes.csv", "BoredApes2.csv")

outputFile = "MergedCSV.csv"
dollarFile = "ETH-USD copy.csv"

mergeCSV("CoolCats2.csv", "BoredApes2.csv", outputFile)
addDollarPrice(outputFile, dollarFile)
attachDollarPrice(outputFile)

csvToJSON(outputFile)



