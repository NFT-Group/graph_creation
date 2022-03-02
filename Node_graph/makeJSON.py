import pandas as pd
import json 


listOfWhaleAddresses = {"0x886478d3cf9581b624cb35b5446693fc8a58b787", "0xe26f91cc2984fb61702a218efa715d86e6a70523"}

d = {'from': ['0x886478d3cf9581b624cb35b5446693fc8a58b787', 
              '0xe26f91cc2984fb61702a218efa715d86e6a70523',
              '0x83bb781a2a2ca1fec0350f178c911848811cc440',
              '0x631b2Bf82637fa199535Dd6190F21C460275dE99',
              '0x37c4bbcee3906213bef1ed2498f90e26382cfa31',
              '0xfeef9d78980083f605c9902c0367df6035d47276',
              '0x1919DB36cA2fa2e15F9000fd9CdC2EdCF863E685',
              '0x0e5d9b06291205dd02a28247c59cccb6517c36d8',
              '0x00Bd3A6660309fb9e0129B9b777a9ccB9c2869DC',
              '0xee5280e9eb7b9d33ca03332db7382b24f4a2d009'],
    'to':    ['0xf6a10fb2639449e398f4cc5defe540191a6a0127',
              '0x07986c37dc04c8ad47c8ea570dd79a821539cd90',
              '0xC50bc863F657938F38699dfaB7eBee57381e49db',
              '0x3d7f610fdcac111f0b7c16384c2792e7e0abb589',
              '0x7401572d8b4e07f89579d804e267ac000c8c67cc',
              '0x22D1a5f9B2A8773135682920B1F8f764D0d6e7F5',
              '0xd1bf89977e21c8159a3af203c24a2ff8841f8d0e',
              '0x3d7f610fdcac111f0b7c16384c2792e7e0abb589',
              '0xf6a10fb2639449e398f4cc5defe540191a6a0127',
              '0x1919DB36cA2fa2e15F9000fd9CdC2EdCF863E685'],
    'hash':  ['0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D',
              '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB',
              '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB',
              '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB',
              '0x8a90CAb2b38dba80c64b7734e58Ee1dB38B8992e',
              '0x8a90CAb2b38dba80c64b7734e58Ee1dB38B8992e',
              '0x8a90CAb2b38dba80c64b7734e58Ee1dB38B8992e',
              '0xBd3531dA5CF5857e7CfAA92426877b022e612cf8',
              '0xBd3531dA5CF5857e7CfAA92426877b022e612cf8',
              '0xBd3531dA5CF5857e7CfAA92426877b022e612cf8'], 
    'price': [10, 4, 2, 3, 5, 7, 8, 9, 19, 27]}

df = pd.DataFrame(data=d)
# print(df)

json_out = df.to_json()

print(json_out)