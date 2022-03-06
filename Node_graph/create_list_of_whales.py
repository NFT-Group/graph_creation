import numpy as np
from numpy import genfromtxt
import pandas as pd

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from trait_distribution import trait_distribution 
import json
import pathlib
from collection_class_lite import Collection_lite


def get_firebase_data_return_pkl_file(pkl_file_name, address, full_database_key, all_transactions_key):

    # CREATE LINK FOR 'FULL DATABASE'

    cred_push_key = str(pathlib.Path(__file__).parent.resolve()) + full_database_key
    cred_push = firebase_admin.credentials.Certificate(cred_push_key)
    default_app = firebase_admin.initialize_app(cred_push, {
        'databaseURL':'https://full-database-9c028-default-rtdb.europe-west1.firebasedatabase.app/'
        })

    # CREATE LINK FOR 'ALL TOKENS' DATABASE

    # cred_pull_tokens_key = str(pathlib.Path(__file__).parent.resolve()) + all_tokens_key
    # cred_pull_tokens = firebase_admin.credentials.Certificate(cred_pull_tokens_key)
    # tokens_app = firebase_admin.initialize_app(cred_pull_tokens, {
    #     'databaseURL':'https://alltokens-8ff48-default-rtdb.europe-west1.firebasedatabase.app/'
    #     }, name = 'tokens_app')

    # CREATE LINK FOR 'ALL TRANSACTIONS' DATABASE

    cred_pull_transactions_key = str(pathlib.Path(__file__).parent.resolve()) + all_transactions_key
    cred_pull_transactions = firebase_admin.credentials.Certificate(cred_pull_transactions_key)
    transactions_app = firebase_admin.initialize_app(cred_pull_transactions, {
        'databaseURL':'https://allcollections-6e66c-default-rtdb.europe-west1.firebasedatabase.app/'
        }, name='transactions_app')


    # JUST ONE BORED APES EXAMPLE FOR NOW BUT CAN MAKE THIS SECTION TRAVERSABLE LATER

    # ref = db.reference('/', app=tokens_app)
    # collection_data = ref.order_by_key().start_at(start_at_name).end_at(end_at_name).get()
    ref = db.reference('/', app=transactions_app)
    transactions = ref.order_by_child('contracthash').equal_to(address).get()
    # print(transactions)
    collection = Collection_lite(transactions)
    collection.prep_data()
    print(collection)
    collection.transactions_df.to_pickle(pkl_file_name)


def create_node_graph_data(pkl_file_name, jsn_output_name):
    transactions = pd.read_pickle(pkl_file_name)
    transactions.sort_values("running_whale_weight", ascending = False, inplace = True)

    top_transactions = transactions['fromaddress'].unique()

    top_transactions = top_transactions[0:200]

    buyers_from_top_seller_list = []


    for seller_id in top_transactions:
        temp = transactions.loc[transactions['fromaddress'] == seller_id, 'toaddress']
        buyers_from_top_seller_list.append(temp.tolist())


    buyers_from_top_seller_list = [address for sublist in buyers_from_top_seller_list for address in sublist]
    df = pd.DataFrame(buyers_from_top_seller_list)

    df.to_csv('shows.csv')    
    intersection = np.intersect1d(top_transactions, buyers_from_top_seller_list)
    # collection_data = ref.order_b
    whale_transactions = []

    for line_number, (index, row) in enumerate(transactions.iterrows()):
        if ((row.fromaddress in intersection) and (row.toaddress in intersection)):
            whale_transactions.append(transactions.iloc[[line_number]])

    whale_transactions = pd.concat(whale_transactions)
    f = open(jsn_output_name, 'w')
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


apeAddress = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'
# cryptoPunkMDAddress = '0x16F5A35647D6F03D5D3da7b35409D65ba03aF3B2'
doodlesAddress = '0x8a90CAb2b38dba80c64b7734e58Ee1dB38B8992e'
coolCatsAddress = '0x1a92f7381b9f03921564a437210bb9396471050c'
cryptoPunkAddress = '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'

cryptoKittiesAddress = '0x06012c8cf97bead5deae237070f9587f8e7a266d'
cloneXAddress = '0x49cF6f5d44E70224e2E23fDcdd2C053F30aDA28B'
crypToadzAddress = '0x1CB1A5e65610AEFF2551A50f76a87a7d3fB649C6'
boredApeKennelAddress = '0xba30E5F9Bb24caa003E9f2f0497Ad287FDF95623'
pudgyPenguinAddress = '0xBd3531dA5CF5857e7CfAA92426877b022e612cf8'

collection_addresses_dict = {'apeAddress': apeAddress, "doodlesAddress": doodlesAddress,
        "coolCatsAddress": coolCatsAddress,
        "cloneXAddress": cloneXAddress, "crypToadzAddress": crypToadzAddress,
        "boredApeKennelAddress": boredApeKennelAddress, "pudgyPenguinAddress": pudgyPenguinAddress}

# #BORED APE DATA

