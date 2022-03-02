import numpy as np
from numpy import genfromtxt
import pandas as pd

transactions = pd.read_pickle("whale_df.pkl")
transactions.to_csv("csvs/whale_dataframe.csv")
transactions.sort_values("running_whale_weight", ascending = False, inplace = True)
# print(transactions)

top_transactions = transactions['fromaddress'].unique()

top_transactions = top_transactions[0:200]
# np.savetxt("csvs/top_sellers.csv",top_transactions)

buyers_from_top_seller_list = []
# for seller_id in top_transactions:
#     for row in transactions['fromaddress']:
#         if(seller_id == row):
#             buyers_from_top_seller_list.append(transactions.loc[transactions['fromaddress'] == seller_id, 'toaddress'])
#     #         buyers_from_top_seller_list.append(transactions.loc[transactions.index[row], 'toaddress')
        
# buyers = np.array(buyers_from_top_seller_list)
for seller_id in top_transactions:
    temp = transactions.loc[transactions['fromaddress'] == seller_id, 'toaddress']
    buyers_from_top_seller_list.append(temp.tolist())
    # df2 = df2.append(temp, ignore_index = True)

buyers_from_top_seller_list = [address for sublist in buyers_from_top_seller_list for address in sublist]
print(buyers_from_top_seller_list)
# print(buyers_from_top_seller_list)

# print(buyers.shape)
# print(top_transactions)
# print(buyers)
intersection = np.intersect1d(top_transactions, buyers_from_top_seller_list)
pd.DataFrame(intersection).to_csv("csvs/intersection.csv")
whale_transactions = []

for line_number, (index, row) in enumerate(transactions.iterrows()):
    if ((row.fromaddress in intersection) and (row.toaddress in intersection)):
        # print("Index is: ", index)
        # print("Row is: ",row)
        # print("Transaction is: ", transactions.iloc[[index]])
        whale_transactions.append(transactions.iloc[[line_number]])

print(whale_transactions)
whale_transactions = pd.concat(whale_transactions)
whale_transactions.to_csv("csvs/whale.csv")

f = open("whale_transactions_node_graph.json", 'w')
f.write("[\n")
counter = 0
counter2 = 0
for sellers_id in intersection:
    f.write('{"name":"transactions.' + sellers_id + '","size":1,"imports":[')
    begin = True
    for index, row in whale_transactions.iterrows():
        counter2 += 1
        # print(row.fromaddress)
        # print(seller_id)
        if(row.fromaddress == sellers_id):
            if(begin):
                f.write('"transactions.' + row.toaddress + '"')
                counter = counter + 1
                begin = False
            else:
                f.write(',"transactions.' + row.toaddress + '"')
                counter = counter + 1
    f.write(']},\n')
f.write("]")
print("counter is", counter)
print("counter2 is", counter2)




# for seller_id in intersection:
#     temp = transactions.loc[transactions['fromaddress'] == seller_id, 'toaddress']
#     # give list of buyers in intersection who have bought from seller_id
#     for toaddress in temp:
#         if toaddress in intersection:
#             whale_transaction_list.append()


#     for buyer in seller_buyer_intersect:

#     for buyer_from_ts in temp:
#         temp2 = transactions.loc[temp['fromaddress'] == seller_id, 'toaddress']

# for address in buyers_from_top_seller_list:
#     for row 
