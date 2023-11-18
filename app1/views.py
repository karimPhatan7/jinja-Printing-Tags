from django.shortcuts import render

# Create your views here.
def karim(request):
    data='Myself Phatan Karimulla and Iam from kadapa district'
    d={'name':data}
    return render(request,'karim.html',context=d)