from django.shortcuts import render,HttpResponse
from .forms import Number


# Create your views here.
def find(request):
    try:
        form=Number()
        if request.method=="POST":
            form=Number(request.POST)
            if form.is_valid():
                num=form.cleaned_data['num']
                if num%2==0:
                    checkvalue="EVEN"
                else:
                    checkvalue="ODD"    
                return render(request,'check/evenodd.html',{'checkvalue':checkvalue})
    
    except:
        form=Number()
        print(checkvalue)        
    return render(request,'check/evenodd.html',{'form':form})