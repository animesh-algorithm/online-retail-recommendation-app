import pandas as pd
from sklearn.utils import shuffle
from django.shortcuts import render

df = shuffle(pd.read_csv('Online Retail.csv'))[:30].values

def home(request):
    context = {
        'data': df
    }
    return render(request, 'home.html', context=context)