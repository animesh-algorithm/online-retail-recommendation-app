import pandas as pd
df = pd.read_csv('preprocessed_data_for_nn_model.csv')

def get_similar_products(model, product_data):
    ind = model.kneighbors(product_data, return_distance=False)
    return df.iloc[ind[0]][['InvoiceNo', 'Description', 'Quantity', 'UnitPrice', 'Country', 'CountryNumeric']]