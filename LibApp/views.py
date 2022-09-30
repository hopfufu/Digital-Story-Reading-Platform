from email.mime import image
from optparse import Values
from django.shortcuts import render
import pickle
import os
# Create your views here.
def index(request):
    with open('popular1.pkl', 'rb') as f:

        popular_df=pickle.load(f)
    
    context_dic={
        'imgUrl':list(popular_df['Image-URL-L']),
    }
        
    return render(request,'index.html',context=context_dic)