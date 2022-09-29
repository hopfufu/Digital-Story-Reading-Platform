from email.mime import image
from multiprocessing import context
from optparse import Values
from django.shortcuts import render
import numpy as np
import pickle
import os
# Create your views here.
def index(request):
    with open('top_10_books.pkl', 'rb') as f:

        top_10_books=pickle.load(f)
    
    context_dic={
        'imgUrl':list(top_10_books['Image-URL-L']),
     }
    print(context_dic)
    # emp={}
    # j=0
    # for i in context_dic:
    #     for j in range(10):
    #         emp[str(j)]=list([context_dic[i][j]])
    #     break
    # print(emp)
    return render(request,'index.html',context=context_dic)

def recomendation(request):
    with open('books.pkl','rb') as f1:
        books=pickle.load(f1)
    with open('sim_score.pkl','rb') as f2:
        sim_score=pickle.load(f2)
    with open('pt.pkl','rb') as f3:
        pt=pickle.load(f3)
    book_search='Whispers'
    if book_search==None:
        return render(request,'recommendations.html')
    else:
        l=[]
        l1=[]
        def recommend():
            #first get the index of the book
            if book_search==None:
                return
            index=np.where(pt.index==book_search)[0][0]
            similar_items=sorted(list(enumerate(sim_score[index])),key=lambda x:x[1],reverse=True)[1:6]
            for i in similar_items:
                t_df=books[pt.index[i[0]]==books['Book-Title']]
                l.append(t_df.drop_duplicates('Book-Title')['Book-Title'].values)
                l1.append(t_df.drop_duplicates('Book-Title')['Image-URL-L'].values)
        recommend()
        d={'a':l[0][0],
            'a1':l[1][0],
            'a2':l[2][0],
            'a3':l[3][0],
            'a4':l[4][0],
            'img':l1[0][0],
            'img1':l1[1][0],
            'img2':l1[2][0],
            'img3':l1[3][0],
            'img4':l1[4][0],
        }
        return render(request,'recommendations.html',context=d)