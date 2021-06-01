import pandas as pd
# from sklearn.utils import shuffle
from django.shortcuts import render
import pickle
from .recommend import get_similar_products

# df = pd.read_csv('Online Retail.csv')[:30].values
df = pd.read_csv('preprocessed_data_for_nn_model.csv')[:30].values
file = open('model.pkl', 'rb')
model = pickle.load(file)
country_mapping = {
    0: 'Australia',
    1: 'Austria',
    2: 'Bahrain',
    3: 'Belgium',
    4: 'Brazil',
    5: 'Canada',
    6: 'Channel Islands',
    7: 'Cyprus',
    8: 'Czech Republic',
    9: 'Denmark',
    10: 'EIRE',
    11: 'European Community',
    12: 'Finland',
    13: 'France',
    14: 'Germany',
    15: 'Greece',
    16: 'Hong Kong',
    17: 'Iceland',
    18: 'Israel',
    19: 'Italy',
    20: 'Japan',
    21: 'Lebanon',
    22: 'Lithuania',
    23: 'Malta',
    24: 'Netherlands',
    25: 'Norway',
    26: 'Poland',
    27: 'Portugal',
    28: 'RSA',
    29: 'Saudi Arabia',
    30: 'Singapore',
    31: 'Spain',
    32: 'Sweden',
    33: 'Switzerland',
    34: 'USA',
    35: 'United Arab Emirates',
    36: 'United Kingdom',
    37: 'Unspecified'
}

def home(request):
    context = {
        'data': df,
    }
    return render(request, 'home.html', context=context)

def recommend(request, desc, qty, price, country):
    product_data = [qty, float(price), country]
    similar_products = get_similar_products(model, [product_data]).values
    context = {
        'description': desc,
        'quantity': qty,
        'unit_price': price,
        'country': country_mapping[country],
        'recommendations': similar_products
    }
    return render(request, 'recommend.html', context=context)