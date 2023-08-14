

from django.shortcuts import render


import joblib
import pickle 
# Create your views here.
# MVT= Model, View, Template
# MVC= Model, View, Controller

from django.http import HttpResponse

def Home(request):
   return render(request,'home.html')

def result(request):
    cls = joblib.load('final model.joblib')
    lis=[]
    lis.append(float(request.GET['Current Loan Amount']))
    lis.append(float(request.GET['Term']))
    lis.append(float(request.GET['Credit Score']))
    lis.append(float(request.GET['Annual Income']))
    lis.append(float(request.GET['Home Ownership']))
    lis.append(float(request.GET['Purpose']))
    lis.append(float(request.GET['Monthly Debt']))
    lis.append(float(request.GET['Years of Credit History']))
    lis.append(float(request.GET['Current Credit Balance']))
    lis.append(float(request.GET['Years in current job']))


    ans =cls.predict([lis])
    if ans == 0:
        ans = 'likely to default'
    else:
        ans = 'eligibile for loan'
    
    return render(request,'LoanStatus.html',{'ans':ans})