# pkl_file_name = "bored_ape.pkl"
# jsn_output_name = "whale_transactions_bored_ape_node_graph.json"
# address = apeAddress
# full_database_key = '/database_store_keys/key_for_full_database_store.json'
# all_tokens_key = '/database_store_keys/key_for_all_tokens_store.json'
# all_transactions_key = '/database_store_keys/key_for_all_transactions_store.json'

# get_firebase_data_return_pkl_file(pkl_file_name, address, full_database_key, all_transactions_key)
# create_node_graph_data(pkl_file_name, jsn_output_name)


# #COOLCATS DATA

# pkl_file_name = "cool_cats.pkl"
# jsn_output_name = "whale_transactions_cool_cats_node_graph.json"
# address = coolCatsAddress
# full_database_key = '/database_store_keys/key_for_full_database_store.json'
# all_transactions_key = '/database_store_keys/key_for_all_transactions_store.json'

# get_firebase_data_return_pkl_file(pkl_file_name, address, full_database_key, all_transactions_key)
# create_node_graph_data(pkl_file_name, jsn_output_name)

# #Doodles

# pkl_file_name = "doodles.pkl"
# jsn_output_name = "whale_transactions_doodles_node_graph.json"
# address = doodlesAddress
# full_database_key = '/database_store_keys/key_for_full_database_store.json'
# all_tokens_key = '/database_store_keys/key_for_all_tokens_store.json'
# all_transactions_key = '/database_store_keys/key_for_all_transactions_store.json'

# get_firebase_data_return_pkl_file(pkl_file_name, address, full_database_key, all_transactions_key)
# create_node_graph_data(pkl_file_name, jsn_output_name)

#Cryptopunks DATA

pkl_file_name = "crypto_punks.pkl"
jsn_output_name = "whale_transactions_crypto_punks_node_graph.json"
address = cryptoPunkAddress
full_database_key = '/database_store_keys/key_for_full_database_store.json'
all_tokens_key = '/database_store_keys/key_for_all_tokens_store.json'
all_transactions_key = '/database_store_keys/key_for_all_transactions_store.json'

get_firebase_data_return_pkl_file(pkl_file_name, address, full_database_key, all_transactions_key)
create_node_graph_data(pkl_file_name, jsn_output_name)

#cloneXAddress DATA

pkl_file_name = "cloneXAddress.pkl"
jsn_output_name = "whale_transactions_cloneXAddress_node_graph.json"
address = cloneXAddress
full_database_key = '/database_store_keys/key_for_full_database_store.json'
all_transactions_key = '/database_store_keys/key_for_all_transactions_store.json'

get_firebase_data_return_pkl_file(pkl_file_name, address, full_database_key, all_transactions_key)
create_node_graph_data(pkl_file_name, jsn_output_name)

#Cryptokitties

pkl_file_name = "cryptokitties.pkl"
jsn_output_name = "whale_transactions_cryptokitties_node_graph.json"
address = cryptoKittiesAddress
full_database_key = '/database_store_keys/key_for_full_database_store.json'
all_tokens_key = '/database_store_keys/key_for_all_tokens_store.json'
all_transactions_key = '/database_store_keys/key_for_all_transactions_store.json'

get_firebase_data_return_pkl_file(pkl_file_name, address, full_database_key, all_transactions_key)
create_node_graph_data(pkl_file_name, jsn_output_name)

#Cryptopunks DATA

pkl_file_name = "crypToadzAddress.pkl"
jsn_output_name = "whale_transactions_crypToadzAddress_node_graph.json"
address = crypToadzAddress
full_database_key = '/database_store_keys/key_for_full_database_store.json'
all_tokens_key = '/database_store_keys/key_for_all_tokens_store.json'
all_transactions_key = '/database_store_keys/key_for_all_transactions_store.json'

get_firebase_data_return_pkl_file(pkl_file_name, address, full_database_key, all_transactions_key)
create_node_graph_data(pkl_file_name, jsn_output_name)

#boredApeKennelAddress DATA

pkl_file_name = "boredApeKennelAddress.pkl"
jsn_output_name = "whale_transactions_boredApeKennelAddress_node_graph.json"
address = boredApeKennelAddress
full_database_key = '/database_store_keys/key_for_full_database_store.json'
all_transactions_key = '/database_store_keys/key_for_all_transactions_store.json'

get_firebase_data_return_pkl_file(pkl_file_name, address, full_database_key, all_transactions_key)
create_node_graph_data(pkl_file_name, jsn_output_name)

#Cryptokitties

pkl_file_name = "pudgyPenguinAddress.pkl"
jsn_output_name = "whale_transactions_pudgyPenguinAddress_node_graph.json"
address = pudgyPenguinAddress
full_database_key = '/database_store_keys/key_for_full_database_store.json'
all_tokens_key = '/database_store_keys/key_for_all_tokens_store.json'
all_transactions_key = '/database_store_keys/key_for_all_transactions_store.json'

get_firebase_data_return_pkl_file(pkl_file_name, address, full_database_key, all_transactions_key)
create_node_graph_data(pkl_file_name, jsn_output_name)
