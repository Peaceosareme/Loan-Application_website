from django.shortcuts import render

#import joblib
#import pickle 
# Create your views here.
# MVT= Model, View, Template
# MVC= Model, View, Controller

#from django.http import HttpResponse

#def Home(request):
 #   return render(request,'home.html')

#def result(request):
#    cls = pickle.load(open('fy.pkl', 'rb'))
#    lis=[]
#    lis.append(request.GET['Current Loan Amount'])
 ##   lis.append(request.GET['Term'])
#    lis.append(request.GET['Credit Score'])
#    lis.append(request.GET['Annual Income'])
#    lis.append(request.GET['Years in current job'])
#    lis.append(request.GET['Home Ownership'])
#    lis.append(request.GET['Purpose'])
#    lis.append(request.GET['Monthly debt'])
 #   lis.append(request.GET['Number of Open Accounts'])
 #   lis.append(request.GET['Number of Credit Problems'])
 #   lis.append(request.GET['Current Credit Balance'])
 #   lis.append(request.GET['Maximum Open Credit'])
 #   lis.append(request.GET['Months since last delinquent'])


  #  ans =cls.predict(float[lis])
  #  if ans == 0:
  #      ans = 'likely to default / charged off'
  #  else:
  #      ans = 'pay loan back/eligibile for loan'
    
   # return render(request,'index.html',{'ans':ans})



