import pandas as pd 

data = {
    'Date':['2024-11-21', 
    '2024-07-11',
    '2024-07-29',
    '2024-01-09',
    '2024-12-29'],

    'Product':['Shoes','Laptop',
    'TV','Carpet',
    'CCTV Cameras'],

    'Quantity':[
        29,100,43,89,18
    ],
    'Revenue':[
        12000, 32000,
        67999, 25440,
        56099
    ]
}

df=pd.DataFrame(data)

print(df)