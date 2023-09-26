from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'calculator.html')
def calculator (request):
     num1=int(request.POST["num1"])
     num2=int(request.POST["num2"])
     cal=request.POST["btn"]
     if cal=='+':
          result=num1+num2
     elif cal=='-':
          result=num1-num2
     elif cal=='x':
          result=num1*num2
     else :
          result=num1/num2
     
            
     return render(request, 'calculator.html',{'msg':result})                    

